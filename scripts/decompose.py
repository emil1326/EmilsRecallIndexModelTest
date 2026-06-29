"""Arm C — query decomposition ("separation model").

Splits a multi-answer / multi-topic query into K single-target sub-queries (few-shot, local
instruct model). Each sub-query is later retrieved independently via Arm A or Arm B and the
results are unioned -> coverage. Rationale: turn the weak regime (multi-answer coverage)
into K instances of the strong regime (single-answer @1). Established technique
(RAG-Fusion / multi-query / sub-question decomposition); the contribution is measuring it
on personal-memory multi-answer against the bar.

This script only DECOMPOSES (-> data/decomposed.jsonl). compose_c.py runs the sub-queries
through a retriever and unions them; it also reports the decomposer's topic-recall (the
unrecoverable-miss ceiling).

Usage: python scripts/decompose.py
"""
import argparse
import json
from pathlib import Path

import common

CFG = common.config()
DATA = common.path("data_dir")

FEWSHOT = """Exemple 1:
Requête: "c'est quoi le deal avec le cache invalidation pis les dependency graphs?"
{"subqueries": ["comment marche le cache invalidation", "a quoi sert un dependency graph dans un cache", "comment invalider en cascade quand un fichier change"]}

Exemple 2:
Requête: "comment optimiser les CPU vs GPU bottlenecks pis gerer les GC allocations dans Unity?"
{"subqueries": ["comment profiler un CPU bottleneck dans Unity", "comment reduire les GC allocations", "c'est quoi un GPU bottleneck sur un avatar"]}

Exemple 3:
Requête: "tout sur le feature checker pis comment il gate le contenu"
{"subqueries": ["c'est quoi le feature checker", "comment gate un toggle lewd sur avatar public", "comment l'OSC app communique avec le checker"]}"""


def decompose_query(query, k, model):
    prompt = f"""Tu décomposes une requête multi-sujets en sous-requêtes ciblées, chacune visant
UN seul aspect/note. FRANGLAIS. Maximum {k} sous-requêtes, le moins possible mais couvrant
tous les sujets distincts de la requête.

{FEWSHOT}

Maintenant décompose:
Requête: "{query}"
Réponds en JSON: {{"subqueries": ["...", "..."]}}"""
    try:
        out = common.ollama_json(prompt, model=model, think=False,
                                 options={"num_predict": 30 + 30 * k, "temperature": 0.4})
        subs = out.get("subqueries", []) if isinstance(out, dict) else []
        subs = [str(s).strip() for s in subs if str(s).strip()][:k]
        return subs or [query]
    except Exception:  # noqa: BLE001
        return [query]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default=CFG["arm_c"]["decompose_model"])
    ap.add_argument("--k", type=int, default=CFG["arm_c"]["max_subqueries"])
    args = ap.parse_args()
    common.set_seed()

    mg = common.read_jsonl(DATA / "multigold.jsonl")
    rows = []
    for i, p in enumerate(mg):
        subs = decompose_query(p["query"], args.k, args.model)
        rows.append({"query": p["query"], "subqueries": subs, "gold": p["slugs"],
                     "kind": "multi", "subtype": p.get("subtype", "")})
        if (i + 1) % 25 == 0:
            print(f"  decomposed {i+1}/{len(mg)}", flush=True)
    common.write_jsonl(DATA / "decomposed.jsonl", rows)
    avg = round(sum(len(r["subqueries"]) for r in rows) / max(1, len(rows)), 2)
    report = {"model": args.model, "max_k": args.k, "queries": len(rows), "avg_subqueries": avg}
    (common.path("results_dir") / "decompose_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2), flush=True)
    print("sample:", rows[0]["query"], "->", rows[0]["subqueries"], flush=True)


if __name__ == "__main__":
    main()
