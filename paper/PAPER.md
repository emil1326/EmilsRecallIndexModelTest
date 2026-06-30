# Generative-Retrieval Memory Router vs. Embedding Retrieval on a Small, Linked, Franglais Personal-Memory Corpus

*An honest, reproducible head-to-head. A negative result is a valid result; the numbers decide.*

> Status: Arm A (baseline) and Arm C (C×A) complete; Arm B (0.5B router) inference in progress —
> its numbers fill into §5.2 / §6 / §7 on completion. Larger router sizes (1.5B/3B) are not feasible
> on the available DirectML stack (§10).

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

### 4.2 Train anchors (verbatim) vs. evaluation queries (generated)
Two things are deliberately kept separate so the evaluation measures real generalization:

- **Train anchors (verbatim, train-only).** `build_corpus.mjs --anchors-only` emits every
  `title→slug`, `summary→slug`, and **`assoc`** (`A.summary → B`) pair as **training** data:
  **4,284 anchors** (672 / 672 / 2,940). These are how the model *learns* the corpus + its link
  graph. **No verbatim text is ever held out for eval.**
- **Evaluation queries (generated, never verbatim).** The held-out set is generated by a 28-agent
  **Sonnet** workflow as queries that contain **zero note-verbatim text**, in two kinds:
  - **symptom** — a problem/symptom-vocabulary question for note *N* (gold = *N*), deliberately in
    *different* words than the title/summary (the cause↔symptom gap embedding cosine struggles with);
  - **assoc** — a genuine **independent second-hop** question: given *N* links *B*, a question someone
    facing *N*'s situation would ask whose answer is the *linked* note *B*, **without quoting** *N* or *B*
    (gold = *B*, source = *N*). At scoring the **source note A is excluded** from candidates, so we
    measure *reaching B*, not "ranking B above its own text."

A disjoint **20 %** of the generated queries is the held-out eval; the rest augment train. Counts:
**1,031 held-out** (656 symptom / 375 assoc), **4,345 train queries**, **8,629 total train**.
**Verified:** held-out query text never appears in train (leak = **0**); every slug is anchored in train.

### 4.3 Why this design matters
Two failure modes are avoided by construction. (1) If a held-out query is a note's *verbatim* summary,
the query *is* the document and any retriever scores HIT@1 ≈ 1.0 — measuring nothing. (2) If an
associative query is the source note's own text (`A.summary → B`), cosine returns A first (so the gold
B is structurally never rank-1), and a trained router can simply *memorise* the pair. Generating
non-verbatim symptom-side and independent second-hop queries, and excluding the source note A at
scoring, removes both — so every arm is measured on genuine generalization.

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
|gold| (multi-answer), reported per held-out kind (**symptom / assoc**) and for multi-answer,
with **95 % bootstrap CIs**. The whole held-out is novel-phrasing (no verbatim text), and the
associative subset excludes the source note A at scoring (§4.2). Same metric code for every arm.

## 5. Results

### 5.1 Arm A — embedding baseline (e5-small + BM25, weight tuned on train) — CLEAN held-out

| Subset | HIT@1 | HIT@4 | HIT@6 | HIT@10 | MRR |
|---|---|---|---|---|---|
| **symptom** (656, cause↔symptom gap) | 0.401 | 0.585 | 0.624 | 0.669 | 0.492 |
| **assoc** (375, independent 2-hop, A excluded) | 0.275 | 0.459 | 0.509 | 0.579 | 0.374 |
| overall single (1,031) | 0.355 | 0.539 | 0.582 | 0.636 | 0.449 |

| Multi-answer | cov@1 | cov@4 | cov@6 | cov@10 |
|---|---|---|---|---|
| coverage (108) | 0.173 | 0.508 | 0.601 | **0.677** |

Invalid-slug rate 0. 95 % CI HIT@1 [0.326, 0.383].

**Reading.** On the **symptom** subset the baseline gets HIT@1 ≈ 0.40 — the cause↔symptom vocab gap
genuinely hurts cosine. On **associative** (independent second-hop, source excluded) it gets HIT@1
0.275 / HIT@10 0.579 — a real target the router must beat. Multi-answer coverage@10 ≈ 0.68 is the weak
spot. Calibration: single-answer is *harder* than the reference system (symptom HIT@1 0.40 vs ≈0.76 —
the symptom queries are deliberately divorced from the notes), while multi-answer is *easier* (0.68 vs
ref 0.3–0.5, because cluster gold-sets are lexically tight); both are noted in §10.

### 5.2 Arm B — generative router (Qwen2.5-0.5B, LoRA)

| Size | symptom HIT@1 | assoc HIT@1 | assoc HIT@10 | multi cov@10 | invalid-slug |
|---|---|---|---|---|---|
| **0.5B** | *(inference running — fills in on completion)* | | | | 0 |
| 1.5B | *not run (DirectML batch-16 OOM on the 152k-vocab loss; feasible only at batch ~4 ≈ many hours; see §10)* | | | | |
| 3B | *not run (same DirectML limits)* | | | | |

The 0.5B router is LoRA-fine-tuned on the 8,629 training pairs (anchors + train queries) and ranks
slugs by length-normalised likelihood — **invalid-slug rate 0** by construction. It is scored on the
same held-out as the baseline (symptom 0.401 / assoc 0.275 to beat); numbers fill in when its inference
pass completes.

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

Bar: HIT@1 > 0.80, HIT@10 / coverage@10 > 0.999. Baseline distances:

| Subset | HIT@1 (gap to 0.80) | HIT@10 / cov@10 (gap to 0.999) |
|---|---|---|
| symptom | 0.401 (−0.40) | 0.669 (−0.33) |
| associative | 0.275 (−0.53) | 0.579 (−0.42) |
| multi-answer | — | cov@10 0.677 (−0.32) |

No arm reaches the bar on the subsets that matter: the embedding baseline is ~0.40 short of HIT@1 on
symptom queries, ~0.53 short on associative, and ~0.32 short of coverage@10. The router's distances are
filled in with its result; to "clear the bar" it would need to first beat these baseline numbers and
then close a much larger gap on top.

## 7. Verdict

- **H1 — bar set, router result pending.** The number to beat on the clean held-out is **symptom HIT@1
  0.401 / associative HIT@1 0.275** (HIT@10 0.579, MRR 0.374) / **multi-answer coverage@10 0.677**. The
  0.5B router is scored on the identical set; the honest prior is that a 0.5B model is underpowered for
  672-way slug generation, and the larger sizes that would test H1 fairly are blocked on this hardware.
- **H2 — not answerable on this hardware.** Only 0.5B is feasible via DirectML; 1.5B hits a hard
  allocator wall on the 152k-vocab cross-entropy loss and 3B likewise (§10). The size-plateau question
  needs a CUDA GPU.
- **Arm C — decomposition does NOT lift coverage.** C×A coverage@10 (0.626) is *below* the holistic
  baseline (0.677) despite a 0.98 decomposer topic-recall: on a strong multilingual retriever, splitting
  a multi-topic query and round-robin-unioning the sub-results adds noise rather than coverage.

## 8. Related work

**Generative retrieval / DSI (the architecture of Arm B).** **DSI** — Tay et al., 2022,
*Transformer Memory as a Differentiable Search Index* (arXiv 2202.06991) — trains one model to
map `query → docid`, the founding idea here. **SEAL** — Bevilacqua et al., 2022 (arXiv
2204.10628) — generates substrings as identifiers under an FM-index, the **constrained-decoding**
technique behind our slug-trie. **NCI** — Wang et al., 2022 (arXiv 2206.02743) — semantic docids
+ beam decoding for ranking. **Scaling** — Pradeep et al., 2023, *How Does Generative Retrieval
Scale to Millions of Passages?* (arXiv 2305.11841) — shows DSI degrades at scale, i.e. our tiny
~680-note corpus is the **favourable** regime.

**Identifier design & multi-answer.** *Multiview Identifiers Enhanced Generative Retrieval*
(Li et al., 2023, arXiv 2305.16675); *Generative Retrieval Meets Multi-Graded Relevance*
(arXiv 2409.18409); *Descriptive & Discriminative docids* (AAAI 2024) — relevant to emitting
**multiple ids** for multi-answer.

**Dynamic-corpus / continual update** (context for the live system, not this static test):
**DSI++** (Mehta et al., arXiv 2212.09744), **IncDSI** (arXiv 2307.10323), **PromptDSI**
(arXiv 2406.12593), **MixLoRA-DSI** (2025, arXiv 2507.09924 — rehearsal-free expandable LoRA
experts). The 2025 TOIS *Survey of Generative Information Retrieval* (RUC-NLPIR) frames the field.

**Agent / personal memory** — public benchmarks **LoCoMo** (Maharana et al., 2024), **Mem0**,
**MemoryCD**, plus 2026 surveys on memory for autonomous LLM agents — are overwhelmingly
**embedding/RAG** or generative-*reconstruction* memory, **not** DSI-style "generate the note-id".

**Baselines (Arm A).** e5 — Wang et al., 2022 (arXiv 2212.03533); multilingual-e5 (arXiv
2402.05672), with `query:`/`passage:` prefixes; BM25 — Robertson & Zaragoza, 2009. **Arm C** is
**RAG-Fusion / multi-query / sub-question (least-to-most) decomposition**, a known lever.

**The broader arc — memory in the weights.** This is the *retrieval* layer of a larger
"parametric memory" vision; the *consolidation* layer (drain working memory into parameters) is
a distinct but allied mechanism. **Titans** (Behrouz et al., arXiv 2501.00663) — a neural
long-term memory updated at **test time** by a surprise rule. **SEAL: Self-Adapting LMs** (arXiv
2506.10943) — the model generates its own finetuning data + self-edits into persistent weights.
*Do (Language) Models Need Sleep?* (arXiv 2605.26099) — an offline phase drains the KV-cache into
fast-weights before eviction. **FSC-Net** (arXiv 2511.11707) and **Nested Learning / Hope**
(multi-timescale optimisation) — hippocampus→neocortex consolidation in LLMs. Our DSI router is
one concrete instance of "route to memory held in weights."

**Positioning.** Generative retrieval is mature in IR and agent-memory is hot, but generative
retrieval used as the *index of a small, linked, personal memory*, optimised for **associative +
multi-answer** recall, is not an established line — that gap is the contribution.

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

- **Eval design dependence.** The whole comparison rests on the held-out being non-verbatim and the
  source note being excluded for associative scoring (§4.2–4.3). Both are enforced in code and verified
  (leak = 0); they are the load-bearing assumptions.
- **Calibration.** Single-answer is *harder* than the reference (symptom HIT@1 0.40 vs ≈0.76) and
  multi-answer is *easier* (cov@10 0.68 vs 0.3–0.5). Harder-than-real is the safe direction; the easy
  multi-answer (lexically tight cluster gold-sets) is the remaining calibration gap.
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

What the measured numbers already imply: the embedding baseline is a **strong, cheap default** for a
real vault — one ANN query, no per-query generation, and it sets a real bar (symptom HIT@1 0.40,
associative HIT@10 0.58, coverage@10 0.68) that leaves clear headroom on exactly the hard cases
(symptom-vocabulary lookup, two-hop association, multi-answer coverage). **Query decomposition is not
worth adopting here** — it *lowered* coverage on top of a strong multilingual retriever despite a 0.98
topic-recall, because splitting + unioning adds noise the holistic query did not have.

Whether a generative router earns a place depends on the size that this hardware could not reach: a
0.5B model is almost certainly too small for 672-way slug generation, so the meaningful test is **1.5B/3B
on a CUDA GPU**. If a larger router shows an edge, the practical shape is **hybrid, not replacement** —
embedding for recall, a router as a re-ranker on the associative/two-hop slice where cosine is weakest —
not a wholesale swap of the embedding daemon. That comparison, plus the larger-model sweep, is the
clear next experiment.
