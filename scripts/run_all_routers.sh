#!/usr/bin/env bash
# Sequential router sweep on DirectML — train+infer+eval each size, one after the other,
# each step VRAM-guarded and gentle (completion-only loss + grad-ckpt). Fills the H2 size curve.
#
# SINGLE GPU CONSUMER ONLY. Run only when NOT in VR / not gaming / Ollama unloaded — ideally
# overnight. Each size is a fresh process, so VRAM fully releases between sizes (the next size's
# gpu_guard waits for headroom before allocating). Safe to Ctrl-C between sizes.
#
# Usage:  bash scripts/run_all_routers.sh            # 1.5B then 3B (0.5B already done)
#         bash scripts/run_all_routers.sh 1.5B       # just one size
set -euo pipefail
cd "$(dirname "$0")/.."

SIZES=("$@"); [ ${#SIZES[@]} -eq 0 ] && SIZES=(1.5B 3B)

# per-size gentle batch (3B is bigger -> smaller batch to stay well under the 10 GB cap)
batch_for() { case "$1" in 3B) echo 4;; *) echo 8;; esac; }

echo ">>> [$(date '+%H:%M:%S')] router sweep: ${SIZES[*]}  (free VRAM: $(powershell -NoProfile -ExecutionPolicy Bypass -File scripts/vram_free.ps1 2>/dev/null) GB)"
for s in "${SIZES[@]}"; do
    echo ">>> ===== size $s (batch $(batch_for "$s"), 4 epochs) ====="
    bash scripts/run_router_size.sh "$s" 4 "$(batch_for "$s")"
done
echo ">>> [$(date '+%H:%M:%S')] ROUTER SWEEP COMPLETE -> results/results.json (sizes: ${SIZES[*]})"
echo ">>> H2 size curve + paired verdicts are in results/results.json (verdict.paired_vs_baseline / H2_assoc_hit@10_by_size)"
