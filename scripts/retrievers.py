"""Reusable retrievers so Arm C (decomposition) can compose over Arm A or Arm B without
duplicating retrieval logic. EmbedRetriever mirrors baseline_embed.py exactly (same
prefixes/fusion); RouterRetriever mirrors infer_router.py (same trie-constrained decoding).
"""
import re

import common
import numpy as np

CFG = common.config()
BC = CFG["baseline"]


def _tok(s):
    return re.findall(r"\w+", s.lower(), re.UNICODE)


def _minmax(x):
    x = np.asarray(x, dtype=np.float64)
    lo, hi = x.min(), x.max()
    return (x - lo) / (hi - lo) if hi > lo else np.zeros_like(x)


class EmbedRetriever:
    """e5-small + BM25 hybrid (Arm A), identical config to the baseline."""

    def __init__(self, notes=None, dense_weight=None):
        notes = notes or common.load_vault()
        self.slugs = sorted(notes)
        docs = [f"{notes[s]['title']}. {notes[s]['summary']}. {notes[s]['body']}" for s in self.slugs]
        from rank_bm25 import BM25Okapi
        from sentence_transformers import SentenceTransformer
        self.bm25 = BM25Okapi([_tok(d) for d in docs])
        dev = "cuda"
        try:
            import torch
            dev = "cuda" if torch.cuda.is_available() else "cpu"
        except Exception:  # noqa: BLE001
            dev = "cpu"
        self.model = SentenceTransformer(BC["embed_model"], device=dev)
        self.doc_emb = np.asarray(self.model.encode(
            [BC["passage_prefix"] + d for d in docs], normalize_embeddings=True,
            batch_size=64, show_progress_bar=False), dtype=np.float32)
        if dense_weight is None:
            meta = common.path("results_dir") / "baseline_meta.json"
            import json
            dense_weight = json.loads(meta.read_text())["tuned_dense_weight"] if meta.exists() else 0.5
        self.w = dense_weight

    def rank(self, query, k=20):
        qe = self.model.encode([BC["query_prefix"] + query], normalize_embeddings=True)[0]
        dense = _minmax(self.doc_emb @ np.asarray(qe, dtype=np.float32))
        bm = _minmax(self.bm25.get_scores(_tok(query)))
        hybrid = self.w * dense + (1 - self.w) * bm
        order = np.argsort(-hybrid)[:k]
        return [self.slugs[i] for i in order]


class RouterRetriever:
    """Generative router (Arm B): base+adapter, trie-constrained beam search."""

    def __init__(self, size="0.5B", device="auto", beams=None):
        import json
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
        from peft import PeftModel
        import router_common as rc
        self.rc = rc
        self.torch = torch
        self.beams = beams or CFG["arm_b"]["infer"]["beam_size"]
        self.device = rc.pick_device(device)
        adapter = common.path("runs_dir") / f"router_{size}"
        base = json.loads((adapter / "train_meta.json").read_text())["base"]
        self.tok = AutoTokenizer.from_pretrained(str(adapter))
        if self.tok.pad_token_id is None:
            self.tok.pad_token = self.tok.eos_token
        dtype = torch.float16 if str(self.device) != "cpu" else torch.float32
        m = AutoModelForCausalLM.from_pretrained(base, torch_dtype=dtype)
        self.model = PeftModel.from_pretrained(m, str(adapter)).to(self.device).eval()
        slugs = (common.path("data_dir") / "slugs.txt").read_text(encoding="utf-8").split()
        self.trie = rc.SlugTrie(slugs, self.tok, self.tok.eos_token_id)
        self.slug_set = set(slugs)
        self.max_new = max(len(v) for v in self.trie.seqs.values()) + 1

    def rank(self, query, k=10):
        return self.rc.rank_by_likelihood(self.model, self.tok, query, self.trie,
                                          self.device, k=k)
