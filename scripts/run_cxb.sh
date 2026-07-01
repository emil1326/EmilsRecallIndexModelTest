#!/usr/bin/env bash
# Arm C×B — decompose each multi-answer query -> route every sub-query through the router ->
# RRF-fuse the sub-rankings -> coverage@k. This is the audit's #1 untested multi-answer lever:
# the router is a far stronger per-sub-query retriever than the baseline (assoc H@10 0.877 vs 0.579),
# and RRF fixes the round-robin union that made C×A regress. GPU, gentle, VRAM-guarded.
#
# Usage:  bash scripts/run_cxb.sh [size]     (default 1.5B — the best trained router)
set -uo pipefail
cd "$(dirname "$0")/.."
PY=".venv-dml/Scripts/python"
SIZE="${1:-1.5B}"
LOG="results/cxb_${SIZE}.log"; : > "$LOG"

echo ">>> [$(date '+%H:%M:%S')] C×B ${SIZE}: compose (decompose -> router -> RRF fusion, batch 16)" | tee -a "$LOG"
"$PY" scripts/compose_c.py --arm B --size "$SIZE" --device dml --fusion rrf --batch 16 2>&1 | tee -a "$LOG"

echo ">>> [$(date '+%H:%M:%S')] C×B ${SIZE}: eval + aggregate" | tee -a "$LOG"
python scripts/eval.py --preds "data/preds_cxB_${SIZE}.jsonl" --arm C --label "CxB_${SIZE}" \
    --out "results/eval_CxB_${SIZE}.json" 2>&1 | tee -a "$LOG"
python scripts/aggregate_results.py 2>&1 | tail -15 | tee -a "$LOG"
echo ">>> [$(date '+%H:%M:%S')] C×B ${SIZE} DONE -> results/eval_CxB_${SIZE}.json" | tee -a "$LOG"
