"""Arm B — train the generative router: LoRA fine-tune a small base model to emit the
note SLUG given the query (DSI-style; the model *becomes* the index).

Device-flexible (DirectML on the RX 9070 XT > CUDA > CPU). Manual training loop (more
portable across backends than HF Trainer on DirectML). Trains only the LoRA adapter.

Usage:
  python scripts/train_router.py --size 0.5B [--data data/train_aug.jsonl] [--device auto]
"""
import argparse
import json
import math
import random
import time
from pathlib import Path

import common
import router_common as rc

CFG = common.config()
AB = CFG["arm_b"]


def build_examples(pairs, tokenizer, max_len):
    eos = tokenizer.eos_token_id
    data = []
    for p in pairs:
        prompt = rc.format_prompt(p["query"])
        target = rc.format_target(p["slug"])
        p_ids = tokenizer.encode(prompt, add_special_tokens=False)
        t_ids = tokenizer.encode(target, add_special_tokens=False) + [eos]
        ids = (p_ids + t_ids)[:max_len]
        labels = ([-100] * len(p_ids) + t_ids)[:max_len]
        data.append((ids, labels))
    return data


def collate(batch, pad_id):
    maxlen = max(len(x[0]) for x in batch)
    input_ids, labels, attn = [], [], []
    for ids, lab in batch:
        pad = maxlen - len(ids)
        input_ids.append(ids + [pad_id] * pad)
        labels.append(lab + [-100] * pad)
        attn.append([1] * len(ids) + [0] * pad)
    import torch
    return (torch.tensor(input_ids), torch.tensor(attn), torch.tensor(labels))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--size", default="0.5B", choices=list(AB["base_models"].keys()))
    ap.add_argument("--data", default=str(common.path("data_dir") / "train_aug.jsonl"))
    ap.add_argument("--device", default="auto")
    ap.add_argument("--epochs", type=int, default=AB["train"]["epochs"])
    ap.add_argument("--limit", type=int, default=0, help="cap #pairs (smoke test)")
    args = ap.parse_args()
    common.set_seed()

    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from peft import LoraConfig, get_peft_model

    device = rc.pick_device(args.device)
    print(f"device={device} size={args.size}", flush=True)
    base = AB["base_models"][args.size]
    tok = AutoTokenizer.from_pretrained(base)
    if tok.pad_token_id is None:
        tok.pad_token = tok.eos_token

    pairs = common.read_jsonl(args.data)
    if not Path(args.data).exists() or not pairs:
        pairs = common.read_jsonl(common.path("data_dir") / "train.jsonl")
    random.shuffle(pairs)
    if args.limit:
        pairs = pairs[: args.limit]
    examples = build_examples(pairs, tok, AB["train"]["max_len"])
    print(f"{len(examples)} training examples", flush=True)

    dtype = torch.float16 if str(device) not in ("cpu",) else torch.float32
    model = AutoModelForCausalLM.from_pretrained(base, torch_dtype=dtype)
    lora = LoraConfig(r=AB["lora"]["r"], lora_alpha=AB["lora"]["alpha"],
                      lora_dropout=AB["lora"]["dropout"], target_modules=AB["lora"]["target_modules"],
                      task_type="CAUSAL_LM")
    model = get_peft_model(model, lora)
    model.to(device)
    model.train()
    model.print_trainable_parameters()

    bs = AB["train"]["batch_size"]
    accum = AB["train"]["grad_accum"]
    opt = torch.optim.AdamW([p for p in model.parameters() if p.requires_grad], lr=AB["train"]["lr"])
    steps_per_epoch = math.ceil(len(examples) / bs)
    total_steps = steps_per_epoch * args.epochs
    warmup = int(AB["train"]["warmup_ratio"] * total_steps)
    sched = torch.optim.lr_scheduler.LambdaLR(
        opt, lambda s: min(1.0, s / max(1, warmup)) * max(0.0, (total_steps - s) / max(1, total_steps - warmup)))

    t0 = time.time()
    gstep = 0
    for ep in range(args.epochs):
        random.shuffle(examples)
        running = 0.0
        for i in range(0, len(examples), bs):
            batch = examples[i:i + bs]
            input_ids, attn, labels = collate(batch, tok.pad_token_id)
            input_ids, attn, labels = input_ids.to(device), attn.to(device), labels.to(device)
            out = model(input_ids=input_ids, attention_mask=attn, labels=labels)
            loss = out.loss / accum
            loss.backward()
            running += out.loss.item()
            if ((i // bs) + 1) % accum == 0:
                opt.step(); sched.step(); opt.zero_grad(); gstep += 1
        print(f"epoch {ep+1}/{args.epochs} loss={running/steps_per_epoch:.4f} "
              f"({time.time()-t0:.0f}s)", flush=True)

    out_dir = common.path("runs_dir") / f"router_{args.size}"
    out_dir.mkdir(parents=True, exist_ok=True)
    model.save_pretrained(str(out_dir))
    tok.save_pretrained(str(out_dir))
    meta = {"base": base, "size": args.size, "device": str(device), "epochs": args.epochs,
            "n_examples": len(examples), "lora": AB["lora"], "train": AB["train"],
            "train_minutes": round((time.time() - t0) / 60, 1)}
    (out_dir / "train_meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"saved adapter -> {out_dir} ({meta['train_minutes']} min)", flush=True)


if __name__ == "__main__":
    main()
