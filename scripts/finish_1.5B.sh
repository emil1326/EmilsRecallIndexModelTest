#!/usr/bin/env bash
# Finish the 1.5B router unattended, the OLD SAFE way: gentle low-batch inference (batch 8,
# pause 0.7), a single long-running process (no kill/relaunch churn), VRAM-guarded. Resumes from
# the existing checkpoint. Soft-retry loop recovers from transient python errors (NOT power-offs —
# those reboot the box; just relaunch this script if that happens). Then eval + aggregate.
set -uo pipefail
cd "$(dirname "$0")/.."
PY=".venv-dml/Scripts/python"
LOG="results/finish_1.5B.log"
: > "$LOG"

echo ">>> [$(date '+%H:%M:%S')] finish 1.5B: gentle resume (batch 8, pause 0.7)" | tee -a "$LOG"
for attempt in 1 2 3 4 5; do
    done=$(wc -l < data/preds_router_1.5B.jsonl 2>/dev/null || echo 0)
    if [ "$done" -ge 1139 ]; then echo ">>> infer complete ($done/1139)" | tee -a "$LOG"; break; fi
    echo ">>> [$(date '+%H:%M:%S')] attempt $attempt: $done/1139 done -> resuming" | tee -a "$LOG"
    "$PY" scripts/infer_router.py --size 1.5B --device dml --batch 8 --pause 0.7 2>&1 | tee -a "$LOG"
    sleep 8
done

done=$(wc -l < data/preds_router_1.5B.jsonl 2>/dev/null || echo 0)
if [ "$done" -lt 1139 ]; then
    echo ">>> [$(date '+%H:%M:%S')] STILL INCOMPLETE ($done/1139) after retries — stopping (checkpoint safe)" | tee -a "$LOG"
    exit 1
fi

echo ">>> [$(date '+%H:%M:%S')] eval + aggregate" | tee -a "$LOG"
python scripts/eval.py --preds data/preds_router_1.5B.jsonl --arm B --label router_1.5B \
    --out results/eval_router_1.5B.json 2>&1 | tee -a "$LOG"
python scripts/aggregate_results.py 2>&1 | tail -25 | tee -a "$LOG"
echo ">>> [$(date '+%H:%M:%S')] 1.5B COMPLETE -> results/eval_router_1.5B.json + results.json" | tee -a "$LOG"
