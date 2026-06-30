"""Aggregate every arm's eval output into the canonical results/results.json:
arm (A / B-size / CxA / CxB-size) x metric (HIT/coverage@{1,4,6,10}, MRR) x pair-kind
(title/summary/assoc) x subset (single / multi / novel-phrasing), plus corpus stats,
split guarantees, environment, and the computed H1/H2/Arm-C verdicts.

Robust to arms not yet run (emits a partial file). Run after each arm's eval; re-run to
refresh. Reads results/eval_*.json (written by eval.py --out) + the *_report.json files.

Usage: python scripts/aggregate_results.py
"""
import json
import glob
import random
from pathlib import Path

import common

RES = common.path("results_dir")
DATA = common.path("data_dir")
BAR = common.config()["metrics"]["bar"]


def _hit(gold, ranked, k, src, kind):
    """hit@k with the §4.2 source-A exclusion for associative records."""
    if kind == "assoc" and src and src not in gold:
        ranked = [s for s in ranked if s != src]
    return 1.0 if any(g in set(ranked[:k]) for g in gold) else 0.0


def paired_bootstrap(arm_a, arm_b, kind, k, n=2000, seed=42):
    """Paired bootstrap 95% CI on the per-query (B - A) hit@k difference for one subset.
    Returns {mean, ci, n, significant} or None if either preds file is missing."""
    pa, pb = DATA / arm_a, DATA / arm_b
    if not (pa.exists() and pb.exists()):
        return None
    A = {r["query"]: r for r in common.read_jsonl(pa)}
    B = {r["query"]: r for r in common.read_jsonl(pb)}
    diffs = []
    for q, a in A.items():
        b = B.get(q)
        if not b or a.get("kind") != kind or len(a["gold"]) != 1:
            continue
        src, gold = a.get("source"), a["gold"]
        diffs.append(_hit(gold, b["ranked"], k, src, kind) - _hit(gold, a["ranked"], k, src, kind))
    if not diffs:
        return None
    rng = random.Random(seed)
    m = len(diffs)
    stats = []
    for _ in range(n):
        stats.append(sum(diffs[rng.randrange(m)] for _ in range(m)) / m)
    stats.sort()
    lo, hi = stats[int(0.025 * n)], stats[int(0.975 * n)]
    return {"mean": round(sum(diffs) / m, 4), "ci95": [round(lo, 4), round(hi, 4)],
            "n": m, "significant": bool(lo > 0 or hi < 0)}


def load(name):
    p = RES / name
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def main():
    # --- collect eval reports (arm label -> report) ---
    arms = {}
    for f in sorted(glob.glob(str(RES / "eval_*.json"))):
        r = json.loads(Path(f).read_text(encoding="utf-8"))
        label = r.get("label") or Path(f).stem.replace("eval_", "")
        arms[label] = r

    build_report = common.path("data_dir") / "corpus_build_report.json"
    out = {
        "corpus": load("corpus_stats.json"),
        "splits": json.loads(build_report.read_text(encoding="utf-8")) if build_report.exists() else None,
        "baseline": load("baseline_meta.json"),
        "augment": load("augment_report.json"),
        "multigold": load("multigold_report.json"),
        "decompose": load("decompose_report.json"),
        "directml_env": load("directml_env.json"),
        "bar": BAR,
        "arms": {},
    }

    def slim(report):
        """Keep the metric-bearing parts of an eval report."""
        if not report:
            return None
        return {k: report[k] for k in ("overall_single", "novel_phrasing", "multi_answer",
                                       "by_kind", "invalid_slug_rate", "ci95", "n_queries")
                if k in report}

    for label, r in arms.items():
        out["arms"][label] = slim(r)

    # --- verdicts ---
    def assoc_hit1(label):
        a = arms.get(label, {}).get("by_kind", {}).get("assoc", {})
        return a.get("hit@1")

    def assoc_hit10(label):
        a = arms.get(label, {}).get("by_kind", {}).get("assoc", {})
        return a.get("hit@10")

    def multi_cov10(label):
        m = arms.get(label, {}).get("multi_answer", {})
        return m.get("coverage@10")

    router_labels = sorted([l for l in arms if l.startswith("router")])
    verdict = {
        "baseline_assoc_hit@1": assoc_hit1("e5+bm25"),
        "baseline_assoc_hit@10": assoc_hit10("e5+bm25"),
        "baseline_multi_cov@10": multi_cov10("e5+bm25"),
        "router_sizes": {l: {"assoc_hit@1": assoc_hit1(l), "assoc_hit@10": assoc_hit10(l),
                             "multi_cov@10": multi_cov10(l)} for l in router_labels},
    }
    # H1: point estimates are misleading on a small held-out — use a PAIRED bootstrap
    # (per-query B-A differences) to decide whether any apparent edge is real.
    if router_labels:
        b_cov = multi_cov10("e5+bm25") or 0
        best_router_cov = max((multi_cov10(l) or 0) for l in router_labels)
        verdict["H1_multi_router_beats_baseline"] = best_router_cov > b_cov
        # paired tests vs the e5+bm25 baseline, per router size, for symptom + assoc
        paired = {}
        for l in router_labels:
            pf = f"preds_{l}.jsonl"
            paired[l] = {
                f"{kind}_hit@{k}": paired_bootstrap("preds_baseline.jsonl", pf, kind, k)
                for kind in ("symptom", "assoc") for k in (1, 10)
            }
        verdict["paired_vs_baseline"] = paired
        # H1 is "supported" only if SOME router significantly beats the baseline on assoc
        verdict["H1_assoc_router_beats_baseline"] = any(
            (paired[l].get("assoc_hit@10") or {}).get("significant") and
            (paired[l].get("assoc_hit@10") or {}).get("mean", 0) > 0
            for l in router_labels)
    # H2: plateau — report assoc@10 by size for inspection
    if len(router_labels) >= 2:
        verdict["H2_assoc_hit@10_by_size"] = {l: assoc_hit10(l) for l in router_labels}
    # Arm C
    for cx in ("CxA", "CxB"):
        cls = [l for l in arms if l.startswith(cx)]
        if cls:
            verdict[f"{cx}_multi_cov@10"] = {l: multi_cov10(l) for l in cls}

    out["verdict"] = verdict

    (RES / "results.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"-> {RES / 'results.json'}")
    print("arms present:", list(arms.keys()))
    print(json.dumps(verdict, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
