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
import gpu_guard

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


def completion_loss(model, input_ids, attn, labels, keep):
    """Memory-efficient causal-LM loss for query->slug.

    HF's built-in loss materialises the full [B, L, vocab] logits in fp32 (≈9 GB at
    batch 16 / L 96 / 152k-vocab, plus an equal-size gradient) — that is the DirectML
    OOM. Here we run the trunk once, then apply the LM head ONLY on the completion
    (slug) token positions selected by `keep`, so the big fp32 tensor is [N_slug, vocab]
    (≈0.1 GB) instead of [B, L, vocab]. Identical loss (mean CE over the same tokens),
    no new kernels — pure indexing, DirectML-safe (the data-dependent `nonzero` that
    builds `keep` runs on CPU before the tensors move to device).
    """
    import torch.nn.functional as F
    base = model.get_base_model()                     # Qwen2ForCausalLM (LoRA injected in-place)
    h = base.model(input_ids=input_ids, attention_mask=attn).last_hidden_state  # [B, L, H]
    h = h[:, :-1, :].reshape(-1, h.size(-1))          # predict-next: [(B*(L-1)), H]
    tgt = labels[:, 1:].reshape(-1)                   # [(B*(L-1))]
    h_sel = h.index_select(0, keep)                   # [N_slug, H]
    tgt_sel = tgt.index_select(0, keep)               # [N_slug]
    logits = base.lm_head(h_sel)                      # [N_slug, vocab]  (head on slug tokens only)
    return F.cross_entropy(logits.float(), tgt_sel)   # mean CE over slug tokens == HF's loss


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--size", default="0.5B", choices=list(AB["base_models"].keys()))
    ap.add_argument("--data", default=str(common.path("data_dir") / "train_aug.jsonl"))
    ap.add_argument("--device", default="auto")
    ap.add_argument("--epochs", type=int, default=AB["train"]["epochs"])
    ap.add_argument("--batch", type=int, default=AB["train"]["batch_size"], help="override batch size (VRAM cap)")
    ap.add_argument("--accum", type=int, default=AB["train"]["grad_accum"], help="grad accumulation (effective batch = batch*accum)")
    ap.add_argument("--limit", type=int, default=0, help="cap #pairs (smoke test)")
    ap.add_argument("--efficient-loss", dest="efficient_loss", action="store_true", default=True,
                    help="completion-only LM-head loss (avoids the [B,L,vocab] fp32 OOM; needed for 1.5B+ on DirectML)")
    ap.add_argument("--no-efficient-loss", dest="efficient_loss", action="store_false",
                    help="use HF's built-in loss (full-vocab fp32; only safe for tiny vocab / 0.5B)")
    ap.add_argument("--grad-ckpt", action="store_true",
                    help="gradient checkpointing — frees trunk activation memory so a bigger batch fits (slower/step)")
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

    data_path = Path(args.data)
    if not data_path.exists():
        data_path = common.path("data_dir") / "train.jsonl"
        print(f"(train_aug.jsonl not found -> using {data_path.name})", flush=True)
    pairs = common.read_jsonl(data_path)
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
    if args.grad_ckpt:
        model.enable_input_require_grads()              # let grad reach LoRA through the frozen base
        model.gradient_checkpointing_enable()
    if str(device) != "cpu":
        gpu_guard.ensure_free_for(args.size, "train")   # wait for VRAM headroom before allocating
    model.to(device)
    model.train()
    model.print_trainable_parameters()
    print(f"loss=completion-only" if args.efficient_loss else "loss=hf-builtin",
          f"grad_ckpt={args.grad_ckpt}", flush=True)

    bs = args.batch
    accum = args.accum
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
            keep = None
            if args.efficient_loss:
                # select the completion (non -100) positions on CPU — avoids DirectML's
                # unsupported data-dependent nonzero on-device.
                tgt_flat = labels[:, 1:].reshape(-1)
                keep = (tgt_flat != -100).nonzero(as_tuple=True)[0]
            input_ids, attn, labels = input_ids.to(device), attn.to(device), labels.to(device)
            if args.efficient_loss:
                if keep.numel() == 0:
                    continue
                raw_loss = completion_loss(model, input_ids, attn, labels, keep.to(device))
            else:
                raw_loss = model(input_ids=input_ids, attention_mask=attn, labels=labels).loss
            loss = raw_loss / accum
            loss.backward()
            running += raw_loss.item()
            if ((i // bs) + 1) % accum == 0:
                opt.step(); sched.step(); opt.zero_grad(); gstep += 1
        print(f"epoch {ep+1}/{args.epochs} loss={running/steps_per_epoch:.4f} "
              f"({time.time()-t0:.0f}s)", flush=True)

    out_dir = common.path("runs_dir") / f"router_{args.size}"
    out_dir.mkdir(parents=True, exist_ok=True)
    model.to("cpu")  # DirectML tensors are OpaqueTensorImpl -> peft save can't read storage
    model.save_pretrained(str(out_dir))
    tok.save_pretrained(str(out_dir))
    meta = {"base": base, "size": args.size, "device": str(device), "epochs": args.epochs,
            "n_examples": len(examples), "lora": AB["lora"], "train": AB["train"],
            "train_minutes": round((time.time() - t0) / 60, 1)}
    (out_dir / "train_meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"saved adapter -> {out_dir} ({meta['train_minutes']} min)", flush=True)
    gpu_guard.release(model, opt)


if __name__ == "__main__":
    main()
