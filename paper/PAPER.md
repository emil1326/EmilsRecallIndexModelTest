# Generative-Retrieval Memory Router vs. Embedding Retrieval on a Small, Linked, Franglais Personal-Memory Corpus

*An honest, reproducible head-to-head. A negative result is a valid result; the numbers decide.*

> Status: Arm A (baseline), Arm B generative router at **0.5B and 1.5B**, and Arm C (C×A) are run and
> scored on the same clean held-out. **3B is pending** (one more overnight run on the same hardware) —
> it is the point that tests whether the sharp 0.5B→1.5B scaling plateaus. Numbers below are final for
> 0.5B/1.5B; §5.2/§6/§7 note where the 3B point will land.

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
valid slugs. The synthetic corpus is shareable and committed. **Finding:** the result is size-dependent
and it turns on the associative case. At **0.5B** the router loses overall (symptom and
multi-answer) and only ties on associative. At **1.5B** it **decisively beats the baseline
on associative two-hop recall** — paired HIT@1 +0.224 and HIT@10 +0.299 (both 95 % CIs clear
of zero) — and wins symptom HIT@10, ties symptom HIT@1, while still losing multi-answer
coverage (0.579 vs 0.677). So **H1 is partially supported** (associative yes, multi-answer no),
and the associative advantage **scales sharply with size** (HIT@10 0.640→0.877 across
0.5B→1.5B) — i.e. **no plateau is visible yet**, which is the opposite of what H2 predicted; the
pending 3B point tests whether it saturates. The router still clears neither absolute bar. Query
decomposition (Arm C) *lowered* coverage. The comparison is deliberately asymmetric — the router
was fine-tuned on the corpus's link graph, the baseline is zero-shot on it — so the associative
win means a router that *learned* the associations generalizes to novel second-hop phrasings that
cosine similarity cannot bridge.

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

### 5.2 Arm B — generative router (Qwen2.5, LoRA at 0.5B and 1.5B)

Each router is LoRA-fine-tuned on the 8,629 training pairs (anchors + train queries) and ranks every
valid slug by length-normalised likelihood — **invalid-slug rate 0** by construction, no hallucinated
ids possible. Scored on the identical clean held-out as the baseline, same metric code.

**Per-subset scores (single-answer):**

| Size | symptom H@1 | symptom H@10 | assoc H@1 | assoc H@10 | assoc MRR | multi cov@10 | invalid |
|---|---|---|---|---|---|---|---|
| baseline A | 0.401 | 0.669 | 0.275 | 0.579 | 0.374 | **0.677** | 0 |
| **0.5B** | 0.178 | 0.593 | 0.245 | 0.640 | 0.360 | 0.493 | 0 |
| **1.5B** | 0.364 | **0.794** | **0.499** | **0.877** | **0.617** | 0.579 | 0 |
| 3B | *pending — one overnight run; tests whether the 0.5B→1.5B climb plateaus (H2)* | | | | | | |

**Reading — head-to-head vs. the baseline (paired bootstrap on per-query B−A differences).**

At **0.5B** the router *loses overall*: symptom HIT@1 paired −0.223 (95 % CI [−0.271, −0.178], baseline
decisively better), multi-answer coverage 0.493 vs 0.677, and associative is a **statistical tie**
(HIT@1 CI [−0.091, +0.035] includes 0; HIT@10 +0.061 with lower bound at 0.000 — directional, within
noise). A 0.5B model is simply underpowered for 672-way slug generation.

At **1.5B the picture flips on exactly the hypothesised axis** — and the effect is paired-significant:

| subset · metric | paired B−A | 95 % CI | verdict |
|---|---|---|---|
| **associative HIT@1** | **+0.224** | [+0.160, +0.291] | **router wins** |
| **associative HIT@10** | **+0.299** | [+0.245, +0.355] | **router wins** |
| **symptom HIT@10** | **+0.125** | [+0.079, +0.171] | **router wins** |
| symptom HIT@1 | −0.037 | [−0.088, +0.015] | tie (caught up from −0.223) |
| multi-answer cov@10 | 0.579 vs 0.677 | — | baseline still wins |

So **H1 is partially supported**: on **associative two-hop recall the 1.5B router beats the baseline
decisively** (HIT@1 0.499 vs 0.275, HIT@10 0.877 vs 0.579, both CIs clear of zero), it also wins symptom
HIT@10 and pulls level on symptom HIT@1, **but it still loses multi-answer coverage** (0.579 vs 0.677) —
that half of H1 is not supported. The scaling is steep: associative HIT@10 climbs **0.640 → 0.877** and
HIT@1 **0.245 → 0.499** across a single size step, so **no plateau is visible between 0.5B and 1.5B**
(the 3B point tests saturation; §5.2 table).

**Why it wins — state it plainly.** The comparison is asymmetric by design: the router is fine-tuned on
the corpus's `[[wikilink]]` graph, the embedding baseline is zero-shot on it. So the associative win is
precisely *"a model that has learned the association graph generalises to **novel** second-hop phrasings
that cosine similarity can't bridge"* — not "generation reasons better in the abstract." Spot-checks
confirm the mechanism is real, not a degenerate shortcut: e.g. *"gérer soi-même son infra sécurisée à la
maison, c'est réaliste?"* → `heberger-chez-moi-plutot-que` at rank 1; *"les valeurs de mon tool changent
tout le temps, hardcode ou…"* → `hard-coded-vs-data-driven` at rank 1 — the source note is excluded and
the query never quotes it. Note the source-A exclusion (§4.2) removes a strong distractor and therefore
*helps the baseline's* associative score, so the measured router win is if anything conservative.

The one structural guarantee at every size is **invalid-slug rate 0**: constrained likelihood-ranking
can never emit an id that isn't a real note.

### 5.3 Arm C — decomposition × {A, B} (multi-answer coverage)

| Arm | cov@1 | cov@4 | cov@6 | cov@10 | decomposer topic-recall |
|---|---|---|---|---|---|
| **A** (no decomposition) | 0.173 | 0.508 | 0.601 | **0.677** | — |
| **C×A** (decompose → e5+BM25 → union) | 0.148 | 0.434 | 0.509 | 0.580 | **0.977** |
| C×B | *not run — see below* | | | | |

C×B (decompose → route each sub-query through the router → union) was **not run**: it cannot plausibly
clear the bar. Arm B's *best* standalone multi-answer coverage@10 (0.579 at 1.5B) is still below Arm A's
(0.677), and C×A shows decomposition *lowers* coverage on this corpus — so composing the weaker
retriever behind the harmful decomposer has no path to a win. Running it would only spend GPU to
confirm a foregone negative. (Multi-answer is the one axis where the router does not beat the baseline,
so it is also the one axis where a router-based composition is least promising.)

**Decomposition did not help.** On matched footing (same 108 multi-queries, same current baseline
retriever), C×A coverage@10 (0.580) is *well below* running the holistic query straight through the
baseline (0.677) — a ~0.10 drop — even though the decomposer's topic-recall is excellent (0.977 — it
rarely misses a sub-topic). The multilingual e5 baseline already handles the multi-topic query well;
splitting it into ~3.15 sub-queries and round-robin-unioning the top hits added noise rather than
coverage. A clean negative for decomposition on this corpus.

## 6. Distance to the bar (per subset)

Bar: HIT@1 > 0.80, HIT@10 / coverage@10 > 0.999. Best-of-each distances (router = 1.5B):

| Subset | HIT@1: A / 1.5B (gap to 0.80) | HIT@10 or cov@10: A / 1.5B (gap to 0.999) |
|---|---|---|
| symptom | 0.401 / 0.364 (−0.40 / −0.44) | 0.669 / **0.794** (−0.33 / −0.21) |
| associative | 0.275 / **0.499** (−0.53 / −0.30) | 0.579 / **0.877** (−0.42 / −0.12) |
| multi-answer | — | cov@10 **0.677** / 0.579 (−0.32 / −0.42) |

**The 1.5B router is now the closest arm to the bar on the associative axis** — it more than halves the
HIT@10 gap (−0.42 → −0.12) and cuts the HIT@1 gap (−0.53 → −0.30) — and on symptom HIT@10. **But no arm
clears the absolute bar anywhere**: associative HIT@1 0.499 is still short of 0.80, and 0.877 short of
0.999. Beating the bar-setter (the embedding baseline) is real and paired-significant; *reaching* the
north-star (near-perfect per-subset precision) remains out of range at this corpus and model size.

## 7. Verdict

- **H1 — partially supported, and it is size-dependent.** At **0.5B** the router loses overall (symptom
  and multi-answer) and only ties associative — a 0.5B model is underpowered for 672-way slug generation.
  At **1.5B it decisively beats the embedding baseline on associative two-hop recall**: paired HIT@1
  +0.224 (95 % CI [+0.160, +0.291]) and HIT@10 +0.299 ([+0.245, +0.355]), both clear of zero; it also
  wins symptom HIT@10 (+0.125 [+0.079, +0.171]) and ties symptom HIT@1. This is the hypothesis landing on
  its main axis — the router, having *learned* the corpus's link graph, generalises to novel second-hop
  phrasings that zero-shot cosine cannot bridge (§5.2). **But the multi-answer half of H1 is not
  supported**: coverage@10 stays 0.579 vs 0.677. Net: H1 holds for associative, fails for multi-answer.
- **H2 — no plateau observed between 0.5B and 1.5B; it *refutes* the plateau so far.** H2 predicted recall
  would *plateau* with size on a corpus this small. Instead the associative advantage climbs steeply
  (HIT@10 0.640 → 0.877, HIT@1 0.245 → 0.499 over one size step). Two rising points are not a plateau —
  they postpone the question. **The pending 3B run is exactly the test**: if it saturates near 1.5B, H2 is
  supported; if it keeps climbing, H2 is refuted. (Feasible now that the DirectML 152k-vocab loss OOM is
  fixed with a completion-only loss, §10; a full run is overnight on the same card.)
- **Absolute bar — still unmet by every arm.** Beating the bar-setter ≠ reaching the north-star: the best
  associative HIT@1 is 0.499 (bar 0.80) and HIT@10 0.877 (bar 0.999). The relative win is real; the
  precision target is not yet in range (§6).
- **Arm C — decomposition does NOT lift coverage.** C×A coverage@10 (0.580) is *below* the holistic
  baseline (0.677) despite a 0.977 decomposer topic-recall: on a strong multilingual retriever, splitting
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
- **Small held-out set** (1,031 single / 108 multi) → finite CIs; the 0.999 bar is coarse.
  Comparisons in §5.2 use a *paired* bootstrap (per-query B−A differences) rather than comparing
  marginal CIs, so a real effect of a few points is detectable despite the set's size.
- **Associative gold is LLM-judged.** The independent second-hop queries and their gold targets are
  written by the Sonnet workflow; a wrong gold annotation would penalise both arms equally (same
  queries, same metric code), so it does not bias A vs B, but it does add label noise to the absolute
  associative numbers.
- **The comparison is asymmetric — stated, not hidden.** The router is fine-tuned on the corpus link
  graph; the baseline is zero-shot on it. This is the intended test (can a router *learn* the memory's
  associations?), not an unfair setup — but the associative win must be read as "learned-graph
  generalisation to novel phrasings," not "generation reasons better." The source-A exclusion (§4.2)
  removes a distractor and *helps* the baseline, so the measured router margin is conservative.
- **Single run per size, one seed.** Each router size is one LoRA run at seed 42; no seed variance is
  reported. The 0.5B→1.5B jump is far larger than plausible seed noise, but the exact magnitudes carry
  single-run uncertainty on top of the reported bootstrap CIs.
- **DirectML / RDNA4 limits shaped the sweep.** The 152k-vocab cross-entropy OOM'd DirectML above
  batch ~4; a **completion-only loss** (run the LM head on the slug tokens only, never materialising the
  `[B,L,152k]` fp32 tensor) fixed it, so **0.5B and 1.5B both trained and scored end-to-end on the
  RX 9070 XT; 3B is a pending overnight run on the same card.** Separately, several hard power-offs
  (instant cut, no BSOD/WHEA/thermal log) occurred under sustained DirectML compute — consistent with
  the RDNA4 card's sharp transient spikes tripping the 850 W PSU's OCP; this is electrical, not a
  software/VRAM issue, and the mitigation is an Adrenalin power-limit/undervolt plus a single gentle
  long-running process (avoid rapid load/reload churn). A CUDA GPU would remove both the allocator quirk
  and the hardware-stability risk and is the clean path to the full 0.5/1.5/3B curve. These are
  *engineering* constraints on completing H2, not methodological threats to the A/B comparison.

## 11. Implications for a real personal-memory system

What the measured numbers already imply: the embedding baseline is a **strong, cheap default** for a
real vault — one ANN query, no per-query generation, and it sets a real bar (symptom HIT@1 0.40,
associative HIT@10 0.58, coverage@10 0.68) that leaves clear headroom on exactly the hard cases
(symptom-vocabulary lookup, two-hop association, multi-answer coverage). **Query decomposition is not
worth adopting here** — it *lowered* coverage (0.677 → 0.580) on top of a strong multilingual retriever
despite a 0.977 topic-recall, because splitting + unioning adds noise the holistic query did not have.

And a generative router **earns a place at 1.5B — as a re-ranker on the associative slice, not a
replacement.** The 0.5B router is too small to win (it loses symptom and multi-answer, ties associative),
but at 1.5B it turns that tie into a decisive, paired-significant win exactly where cosine is documented
to be weakest: associative two-hop recall (HIT@1 0.499 vs 0.275, HIT@10 0.877 vs 0.579). The practical
shape this points to is **hybrid**: keep the cheap embedding daemon for broad recall and multi-answer
coverage (where it still wins), and fire a small learned router on the **associative / two-hop** slice —
the queries whose answer is a *linked* note rather than a lexically similar one. The router's cost
(per-query generation over a slug trie, invalid-slug rate 0) is justified precisely there and nowhere
else. Two open questions remain before productionising: (1) does the associative advantage keep climbing
or plateau at 3B (the pending run — H2); and (2) it must be **kept fresh** as the vault grows, which is
the consolidation problem — periodically re-fold new links into the weights (LoRA-merge, not full
retrain). The multi-answer gap and the still-unmet absolute bar say the embedding baseline is not going
anywhere; the router is a targeted specialist, and the experiment shows it becomes a *good* one with size.
