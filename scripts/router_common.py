"""Shared format + slug-trie constrained decoding for the generative router (Arm B).

The SAME prompt/target format is used by train_router.py and infer_router.py, and the
trie guarantees inference can only emit VALID slugs (invalid-slug rate = 0 by construction
— a NON-NEGOTIABLE validity control from the brief).
"""

PROMPT_TMPL = "query: {q}\nslug:"
TARGET_TMPL = " {slug}"   # leading space so the slug is one clean continuation


def format_prompt(query):
    return PROMPT_TMPL.format(q=query.strip())


def format_target(slug):
    return TARGET_TMPL.format(slug=slug)


def pick_device(prefer="auto"):
    """Return a torch device string/object: dml (DirectML) > cuda > cpu."""
    import torch
    if prefer == "cpu":
        return "cpu"
    if prefer in ("dml", "auto"):
        try:
            import torch_directml  # noqa: F401
            return torch_directml.device()
        except Exception:  # noqa: BLE001
            if prefer == "dml":
                raise
    if torch.cuda.is_available():
        return "cuda"
    return "cpu"


class SlugTrie:
    """Trie over the token-id sequences of every valid slug target (incl. trailing EOS),
    used to constrain generation so only valid slugs can be produced."""

    def __init__(self, slugs, tokenizer, eos_id):
        self.eos_id = eos_id
        self.root = {}
        self.seqs = {}
        for slug in slugs:
            ids = tokenizer.encode(format_target(slug), add_special_tokens=False)
            ids = ids + [eos_id]
            self.seqs[slug] = ids
            node = self.root
            for t in ids:
                node = node.setdefault(t, {})

    def allowed(self, generated_ids):
        """Given the token ids generated AFTER the prompt, return the list of allowed
        next token ids (the trie continuations). Empty -> only EOS / dead end."""
        node = self.root
        for t in generated_ids:
            if t in node:
                node = node[t]
            else:
                return []  # off-trie (shouldn't happen under constraint)
        return list(node.keys())


def rank_by_likelihood(model, tok, query, trie, device, k=10, batch_size=96):
    """Exact constrained ranking for a SMALL corpus: score every valid slug's token
    sequence under the model (teacher forcing) and rank by total log-prob. Guarantees
    only valid slugs (no hallucination, invalid-rate=0) without beam-search fragility.

    Returns the top-k slugs (highest likelihood first)."""
    import torch
    import torch.nn.functional as F

    prompt_ids = tok.encode(format_prompt(query), add_special_tokens=False)
    P = len(prompt_ids)
    slugs = list(trie.seqs.keys())
    pad_id = tok.pad_token_id if tok.pad_token_id is not None else tok.eos_token_id

    scores = {}
    for i in range(0, len(slugs), batch_size):
        chunk = slugs[i:i + batch_size]
        seqs = [prompt_ids + trie.seqs[s] for s in chunk]  # trie.seqs includes trailing EOS
        maxlen = max(len(s) for s in seqs)
        input_ids = torch.full((len(chunk), maxlen), pad_id, dtype=torch.long)
        attn = torch.zeros((len(chunk), maxlen), dtype=torch.long)
        for r, s in enumerate(seqs):
            input_ids[r, :len(s)] = torch.tensor(s)
            attn[r, :len(s)] = 1
        with torch.no_grad():
            logits = model(input_ids=input_ids.to(device), attention_mask=attn.to(device)).logits
            logprobs = F.log_softmax(logits.float(), dim=-1).cpu()
        for r, s in enumerate(chunk):
            tgt = trie.seqs[s]                       # slug tokens + EOS
            total = 0.0
            for j in range(len(tgt)):
                pos = P + j - 1                      # logits at pos predict token at pos+1
                total += logprobs[r, pos, tgt[j]].item()
            scores[s] = total / len(tgt)             # length-normalized log-prob
    return [s for s, _ in sorted(scores.items(), key=lambda x: -x[1])[:k]]


def make_prefix_allowed_fn(trie, prompt_len_by_batch):
    """Build a prefix_allowed_tokens_fn for HF generate. prompt_len_by_batch maps the
    flat beam/batch index handling to the prompt length so we only constrain the
    generated suffix."""
    def fn(batch_id, input_ids):
        # input_ids: full sequence (prompt + generated). Slice off the prompt.
        plen = prompt_len_by_batch
        gen = input_ids.tolist()[plen:]
        allowed = trie.allowed(gen)
        if not allowed:
            return [trie.eos_id]
        return allowed
    return fn
