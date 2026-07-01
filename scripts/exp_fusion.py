"""Offline experiment (CPU, no GPU): does a better UNION method fix Arm C's multi-answer
regression? The audit found decompose->union regressed (C x A cov@10 0.580 < holistic 0.677)
and blamed the round-robin union (wastes top slots on each sub-query's rank-1/2 distractors),
NOT the decomposition (topic-recall 0.977). Test: retrieve each sub-query ONCE via the baseline
(e5+bm25, CPU), then sweep union methods x depth and score coverage@10 the same way eval.py does.

Round-robin baseline here should reproduce the committed C x A (~0.580); RRF is the candidate fix.
"""
import argparse
import json

import common
import retrievers


def coverage_at_k(gold, ranked, k):
    topk = set(ranked[:k])
    return sum(1 for g in gold if g in topk) / len(gold) if gold else 0.0


def union_roundrobin(rankings, k):
    out, seen = [], set()
    depth = max((len(r) for r in rankings), default=0)
    for d in range(depth):
        for r in rankings:
            if d < len(r) and r[d] not in seen:
                seen.add(r[d]); out.append(r[d])
                if len(out) >= k:
                    return out
    return out


def union_rrf(rankings, k, c=60):
    """Reciprocal Rank Fusion: score(slug) = sum over sub-queries of 1/(c + rank). A slug that
    is moderately ranked across SEVERAL sub-queries beats a distractor that is rank-1 in one."""
    fused = {}
    for r in rankings:
        for rank, slug in enumerate(r):
            fused[slug] = fused.get(slug, 0.0) + 1.0 / (c + rank)
    return [s for s, _ in sorted(fused.items(), key=lambda x: -x[1])[:k]]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--retrieve-k", type=int, default=20, help="rank depth pulled per sub-query (once)")
    args = ap.parse_args()

    decomposed = common.read_jsonl(common.path("data_dir") / "decomposed.jsonl")
    retr = retrievers.EmbedRetriever()

    # retrieve each sub-query ONCE at retrieve-k; truncate to per_sub for each config
    print(f"retrieving {sum(len(d['subqueries']) for d in decomposed)} sub-queries at k={args.retrieve_k}...", flush=True)
    per_query = []
    for d in decomposed:
        rankings = [retr.rank(sq, k=args.retrieve_k) for sq in d["subqueries"]]
        per_query.append((d["gold"], rankings))

    def mean_cov(fusion, per_sub, k=10, c=60):
        covs = []
        for gold, rankings in per_query:
            trimmed = [r[:per_sub] for r in rankings]
            u = union_rrf(trimmed, k, c) if fusion == "rrf" else union_roundrobin(trimmed, k)
            covs.append(coverage_at_k(gold, u, k))
        return sum(covs) / len(covs)

    print("\n  holistic baseline cov@10 (no decomposition) = 0.677   [target to beat]")
    print("  round-robin C x A (committed)               = 0.580   [what we're fixing]\n")
    print(f"  {'method':14s} {'per_sub':>8s}  cov@10")
    for per_sub in (6, 10, 20):
        print(f"  {'roundrobin':14s} {per_sub:>8d}  {mean_cov('roundrobin', per_sub):.4f}")
    for per_sub in (6, 10, 20):
        for c in (10, 60):
            print(f"  {'rrf(c=%d)'%c:14s} {per_sub:>8d}  {mean_cov('rrf', per_sub, c=c):.4f}")


if __name__ == "__main__":
    main()
