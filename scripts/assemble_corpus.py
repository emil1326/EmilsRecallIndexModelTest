"""Assemble the final vault from the Sonnet workflow output + Emil's seed notes.

Inputs:
  corpus/generated_notes.json  -> {"byCluster": {clusterKey: [{title,summary,body,type,links:[titles]}]}}
  corpus/seed_notes.jsonl      -> Emil's conversational notes {cluster,title,summary,body,type}

Steps: merge seeds into their clusters -> unique kebab slugs (<=5 words) -> resolve each
note's link TITLES to slugs (intra-cluster + seeds; drop unresolved) -> add deterministic
cross-cluster BRIDGE edges -> enforce out-degree cap + min links -> validate (no dangling,
graph stats) -> write <slug>.md + manifest.json + results/corpus_stats.json.

Usage: python scripts/assemble_corpus.py
"""
import json
import random
import re
from pathlib import Path

import common

CFG = common.config()
VAULT = common.path("corpus_dir")
GEN = VAULT.parent / "generated_notes.json"
SEEDS = VAULT.parent / "seed_notes.jsonl"
MANIFEST = VAULT.parent / "manifest.json"
MAX_OUT = 8
TYPES = set(CFG["corpus"]["types"])

# thematically-adjacent clusters -> low-surface-similarity cross-topic edges
BRIDGES = [
    ("analysis-cache", "arrow-java"), ("analysis-cache", "performance"),
    ("analysis-cache", "data-pipeline"), ("embedding-daemon", "memory-architecture"),
    ("embedding-daemon", "data-pipeline"), ("embedding-daemon", "prompt-engineering"),
    ("memory-architecture", "prompt-engineering"), ("memory-architecture", "franglais-naming"),
    ("unity-tooling", "vrchat-avatars"), ("unity-tooling", "avatar-optimization"),
    ("unity-tooling", "feature-checker"), ("unity-tooling", "shaders-rendering"),
    ("feature-checker", "osc-integration"), ("feature-checker", "server-backend"),
    ("feature-checker", "content-creation"), ("avatar-optimization", "performance"),
    ("avatar-optimization", "shaders-rendering"), ("rocm-gpu", "tools-prefs"),
    ("rocm-gpu", "performance"), ("rocm-gpu", "shaders-rendering"),
    ("web-projects", "side-projects"), ("web-projects", "server-backend"),
    ("learning-method", "debugging"), ("learning-method", "work-habits"),
    ("work-habits", "identity-values"), ("work-habits", "decisions"),
    ("git-workflow", "testing-strategy"), ("git-workflow", "tools-prefs"),
    ("franglais-naming", "identity-values"), ("franglais-naming", "collab-feedback"),
    ("server-backend", "osc-integration"), ("content-creation", "vrchat-avatars"),
    ("content-creation", "collab-feedback"), ("decisions", "arrow-java"),
    ("identity-values", "collab-feedback"), ("vrchat-avatars", "avatar-optimization"),
]


def norm_title(t):
    return re.sub(r"\s+", " ", t.lower().strip())


def short_slug(title, used):
    words = common.slugify(title).split("-")
    base = "-".join([w for w in words if w][:5]) or "note"
    slug, i = base, 2
    while slug in used:
        slug = f"{base}-{i}"
        i += 1
    used.add(slug)
    return slug


def main():
    common.set_seed()
    rng = random.Random(CFG["seed"] + 7)

    gen = json.loads(GEN.read_text(encoding="utf-8"))
    by_cluster = gen["byCluster"] if "byCluster" in gen else gen

    # collect raw notes per cluster: seeds first (so they anchor), then generated
    clusters = {}
    if SEEDS.exists():
        for s in common.read_jsonl(SEEDS):
            clusters.setdefault(s["cluster"], []).append(
                {"title": s["title"], "summary": s["summary"], "body": s.get("body", ""),
                 "type": s.get("type", "journal"), "links": [], "source": "conversation"})
    for ck, notes in by_cluster.items():
        for n in notes:
            if not n.get("title") or not n.get("summary"):
                continue
            clusters.setdefault(ck, []).append(
                {"title": n["title"], "summary": n["summary"], "body": n.get("body", ""),
                 "type": n.get("type") if n.get("type") in TYPES else "lesson",
                 "links": n.get("links", []), "source": "generated"})

    # assign slugs; build per-cluster title->slug map
    used = set()
    notes = {}              # slug -> record
    cluster_slugs = {}      # cluster -> [slug]
    title2slug = {}         # cluster -> {norm_title: slug}
    for ck, recs in clusters.items():
        cluster_slugs[ck] = []
        title2slug[ck] = {}
        seen_titles = set()
        for r in recs:
            nt = norm_title(r["title"])
            if nt in seen_titles:        # dedup identical titles within cluster
                continue
            seen_titles.add(nt)
            slug = short_slug(r["title"], used)
            notes[slug] = {"slug": slug, "title": r["title"], "summary": r["summary"],
                           "body": r["body"], "type": r["type"], "cluster": ck,
                           "source": r["source"], "_linktitles": r["links"], "links": []}
            cluster_slugs[ck].append(slug)
            title2slug[ck][nt] = slug

    # resolve intra-cluster link TITLES -> slugs
    for slug, n in notes.items():
        ck = n["cluster"]
        for lt in n["_linktitles"]:
            tgt = title2slug[ck].get(norm_title(lt))
            if tgt and tgt != slug and tgt not in n["links"] and len(n["links"]) < MAX_OUT:
                n["links"].append(tgt)
        del n["_linktitles"]

    # min intra-cluster links (fallback to siblings) so nothing is isolated
    for ck, sl in cluster_slugs.items():
        for i, s in enumerate(sl):
            for j in (1, 2, 3):
                if len(notes[s]["links"]) >= 3 or len(sl) <= 1:
                    break
                t = sl[(i + j) % len(sl)]
                if t != s and t not in notes[s]["links"]:
                    notes[s]["links"].append(t)

    # cross-cluster bridges (low surface similarity -> strong associative signal)
    for a, b in BRIDGES:
        if not cluster_slugs.get(a) or not cluster_slugs.get(b):
            continue
        for _ in range(rng.randint(1, 3)):
            sa = rng.choice(cluster_slugs[a])
            sb = rng.choice(cluster_slugs[b])
            if sb != sa and sb not in notes[sa]["links"] and len(notes[sa]["links"]) < MAX_OUT:
                notes[sa]["links"].append(sb)

    # write vault
    VAULT.mkdir(parents=True, exist_ok=True)
    for p in VAULT.glob("*.md"):
        p.unlink()
    for slug, n in notes.items():
        links_block = ("links:\n" + "".join(f'  - "[[{t}]]"\n' for t in n["links"])
                       if n["links"] else "links: []\n")
        (VAULT / f"{slug}.md").write_text(
            f"---\ntitle: {n['title']}\nsummary: {n['summary']}\ntype: {n['type']}\n"
            f"{links_block}---\n{n['body']}\n", encoding="utf-8")

    manifest = {"notes": notes, "clusters": {k: {"slugs": v} for k, v in cluster_slugs.items()},
                "links_built": True}
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    # validate + stats
    total_links = sum(len(n["links"]) for n in notes.values())
    indeg = {s: 0 for s in notes}
    dangling = 0
    for n in notes.values():
        for t in n["links"]:
            if t in notes:
                indeg[t] += 1
            else:
                dangling += 1
    stats = {
        "notes": len(notes),
        "from_conversation": sum(1 for n in notes.values() if n["source"] == "conversation"),
        "from_generated": sum(1 for n in notes.values() if n["source"] == "generated"),
        "clusters": len(cluster_slugs),
        "total_links": total_links,
        "links_per_note_avg": round(total_links / max(1, len(notes)), 2),
        "dangling_links": dangling,
        "max_out_degree": max((len(n["links"]) for n in notes.values()), default=0),
        "max_in_degree": max(indeg.values(), default=0),
        "isolated_notes": sum(1 for s in notes if len(notes[s]["links"]) == 0 and indeg[s] == 0),
        "title_words_avg": round(sum(len(n["title"].split()) for n in notes.values()) / max(1, len(notes)), 1),
        "summary_words_avg": round(sum(len(n["summary"].split()) for n in notes.values()) / max(1, len(notes)), 1),
        "types": {},
        "notes_per_cluster": {k: len(v) for k, v in cluster_slugs.items()},
    }
    for n in notes.values():
        stats["types"][n["type"]] = stats["types"].get(n["type"], 0) + 1
    (common.path("results_dir")).mkdir(parents=True, exist_ok=True)
    (common.path("results_dir") / "corpus_stats.json").write_text(
        json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in stats.items() if k != "notes_per_cluster"},
                     ensure_ascii=False, indent=2))
    print(f"wrote {len(notes)} notes -> {VAULT}")
    if dangling:
        print(f"!! {dangling} DANGLING LINKS")


if __name__ == "__main__":
    main()
