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
