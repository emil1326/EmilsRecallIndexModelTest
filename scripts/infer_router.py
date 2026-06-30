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
import gpu_guard

CFG = common.config()
AB = CFG["arm_b"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--size", default="0.5B")
    ap.add_argument("--device", default="auto")
    ap.add_argument("--beams", type=int, default=AB["infer"]["beam_size"])
    ap.add_argument("--topk", type=int, default=AB["infer"]["top_k_out"])
    ap.add_argument("--batch", type=int, default=64, help="likelihood-scoring batch (VRAM cap)")
    ap.add_argument("--pause", type=float, default=0.0, help="seconds to idle between queries (gentle GPU)")
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
    if str(device) != "cpu":
        gpu_guard.ensure_free_for(args.size, "infer")   # wait for VRAM headroom (no OOM / single consumer)
    model.to(device).eval()

    slugs = (common.path("data_dir") / "slugs.txt").read_text(encoding="utf-8").split()
    trie = rc.SlugTrie(slugs, tok, tok.eos_token_id)

    def retrieve(query):
        return rc.rank_by_likelihood(model, tok, query, trie, device, k=args.topk,
                                     batch_size=args.batch)

    import time, json
    out = args.out or str(common.path("data_dir") / f"preds_router_{args.size}.jsonl")
    # RESUMABLE: skip queries already written (a crash loses nothing — just rerun)
    done = set()
    if Path(out).exists():
        for r in common.read_jsonl(out):
            done.add(r["query"])
        print(f"resuming: {len(done)} queries already done", flush=True)

    items = [("single", p) for p in common.read_jsonl(common.path("data_dir") / "heldout.jsonl")]
    mg = common.path("data_dir") / "multigold.jsonl"
    if mg.exists():
        items += [("multi", p) for p in common.read_jsonl(mg)]

    f = open(out, "a", encoding="utf-8")
    try:
        n = 0
        for kind, p in items:
            if p["query"] in done:
                continue
            gold = [p["slug"]] if kind == "single" else p["slugs"]
            rec = {"query": p["query"], "kind": p.get("kind", kind) if kind == "single" else "multi",
                   "gold": gold, "ranked": retrieve(p["query"])}
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            f.flush()
            n += 1
            if n % 25 == 0:
                print(f"  {n} new ({len(done)+n}/{len(items)})", flush=True)
            if args.pause:
                time.sleep(args.pause)
    finally:
        f.close()
    if str(device) != "cpu":
        gpu_guard.release(model)
    print(f"-> {out} (+{n} preds, {len(done)+n} total). Now: python scripts/eval.py --preds {out} --arm B --label router_{args.size}", flush=True)


if __name__ == "__main__":
    main()
