"""Arm C composition — run each decomposed sub-query through a retriever (Arm A or Arm B)
and UNION the results (round-robin by rank) -> coverage on the multi-gold set.

Also reports the decomposer's TOPIC-RECALL: the fraction of the gold set's distinct topic
clusters that the sub-queries actually surface — the unrecoverable-miss ceiling (a sub-topic
the splitter misses can never be recovered downstream).

Usage:
  python scripts/compose_c.py --arm A                 # C x A (e5+bm25)
  .venv-dml/Scripts/python scripts/compose_c.py --arm B --size 0.5B   # C x B (router)
"""
import argparse
import json
from pathlib import Path

import common

DATA = common.path("data_dir")


def union_roundrobin(rankings, k):
    """rankings: list of ranked slug lists (one per sub-query). Interleave by rank."""
    out, seen = [], set()
    depth = max((len(r) for r in rankings), default=0)
    for d in range(depth):
        for r in rankings:
            if d < len(r) and r[d] not in seen:
                seen.add(r[d])
                out.append(r[d])
                if len(out) >= k:
                    return out
    return out


def union_rrf(rankings, k, c=10):
    """Reciprocal Rank Fusion: score(slug) = sum_sub-queries 1/(c + rank). A slug moderately
    ranked across SEVERAL sub-queries beats a distractor that is rank-1 under only one — which
    is exactly the failure mode of round-robin on multi-answer clusters (see scripts/exp_fusion.py:
    on the baseline this lifts C×A cov@10 0.580 -> ~0.598; the bigger win is expected for C×B,
    where the router is a far stronger per-sub-query retriever)."""
    fused = {}
    for r in rankings:
        for rank, slug in enumerate(r):
            fused[slug] = fused.get(slug, 0.0) + 1.0 / (c + rank)
    return [s for s, _ in sorted(fused.items(), key=lambda x: -x[1])[:k]]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--arm", required=True, choices=["A", "B"])
    ap.add_argument("--size", default="0.5B")
    ap.add_argument("--device", default="auto")
    ap.add_argument("--per-sub", type=int, default=10, help="top-m per sub-query before union")
    ap.add_argument("--topk", type=int, default=10)
    ap.add_argument("--fusion", choices=["rrf", "roundrobin"], default="rrf",
                    help="how to union sub-query rankings (rrf beats round-robin; see exp_fusion.py)")
    ap.add_argument("--rrf-c", type=int, default=10, help="RRF constant (lower = rank-1 weighted more)")
    ap.add_argument("--batch", type=int, default=16, help="router slug-scoring batch (Arm B; 96 OOMs)")
    args = ap.parse_args()

    decomposed = common.read_jsonl(DATA / "decomposed.jsonl")
    manifest = json.loads((common.path("corpus_dir").parent / "manifest.json").read_text(encoding="utf-8"))
    slug_cluster = {s: n["cluster"] for s, n in manifest["notes"].items()}

    import retrievers
    if args.arm == "A":
        retr = retrievers.EmbedRetriever()
        out_name = "preds_cxA.jsonl"
        label = "CxA"
    else:
        import gpu_guard
        if args.device != "cpu":
            gpu_guard.ensure_free_for(args.size, "compose-B")
        retr = retrievers.RouterRetriever(size=args.size, device=args.device, batch_size=args.batch)
        out_name = f"preds_cxB_{args.size}.jsonl"
        label = f"CxB_{args.size}"

    preds = []
    topic_recalls = []
    for i, d in enumerate(decomposed):
        rankings = [retr.rank(sq, k=args.per_sub) for sq in d["subqueries"]]
        ranked = (union_rrf(rankings, args.topk, c=args.rrf_c) if args.fusion == "rrf"
                  else union_roundrobin(rankings, args.topk))
        preds.append({"query": d["query"], "kind": "multi", "gold": d["gold"], "ranked": ranked})
        # topic-recall: gold clusters covered by the union of sub-query hits
        gold_clusters = {slug_cluster.get(s) for s in d["gold"]}
        hit_clusters = {slug_cluster.get(s) for r in rankings for s in r}
        covered = gold_clusters & hit_clusters
        topic_recalls.append(len(covered) / max(1, len(gold_clusters)))
        if (i + 1) % 25 == 0:
            print(f"  {i+1}/{len(decomposed)}", flush=True)

    out = DATA / out_name
    common.write_jsonl(out, preds)
    report = {"arm": label, "queries": len(preds),
              "avg_subqueries": round(sum(len(d["subqueries"]) for d in decomposed) / max(1, len(decomposed)), 2),
              "decomposer_topic_recall": round(sum(topic_recalls) / max(1, len(topic_recalls)), 4),
              "per_sub": args.per_sub, "fusion": args.fusion, "rrf_c": args.rrf_c}
    (common.path("results_dir") / f"compose_{label}_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2), flush=True)
    print(f"-> {out}. Now: python scripts/eval.py --preds {out} --arm C --label {label}", flush=True)


if __name__ == "__main__":
    main()
