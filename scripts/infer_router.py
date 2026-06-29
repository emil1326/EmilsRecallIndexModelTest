"""Arm B — inference: load base+adapter and emit ranked top-k slugs per held-out query
via constrained beam search over the slug trie (only valid slugs can be produced, so the
invalid-slug rate is 0 by construction).

Outputs preds for the held-out single-answer set AND the multi-gold set, then scored by
eval.py on the same metric code as the baseline (apples-to-apples).

Usage:
  python scripts/infer_router.py --size 0.5B [--device auto] [--beams 12] [--topk 10]
"""
import argparse
import json
from pathlib import Path

import common
import router_common as rc

CFG = common.config()
AB = CFG["arm_b"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--size", default="0.5B")
    ap.add_argument("--device", default="auto")
    ap.add_argument("--beams", type=int, default=AB["infer"]["beam_size"])
    ap.add_argument("--topk", type=int, default=AB["infer"]["top_k_out"])
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    common.set_seed()

    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from peft import PeftModel

    device = rc.pick_device(args.device)
    adapter_dir = common.path("runs_dir") / f"router_{args.size}"
    base = json.loads((adapter_dir / "train_meta.json").read_text())["base"]
    print(f"device={device} base={base} adapter={adapter_dir}", flush=True)

    tok = AutoTokenizer.from_pretrained(str(adapter_dir))
    if tok.pad_token_id is None:
        tok.pad_token = tok.eos_token
    dtype = torch.float16 if str(device) != "cpu" else torch.float32
    model = AutoModelForCausalLM.from_pretrained(base, torch_dtype=dtype)
    model = PeftModel.from_pretrained(model, str(adapter_dir))
    model.to(device).eval()

    slugs = (common.path("data_dir") / "slugs.txt").read_text(encoding="utf-8").split()
    trie = rc.SlugTrie(slugs, tok, tok.eos_token_id)
    max_new = max(len(v) for v in trie.seqs.values()) + 1
    slug_set = set(slugs)

    @torch.no_grad()
    def retrieve(query):
        prompt = rc.format_prompt(query)
        enc = tok(prompt, return_tensors="pt").to(device)
        plen = enc["input_ids"].shape[1]
        fn = rc.make_prefix_allowed_fn(trie, plen)
        gen = model.generate(
            **enc, num_beams=args.beams, num_return_sequences=min(args.beams, max(args.topk, args.beams)),
            max_new_tokens=max_new, prefix_allowed_tokens_fn=fn,
            do_sample=False, early_stopping=True, pad_token_id=tok.pad_token_id,
        )
        ranked, seen = [], set()
        for seq in gen:
            text = tok.decode(seq[plen:], skip_special_tokens=True).strip()
            if text in slug_set and text not in seen:
                seen.add(text)
                ranked.append(text)
            if len(ranked) >= args.topk:
                break
        return ranked

    preds = []
    heldout = common.read_jsonl(common.path("data_dir") / "heldout.jsonl")
    for i, p in enumerate(heldout):
        preds.append({"query": p["query"], "kind": p["kind"], "gold": [p["slug"]],
                      "ranked": retrieve(p["query"])})
        if (i + 1) % 50 == 0:
            print(f"  heldout {i+1}/{len(heldout)}", flush=True)
    mg = common.path("data_dir") / "multigold.jsonl"
    if mg.exists():
        for p in common.read_jsonl(mg):
            preds.append({"query": p["query"], "kind": "multi", "gold": p["slugs"],
                          "ranked": retrieve(p["query"])})

    out = args.out or str(common.path("data_dir") / f"preds_router_{args.size}.jsonl")
    common.write_jsonl(out, preds)
    print(f"-> {out} ({len(preds)} preds). Now: python scripts/eval.py --preds {out} --arm B --label router_{args.size}", flush=True)


if __name__ == "__main__":
    main()
