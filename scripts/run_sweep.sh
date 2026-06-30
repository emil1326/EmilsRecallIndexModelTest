#!/bin/bash
# Overnight Arm B (size sweep) + Arm C (composition) driver.
# Single GPU consumer (DirectML). No Ollama needed (decomposition already done).
#
# GUARDS (Emil's rules): keep VRAM usage <= 10 GB (per-size batch caps below) and require
# >= 12 GB FREE before every GPU step (waits up to ~10 min, then skips — so heavy steps
# defer until the game/apps are closed). Each size runs in its own process (VRAM freed on
# exit). Per-step failures are logged and skipped. Re-runnable (skips sizes already eval'd).
#
# Usage:  bash scripts/run_sweep.sh            (sizes 0.5B 1.5B 3B, 4 epochs)
#         SIZES="0.5B 1.5B" EPOCHS=5 bash scripts/run_sweep.sh
set -u
cd "$(dirname "$0")/.."
DML=".venv-dml/Scripts/python.exe"
PY="python"
LOG="results/sweep.log"
SIZES="${SIZES:-0.5B 1.5B 3B}"
EPOCHS="${EPOCHS:-4}"
NEED_FREE="${NEED_FREE:-12}"     # GB free required before a GPU step
mkdir -p results runs
exec > >(tee -a "$LOG") 2>&1
echo "===================================================================="
echo "SWEEP START $(date)  sizes=[$SIZES] epochs=$EPOCHS need_free=${NEED_FREE}GB"

# per-size batch caps -> keep VRAM usage <= 10 GB
train_batch () { case "$1" in 0.5B) echo 16;; 1.5B) echo 16;; 3B) echo 8;; *) echo 8;; esac; }
infer_batch () { case "$1" in 0.5B) echo 256;; 1.5B) echo 160;; 3B) echo 96;; *) echo 96;; esac; }

# free the GPU of any Ollama / llama.cpp runner (single consumer)
echo "[safety] stopping Ollama + llama-server runners..."
powershell.exe -NoProfile -Command "Get-Process ollama,'ollama app',llama-server -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue" 2>/dev/null
sleep 3

free_vram () { powershell.exe -NoProfile -File scripts/vram_free.ps1 2>/dev/null | tr -d '\r\n ' | tr ',' '.'; }
require_vram () {            # $1 = GB needed; waits patiently (overnight), 0=ok 1=gave up
  local need="$1" tries="${WAIT_TRIES:-80}" f       # 80 x 180s = up to 4h
  while [ "$tries" -gt 0 ]; do
    f=$(free_vram)
    if awk "BEGIN{exit !(($f)+0 >= $need)}" 2>/dev/null; then echo "[vram] ${f}GB free (>=${need}) OK -> go"; return 0; fi
    echo "[vram $(date +%H:%M)] only ${f}GB free (need ${need}) — GPU busy, waiting 180s ($tries left)..."; sleep 180; tries=$((tries-1))
  done
  echo "[vram] gave up waiting for ${need}GB free"; return 1
}
step () { echo; echo ">>> [$(date +%H:%M:%S)] $*"; }

# --- Arm B: per size, train -> infer -> eval ---
for SIZE in $SIZES; do
  if [ -f "results/eval_router_${SIZE}.json" ]; then echo "[skip] $SIZE eval exists"; continue; fi
  TB=$(train_batch "$SIZE"); IB=$(infer_batch "$SIZE")
  step "TRAIN $SIZE (epochs=$EPOCHS batch=$TB)"
  require_vram "$NEED_FREE" || { echo "!! skip $SIZE train (gpu busy)"; continue; }
  "$DML" scripts/train_router.py --size "$SIZE" --epochs "$EPOCHS" --batch "$TB" --device dml || { echo "!! train $SIZE failed"; continue; }
  step "INFER $SIZE (likelihood, batch=$IB)"
  require_vram "$NEED_FREE" || { echo "!! skip $SIZE infer (gpu busy)"; continue; }
  "$DML" scripts/infer_router.py --size "$SIZE" --batch "$IB" --device dml || { echo "!! infer $SIZE failed"; continue; }
  step "EVAL $SIZE"
  "$PY" scripts/eval.py --preds "data/preds_router_${SIZE}.jsonl" --arm B --label "router_${SIZE}" \
        --out "results/eval_router_${SIZE}.json" || echo "!! eval $SIZE failed"
done

# --- Arm C: compose over A (CPU) and the largest trained router (GPU) ---
step "COMPOSE C x A (e5+bm25, CPU)"
"$PY" scripts/compose_c.py --arm A && \
  "$PY" scripts/eval.py --preds data/preds_cxA.jsonl --arm C --label CxA --out results/eval_CxA.json || echo "!! CxA failed"

CXB_SIZE=""
for SIZE in $SIZES; do [ -f "runs/router_${SIZE}/adapter_model.safetensors" ] && CXB_SIZE="$SIZE"; done
if [ -n "$CXB_SIZE" ]; then
  step "COMPOSE C x B (router $CXB_SIZE)"
  if require_vram "$NEED_FREE"; then
    "$DML" scripts/compose_c.py --arm B --size "$CXB_SIZE" --device dml && \
      "$PY" scripts/eval.py --preds "data/preds_cxB_${CXB_SIZE}.jsonl" --arm C --label "CxB_${CXB_SIZE}" \
            --out "results/eval_CxB_${CXB_SIZE}.json" || echo "!! CxB failed"
  else echo "!! skip CxB (gpu busy)"; fi
fi

step "AGGREGATE"
"$PY" scripts/aggregate_results.py || echo "!! aggregate failed"
echo "SWEEP DONE $(date)"
echo "===================================================================="
