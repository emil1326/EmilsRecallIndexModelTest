# Experiment precisions — read this alongside EXPERIMENT.md

This supplements `EXPERIMENT.md` with the three things that were under-specified and caused confusion on the first run: **(1)** a precise technical description of the idea, **(2)** the papers it builds on, **(3)** concrete example memories so the synthetic corpus matches the real distribution.

---

## 0. Eval confounds found in run 1 — FIX THESE BEFORE TRUSTING ANY ARM

Run 1 produced Arm A (baseline) numbers that are **misleading**, and both causes are the same mistake: **using verbatim note text as the eval query.** Fix before running/trusting Arm B or C — otherwise "B beats A" could be an artifact, not a real win.

1. **Summary subset is trivial.** Held-out `summary` queries were the note's *verbatim summary* → embedding baseline HIT@1 = 1.000 (the query literally *is* the document). Measures nothing. **Fix:** the EVAL set must use **LLM-paraphrased, symptom-side** reformulations, never verbatim title/summary. Verbatim title/summary are **TRAIN-only anchors**; never put them in held-out.

2. **Associative subset is broken AND biased toward Arm B.** The assoc pair was built `query = A.summary → gold = B`. But A.summary retrieves **A** at rank 1 (it's A's own text), so gold B is structurally never rank-1 → baseline assoc HIT@1 = **0.000 is an artifact, not a finding**. Worse: Arm B is *trained* on exactly `(A.summary → B)`, so it can **memorize** the pair and "win" — that's memorization, not associative retrieval. **Fix:** an associative query must be a **genuine second-hop information need phrased independently of A's text** (LLM-generated: "a question a person would ask, for which B is the answer, without quoting A"), and at scoring time **exclude the source note A from candidates** (or mark A also-relevant). Then you measure *reaching B*, not "rank B above its own source."

3. **General rule:** the **held-out eval set must contain ZERO note-verbatim text.** Train on anchors (verbatim title/summary) + paraphrases; **evaluate only on held-out paraphrases / genuine second-hop questions / multi-answer cluster queries** the model never saw as text. `build-corpus.mjs` emits verbatim pairs — those are TRAIN anchors; **build the held-out separately from the paraphrase/decomposition generators**, not by splitting verbatim pairs. Otherwise every arm comparison is contaminated by trivial-match or memorization.

4. **Corpus is too easy — calibrate difficulty to the reference.** Run 1's baseline multi-answer **coverage@10 = 0.696**, but the *real* system sits at **0.26–0.48**. The synthetic clusters are far more retrievable than the real vault → the experiment is answering an easier question than ours. Likely causes: linked notes share too much surface vocabulary (so cosine finds them easily), or clusters are too lexically tight. **Fix:** calibrate the synthetic corpus so the **embedding baseline lands near the reference** (single HIT@1 ≈ 0.76, multi coverage@10 ≈ 0.3–0.5) — that's the sanity check that the synthetic reproduces the real *hardness* (especially the symptom↔cause vocab gap). If the baseline is too high, make links semantically-but-not-lexically related and widen the symptom/cause wording gap.

The win condition is unchanged (HIT@1 > 0.80, coverage@10 > 0.999) — but it only *means* something measured on a clean, paraphrase-based held-out, with the associative confound removed, on a corpus calibrated to the real difficulty.

## 1. The idea, made precise (this is where the first run got lost)

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
*(These were under-cited in run 1's PAPER.md §8 — add them. They don't change the DSI-vs-embedding comparison, but they place the result in the memory-in-weights arc the project actually cares about.)*

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
