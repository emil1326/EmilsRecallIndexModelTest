# EmilsRecallIndex — Generative-retrieval memory router vs embedding retrieval

A self-contained, reproducible experiment testing whether a small LLM fine-tuned as a
**generative retriever** (query → note-slug, à la DSI / Differentiable Search Index)
can beat a strong **embedding-retrieval** baseline (`multilingual-e5-small` + BM25) on a
small, densely-linked, *franglais* personal-memory corpus — **especially on associative
("two-hop") and multi-answer queries**, where embedding retrieval is documented to be weak.

Everything here runs on a synthetic corpus (no real personal data), so the whole repo is
shareable. See **[`paper/PAPER.md`](paper/PAPER.md)** for the writeup and verdict, and
**[`results/results.json`](results/results.json)** for the raw numbers.

> Full brief: [`EXPERIMENT.md`](EXPERIMENT.md).

## The three arms

| Arm | What | Runs on |
|-----|------|---------|
| **A** | Embedding retrieval baseline — e5-small dense + BM25 hybrid (the bar to beat) | CPU |
| **B** | Generative router (DSI) — LoRA fine-tune, `query → slug`; inference ranks every valid slug by likelihood (0 hallucinated ids) | AMD RX 9070 XT via **DirectML** |
| **C** | Query decomposer — splits a multi-answer query into K single-target sub-queries, composed in front of A *or* B | Ollama (local) + A/B |

## The bar (north-star)

The goal isn't merely to beat the baseline — it's the most precise personal-memory
retrieval achievable. Target, on every subset: **HIT@1 > 0.80** and **HIT@10 / coverage@10
> 0.999**. The paper reports the distance to this bar for each arm × model-size × subset.

## Layout

```
EXPERIMENT.md              the full brief
vault-stats.json           anonymous structural stats of the real vault (counts only)
configs/experiment.json    single source of truth: seeds, models, hyperparams, paths
corpus/                    synthetic vault generator + generated <slug>.md notes
scripts/
  common.py                shared utils: config, HF-cache redirect, seeding, Ollama client
  gen_corpus.py            local-LLM corpus generator (fallback) + link graph + validation
  assemble_corpus.py       merge Sonnet-workflow notes + conversational seed notes → vault
  build_corpus.mjs         (query→slug) pair builder — train/heldout/slugs, no-leak guarantees
  build_multigold.py       multi-answer gold sets (coverage@k) from the link graph
  augment.py               K paraphrase queries per train note (dedup vs held-out)
  baseline_embed.py        Arm A: e5 + BM25 hybrid retrieval
  train_router.py          Arm B: LoRA training (query→slug)
  infer_router.py          Arm B: rank every valid slug by likelihood (no hallucinated ids)
  router_common.py         shared prompt/target format, slug trie, likelihood ranking
  retrievers.py            reusable EmbedRetriever (A) + RouterRetriever (B) for Arm C
  decompose.py             Arm C: few-shot query decomposition (multi → K sub-queries)
  compose_c.py             Arm C: union sub-query retrievals + decomposer topic-recall
  eval.py                  shared metric harness: HIT/MRR/coverage@k, subsets, pair-kinds
  aggregate_results.py     collect all arms → results.json + H1/H2/Arm-C verdicts
  setup_directml.py        DirectML GPU smoke-test
  run_sweep.sh             unattended Arm B+C sweep (VRAM-guarded, single-consumer)
corpus/seed_notes.jsonl    Emil's 12 conversational, opinionated seed notes (voice anchors)
data/                      train.jsonl, heldout.jsonl, multigold.jsonl, slugs.txt, preds_*.jsonl
results/                   results.json + per-arm metric dumps + corpus/build stats
paper/PAPER.md             the writeup: method, results, distance-to-bar, verdict, threats
```

## Reproduce

Prereqs: Python 3.10, Node 22, a running [Ollama](https://ollama.com) with the configured
models pulled (`gemma4:e2b`, `qwen3.5:4b/9b`), and — for Arm B — an AMD GPU with DirectML.

> **AMD RDNA4 (gfx1201) GPU note.** The stock Ollama installer ships ROCm 6.4.2 and silently
> falls back to CPU on the RX 9070 XT. **Update Ollama to ≥ 0.30.11** (bundles ROCm v7.1) —
> it then auto-detects the card with zero env vars. No driver update or third-party build
> needed. (This repo's results used Ollama 0.30.11.)

```bash
# 1. CPU stack (baseline, eval, generation orchestration, Arm C)
python -m pip install -r requirements.txt

# 2. Corpus: the committed corpus/ is the one used. To regenerate, the workflow is
#    conversational seed notes (corpus/seed_notes.jsonl) + a Sonnet multi-agent expansion
#    -> corpus/generated_notes.json, then:
python scripts/assemble_corpus.py            # merge + slugs + links + validate -> corpus/vault
#    (scripts/gen_corpus.py is a pure-local-LLM fallback generator.)

# 3. Build (query→slug) pairs + the multi-answer gold set + augmentation
node scripts/build_corpus.mjs --vault corpus/vault
python scripts/build_multigold.py
python scripts/augment.py

# 4. Arm A baseline + eval
python scripts/baseline_embed.py
python scripts/eval.py --preds data/preds_baseline.jsonl --arm A --label e5+bm25

# 5. Arm B + Arm C: one unattended, VRAM-guarded sweep (separate DirectML venv)
py -3.10 -m venv .venv-dml
.venv-dml/Scripts/python -m pip install -r requirements-directml.txt
.venv-dml/Scripts/python scripts/setup_directml.py     # GPU smoke-test (run once)
python scripts/decompose.py                            # Arm C sub-queries (Ollama)
SIZES="0.5B 1.5B" EPOCHS=4 bash scripts/run_sweep.sh   # train→infer→eval per size, + Arm C, + aggregate
```

`run_sweep.sh` enforces a single GPU consumer, caps VRAM ≤10 GB, and waits for ≥12 GB free
before each step. All randomness is seeded from `configs/experiment.json` (`seed: 42`); model
downloads cache under `.cache/huggingface` on the data drive (not C:).

---

*Part of Emil's personal-memory tooling — the production system this probes is an embedding
daemon over a real franglais vault. This experiment asks whether a generative router would
serve that vault better on its weak spots.*
