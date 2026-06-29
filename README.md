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
| **B** | Generative router (DSI) — LoRA fine-tune, `query → slug`, constrained decode over a slug trie | AMD RX 9070 XT via **DirectML** |
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
  gen_corpus.py            (Arm 0) generate the synthetic franglais vault, seeded
  build_corpus.mjs         (query→slug) pair builder — train/heldout/slugs, no-leak guarantees
  build_multigold.py       multi-answer gold sets (coverage@k) from the link graph
  augment.py               K paraphrase queries per train note (dedup vs held-out)
  baseline_embed.py        Arm A: e5 + BM25 hybrid retrieval
  train_router.py          Arm B: LoRA training (query→slug)
  infer_router.py          Arm B: trie-constrained decoding → ranked slugs
  decompose.py             Arm C: few-shot query decomposition
  eval.py                  shared metric harness: HIT/MRR/coverage@k, subsets, pair-kinds
  setup_directml.py        DirectML install + GPU smoke-test
data/                      train.jsonl, heldout.jsonl, multigold.jsonl, slugs.txt, preds_*.jsonl
results/                   results.json + per-arm metric dumps
paper/PAPER.md             the writeup: method, results, distance-to-bar, verdict, threats
```

## Reproduce

Prereqs: Python 3.10, Node 22, a running [Ollama](https://ollama.com) with the configured
models pulled (default `qwen3.5:9b`, `nomic-embed-text`), and — for Arm B — an AMD GPU with
DirectML.

```bash
# 1. CPU stack (baseline, eval, generation orchestration, Arm C)
python -m pip install -r requirements.txt

# 2. Generate the synthetic vault (seeded, reproducible)
python scripts/gen_corpus.py

# 3. Build (query→slug) pairs + the multi-answer gold set
node scripts/build_corpus.mjs --vault corpus/vault
python scripts/build_multigold.py
python scripts/augment.py

# 4. Arm A baseline + eval
python scripts/baseline_embed.py
python scripts/eval.py --arm A

# 5. Arm B: DirectML training (separate venv) + sweep
py -3.10 -m venv .venv-dml
.venv-dml/Scripts/python -m pip install -r requirements-directml.txt
.venv-dml/Scripts/python scripts/setup_directml.py        # GPU smoke-test
.venv-dml/Scripts/python scripts/train_router.py --size 0.5B   # 1.5B, 3B
.venv-dml/Scripts/python scripts/infer_router.py --size 0.5B
python scripts/eval.py --arm B

# 6. Arm C decomposition (compose over A and B)
python scripts/decompose.py
python scripts/eval.py --arm C
```

All randomness is seeded from `configs/experiment.json` (`seed: 42`). Model downloads are
cached under `.cache/huggingface` on the data drive (not C:).

---

*Part of Emil's personal-memory tooling — the production system this probes is an embedding
daemon over a real franglais vault. This experiment asks whether a generative router would
serve that vault better on its weak spots.*
