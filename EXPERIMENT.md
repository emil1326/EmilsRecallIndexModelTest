# Experiment brief — Generative-retrieval memory router vs embedding retrieval

> **You are a fresh autonomous coding agent.** You have no prior context — this document is self-contained and complete. Do not assume knowledge of any prior conversation, of "Mira", or of any external system. Read this fully, then execute the whole sequence yourself (generate data → train → evaluate → ship a repo + a short paper). Your output is a GitHub repository and a writeup that **proves or disproves** the hypothesis below, with raw numbers. A negative result is a fully valid, valuable outcome — report it honestly.

## 1. Background

A personal-memory assistant stores a few hundred short atomic notes (one fact each), connected by a `[[wikilink]]` graph, and retrieves the relevant note(s) for a given query. The current production approach is **embedding retrieval** (dense sentence embeddings + BM25, cosine similarity). Its documented weakness: it misses **associative ("two-hop") relevance** — when a query is about note A and the genuinely relevant note is B because A links to B, cosine on A-vs-B text often fails.

This experiment tests an alternative: **generative retrieval**, a.k.a. **Differentiable Search Index (DSI)** (Tay et al., Google, 2022). Instead of embedding+nearest-neighbour, a small language model is fine-tuned to *generate the document id* (here: the note **slug**) directly from the query. The model **becomes the index**. The intuition: trained on the corpus + its link graph, the model can learn associative routing that cosine cannot.

## 2. Hypotheses (falsifiable — you must be willing to disprove them)

- **H1** — A small LLM fine-tuned as a generative retriever (query → slug) **beats a strong embedding-retrieval baseline** on a small linked personal-memory corpus, **especially on (a) associative/two-hop queries and (b) MULTI-ANSWER queries** — one query whose correct answer is *several* slugs, often **spanning more than one topic** — measured by recall@k, MRR, and **coverage@k** (did we surface the *whole* relevant set, not just one?) on a clean held-out set.
- **H2** — There is a **base-model size beyond which recall plateaus** for a corpus this small (a few hundred notes). I.e. bigger ≠ proportionally better here.

> **Multi-answer is central, not a footnote.** Real retrieval here is *often* multiple notes at once, sometimes across topics (e.g. "what do we know about X" should surface a whole cluster, not one note). **Coverage@k** (fraction of the gold set retrieved) is a first-class metric, not an afterthought. It is also the production system's **documented weak spot** (see *Reference* below: coverage@10 ≈ 0.26–0.48), so it is the prime thing the generative router must beat. Generative retrieval has a natural angle here — generate *several* candidate ids and re-rank (cf. n-gram / multiview-identifier methods) — exercise it.

## Target — the bar this is chasing (north-star)

The goal isn't *merely* to beat the baseline — it's **the most precise personal-memory retrieval achievable**. Concrete success bar, to hold on **every** benchmark subset (single-answer, multi-answer/coverage, associative, novel-phrasing):

- **HIT@1 > 0.80** — the single most-relevant note is rank 1 at least 4 times in 5.
- **HIT@10 > 0.999** — the relevant note is in the top-10 essentially always; for multi-answer, **coverage@10 > 0.999** (the *whole* gold set is in the top-10).
- Always report **@1, @4, @6, @10** (k=6 ≈ what the live hook injects per turn; @4 is a sensitive mid-point).

This bar is **demanding** — the current embedding system sits at ~**0.76 @1 / 0.96 @10** single-answer and far below on multi-answer coverage. So the experiment doesn't just report win/lose vs baseline: for **each subset × each model size**, report the **distance to (0.80 @1, 0.999 @10)** and state whether *any* configuration clears it. "How close to the most-precise-possible bar, and what would it take to clear it" is the question `PAPER.md` answers.

The experiment's value is the *answer*, not a positive answer. If embedding retrieval wins, or if size doesn't plateau, **say so with the numbers**. Cherry-picking or a strawman baseline = experiment failure.

## Reference — the real system we're probing (sanity anchor, NOT a direct comparison)

These are measured numbers from the *real* production system (an embedding daemon: `multilingual-e5-small` dense + BM25 hybrid) on the *real* vault. Your experiment runs on a **synthetic** corpus, so these are not a head-to-head — they're a **reality anchor** (a faithful synthetic baseline should land in a similar ballpark) and they pinpoint the **target weakness**.

- **Single-answer (held-out, vault):** HIT@1 ≈ **0.76**, HIT@4 ≈ **0.92**, HIT@6 ≈ **~0.94** (interpolated, not separately logged), HIT@10 ≈ **0.96**, nDCG@10 ≈ **0.78**. → **below the bar** (0.80 @1 / 0.999 @10): that gap is the target.
- **De-biased (independent LLM-judge labels):** hybrid nDCG@10 ≈ **0.82**.
- **Public BEIR (same daemon, for external comparability):** SciFact nDCG@10 **0.676**, NFCorpus **0.311**; the e5+BM25 hybrid *significantly* beats BM25 alone.
- **Multi-answer COVERAGE@10 ≈ 0.26–0.48** ← **the weak spot.** Single-answer ranking is strong; surfacing the *whole* relevant cluster is not. This is exactly what H1's multi-answer clause targets.

So: the bar for "single-answer" is already high (~0.96 HIT@10) — the generative router likely won't beat that and doesn't need to. **The interesting win, if any, is on associative + multi-answer coverage**, where the embedding system is weak. Frame the result around that.

## 3. Hardware & setup

Target machine: **AMD Radeon RX 9070 XT** (RDNA4, LLVM target `gfx1201`, 16 GB).

- **ROCm 7.2+** (first official RDNA4 support, March 2026). Native Windows ROCm is incomplete for training → use **WSL2 + ROCm 7.2** or a **Linux dual-boot** (more stable). Verify the current ROCm↔PyTorch compatibility matrix at setup time; pin versions.
- Install PyTorch with the ROCm wheel, plus `transformers`, `peft`, `accelerate`, `datasets`, `sentence-transformers` (for the baseline). **Avoid `bitsandbytes`/4-bit QLoRA** — fragile on AMD; 16 GB is plenty for **fp16 LoRA** on 0.5–3B models.
- All compute is **local/on-machine**. No data leaves the machine. No external API calls with corpus content (use a local model for any generation — e.g. Ollama via ROCm).

## 4. The corpus — SYNTHETIC, no real data

Do **not** use any real personal data. Generate a **synthetic personal-memory corpus** whose *structure* matches a real one. Target stats are in `vault-stats.json` (anonymous — counts only):

- ~**680 notes**, each: a short `title` (~6 words), a one-sentence `summary` (~24 words), a longer `body`, and a `[[links]]` list.
- **Franglais**: French prose mixed with English technical terms in the same note (this is deliberate — it stresses multilingual paraphrase).
- A **dense directed link graph**: ~**3.7 links/note** on average, with a few "hub" notes (out-degree up to ~8). **This graph is the associative signal — the #1 thing the experiment probes.** Make links *semantically meaningful* (a note links to genuinely related notes), not random — otherwise the associative test is meaningless.
- **Multi-answer gold sets (build these deliberately).** Real queries often have a *set* of correct slugs, sometimes across topics. Construct a **multi-gold held-out set** — `query → [slug, slug, …]` — from the graph: e.g. a **hub/cluster query** that should return all its members, a note + its strongly-linked neighbours, or a question that legitimately spans two topics. `build-corpus.mjs` only emits single `(query → slug)` pairs, so you must build this multi-gold set yourself. It powers **coverage@k** and the H1 multi-answer test — without it, the headline question goes unmeasured.
- High topic diversity over few notes (technical, methodological, reflective).

Generate it with a **local LLM** (so it's varied, not templated) and a fixed **seed** for reproducibility. Note format (markdown, flat frontmatter):

```
---
title: Cache analyse rebuild paresseux
summary: Le cache se reconstruit seulement sur requete, pas si le dernier cache est intact, anticipe juste avant expiration
type: lesson
links:
  - "[[analysis-cache-security-reapply]]"
  - "[[roadmap-arrow-java]]"
---
<body: 2-5 sentences expanding the fact, franglais>
```

`type` ∈ {lesson, reference, identity, feedback, user, journal}. Slugs are kebab-case, unique, and are the model's **output vocabulary**.

## Experimental arms (compare AND compose — non-exclusive)

Three arms. They are **not** mutually exclusive — C composes in front of A or B.

- **Arm A — baseline:** embedding retrieval (e5-small + BM25). The bar to beat.
- **Arm B — generative router (DSI):** the model *is* the index, `query → slug` (the main hypothesis, H1/H2).
- **Arm C — query decomposition ("separation model"):** a small model **splits a multi-answer / multi-topic query into K single-target sub-queries**, each retrieved independently (via A *or* B), results **unioned** → coverage. Rationale: it turns the *weak* regime (multi-answer coverage ≈ 0.26–0.48) into **K instances of the strong regime** (single-answer @1 ≈ 0.76). It won't be perfect, but it's leverage exactly where the system is weakest. The **2–3B** size discussed for the router fits *this* role better (decomposition is generation/reasoning, not lookup).
  - **Non-exclusive & composable:** evaluate C × {A, B}. Report both.
  - **Established technique** (RAG-Fusion / multi-query retrieval / sub-question decomposition) — so it is a *known lever*, not a novelty claim; cite it. The contribution is **measuring** it on personal-memory multi-answer against the bar.
  - **Failure modes to measure (don't hide them):** (1) *decomposition-recall ceiling* — a sub-topic the splitter misses is an unrecoverable miss, so report the splitter's own recall of the gold set's topics; (2) *cardinality* — how does it decide K / when to stop; (3) *latency* — K retrievals + one generation per query.

## 5. Pipeline — exact steps

1. **Generate the synthetic vault** → a directory of `<slug>.md` files (per §4). Commit the generator + a fixed seed so it's reproducible. The synthetic corpus *can* be committed (it's fake).
2. **Build (query → slug) pairs.** Reuse the provided **`build-corpus.mjs`** (`node build-corpus.mjs --vault <synthetic-dir>`). It emits `train.jsonl`, `heldout.jsonl`, `slugs.txt`. It builds three pair kinds:
   - `title` → slug (anchors every slug; always in train),
   - `summary` → slug (different phrasing),
   - `assoc` → for A linking [[B]], `A.summary → B` (**the associative signal**).
   It holds out a deterministic 15% of `summary`/`assoc` pairs (split by hash, **no vocab leak** — every held-out slug is anchored in train). Read its code; keep its guarantees.
3. **Augment (the generalization lever).** The deterministic corpus is small (~3.4k pairs). For each **training** note, generate **K paraphrase queries** (vary vocabulary toward the *symptom*/question side, not just the summary words) with the local LLM → add to train. **Never augment held-out queries**, and never let an augmented query duplicate a held-out one. K is a knob (try ~5–10).
4. **Train** — LoRA (fp16, PEFT) on a base model. **Sweep base size**: e.g. Qwen3-class **0.5B, 1.5B, 3B** (or nearest available). Target: emit the slug string given the query. Log the size sweep.
5. **Infer** — load base+adapter, **constrained decoding over the `slugs.txt` trie** so the model can only emit *valid* slugs (no hallucinated ids). Produce ranked top-k slugs per held-out query → `preds.jsonl`.
6. **Baseline** — implement **embedding retrieval** on the *same* synthetic corpus: `intfloat/multilingual-e5-small` (matches a real franglais setup) for dense cosine, optionally fused with BM25. Make it **genuinely strong** (correct prefixes, tuned weight) — not a strawman. Score it on the *same* held-out set.
7. **Evaluate** — `HIT@{1,4,6,10}` (k=6 ≈ live per-turn injection), `MRR`, and — **first-class** — **coverage@{1,4,6,10}** on the multi-gold set (fraction of the gold *set* retrieved in top-k; this is THE multi-answer metric). Report **per pair-kind** (title / summary / **assoc**), break out the **novel-phrasing subset** (`summary`/`assoc` held-out = real generalization), and report **single-answer vs multi-answer separately** (the win, if any, is expected on multi-answer + assoc — cf. *Reference*). Compare model (each size) vs baseline on identical inputs.
8. **Arm C — decomposition (compose, don't replace).** Build a query decomposer: a small model mapping a multi-answer/multi-topic query → a list of single-target sub-queries. **Start cheap** — few-shot prompt a local instruct model; fine-tune (the ~2–3B) only if few-shot underperforms. Run each sub-query through **Arm A and Arm B**, union the top hits, score **coverage@{1,4,6,10}** on the multi-gold held-out. Report **A vs B vs C×A vs C×B**, plus the decomposer's own **topic-recall** (the unrecoverable-miss ceiling). The question: does decomposition move multi-answer coverage toward the bar where a single retriever can't?

## 6. Validity controls — NON-NEGOTIABLE

Autonomous experiments self-deceive here. Enforce all of:

- **Clean held-out.** Held-out queries never appear in train *or* augmentation. Every held-out slug is anchored in train (no output-vocab leak). Verify and report this.
- **Apples-to-apples.** Model and baseline scored on the *exact same* held-out set, same metric code.
- **Strong baseline.** Real e5-small (+BM25), correctly configured. A weak baseline invalidates the result.
- **No hallucinated ids.** Constrained decoding over the slug trie; report any invalid-slug rate (should be 0).
- **Size sweep → plateau.** Report recall vs size; state where (if) it plateaus (H2).
- **Negative results are valid.** If the baseline wins overall or on assoc, report it plainly. The paper must state the verdict on H1/H2 either way.
- **Reproducible.** Fixed seeds, pinned package versions, committed configs. Anyone should reproduce your numbers.
- **Show the work.** The writeup includes the raw results table + methodology + threats to validity, not just a conclusion.

## Related work & prior art (position the paper — and refresh it yourself)

Snapshot as of ~June 2026 (verify and extend with your own fresh literature search — the field moves fast):

- **Generative retrieval / DSI is mature in IR.** DSI (Tay et al., 2022) maps query→docid. Successors improve the *identifier*: semantic/title ids, **n-gram ids with FM-index (SEAL)**, **multiview identifiers**, **descriptive+discriminative docids**, **multi-graded relevance**. **Multi-answer is a solved sub-problem in principle**: generate several candidate ids and re-rank.
- **Dynamic-corpus updates** (the live-memory pain) have a dedicated line: **DSI++**, **IncDSI**, **PromptDSI**, **MixLoRA-DSI (2025)** (expandable LoRA experts, rehearsal-free).
- **Agent / personal memory is a hot, separate field** with public benchmarks you can borrow for external validation: **Mem0**, **LoCoMo**, **PERMA**, **MemoryCD**, the **MemAgents (ICLR 2026)** workshop. But these are overwhelmingly **embedding/RAG** or **generative-reconstruction** memory — **not DSI-style "generate the note-id".**
- **The gap this experiment probes:** generative retrieval used *as the index of a small, linked, personal memory*, optimized for **associative + multi-answer** recall, is **not an established line**. The building blocks exist; the application is open. That's the paper's contribution claim — state it honestly (and check whether someone has since done it).

The `PAPER.md` must include a real related-work section and **cite**. If feasible, add an **external check on a public agent-memory benchmark** (e.g. LoCoMo) so the result isn't synthetic-only.

## 7. Deliverable

A **GitHub repository** containing:
- the synthetic-corpus generator (+ seed), `build-corpus.mjs`, train/infer/eval scripts, configs;
- `results.json` — all metrics: **arm (A / B / C×A / C×B) × model size × metric (HIT/coverage@{1,4,6,10}, MRR) × pair-kind (title/summary/assoc) × subset (single / multi / novel-phrasing)**. **Metrics only**; the corpus is synthetic so it's shareable too.
- **`PAPER.md`** (a few pages): hypothesis, method, **all three arms**, setup, results table, **distance to the bar (0.80 @1 / 0.999 @10) per subset**, **verdict (H1/H2 proven or disproven; does decomposition lift multi-answer coverage?)**, where size plateaus, threats to validity, and what it implies for a real personal-memory system.

Keep the repo public-shareable (no real data exists — it's all synthetic). When done, the repo URL + `PAPER.md` are the result to hand back.

## 8. Provided files

- `build-corpus.mjs` — the (query→slug) pair builder. Reuse as-is; read it to honor the held-out/no-leak guarantees.
- `vault-stats.json` — anonymous target stats for the synthetic corpus.
- `README.md` — short orientation.

You write everything else (generator, augment, train, infer, eval, paper).

---

# Precisions & clarifications (consolidated)

## 0. Evaluation requirements — the protocol every arm is held to

The comparison is only meaningful if "B beats A" can reflect *real retrieval skill* and not a measurement artifact. The single failure mode to design out is **using verbatim note text as an eval query**: it makes the baseline look trivially perfect or structurally broken, and lets a trained router win by memorization. The held-out is therefore built to these rules:

1. **No verbatim summaries in the eval set.** A held-out query that *is* the note's summary gives the embedding baseline HIT@1 = 1.000 — the query literally is the document, so it measures nothing. The eval set uses **LLM-paraphrased, symptom-side** reformulations only. Verbatim title/summary are **TRAIN-only anchors**, never held-out.

2. **Associative queries are genuine, independent second hops.** An assoc query must be a real second-hop information need **phrased independently of A's text** (LLM-generated: "a question for which B is the answer, without quoting A"), not `A.summary → B`. Building it from A's own text would (a) make the source note A rank-1 for the baseline, structurally suppressing gold B, and (b) let a router *trained* on `(A.summary → B)` win by memorizing the pair. At scoring time the **source note A is excluded from candidates**, so the metric measures *reaching B*, not "ranking B above its own source."

3. **General rule: the held-out contains ZERO note-verbatim text.** Train on anchors (verbatim title/summary) + paraphrases; **evaluate only on** held-out paraphrases, genuine second-hop questions, and multi-answer cluster queries the model never saw as text. `build-corpus.mjs` emits verbatim pairs — those are TRAIN anchors; the held-out is **built separately** by the paraphrase/decomposition generators, not by splitting verbatim pairs.

4. **Difficulty is calibrated to a real reference.** Target: the embedding baseline should land near a real personal-memory system (single HIT@1 ≈ 0.76, multi coverage@10 ≈ 0.3–0.5) so the synthetic corpus reproduces the real *hardness* — especially the symptom↔cause vocab gap. Where the baseline runs easy (lexically tight clusters), that is noted as a calibration threat rather than hidden.

The win condition (HIT@1 > 0.80, coverage@10 > 0.999) only *means* something measured on a clean, paraphrase-based held-out with the source note excluded for associative scoring.

## 1. The idea, made precise

**One sentence:** instead of retrieving notes by embedding-similarity, fine-tune a small LLM to **generate, token by token, the identifier (the `slug`) of the relevant note(s)** for a query. The model's *weights become the index* — there is no vector store and no nearest-neighbour search in this arm.

### The function being learned
- Input: a natural-language **query** (a question, a symptom, a topic).
- Output: one or more **slugs** — the filenames-minus-`.md` of notes (e.g. `kapt-incremental-breaks-mapstruct`). The set of all slugs is a **closed output vocabulary** of a few hundred strings.
- The model is literally `f(query) → ranked list of slugs`. The slug then *points* to the note body (which still lives in the vault as a file); the model does **not** generate or read note content. The unit of retrieval is the **id**, not the text.

### Training (Arm B)
- Plain **supervised fine-tuning** (next-token cross-entropy): given a `query`, the target sequence is the gold `slug` string. **No reinforcement learning, no reward model** — see `[[judge-as-eval-not-reward]]`: RL on this would Goodhart. Just `(query → slug)` pairs through a causal/seq2seq LM with **LoRA**.
- Training data = the `(query → slug)` pairs from `build-corpus.mjs` (title→slug, summary→slug, assoc) **plus** the paraphrase augmentation. See §3 for what these look like.

### Inference — constrained decoding (critical, easy to get wrong)
- A free LM would hallucinate slugs that don't exist. So decode under a **prefix trie built from the real slug list** (`slugs.txt`): at each step only tokens that continue a valid slug are allowed. The model can therefore *only* emit real ids. (This is the SEAL/FM-index technique — §2.)
- To get a **ranked top-k**, use constrained **beam search** (beam = k) or constrained sampling; the beam scores give the ranking. For **multi-answer**, the model must emit a *set* — either a delimited list of slugs in one sequence, or take the top-k beams as the set. Decide and document which.

### Evaluation (how the numbers are computed)
- For each held-out query, the arm produces a ranked slug list. Compare to the **gold slug(s)**:
  - `HIT@k` (single-answer): is the gold slug in the top-k? Report k ∈ {1,4,6,10}.
  - `coverage@k` (multi-answer): fraction of the gold *set* present in the top-k. **First-class metric** — it's the production weak spot (~0.26–0.48 @10).
  - `MRR`: 1/rank of the first correct slug.
- The **baseline (Arm A)** is scored the exact same way on the exact same held-out: embedding retrieval ranks slugs by `cosine(query, note)`; take its top-k.

### The three arms (recap, precisely)
- **A — embedding baseline:** `multilingual-e5-small` (+ optional BM25) → cosine → top-k slugs. No training. The bar to beat.
- **B — generative router (DSI):** the fine-tuned LM above. The main hypothesis.
- **C — query decomposition ("separation model"):** a small model splits a multi-answer query into K single-target sub-queries; each sub-query goes through A *or* B; union the results → coverage. Composes with A or B (evaluate C×A and C×B). Turns the weak multi-answer regime into K instances of the strong single-answer regime.

### What this is NOT (the confusions to avoid)
- **Not RAG with an LLM reader.** The LM does not read documents and write an answer. It emits *ids*. No generation of note content, ever.
- **Not embedding-based** (in Arm B). There is no vector index, no kNN. The "index" is the model's weights.
- **The slug is the retrieval unit.** Notes stay as files; the model routes to them. Content is never trained into the model as something to *reproduce* — only the `query → id` mapping.
- **Not RL.** Supervised next-token only. No reward, no judge-in-the-loop at train time (a judge is allowed as read-only *eval*, never as training reward).

---

## 2. Papers it builds on (verify ids + cite in PAPER.md; my snapshot may be imperfect)

**Core — generative retrieval / DSI**
- **DSI** — Tay et al., 2022, *Transformer Memory as a Differentiable Search Index*, arXiv 2202.06991. The founding idea: `query → docid` from a single Transformer. **This is the architecture of Arm B.**
- **SEAL** — Bevilacqua et al., 2022, *Autoregressive Search Engines: Generating Substrings as Document Identifiers*, arXiv 2204.10628. **Constrained decoding over valid identifiers (FM-index)** — the technique behind our slug-trie decoding.
- **NCI** — Wang et al., 2022, *A Neural Corpus Indexer for Document Retrieval*, arXiv 2206.02743. Semantic docids + beam decoding for ranking.
- **Scaling** — Pradeep et al., 2023, *How Does Generative Retrieval Scale to Millions of Passages?*, arXiv 2305.11841. Why our **tiny corpus (~680) is the favourable regime** (it degrades at scale).

**Identifier design & multi-answer**
- *Multiview Identifiers Enhanced Generative Retrieval*, Li et al., 2023, arXiv 2305.16675.
- *Generative Retrieval Meets Multi-Graded Relevance*, arXiv 2409.18409.
- *Descriptive & Discriminative docids for Generative Retrieval* (AAAI 2024). Relevant to emitting **multiple ids** (multi-answer).

**Dynamic corpus / continual update** (context for the standing system, not needed for this static synthetic test — cite in related work)
- DSI++ (Mehta et al., arXiv 2212.09744), IncDSI (arXiv 2307.10323), PromptDSI (arXiv 2406.12593), **MixLoRA-DSI** (2025, arXiv 2507.09924).

**Arm C — query decomposition** (established RAG technique, cite as known lever not novelty)
- RAG-Fusion / multi-query retrieval; sub-question / least-to-most decomposition. Find current canonical cites.

**Baselines (Arm A)**
- e5 — Wang et al., 2022, *Text Embeddings by Weakly-Supervised Contrastive Pre-training*, arXiv 2212.03533; multilingual-e5, arXiv 2402.05672. BM25 — Robertson & Zaragoza, 2009.

**Parametric memory & consolidation — the broader arc this experiment is one layer of (DO cite these).** This routing experiment is the *retrieval* layer of a larger "memory in the weights" vision; the *consolidation* layer is a distinct mechanism (drain working memory into parameters) but the same goal. Position the experiment against it:
- *Do (Language) Models Need Sleep? Offline Recurrence for Improved Online Inference* — arXiv **2605.26099**. Sleep phase drains the KV-cache into **fast-weights** before eviction. The "consolidate memory into weights" cousin.
- **Titans: Learning to Memorize at Test Time** — Behrouz et al., arXiv **2501.00663**. A neural long-term memory module updated at **test time** (surprise rule) — fast-weights memory.
- **SEAL: Self-Adapting Language Models** — arXiv **2506.10943**. The model generates its own finetuning data + self-edits → persistent weight updates (RL-rewarded). The "decide what to bake" cousin.
- **FSC-Net: Fast-Slow Consolidation Networks** — arXiv **2511.11707**; and Google's **Nested Learning / Hope** (multi-timescale optimisation). Hippocampus→neocortex consolidation in LLMs.
*(These belong in PAPER.md §8. They don't change the DSI-vs-embedding comparison, but they place the result in the memory-in-weights arc the project actually cares about.)*

**Positioning claim:** generative retrieval (DSI) is mature in IR, and agent-memory is a hot field — but **generative retrieval used as the *index of a small, linked, personal memory*, optimized for associative + multi-answer recall, is not an established line.** That gap is the contribution. Verify nobody has since done exactly this.

---

## 3. Example memories — match THIS distribution

The synthetic corpus must look like the real one. Real-vault texture (anonymous): **franglais** (French prose, English technical terms inline), `title` ~6–8 words, `summary` ~24 words often with `;`-separated clauses, a dense `[[links]]` graph (~3.7/note, hubs up to ~20+), `type` ∈ {lesson, reference, feedback, identity, project, user}. Crucially, the `title`/`summary` are written in **cause vocabulary**, while a real query comes in **symptom vocabulary** — that gap is the hard case. Below are *fabricated but faithful* examples (format + texture). Generate hundreds in this style.

### Example notes (a small linked cluster)

```
---
title: kapt incremental casse le mapper MapStruct
summary: kapt incremental regenere parfois un mapper MapStruct casse, toEntity droppe des champs constructeur, entite blank et POST 400 ; masque par les tests mockes ; fix clean-regen
type: lesson
links:
  - "[[lire-le-code-genere-pas-l-annotation]]"
  - "[[hub-build-pieges]]"
---
Quand kapt tourne en incremental, il regenere par intermittence un mapper MapStruct ou toEntity oublie des champs passes au constructeur. L'entite sort blank, le POST renvoie 400. Les tests unitaires mockent le mapper donc ils restent verts -> le bug ne se voit qu'au runtime. Fix : clean-regen (./gradlew clean kaptKotlin) et LIRE le mapper genere.
```

```
---
title: Lire le code genere, pas l'annotation
summary: Devant un bug de mapping ou de serialisation, lire la SORTIE generee (mapper, JSON) plutot que l'annotation source ; l'annotation ment, le genere dit la verite
type: lesson
links:
  - "[[kapt-incremental-casse-le-mapper-mapstruct]]"
  - "[[hub-build-pieges]]"
---
Reflexe : quand un mapping/une serialisation foire, ne pas relire l'annotation en esperant comprendre — ouvrir le fichier GENERE (le mapper kapt, le JSON Jackson reel). L'intention (annotation) et le resultat (code genere) divergent justement dans les bugs.
```

```
---
title: Emil prefere le plus petit diff calque sur l'existant
summary: Sur un changement, Emil veut le plus petit patch qui calque un pattern deja present, pas une abstraction neuve ; un helper pour un seul cas le frustre
type: feedback
links:
  - "[[hub-comment-on-travaille]]"
---
Quand je propose un refactor large ou un helper generique pour un seul call-site, Emil recadre : le plus petit changement, calque sur le pattern existant. **Why:** la dette d'une abstraction prematuree coute plus que la duplication d'un cas. **How to apply:** chercher le pattern voisin et le copier avant d'inventer une couche.
```

```
---
title: Hub build/pieges — kapt, EOL, accents de path
summary: Cluster des pieges de build du repo ; kapt incremental, CRLF vs LF, accent dans le path .gradle qui casse l'argfile ; cheap-fix connu pour chacun
type: reference
links:
  - "[[kapt-incremental-casse-le-mapper-mapstruct]]"
  - "[[lire-le-code-genere-pas-l-annotation]]"
  - "[[accent-path-gradle-casse-argfile]]"
  - "[[crlf-obligatoire-fichiers-windows]]"
---
Hub des pieges de build. THESE : la plupart sont des cheap-fix une fois la cause vue, mais chacun se presente d'abord comme un symptome opaque (entite blank, 400, ClassNotFound, churn git). Membres : kapt incremental, accent-path-gradle, CRLF/LF, lire-le-genere.
```

### Example QUERIES per note (the four kinds the eval must cover)

- **Title-side (easy, lexical):** `kapt incremental casse mapstruct` → `kapt-incremental-casse-le-mapper-mapstruct`
- **Summary/symptom-side (the vocab gap — HARD):** `pourquoi mon entite sort vide et le POST retourne 400 alors que les tests passent ?` → same slug. *Note: zero lexical overlap with title; this is where embedding cosine struggles and the model must have learned the mapping.*
- **Associative (two-hop):** `comment debugger un mapping kotlin qui foire` → gold is `lire-le-code-genere-pas-l-annotation` (the linked principle, not the kapt note itself).
- **Multi-answer / cluster (→ a SET, often cross-topic):** `c'est quoi les pieges de build du repo ?` → `[hub-build-pieges, kapt-incremental-casse-le-mapper-mapstruct, accent-path-gradle-casse-argfile, crlf-obligatoire-fichiers-windows]`. Coverage@k measures how much of this set is surfaced.

### Generation guidance for the synthetic corpus
- Write notes in **franglais** with real-looking English technical terms (Kotlin/React/SQL/git/ML), not generic filler.
- Make `summary` ≠ `title` in wording (so summary-side queries are a real paraphrase test).
- Build a **meaningful** link graph (related notes link; hubs gather a topic's members) — random links destroy the associative test.
- Include `feedback`/`identity`/`project` notes (about *how someone works* / *why*), not only technical lessons — the real vault is ~half non-technical, and those have softer, more associative queries.
- For each note, synthesize **K paraphrase queries** spanning the four kinds above, weighted toward **symptom-side and associative** (the hard cases). Hold some out (never trained/augmented) for eval.
