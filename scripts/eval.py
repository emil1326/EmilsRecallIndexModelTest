"""Shared evaluation harness — the SAME metric code for every arm (apples-to-apples).

Input: a predictions file, one JSON per held-out query:
  {"query": "...", "kind": "title|summary|assoc|multi", "gold": ["slug", ...],
   "ranked": ["slug", ...]}            # ranked top-k slugs the retriever returned

Metrics:
  * single-answer (|gold|==1): HIT@{1,4,6,10}, MRR  (k=6 ~ live per-turn injection)
  * multi-answer  (|gold|>1):  COVERAGE@{1,4,6,10} = |gold ∩ top-k| / |gold|  (first-class),
                               plus HIT@k (any gold in top-k)
  * broken out per pair-kind (title / summary / assoc) and by subset
    (single / multi / novel-phrasing = held-out summary+assoc = real generalization)
  * distance to the bar (HIT@1>0.80, HIT@10>0.999, coverage@10>0.999)
  * invalid-slug rate (ranked ids not in slugs.txt — must be ~0 for the generative router)
  * 95% bootstrap CIs on HIT@1 / HIT@10 / coverage@10 (held-out is small -> report uncertainty)

Usage:
  python scripts/eval.py --preds data/preds_baseline.jsonl --arm A --label e5+bm25
"""
import argparse
import json
import random
from pathlib import Path

import common

K_VALUES = common.config()["metrics"]["k_values"]  # [1,4,6,10]
BAR = common.config()["metrics"]["bar"]


# ---- per-query metrics ----
def hit_at_k(gold, ranked, k):
    topk = set(ranked[:k])
    return 1.0 if any(g in topk for g in gold) else 0.0


def coverage_at_k(gold, ranked, k):
    topk = set(ranked[:k])
    hit = sum(1 for g in gold if g in topk)
    return hit / len(gold) if gold else 0.0


def reciprocal_rank(gold, ranked):
    goldset = set(gold)
    for i, s in enumerate(ranked):
        if s in goldset:
            return 1.0 / (i + 1)
    return 0.0


# ---- aggregation ----
def mean(xs):
    xs = list(xs)
    return sum(xs) / len(xs) if xs else 0.0


def bootstrap_ci(values, fn, n=1000, seed=0, alpha=0.05):
    """95% percentile bootstrap CI for a mean-like statistic over per-query values."""
    if not values:
        return [0.0, 0.0]
    rng = random.Random(seed)
    n_items = len(values)
    stats = []
    for _ in range(n):
        sample = [values[rng.randrange(n_items)] for _ in range(n_items)]
        stats.append(fn(sample))
    stats.sort()
    lo = stats[int((alpha / 2) * n)]
    hi = stats[int((1 - alpha / 2) * n)]
    return [round(lo, 4), round(hi, 4)]


def eval_group(records):
    """records: list of {gold, ranked}. Returns metric dict (auto single vs multi)."""
    single = [r for r in records if len(r["gold"]) == 1]
    multi = [r for r in records if len(r["gold"]) > 1]
    out = {"n": len(records), "n_single": len(single), "n_multi": len(multi)}
    if single:
        for k in K_VALUES:
            out[f"hit@{k}"] = round(mean(hit_at_k(r["gold"], r["ranked"], k) for r in single), 4)
        out["mrr"] = round(mean(reciprocal_rank(r["gold"], r["ranked"]) for r in single), 4)
    if multi:
        for k in K_VALUES:
            out[f"coverage@{k}"] = round(mean(coverage_at_k(r["gold"], r["ranked"], k) for r in multi), 4)
            out[f"hit@{k}_any"] = round(mean(hit_at_k(r["gold"], r["ranked"], k) for r in multi), 4)
    return out


def distance_to_bar(metrics):
    d = {}
    if "hit@1" in metrics:
        d["hit@1_gap"] = round(BAR["hit_at_1"] - metrics["hit@1"], 4)
        d["hit@10_gap"] = round(BAR["hit_at_10"] - metrics.get("hit@10", 0.0), 4)
        d["clears_bar"] = metrics["hit@1"] >= BAR["hit_at_1"] and metrics.get("hit@10", 0) >= BAR["hit_at_10"]
    if "coverage@10" in metrics:
        d["coverage@10_gap"] = round(BAR["coverage_at_10"] - metrics["coverage@10"], 4)
        d["clears_coverage_bar"] = metrics["coverage@10"] >= BAR["coverage_at_10"]
    return d


def evaluate(preds, slug_vocab=None):
    # Run 2 fix: for associative queries, EXCLUDE the source note A from the ranked list before
    # scoring (we measure reaching the linked B, not ranking B above its own source text).
    for p in preds:
        src = p.get("source")
        if p.get("kind") == "assoc" and src and src not in p.get("gold", []):
            p["ranked"] = [s for s in p["ranked"] if s != src]

    # invalid-slug rate (hallucinated ids)
    invalid = total_ranked = 0
    if slug_vocab is not None:
        for r in preds:
            for s in r["ranked"]:
                total_ranked += 1
                if s not in slug_vocab:
                    invalid += 1

    def subset(name, recs):
        m = eval_group(recs)
        m["distance_to_bar"] = distance_to_bar(m)
        return m

    single = [r for r in preds if len(r["gold"]) == 1]
    multi = [r for r in preds if len(r["gold"]) > 1]
    # Run 2 held-out is all LLM-generated, non-verbatim -> "novel phrasing" = all single
    novel = [r for r in single if r.get("kind") in ("summary", "assoc", "symptom")]

    report = {
        "overall_single": subset("single", single),
        "multi_answer": subset("multi", multi),
        "novel_phrasing": subset("novel", novel),
        "by_kind": {},
        "invalid_slug_rate": round(invalid / total_ranked, 5) if total_ranked else None,
    }
    for kind in ("title", "summary", "symptom", "assoc"):
        recs = [r for r in single if r.get("kind") == kind]
        if recs:
            report["by_kind"][kind] = eval_group(recs)

    # bootstrap CIs (small held-out -> report uncertainty)
    ci = {}
    if single:
        for k in (1, 10):
            vals = [hit_at_k(r["gold"], r["ranked"], k) for r in single]
            ci[f"hit@{k}"] = bootstrap_ci(vals, mean)
    if multi:
        vals = [coverage_at_k(r["gold"], r["ranked"], 10) for r in multi]
        ci["coverage@10"] = bootstrap_ci(vals, mean)
    report["ci95"] = ci
    return report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--preds", required=True)
    ap.add_argument("--arm", default="?")
    ap.add_argument("--label", default="")
    ap.add_argument("--slugs", default=str(common.path("data_dir") / "slugs.txt"))
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    preds = common.read_jsonl(args.preds)
    slug_vocab = None
    if Path(args.slugs).exists():
        slug_vocab = set(Path(args.slugs).read_text(encoding="utf-8").split())

    report = evaluate(preds, slug_vocab)
    report = {"arm": args.arm, "label": args.label, "preds": args.preds, "n_queries": len(preds), **report}

    out = args.out or str(common.path("results_dir") / f"eval_arm{args.arm}.json")
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    print(f"\n-> {out}")


if __name__ == "__main__":
    main()
