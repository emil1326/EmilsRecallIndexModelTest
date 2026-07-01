#!/usr/bin/env bash
# Guarded single-size router run for DirectML (Arm B) — train -> infer -> eval -> aggregate.
# Uses the completion-only loss (no [B,L,vocab] fp32 OOM) + gradient checkpointing, gentle batch.
# SINGLE GPU CONSUMER ONLY: do not run while in VR / a game / Ollama is loaded.
#
# Usage:  bash scripts/run_router_size.sh 1.5B [epochs] [batch]
set -euo pipefail
cd "$(dirname "$0")/.."

SIZE="${1:-1.5B}"
EPOCHS="${2:-4}"
BATCH="${3:-8}"           # TRAIN micro-batch (memory-bound: weights+activations); eff = BATCH*2 via accum
INFER_BATCH="${4:-64}"    # INFER slug-scoring batch — memory-light (no grad/optim), so score many slugs
                          # per forward pass. 672 slugs / 64 = ~11 passes/query vs 84 at batch 8 (~8x faster).
PY=".venv-dml/Scripts/python"
LOG="results/router_${SIZE}.log"

echo ">>> [$(date '+%H:%M:%S')] router ${SIZE}: train epochs=${EPOCHS} batch=${BATCH} (efficient loss + grad-ckpt)" | tee -a "$LOG"

# train (gpu_guard inside waits for VRAM headroom before allocating; efficient loss is default-on)
"$PY" scripts/train_router.py --size "$SIZE" --device dml \
    --epochs "$EPOCHS" --batch "$BATCH" --accum 2 --grad-ckpt 2>&1 | tee -a "$LOG"

echo ">>> [$(date '+%H:%M:%S')] router ${SIZE}: infer (scoring batch ${INFER_BATCH})" | tee -a "$LOG"
"$PY" scripts/infer_router.py --size "$SIZE" --device dml --batch "$INFER_BATCH" --pause 0.5 2>&1 | tee -a "$LOG"

echo ">>> [$(date '+%H:%M:%S')] router ${SIZE}: eval + aggregate" | tee -a "$LOG"
# size-specific --out so each size keeps its own eval (distinct label -> aggregate keeps all sizes)
python scripts/eval.py --preds "data/preds_router_${SIZE}.jsonl" --arm B --label "router_${SIZE}" \
    --out "results/eval_router_${SIZE}.json" 2>&1 | tee -a "$LOG"
python scripts/aggregate_results.py 2>&1 | tail -30 | tee -a "$LOG"

echo ">>> [$(date '+%H:%M:%S')] router ${SIZE}: DONE -> data/preds_router_${SIZE}.jsonl, results/eval_router_${SIZE}.json" | tee -a "$LOG"
