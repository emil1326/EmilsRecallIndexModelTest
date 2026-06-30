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
from pathlib import Path

import common

RES = common.path("results_dir")
BAR = common.config()["metrics"]["bar"]


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
    # H1: best router beats baseline on assoc + multi?
    if router_labels:
        b_assoc = assoc_hit10("e5+bm25") or 0
        best_router_assoc = max((assoc_hit10(l) or 0) for l in router_labels)
        verdict["H1_assoc_router_beats_baseline"] = best_router_assoc > b_assoc
        b_cov = multi_cov10("e5+bm25") or 0
        best_router_cov = max((multi_cov10(l) or 0) for l in router_labels)
        verdict["H1_multi_router_beats_baseline"] = best_router_cov > b_cov
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
