#!/bin/bash
# Overnight Arm B (size sweep) + Arm C (composition) driver.
# RUN ONLY WHEN THE GPU IS OTHERWISE IDLE (Emil asleep, game/apps closed) — single GPU
# consumer (DirectML). No Ollama needed (decomposition is already done).
#
# Robust: each size runs in its own process (VRAM freed on exit); per-step failures are
# logged and skipped so a late failure (e.g. 3B OOM) still leaves earlier results. All
# output -> results/sweep.log. Re-runnable (skips sizes whose eval already exists).
#
# Usage:  bash scripts/run_sweep.sh           (default sizes 0.5B 1.5B 3B, 4 epochs)
#         SIZES="0.5B 1.5B" EPOCHS=5 bash scripts/run_sweep.sh
set -u
cd "$(dirname "$0")/.."
DML=".venv-dml/Scripts/python.exe"
PY="python"
LOG="results/sweep.log"
SIZES="${SIZES:-0.5B 1.5B 3B}"
EPOCHS="${EPOCHS:-4}"
mkdir -p results runs
exec > >(tee -a "$LOG") 2>&1
echo "===================================================================="
echo "SWEEP START  sizes=[$SIZES] epochs=$EPOCHS"

# --- safety: free the GPU of any Ollama / llama.cpp runner (single consumer) ---
echo "[safety] stopping Ollama + llama-server runners to free VRAM..."
powershell.exe -NoProfile -Command "Get-Process ollama,'ollama app',llama-server -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue" 2>/dev/null
sleep 3

step () { echo; echo ">>> [$(date +%H:%M:%S)] $*"; }

# --- Arm B: train -> infer -> eval, per size ---
for SIZE in $SIZES; do
  if [ -f "results/eval_router_${SIZE}.json" ]; then echo "[skip] $SIZE eval exists"; continue; fi
  step "TRAIN $SIZE (epochs=$EPOCHS)"
  "$DML" scripts/train_router.py --size "$SIZE" --epochs "$EPOCHS" --device dml || { echo "!! train $SIZE failed"; continue; }
  step "INFER $SIZE (likelihood ranking)"
  "$DML" scripts/infer_router.py --size "$SIZE" --device dml || { echo "!! infer $SIZE failed"; continue; }
  step "EVAL $SIZE"
  "$PY" scripts/eval.py --preds "data/preds_router_${SIZE}.jsonl" --arm B --label "router_${SIZE}" \
        --out "results/eval_router_${SIZE}.json" || echo "!! eval $SIZE failed"
done

# --- Arm C: decomposition composed over A (CPU) and B (router GPU) ---
step "COMPOSE C x A (e5+bm25, CPU)"
"$PY" scripts/compose_c.py --arm A && \
  "$PY" scripts/eval.py --preds data/preds_cxA.jsonl --arm C --label CxA --out results/eval_CxA.json || echo "!! CxA failed"

# pick the largest router that trained for CxB
CXB_SIZE=""
for SIZE in $SIZES; do [ -f "runs/router_${SIZE}/adapter_model.safetensors" ] && CXB_SIZE="$SIZE"; done
if [ -n "$CXB_SIZE" ]; then
  step "COMPOSE C x B (router $CXB_SIZE, DirectML)"
  "$DML" scripts/compose_c.py --arm B --size "$CXB_SIZE" --device dml && \
    "$PY" scripts/eval.py --preds "data/preds_cxB_${CXB_SIZE}.jsonl" --arm C --label "CxB_${CXB_SIZE}" \
          --out "results/eval_CxB_${CXB_SIZE}.json" || echo "!! CxB failed"
fi

step "AGGREGATE"
"$PY" scripts/aggregate_results.py || echo "!! aggregate failed"
echo "===================================================================="
echo "SWEEP DONE  $(date +%H:%M:%S)"
