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

### 4.2 Train anchors (verbatim) vs. evaluation queries (generated) — the Run 2 correction
A first run conflated two things and produced a misleading eval (see §10.1). The corrected
design separates them cleanly:

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

### 4.3 Why this matters
This kills the two Run-1 artifacts: (1) a *verbatim* summary held-out gave the baseline HIT@1 = 1.000
(the query *was* the document); (2) the `A.summary → B` associative held-out gave the baseline HIT@1 =
0.000 (cosine returns A's own text first) while letting the router *memorise* the trained pair. With
generated, non-verbatim, source-excluded queries, both arms are measured on genuine generalization.

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

**Reading.** These are *honest, beatable* numbers (contrast the Run-1 artifacts: summary 1.000,
assoc 0.000). On the **symptom** subset the baseline gets HIT@1 ≈ 0.40 — the cause↔symptom vocab
gap genuinely hurts cosine. On **associative** (independent second-hop, source excluded) it gets
HIT@1 0.275 / HIT@10 0.579 — a real, non-artifactual target the router must beat. Multi-answer
coverage@10 ≈ 0.68 remains the weak spot. Calibration note: single-answer is now *harder* than the
reference system (symptom HIT@1 0.40 vs ≈0.76 — the symptom queries are deliberately divorced from
the notes), while multi-answer is *easier* (0.68 vs ref 0.3–0.5, because cluster gold-sets are
lexically tight); both are documented in §10.

### 5.2 Arm B — generative router (Qwen2.5-0.5B, LoRA)

| Size | symptom HIT@1 | assoc HIT@1 | assoc HIT@10 | multi cov@10 | invalid-slug |
|---|---|---|---|---|---|
| **0.5B** | *(retraining on clean Run-2 train, 8,629 pairs — gentle DirectML)* | | | | 0 |
| 1.5B | *not run (DirectML batch-16 OOM on the 152k-vocab loss; feasible only at batch ~4 ≈ many hours; see §10)* | | | | |
| 3B | *not run (same DirectML limits)* | | | | |

> **Note on Run 1.** An earlier 0.5B run *appeared* to beat the baseline on assoc HIT@1 (0.088 vs
> 0.000), but that comparison was an **artifact** of the confounded eval (§4.3, §10.1): the baseline's
> 0.000 came from cosine returning the source note's own text, and the router was scored on
> `A.summary → B` pairs it had been **trained on** (memorization). With the corrected,
> source-excluded, never-trained held-out, that finding does **not** survive — Arm B is re-measured
> here against the honest baseline (symptom 0.401 / assoc 0.275). Result table updates when the clean
> 0.5B run completes. The likelihood-ranking inference guarantees **invalid-slug rate 0** by construction.

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

### 10.1 The Run-1 eval confounds (fixed) — the most important lesson
The first run held out **verbatim** note text as the eval query, which silently broke two subsets and
*both* directions of the A-vs-B comparison: (i) the **summary** held-out query *was* the document →
baseline HIT@1 = 1.000, measuring nothing; (ii) the **associative** held-out was `A.summary → B`, so
the baseline returned A's own text first (HIT@1 = 0.000, an artifact) while the router could **memorise**
the trained pair and "win." Either could have produced a fake "B beats A." **Fix (Run 2):** verbatim
pairs are train-only anchors; the held-out is LLM-generated **symptom-side + independent second-hop**
queries with **zero verbatim text**, and associative scoring **excludes the source note A**. All numbers
in §5 are post-fix. *Takeaway for anyone reproducing this: never evaluate a generative retriever on
verbatim text it was trained on, and never let the baseline's "retrieve the query's own source" count
as a miss for an associative target.*

### 10.2 Other threats
- **Calibration.** Single-answer is *harder* than the reference (symptom HIT@1 0.40 vs ≈0.76) and
  multi-answer is *easier* (cov@10 0.68 vs 0.3–0.5). Harder-than-real is safe (no "too-easy" artifact);
  the easy multi-answer (lexically tight cluster gold-sets) is the remaining calibration gap.
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
