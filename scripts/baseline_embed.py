"""Arm A — embedding-retrieval baseline (the bar to beat).

intfloat/multilingual-e5-small dense cosine (with the MANDATORY query:/passage:
prefixes — the #1 way to accidentally build a strawman) fused with BM25. The fusion
weight is tuned on TRAIN pairs (never the held-out set — no test leakage), per the
brief's "genuinely strong, not a strawman" requirement.

Produces preds for the held-out single-answer set AND the multi-gold set, then they
are scored by the shared eval.py. Also dumps dense-only / bm25-only component metrics.

Usage: python scripts/baseline_embed.py [--vault corpus/vault]
"""
import argparse
import re
import json
from pathlib import Path

import common
import numpy as np

CFG = common.config()
BC = CFG["baseline"]
TOP_K = 20  # keep enough for coverage@10 with margin


def tok(s):
    return re.findall(r"\w+", s.lower(), re.UNICODE)


def minmax(x):
    x = np.asarray(x, dtype=np.float64)
    lo, hi = x.min(), x.max()
    return (x - lo) / (hi - lo) if hi > lo else np.zeros_like(x)


def auto_device():
    try:
        import torch
        if torch.cuda.is_available():
            return "cuda"
    except Exception:  # noqa: BLE001
        pass
    return "cpu"  # e5-small is tiny; CPU encodes the whole vault in seconds


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", default=None)
    ap.add_argument("--out", default=str(common.path("data_dir") / "preds_baseline.jsonl"))
    args = ap.parse_args()

    notes = common.load_vault(args.vault)
    slugs = sorted(notes)
    idx = {s: i for i, s in enumerate(slugs)}
    docs = [f"{notes[s]['title']}. {notes[s]['summary']}. {notes[s]['body']}" for s in slugs]
    print(f"baseline over {len(slugs)} docs")

    # --- BM25 ---
    from rank_bm25 import BM25Okapi
    bm25 = BM25Okapi([tok(d) for d in docs])

    # --- dense e5 (correct prefixes!) ---
    from sentence_transformers import SentenceTransformer
    device = auto_device()
    print(f"loading {BC['embed_model']} on {device}")
    model = SentenceTransformer(BC["embed_model"], device=device)
    doc_emb = model.encode([BC["passage_prefix"] + d for d in docs],
                           normalize_embeddings=True, batch_size=64, show_progress_bar=False)
    doc_emb = np.asarray(doc_emb, dtype=np.float32)

    _qcache = {}

    def scores_for(query):
        if query not in _qcache:
            qe = model.encode([BC["query_prefix"] + query], normalize_embeddings=True)[0]
            dense = doc_emb @ np.asarray(qe, dtype=np.float32)  # cosine (both normalized)
            bm = np.asarray(bm25.get_scores(tok(query)), dtype=np.float64)
            _qcache[query] = (minmax(dense), minmax(bm))
        return _qcache[query]

    def rank(query, w):  # w = dense weight
        ds, bs = scores_for(query)
        hybrid = w * ds + (1 - w) * bs
        order = np.argsort(-hybrid)[:TOP_K]
        return [slugs[i] for i in order]

    # --- tune fusion weight on TRAIN (no leakage) ---
    train = common.read_jsonl(common.path("data_dir") / "train.jsonl")
    # sample non-title train pairs (title->slug is trivially memorized; tune on the
    # harder summary/assoc pairs that resemble real queries)
    dev = [p for p in train if p.get("kind") in ("summary", "assoc")]
    common.set_seed()
    import random
    random.shuffle(dev)
    dev = dev[:400]
    weights = [0.0, 0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    best_w, best_mrr = 0.7, -1.0
    for w in weights:
        rr = []
        for p in dev:
            r = rank(p["query"], w)
            rr.append(next((1.0 / (i + 1) for i, s in enumerate(r) if s == p["slug"]), 0.0))
        mrr = sum(rr) / len(rr) if rr else 0
        if mrr > best_mrr:
            best_mrr, best_w = mrr, w
        print(f"  w(dense)={w:.2f} -> train MRR {mrr:.3f}")
    print(f"tuned dense_weight = {best_w} (train MRR {best_mrr:.3f})")

    # --- predict on held-out + multi-gold ---
    def make_preds(weight):
        preds = []
        for p in common.read_jsonl(common.path("data_dir") / "heldout.jsonl"):
            preds.append({"query": p["query"], "kind": p["kind"], "gold": [p["slug"]],
                          "ranked": rank(p["query"], weight)})
        mg_path = common.path("data_dir") / "multigold.jsonl"
        if mg_path.exists():
            for p in common.read_jsonl(mg_path):
                preds.append({"query": p["query"], "kind": "multi", "gold": p["slugs"],
                              "ranked": rank(p["query"], weight)})
        return preds

    preds = make_preds(best_w)
    common.write_jsonl(args.out, preds)
    # component baselines for the paper (dense-only, bm25-only)
    common.write_jsonl(common.path("data_dir") / "preds_baseline_dense.jsonl", make_preds(1.0))
    common.write_jsonl(common.path("data_dir") / "preds_baseline_bm25.jsonl", make_preds(0.0))

    meta = {"embed_model": BC["embed_model"], "tuned_dense_weight": best_w,
            "train_dev_mrr": round(best_mrr, 4), "n_docs": len(slugs), "device": device}
    (common.path("results_dir") / "baseline_meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"-> {args.out} ({len(preds)} preds). Now: python scripts/eval.py --preds {args.out} --arm A")


if __name__ == "__main__":
    main()
