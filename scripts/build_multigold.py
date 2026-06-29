"""Build the MULTI-GOLD held-out set — query -> [slug, slug, ...] — that powers
coverage@k (the first-class multi-answer metric and H1's central clause).

Three deliberately-different multi-answer shapes, all derived from the link graph so
the gold sets are genuinely coherent:
  * neighbors   : a note + its strongly-linked out-neighbours (the local cluster a query
                  about that note should surface)
  * cluster     : a coherent subset of one topic cluster ("what do we know about X")
  * cross-topic : notes spanning two BRIDGE-connected clusters (the hard case — gold set
                  crosses topics, exactly where embedding cosine struggles)

Query text is generated in franglais by the local LLM (GPU). These are EVAL queries, so
each is normalized-deduped against train + held-out (no leak). Seeded.

Usage: python scripts/build_multigold.py
"""
import argparse
import json
import random
from pathlib import Path

import common

CFG = common.config()
DATA = common.path("data_dir")
MANIFEST = common.path("corpus_dir").parent / "manifest.json"


def gen_query(gold_notes, subtype, model):
    listing = "\n".join(f"- {n['title']} :: {n['summary'][:90]}" for n in gold_notes)
    hint = {
        "neighbors": "une question large sur le sujet central qui devrait ramener TOUTES ces notes reliées",
        "cluster": "une requête du genre 'qu'est-ce que je sais sur X' qui couvre TOUT ce groupe",
        "cross-topic": "une question qui touche les DEUX sujets en même temps et devrait ramener les notes des deux côtés",
    }[subtype]
    prompt = f"""Voici un GROUPE de notes reliées dans une mémoire perso:

{listing}

Écris UNE seule requête FRANGLAIS (français + termes techniques anglais) qu'un user taperait,
{hint}. Naturelle, pas une liste. Réponds en JSON: {{"query": "..."}}"""
    try:
        out = common.ollama_json(prompt, model=model, options={"num_predict": 80, "temperature": 0.8})
        return str(out.get("query", "")).strip() if isinstance(out, dict) else ""
    except Exception:  # noqa: BLE001
        return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default=CFG["ollama"]["decompose_model"])
    ap.add_argument("--max-per-type", type=int, default=40)
    args = ap.parse_args()
    common.set_seed()
    rng = random.Random(CFG["seed"] + 11)

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    notes = manifest["notes"]
    clusters = {k: v["slugs"] for k, v in manifest["clusters"].items()}

    # forbid overlap with train + held-out queries
    forbidden = set()
    for fn in ("train.jsonl", "heldout.jsonl"):
        if (DATA / fn).exists():
            forbidden |= {common.normalize_query(p["query"]) for p in common.read_jsonl(DATA / fn)}

    gold_sets = []  # (subtype, [slugs])

    # 1) neighbors: note + its out-links (out-degree >= 3)
    cand = [s for s in notes if len(notes[s]["links"]) >= 3]
    rng.shuffle(cand)
    for s in cand[: args.max_per_type]:
        g = [s] + notes[s]["links"][:5]
        gold_sets.append(("neighbors", list(dict.fromkeys(g))))

    # 2) cluster subsets
    big = [k for k, sl in clusters.items() if len(sl) >= 6]
    for k in big:
        for _ in range(max(1, args.max_per_type // max(1, len(big)))):
            sub = rng.sample(clusters[k], rng.randint(4, min(6, len(clusters[k]))))
            gold_sets.append(("cluster", sub))

    # 3) cross-topic: notes that link across clusters + a mate on each side
    cross_pairs = []
    for s in notes:
        for t in notes[s]["links"]:
            if t in notes and notes[t]["cluster"] != notes[s]["cluster"]:
                cross_pairs.append((s, t))
    rng.shuffle(cross_pairs)
    for s, t in cross_pairs[: args.max_per_type]:
        ca, cb = notes[s]["cluster"], notes[t]["cluster"]
        extra_a = [x for x in clusters.get(ca, []) if x != s][:1]
        extra_b = [x for x in clusters.get(cb, []) if x != t][:1]
        gold_sets.append(("cross-topic", list(dict.fromkeys([s, t] + extra_a + extra_b))))

    print(f"{len(gold_sets)} candidate gold sets; generating franglais queries on {args.model}...", flush=True)
    rows, dropped = [], 0
    seen = set(forbidden)
    for i, (subtype, slugs) in enumerate(gold_sets):
        slugs = [s for s in slugs if s in notes]
        if len(slugs) < 2:
            continue
        gnotes = [{"title": notes[s]["title"], "summary": notes[s]["summary"]} for s in slugs]
        q = gen_query(gnotes, subtype, args.model)
        nq = common.normalize_query(q)
        if not nq or nq in seen:
            dropped += 1
            continue
        seen.add(nq)
        rows.append({"query": q, "slugs": slugs, "kind": "multi", "subtype": subtype})
        if (i + 1) % 25 == 0:
            print(f"  {i+1}/{len(gold_sets)} | {len(rows)} kept | {dropped} dropped", flush=True)

    common.write_jsonl(DATA / "multigold.jsonl", rows)
    by_sub = {}
    for r in rows:
        by_sub[r["subtype"]] = by_sub.get(r["subtype"], 0) + 1
    report = {"multigold_queries": len(rows), "by_subtype": by_sub, "dropped": dropped,
              "avg_gold_size": round(sum(len(r["slugs"]) for r in rows) / max(1, len(rows)), 2)}
    (common.path("results_dir") / "multigold_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
