"""Generate the synthetic franglais personal-memory vault (Arm 0).

Pipeline:
  1. ~22 themed clusters (seeded sizes summing to ~680 notes).
  2. Per cluster: one planning call -> diverse note titles+angles+types.
  3. Per note: one content call -> {summary, body} (franglais, ~24-word summary).
  4. Links: per-cluster LLM judgment of CONCEPTUAL relatedness (constrained to the
     cluster's real slugs), + deterministic inter-cluster bridges between hub notes.
     => the associative signal is semantically meaningful, not random, and every
        [[link]] resolves.
  5. Write <slug>.md (flat frontmatter) + validate graph stats + corpus_stats.json.

Resumable: notes/links checkpoint to corpus/manifest.json; re-running skips done work.
Reproducible: all randomness seeded from configs/experiment.json.

Usage:
  python scripts/gen_corpus.py            # full ~680-note vault
  python scripts/gen_corpus.py --smoke    # 2 tiny clusters, ~12 notes (validate loop)
  python scripts/gen_corpus.py --links-only   # rebuild links from existing notes
"""
import argparse
import json
import random
import sys
from pathlib import Path

import common

CFG = common.config()
VAULT = common.path("corpus_dir")
MANIFEST = VAULT.parent / "manifest.json"

# --- Cluster themes: a developer's franglais "second brain". High topic diversity
#     (technique / methodo / identité / réflexion), incl. nods to Emil's real domains
#     (Unity/VRChat tooling, web projects) — all content is synthetic. -------------
CLUSTERS = [
    ("analysis-cache", "le cache d'un outil d'analyse de code: lazy rebuild, invalidation, "
     "reapply de règles de sécurité, expiration anticipée", ["lesson", "reference", "journal"]),
    ("arrow-java", "Arrow, un outil Java maison: roadmap, build Gradle, features, refactors", ["reference", "lesson", "journal"]),
    ("embedding-daemon", "le daemon de retrieval mémoire: e5-small dense, BM25, hybrid fusion, prefixes query/passage", ["reference", "lesson"]),
    ("memory-architecture", "l'architecture de la mémoire personnelle: notes atomiques, wikilinks, slugs, frontmatter", ["reference", "lesson", "journal"]),
    ("prompt-engineering", "patterns de prompt: system prompts, few-shot, franglais prompting, JSON forcé", ["lesson", "reference"]),
    ("git-workflow", "habitudes git: branches, commits atomiques, conventions de message, rebase", ["lesson", "reference"]),
    ("unity-tooling", "outils editor Unity (EmilsWork): fenetres custom, AAC applicator, feature locker", ["reference", "lesson", "journal"]),
    ("vrchat-avatars", "systemes d'avatar VRChat: toggles, parametres, optimisation, expressions", ["reference", "lesson"]),
    ("web-projects", "projets web: classe de creation d'images en code, interpreteur de langage custom, site perso", ["journal", "lesson", "reference"]),
    ("rocm-gpu", "galeres GPU/ROCm: RDNA4 gfx1201, DirectML, WSL2, training local, fallback CPU", ["lesson", "journal"]),
    ("testing-strategy", "strategie de tests: tests flaky, fixtures, mocks, couverture, TDD partiel", ["lesson", "reference"]),
    ("performance", "performance et profiling: latence, allocations, hotspots, benchmark, caches CPU", ["lesson", "reference"]),
    ("data-pipeline", "pipelines de donnees: jsonl, dedup, splits held-out, seeds, reproductibilite", ["reference", "lesson"]),
    ("learning-method", "comment Emil apprend une techno inconnue: 'knowing nothing about this beast', Google, erreurs", ["journal", "lesson", "identity"]),
    ("debugging", "philosophie de debug: bisection, logs, hypotheses, repro minimal, patience", ["lesson", "journal"]),
    ("work-habits", "habitudes de travail: focus, procrastination, energie, sessions longues, pauses", ["journal", "identity", "feedback"]),
    ("decisions", "decisions d'architecture: trade-offs, ADR, pourquoi tel choix, regrets", ["reference", "lesson"]),
    ("identity-values", "qui est Emil: valeurs, motivations, gout du fait-maison, curiosite, perseverance", ["identity", "user", "journal"]),
    ("collab-feedback", "comment Emil veut collaborer et recevoir du feedback: ton, directness, branding", ["feedback", "user", "identity"]),
    ("tools-prefs", "preferences d'outils: editeur, OS Windows, langages, raccourcis, terminal", ["user", "reference", "identity"]),
    ("side-projects", "petits projets fun: generateur de nombres aleatoires rate, experiences, prototypes", ["journal", "lesson"]),
    ("franglais-naming", "le melange franglais lui-meme et les conventions de nommage (EmilsWork, kebab-case)", ["reference", "identity", "lesson"]),
]


def allocate_sizes(total, n, seed):
    """Uneven cluster sizes (some hubs bigger) summing to ~total."""
    rng = random.Random(seed)
    weights = [rng.uniform(0.6, 1.8) for _ in range(n)]
    s = sum(weights)
    sizes = [max(8, round(total * w / s)) for w in weights]
    # nudge to hit total exactly-ish
    while sum(sizes) > total:
        sizes[sizes.index(max(sizes))] -= 1
    while sum(sizes) < total:
        sizes[sizes.index(min(sizes))] += 1
    return sizes


def load_manifest():
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text(encoding="utf-8"))
    return {"notes": {}, "clusters": {}, "links_built": False}


def save_manifest(m):
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(m, ensure_ascii=False, indent=2), encoding="utf-8")


def plan_cluster(key, theme, types, n, seed):
    """One call -> n note specs: {title, angle, type}."""
    type_str = ", ".join(types)
    prompt = f"""Tu construis un vault de mémoire personnelle (style "second brain") d'un développeur.
Thème de ce cluster: {theme}

Génère EXACTEMENT {n} notes ATOMIQUES distinctes pour ce thème. Chaque note = UN fait précis.
Écris en FRANGLAIS: phrase FRANÇAISE de base avec des termes techniques anglais gardés en anglais
(ex: "Le cache se rebuild lazy seulement on-demand", "J'ai galéré avec le shader compile sur RDNA4").
Varie les angles (problème vécu, leçon apprise, référence technique, décision, réflexion).
Évite les doublons. Titres de 4 à 8 mots, en franglais, concrets et spécifiques (pas génériques).

Réponds en JSON: {{"notes": [{{"title": "...", "angle": "une phrase franglais sur le contenu précis", "type": "un de: {type_str}"}}]}}"""
    out = common.ollama_json(prompt, options={"num_predict": 60 + 38 * n, "temperature": 0.8})
    notes = out.get("notes", []) if isinstance(out, dict) else (out if isinstance(out, list) else [])
    cleaned = []
    seen = set()
    for nd in notes:
        if not isinstance(nd, dict):
            continue
        title = str(nd.get("title", "")).strip().strip('"').strip("*").strip()
        if not title or title.lower() in seen:
            continue
        seen.add(title.lower())
        t = str(nd.get("type", types[0])).strip().lower()
        if t not in CFG["corpus"]["types"]:
            t = types[0]
        cleaned.append({"title": title, "angle": str(nd.get("angle", "")).strip(), "type": t})
    return cleaned


def gen_note_content(cluster_theme, spec):
    prompt = f"""Note de mémoire personnelle d'un développeur, en FRANGLAIS.
FRANGLAIS = phrase FRANÇAISE de base, avec les termes techniques gardés en ANGLAIS.
Exemple de bon franglais: "Le lazy rebuild du cache se déclenche only on-demand, jamais si le
dernier cache est encore valid — ça évite des full rebuilds inutiles au startup."

Thème du cluster: {cluster_theme}
Titre de la note: {spec['title']}
Angle précis: {spec['angle']}

Écris:
- "summary": UNE phrase de 22 à 26 mots, FRANGLAIS (français de base + termes techniques anglais),
  dense et concrète, qui capture LE fait précis. NE PAS écrire tout en anglais.
- "body": 2 à 4 phrases qui développent le fait, même franglais, concret et vécu, sans blabla.

Pas de markdown, pas de listes. Réponds en JSON: {{"summary": "...", "body": "..."}}"""
    out = common.ollama_json(prompt, options={"num_predict": 300, "temperature": 0.75})
    summary = str(out.get("summary", "")).strip()
    body = str(out.get("body", "")).strip()
    return summary, body


def unique_slug(title, used):
    base = common.slugify(title)
    if not base:
        base = "note"
    slug = base
    i = 2
    while slug in used:
        slug = f"{base}-{i}"
        i += 1
    used.add(slug)
    return slug


def gen_notes(smoke=False):
    seed = CFG["seed"]
    clusters = CLUSTERS[:2] if smoke else CLUSTERS
    total = 12 if smoke else CFG["corpus"]["target_notes"]
    sizes = allocate_sizes(total, len(clusters), seed)
    if smoke:
        sizes = [6, 6]

    m = load_manifest()
    used_slugs = set(m["notes"].keys())

    for ci, ((key, theme, types), n) in enumerate(zip(clusters, sizes)):
        if key in m["clusters"] and len(m["clusters"][key].get("slugs", [])) >= n:
            print(f"[{ci+1}/{len(clusters)}] cluster {key}: already done ({n})", flush=True)
            continue
        print(f"[{ci+1}/{len(clusters)}] planning cluster {key} (target {n})...", flush=True)
        specs = []
        for attempt in range(3):
            specs = plan_cluster(key, theme, types, n, seed + ci)
            if len(specs) >= max(4, int(n * 0.7)):
                break
            print(f"    plan gave {len(specs)}, retry...", flush=True)
        specs = specs[:n]
        cluster_slugs = list(m["clusters"].get(key, {}).get("slugs", []))
        done_titles = {m["notes"][s]["title"].lower() for s in cluster_slugs}
        for si, spec in enumerate(specs):
            if spec["title"].lower() in done_titles:
                continue
            try:
                summary, body = gen_note_content(theme, spec)
            except Exception as e:  # noqa: BLE001
                print(f"    note '{spec['title'][:40]}' failed: {e}", flush=True)
                continue
            if not summary:
                continue
            slug = unique_slug(spec["title"], used_slugs)
            m["notes"][slug] = {
                "slug": slug, "title": spec["title"], "summary": summary,
                "body": body, "type": spec["type"], "cluster": key, "links": [],
            }
            cluster_slugs.append(slug)
            m["clusters"].setdefault(key, {})["theme"] = theme
            m["clusters"][key]["slugs"] = cluster_slugs
            if (si + 1) % 5 == 0:
                save_manifest(m)
                print(f"    {key}: {si+1}/{len(specs)} notes", flush=True)
        save_manifest(m)
        print(f"    cluster {key} done: {len(cluster_slugs)} notes (total {len(m['notes'])})", flush=True)
    print(f"NOTES DONE: {len(m['notes'])} notes across {len(m['clusters'])} clusters", flush=True)
    return m


# --- Phase 2: links (conceptual, constrained to real slugs) ------------------
# Thematically-adjacent cluster pairs -> a few cross-topic bridge edges. These are
# inherently low surface-similarity (different topics) => strong associative signal
# and the substrate for cross-topic multi-answer queries.
BRIDGES = [
    ("analysis-cache", "arrow-java"), ("analysis-cache", "performance"),
    ("embedding-daemon", "memory-architecture"), ("embedding-daemon", "data-pipeline"),
    ("memory-architecture", "prompt-engineering"), ("rocm-gpu", "unity-tooling"),
    ("unity-tooling", "vrchat-avatars"), ("web-projects", "side-projects"),
    ("git-workflow", "testing-strategy"), ("debugging", "performance"),
    ("learning-method", "debugging"), ("identity-values", "collab-feedback"),
    ("collab-feedback", "franglais-naming"), ("tools-prefs", "git-workflow"),
    ("decisions", "arrow-java"), ("work-habits", "learning-method"),
    ("data-pipeline", "rocm-gpu"), ("prompt-engineering", "embedding-daemon"),
    ("franglais-naming", "identity-values"), ("side-projects", "web-projects"),
]
MAX_OUT = 8  # hub out-degree cap (vault-stats: hub_outdegree_up_to 8)


def link_cluster(key, slugs, notes):
    """LLM judges which siblings each note genuinely relates to (different facets of
    the same topic preferred -> conceptual, lexically-varied edges, not paraphrases)."""
    items = [{"slug": s, "title": notes[s]["title"], "type": notes[s]["type"],
              "summary": notes[s]["summary"]} for s in slugs]
    listing = "\n".join(
        f'- {it["slug"]} [{it["type"]}] {it["title"]} :: {it["summary"][:90]}' for it in items)
    valid = set(slugs)
    prompt = f"""Voici les notes d'un cluster de mémoire personnelle (un slug par note):

{listing}

Pour CHAQUE note, choisis 3 à 5 autres notes de CETTE liste qu'un humain wikilinkerait
parce qu'elles sont VRAIMENT reliées (cause->conséquence, problème->leçon->outil->décision,
concept->usage). PRÉFÈRE relier des notes qui abordent le sujet sous un ANGLE DIFFÉRENT
(types différents) plutôt que des quasi-doublons. Utilise UNIQUEMENT les slugs ci-dessus.

JSON: {{"links": {{"slug-a": ["slug-b", "slug-c"], ...}}}}"""
    try:
        out = common.ollama_json(prompt, options={"num_predict": 40 + 24 * len(slugs),
                                                   "temperature": 0.5}, timeout=300)
        raw = out.get("links", {}) if isinstance(out, dict) else {}
    except Exception as e:  # noqa: BLE001
        print(f"    link call failed for {key}: {e} -> heuristic fallback", flush=True)
        raw = {}
    adj = {}
    for s in slugs:
        tgts = raw.get(s, []) if isinstance(raw.get(s, []), list) else []
        clean = [t for t in tgts if t in valid and t != s]
        # dedup, cap
        seen, out_list = set(), []
        for t in clean:
            if t not in seen:
                seen.add(t)
                out_list.append(t)
        adj[s] = out_list[:MAX_OUT]
    # heuristic fallback for notes the LLM left thinly linked: link to next siblings
    sl = list(slugs)
    target_min = 3 if len(sl) > 3 else 2
    for i, s in enumerate(sl):
        for j in (1, 2, 3, 4):
            if len(adj[s]) >= target_min:
                break
            t = sl[(i + j) % len(sl)]
            if t != s and t not in adj[s]:
                adj[s].append(t)
    return adj


def build_links(m, seed=None):
    seed = CFG["seed"] if seed is None else seed
    rng = random.Random(seed + 999)
    notes = m["notes"]
    for s in notes:
        notes[s]["links"] = []
    # intra-cluster conceptual links
    for ci, (key, cl) in enumerate(m["clusters"].items()):
        slugs = [s for s in cl.get("slugs", []) if s in notes]
        if len(slugs) < 2:
            continue
        print(f"  linking cluster {key} ({len(slugs)} notes)...", flush=True)
        adj = link_cluster(key, slugs, notes)
        for s, tgts in adj.items():
            for t in tgts:
                if t not in notes[s]["links"] and len(notes[s]["links"]) < MAX_OUT:
                    notes[s]["links"].append(t)
    # inter-cluster bridges between hub-ish notes (first few of each cluster)
    cl_slugs = {k: [s for s in v.get("slugs", []) if s in notes] for k, v in m["clusters"].items()}
    for a, b in BRIDGES:
        if not cl_slugs.get(a) or not cl_slugs.get(b):
            continue
        for _ in range(rng.randint(1, 2)):
            sa = rng.choice(cl_slugs[a][:max(1, len(cl_slugs[a]) // 2)])
            sb = rng.choice(cl_slugs[b][:max(1, len(cl_slugs[b]) // 2)])
            if sb not in notes[sa]["links"] and len(notes[sa]["links"]) < MAX_OUT:
                notes[sa]["links"].append(sb)
    m["links_built"] = True
    save_manifest(m)
    return m


# --- Phase 3: write .md + validate ------------------------------------------
def write_vault(m):
    VAULT.mkdir(parents=True, exist_ok=True)
    # clear stale .md
    for p in VAULT.glob("*.md"):
        p.unlink()
    for slug, n in m["notes"].items():
        links_yaml = "".join(f'  - "[[{t}]]"\n' for t in n["links"])
        if not links_yaml:
            links_yaml = "  []\n"
            links_block = "links: []\n"
        else:
            links_block = "links:\n" + links_yaml
        fm = (f"---\ntitle: {n['title']}\n"
              f"summary: {n['summary']}\n"
              f"type: {n['type']}\n"
              f"{links_block}---\n{n['body']}\n")
        (VAULT / f"{slug}.md").write_text(fm, encoding="utf-8")
    print(f"WROTE {len(m['notes'])} notes to {VAULT}", flush=True)


def validate(m):
    notes = m["notes"]
    n = len(notes)
    out_deg = {s: len(notes[s]["links"]) for s in notes}
    in_deg = {s: 0 for s in notes}
    dangling = 0
    total_links = 0
    for s in notes:
        for t in notes[s]["links"]:
            total_links += 1
            if t in notes:
                in_deg[t] += 1
            else:
                dangling += 1
    stats = {
        "notes": n,
        "total_links": total_links,
        "links_per_note_avg": round(total_links / max(1, n), 2),
        "dangling_links": dangling,
        "max_out_degree": max(out_deg.values()) if out_deg else 0,
        "max_in_degree": max(in_deg.values()) if in_deg else 0,
        "isolated_notes": sum(1 for s in notes if out_deg[s] == 0 and in_deg[s] == 0),
        "clusters": len(m["clusters"]),
        "types": {},
        "title_words_avg": round(sum(len(notes[s]["title"].split()) for s in notes) / max(1, n), 1),
        "summary_words_avg": round(sum(len(notes[s]["summary"].split()) for s in notes) / max(1, n), 1),
    }
    for s in notes:
        t = notes[s]["type"]
        stats["types"][t] = stats["types"].get(t, 0) + 1
    out_path = common.path("results_dir") / "corpus_stats.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8")
    print("=== CORPUS STATS ===", flush=True)
    print(json.dumps(stats, ensure_ascii=False, indent=2), flush=True)
    if dangling:
        print(f"!! {dangling} DANGLING LINKS — must be 0", flush=True)
    return stats


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    ap.add_argument("--phase", choices=["notes", "links", "write", "all"], default="all")
    args = ap.parse_args()
    common.set_seed()

    m = load_manifest()
    if args.phase in ("notes", "all"):
        m = gen_notes(smoke=args.smoke)
    if args.phase in ("links", "all"):
        print("=== building links ===", flush=True)
        m = build_links(m)
    if args.phase in ("write", "all"):
        write_vault(m)
        validate(m)
