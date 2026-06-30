"""Run 2 — turn the Sonnet-generated queries (corpus/eval_queries_raw.json) into clean
train/held-out splits with verified no-leak.

Validates slugs, drops malformed (assoc gold must differ from source), normalised-dedups
against the verbatim anchors and within itself, then holds out a disjoint ~20% for eval
and adds the rest to train. Writes data/heldout.jsonl, data/augment.jsonl,
data/train_aug.jsonl, results/queries_report.json.

Usage: python scripts/process_queries.py [--heldout 0.2]
"""
import argparse
import json
import random
from pathlib import Path

import common

DATA = common.path("data_dir")
RAW = common.path("corpus_dir").parent / "eval_queries_raw.json"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--heldout", type=float, default=0.2)
    args = ap.parse_args()
    common.set_seed()
    rng = random.Random(common.config()["seed"] + 23)

    raw = json.loads(RAW.read_text(encoding="utf-8"))
    queries = raw["queries"] if isinstance(raw, dict) and "queries" in raw else raw
    slug_set = set((DATA / "slugs.txt").read_text(encoding="utf-8").split())
    anchors = common.read_jsonl(DATA / "train.jsonl")
    anchor_q = {common.normalize_query(p["query"]) for p in anchors}

    # validate + dedup
    seen, uniq = set(), []
    dropped = {"bad_slug": 0, "assoc_self": 0, "dup": 0, "in_anchor": 0, "empty": 0}
    for r in queries:
        q = str(r.get("query", "")).strip()
        gold, src, kind = r.get("gold"), r.get("source"), r.get("kind")
        if not q:
            dropped["empty"] += 1; continue
        if gold not in slug_set or (src and src not in slug_set):
            dropped["bad_slug"] += 1; continue
        if kind == "assoc" and gold == src:
            dropped["assoc_self"] += 1; continue
        nq = common.normalize_query(q)
        if nq in anchor_q:
            dropped["in_anchor"] += 1; continue
        if nq in seen:
            dropped["dup"] += 1; continue
        seen.add(nq)
        uniq.append({"query": q, "kind": kind, "gold": [gold], "source": src})

    rng.shuffle(uniq)
    heldout, aug, eval_q = [], [], set()
    for r in uniq:
        if rng.random() < args.heldout:
            heldout.append(r)
            eval_q.add(common.normalize_query(r["query"]))
        else:
            aug.append({"query": r["query"], "slug": r["gold"][0], "kind": r["kind"], "source": r["source"]})
    aug = [a for a in aug if common.normalize_query(a["query"]) not in eval_q]  # final no-leak guard

    common.write_jsonl(DATA / "heldout.jsonl", heldout)
    common.write_jsonl(DATA / "augment.jsonl", aug)
    common.write_jsonl(DATA / "train_aug.jsonl", anchors + aug)

    leak = sum(1 for h in heldout if common.normalize_query(h["query"]) in anchor_q
               or common.normalize_query(h["query"]) in {common.normalize_query(a["query"]) for a in aug})
    kc = lambda rows: {k: sum(1 for r in rows if r.get("kind") == k) for k in ("symptom", "assoc")}
    report = {"raw": len(queries), "valid_unique": len(uniq), "dropped": dropped,
              "heldout": len(heldout), "heldout_by_kind": kc(heldout),
              "train_queries": len(aug), "train_by_kind": kc(aug),
              "train_aug_total": len(anchors) + len(aug), "leak": leak}
    (common.path("results_dir") / "queries_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if leak:
        print("!!! LEAK DETECTED")


if __name__ == "__main__":
    main()
