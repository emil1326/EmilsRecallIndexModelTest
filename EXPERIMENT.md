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
