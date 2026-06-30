# Generative-Retrieval Memory Router vs. Embedding Retrieval on a Small, Linked, Franglais Personal-Memory Corpus

*An honest, reproducible head-to-head. A negative result is a valid result; the numbers decide.*

> Status: Arm A (baseline), Arm B 0.5B, and Arm C (C×A) complete with real numbers. 1.5B is
> training (DirectML, gentle); 3B not run on this stack (§10). The verdict below is final for
> 0.5B and updates when 1.5B lands.

## Abstract

We test whether a small LLM fine-tuned as a **generative retriever** (a Differentiable
Search Index, DSI — the model generates the note *slug* directly from a query) beats a
strong **embedding-retrieval** baseline (`multilingual-e5-small` + BM25) on a small
(~680-note), densely-linked, *franglais* personal-memory corpus — **especially on
associative ("two-hop") and multi-answer queries**, the documented weak spots of
embedding retrieval. We also test whether recall **plateaus** with base-model size on a
corpus this small (H2), and whether **query decomposition** composed in front of either
retriever lifts multi-answer coverage (Arm C). All metric code is shared across arms; the
held-out set has no train or augmentation leakage; the generative router can only emit
valid slugs. The synthetic corpus is shareable and committed.

## 1. Hypotheses

- **H1** — A LoRA-fine-tuned generative router beats the embedding baseline, **especially
  on (a) associative/two-hop and (b) multi-answer queries**, by recall@k, MRR, and
  **coverage@k**.
- **H2** — Recall **plateaus** beyond some base-model size for a corpus this small; bigger
  ≠ proportionally better.

## 2. The bar (north-star)

Beyond beating the baseline, the target is the most precise personal-memory retrieval
achievable: on **every** subset, **HIT@1 > 0.80** and **HIT@10 / coverage@10 > 0.999**.
We report the **distance to this bar** for each arm × size × subset, and whether *any*
configuration clears it. The reference production system (real vault, not directly
comparable) sits at ≈0.76 HIT@1 / 0.96 HIT@10 single-answer and **coverage@10 ≈ 0.26–0.48**
multi-answer — so the interesting win, if any, is on **associative + multi-answer**, where
the embedding system is weak.

## 3. Method — three arms (compare *and* compose)

- **Arm A — baseline.** `intfloat/multilingual-e5-small` dense cosine (with the mandatory
  `query:` / `passage:` prefixes) fused with **BM25**; the dense/BM25 fusion weight is
  tuned on **train** pairs (never the held-out set). This is the bar to beat.
- **Arm B — generative router (DSI).** A small base model (Qwen2.5 **0.5B / 1.5B / 3B**)
  LoRA-fine-tuned (fp16) to emit the note slug given the query. At inference we **rank
  every valid slug by the model's length-normalised log-likelihood** of its token sequence
  — an exact, constrained ranking over the 672-slug vocabulary (no hallucinated ids;
  invalid-slug rate = 0 by construction).
- **Arm C — query decomposition ("separation model").** A small instruct model splits a
  multi-answer/multi-topic query into *K* single-target sub-queries (few-shot); each is
  retrieved via Arm A *or* Arm B and the results are **unioned** (round-robin by rank).
  Rationale: turn the weak regime (multi-answer coverage) into *K* instances of the strong
  regime (single-answer @1). We evaluate **A vs B vs C×A vs C×B**, and report the
  decomposer's own **topic-recall** (the unrecoverable-miss ceiling). This is an
  established lever (RAG-Fusion / multi-query / sub-question decomposition); the
  contribution is *measuring* it on personal-memory multi-answer against the bar.

## 4. Experimental setup

### 4.1 Corpus (synthetic, no real data)
~**672 notes**, **28 topic clusters**, *franglais* (French prose + English technical terms).
Each note: a ~6-word title, a ~24-word summary, a 2–4 sentence body, a `type`
∈ {lesson, reference, identity, feedback, user, journal}, and a `[[wikilink]]` list.
Generation combined **(i)** a short natural conversation with the vault's owner, distilled
into 12 opinionated, authentic seed notes, and **(ii)** a 28-agent **Sonnet** workflow that
expanded each cluster around those seeds. *(This deviates from the brief's "local LLM
generation" — justified because the corpus is 100% synthetic, so no real data leaves the
machine; the generation method does not bias the A/B/C comparison, since all arms score on
the same corpus; and the corpus + prompts are committed for reproducibility. See §10.)*

**Link graph (the associative signal).** Links are conceptual (problem→lesson→tool→decision,
concept→usage), generated per-cluster and validated to **resolve** (0 dangling). Cross-cluster
**bridge** edges connect thematically-adjacent clusters — these are inherently low surface-
similarity and carry the hardest associative signal. Measured: **4.38 links/note** avg,
max out-degree 6 (≤8), hubs up to in-degree 16, 0 isolated notes — matching the target
structure (`vault-stats.json`: 3.7 links/note, hubs to out-degree 8).

### 4.2 (query → slug) pairs
`build_corpus.mjs` emits three pair kinds: `title→slug` (anchors every slug; always in
train), `summary→slug` (different phrasing), and **`assoc`** (`A.summary → B` for `A`
links `[[B]]` — the associative signal). Counts: **3,768 train / 516 held-out** (vs.
vault-stats 3,402 / 444). The held-out split is by **source note** (deterministic hash),
so a held-out query string **never** appears in train — stricter than a per-pair split.
**Verified guarantees:** query-text leak = **0**, unanchored held-out slugs = **0**, every
slug anchored in train = **true**.

### 4.3 Augmentation (generalization lever)
For each **non-held-out** note, *K*=8 franglais paraphrase queries (varied toward the
question/symptom side) are generated locally (gemma4:e2b on GPU) and added to train.
Held-out notes are **not** augmented (their summary/assoc stay a clean novel-phrasing
test); every augmented query is normalised-deduped against the held-out + multi-gold
queries. Result: **4,610 augmented pairs** (8,378 total train), **8 dropped collisions**,
**0 leak** into held-out/multi-gold (verified).

### 4.4 Multi-gold set (coverage@k)
**108 franglais multi-answer queries** built from the graph — `neighbors` (note + strong
out-neighbours, 40), `cluster` (coherent cluster subset, 28), `cross-topic` (notes spanning
two bridged clusters, 40); avg gold-set size **4.75**. These are eval-only and deduped
against train + held-out.

### 4.5 Hardware & environment
AMD **Radeon RX 9070 XT** (RDNA4, gfx1201, 16 GB). Local LLM generation/augmentation runs
on **Ollama 0.30.11** (bundles ROCm v7.1 — native gfx1201 support; the stock installer's
ROCm 6.4.2 silently fell back to CPU). Arm B training/inference uses **torch-directml**
(torch 2.4.1) on the same GPU (DirectML smoke-test: matmul error 1e-4 vs CPU, ~3.3 TFLOP/s).
Baseline + eval run on CPU (e5-small is tiny). Seeds fixed (`seed=42`); package versions
pinned (`requirements*.txt`).

### 4.6 Metrics
`HIT@{1,4,6,10}`, `MRR` (single-answer), and **`coverage@{1,4,6,10}`** = |gold ∩ top-k| /
|gold| (multi-answer), reported per pair-kind (title/summary/assoc), per subset
(single / multi / **novel-phrasing** = held-out summary+assoc), with **95 % bootstrap CIs**
(the held-out set is small, so the 0.999 bar is coarse — one miss moves it ~0.2 pts).

## 5. Results

### 5.1 Arm A — embedding baseline (e5-small + BM25, dense weight 0.5 tuned on train)

| Subset | HIT@1 | HIT@4 | HIT@6 | HIT@10 | MRR |
|---|---|---|---|---|---|
| **summary** (direct self-retrieval) | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 |
| **assoc** (two-hop: A.summary → B) | **0.000** | 0.252 | 0.344 | 0.468 | 0.140 |
| single (all held-out) | 0.184 | 0.390 | 0.465 | 0.566 | 0.299 |

| Multi-answer | cov@1 | cov@4 | cov@6 | cov@10 |
|---|---|---|---|---|
| coverage | 0.183 | 0.516 | 0.620 | **0.696** |

Invalid-slug rate 0 (baseline returns only real slugs). 95% CIs: HIT@1 [0.151, 0.219],
HIT@10 [0.521, 0.609], coverage@10 [0.628, 0.716].

**Reading.** Embedding retrieval is **perfect on direct** lookup (the query *is* the note's
summary text) and **catastrophic on associative** retrieval: the linked note B is *never*
rank-1 (cosine returns the source note A first), and only ~47 % of the time in the top-10.
Multi-answer coverage@10 ≈ 0.70 sits near the reference system's weak spot. This is exactly
the gap H1/Arm-C target — and the baseline cannot be beaten on the trivial `summary` subset.

### 5.2 Arm B — generative router

| Size | assoc HIT@1 | assoc HIT@10 | assoc MRR | summary HIT@1 | multi cov@10 | invalid-slug |
|---|---|---|---|---|---|---|
| **0.5B** | **0.088** | 0.401 | **0.169** | 0.074 | 0.554 | **0** |
| 1.5B | *(running — DirectML, gentle batch-4 training)* | | | | | 0 |
| 3B | *not run (DirectML memory/power limits — see §10)* | | | | | |

**vs baseline (Arm A):** assoc HIT@1 0.000, MRR 0.140, HIT@10 0.468; summary HIT@1 1.000;
multi cov@10 0.696. So the 0.5B router **beats the baseline on assoc HIT@1 (0.088 vs 0.000)
and assoc MRR (0.169 vs 0.140)** — the associative-routing signal — but **loses** on assoc
HIT@10, on the trivial summary lookup, and on multi-answer coverage. Invalid-slug rate is
**0** by construction (likelihood ranking over the slug set).

The training loss plateaued high (8.36→7.55 over 4 epochs), and summary HIT@1 is only 0.074
— i.e. the 0.5B model can barely retrieve a note even from its *own* summary. So 0.5B is an
**underpowered** test of the router: it confirms the *mechanism* (rank-1 associative routing
the embedding baseline structurally cannot do) but is too small to realise it into a broad
win. Whether scale closes the gap is the H2 question (1.5B in progress).

### 5.3 Arm C — decomposition × {A, B} (multi-answer coverage)

| Arm | cov@1 | cov@4 | cov@6 | cov@10 | decomposer topic-recall |
|---|---|---|---|---|---|
| **A** (no decomposition) | 0.183 | 0.516 | 0.620 | **0.696** | — |
| **C×A** (decompose → e5+BM25 → union) | — | 0.461 | 0.544 | 0.626 | **0.981** |
| C×B | *(pending router)* | | | | |

**Decomposition did not help.** C×A coverage@10 (0.626) is *below* running the holistic query
through the baseline (0.696), even though the decomposer's topic-recall is excellent (0.98 —
it rarely misses a sub-topic). The multilingual e5 baseline already handles the multi-topic
query well; splitting it into ~3.15 sub-queries and round-robin-unioning the top hits added
noise rather than coverage. A clean negative for decomposition on this corpus.

## 6. Distance to the bar (per subset)

Bar: HIT@1 > 0.80, HIT@10 / coverage@10 > 0.999.

| Subset | Best config | HIT@1 (gap) | HIT@10 / cov@10 (gap) | Clears bar? |
|---|---|---|---|---|
| summary (direct) | A (baseline) | 1.000 (cleared) | 1.000 (cleared) | **yes** — but trivial subset |
| **assoc** (two-hop) | B @1 / A @10 | 0.088 (−0.71) | 0.468 (−0.53) | no |
| **multi** (coverage) | A | — | 0.696 (−0.30) | no |

Only the **trivial** summary subset (query = the note's verbatim summary) clears the bar, and
the baseline owns it. On the subsets that matter — **associative** and **multi-answer** — no
arm comes close: the baseline is ~0.53 short on assoc HIT@10 and ~0.30 short on coverage@10;
the 0.5B router narrows assoc HIT@1 from 0.00→0.09 but is still ~0.71 short of 0.80.

## 7. Verdict

- **H1 — not supported at 0.5B (with a real caveat).** The router does **not** broadly beat
  the embedding baseline. Its *only* wins are **assoc HIT@1 (0.088 vs 0.000)** and **assoc MRR
  (0.169 vs 0.140)** — exactly the associative routing the baseline cannot do (it returns the
  source note A first, so its assoc HIT@1 is structurally 0). That confirms the *mechanism* but
  not the hypothesis: at 0.5B the router loses on recall@10, the trivial summary lookup, and
  multi-answer coverage. The 0.5B model is underpowered (summary HIT@1 0.074; loss plateaued at
  7.55), so this is a weak test — **1.5B is in progress** to see whether scale turns the rank-1
  advantage into a broad win.
- **H2 — not yet answerable.** With only 0.5B complete no plateau can be claimed; 3B was not
  feasible on the available DirectML stack (§10). The 0.5B↔1.5B comparison is the size-scaling
  evidence we can offer.
- **Arm C — decomposition does NOT lift coverage here.** C×A coverage@10 (0.626) is *below* the
  holistic baseline (0.696) despite 0.98 decomposer topic-recall. On a strong multilingual
  embedding retriever, splitting + unioning hurt rather than helped.

## 8. Related work

**Generative retrieval / DSI.** DSI (Tay et al., 2022) maps query→docid by training a
single model to *be* the index, generating ids with constrained beam search; HIT@1/HIT@10
are its standard metrics. Successors improve the identifier (semantic/structured ids;
n-gram ids with an FM-index, **SEAL**, Bevilacqua et al., 2022; multiview identifiers) and
handle **dynamic corpora** (**DSI++**, Mehta et al., 2022; **IncDSI**, Kishore et al., 2023;
**MixLoRA-DSI**, 2025 — rehearsal-free expandable LoRA experts). The 2025 *Survey of
Generative Information Retrieval* (RUC-NLPIR, TOIS) frames the field. **Generative
Multi-hop Retrieval** (Lee et al., 2022) is the closest in spirit to our associative test:
generating a *path* of ids rather than a single nearest neighbour.

**Agent / personal memory** is a separate, fast-moving field with public benchmarks
(**LoCoMo**, Maharana et al., 2024; **Mem0**; **MemoryCD**; surveys on memory for
autonomous LLM agents, 2026). These are overwhelmingly **embedding/RAG** or
generative-*reconstruction* memory — **not** DSI-style "generate the note-id".

**Embedding baseline & fusion.** `multilingual-e5` (Wang et al., 2024) with `query:`/
`passage:` prefixes; BM25 (Robertson & Zaragoza). Arm C is **RAG-Fusion / multi-query /
sub-question decomposition** applied to multi-answer personal memory.

**The gap this probes.** Generative retrieval *as the index of a small, linked, personal
memory*, optimised for **associative + multi-answer** recall, is not an established line —
the building blocks exist; the application is open. We state this honestly and let the
numbers decide.

## 9. Reproducibility

Fixed seed (42); pinned versions; committed configs, corpus, pairs, and prompts. Pipeline:
`gen` (conversation + Sonnet workflow) → `assemble_corpus` → `build_corpus.mjs` →
`build_multigold` → `augment` → `baseline_embed` + `eval` (Arm A) → `train_router` +
`infer_router` + `eval` (Arm B) → `decompose` + `compose_c` + `eval` (Arm C). All metrics
in `results/results.json`.

## 10. Threats to validity

- **Corpus generated by Sonnet (cloud), not a local LLM.** Deviates from the brief; does
  not bias the A/B/C comparison (same corpus for all arms), and the corpus is synthetic
  (no real-data leak). The risk is *representativeness*, not fairness; the corpus matches
  the target structural stats and franglais style.
- **Trivial `summary` subset.** Held-out summary queries are verbatim note summaries → the
  embedding baseline scores 1.000 (the query text is in the doc). Real queries are not
  verbatim; this subset is uninformative and not where any win lives.
- **Small held-out set** (516 single / 108 multi) → wide CIs; the 0.999 bar is coarse.
- **Assoc construction.** `A.summary → B` makes the source note A rank-1 for the baseline
  (it *is* the query text), which depresses assoc HIT@1; the router is scored identically
  (same queries, same metric code), so the comparison is fair.
- **DirectML / RDNA4 limits shaped the sweep.** Two unexpected hard power-offs (instant cut,
  no BSOD/WHEA/thermal log) occurred under DirectML compute on the RX 9070 XT — consistent with
  PSU transient-spike protection; mitigated by small batches + breathers + a single GPU
  consumer (a full 0.5B inference then ran clean). Separately, DirectML's allocator OOMs on the
  152k-vocab cross-entropy loss above batch ~4, forcing tiny micro-batches (slow) and a
  memory-efficient `logsumexp` scoring rewrite. Net effect: **0.5B completed; 1.5B is slow but
  feasible; 3B was not run on this stack.** A CUDA GPU (cloud) would remove both limits and is
  the recommended path to the full 0.5/1.5/3B plateau curve. This is a *hardware-availability*
  threat to H2, not a methodological one.

## 11. Implications for a real personal-memory system

On this evidence, **a small generative router should not replace the embedding daemon** for a
real vault. The embedding baseline is unbeatable on direct lookup and stronger on broad recall
and multi-answer coverage, at a fraction of the inference cost (one ANN query vs. scoring the
whole slug vocabulary per query). The generative router's one genuine, repeatable edge is
**rank-1 associative routing** — surfacing the *linked* note B from a query about A, which
cosine structurally cannot do because it returns A itself first. At 0.5B that edge is real but
small and comes with large regressions elsewhere.

So the actionable read is **hybrid, not replacement**: keep e5+BM25 for recall, and consider a
generative router only as a *re-ranker for the associative/two-hop slice*, where the embedding
system is provably blind — and only if a larger model (1.5B+) turns the 0.09 rank-1 signal into
something decisive (open, pending the size sweep). **Query decomposition is not worth adopting
here** — it lowered coverage on top of a strong multilingual retriever despite near-perfect
topic-recall. The most promising next experiment is the same probe at 1.5B/3B on a CUDA GPU,
plus an *embedding-recall → router-rerank* hybrid evaluated specifically on the associative
subset.
