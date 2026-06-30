"""Central GPU resource router — one place that gates and cleans up DirectML VRAM.

Every GPU phase calls ensure_free() before allocating (waits until enough VRAM is free,
so a leaked/slow-freed previous phase or a concurrent app can't push us into OOM) and
release() after (drops refs + gc so VRAM returns before the process exits). Combined with
small batches, this keeps the GPU footprint low — which also lowers the compute/power
spike, the suspected crash trigger.

Reads free VRAM via scripts/vram_free.ps1 (true registry total - per-ADAPTER dedicated usage).
"""
import gc
import subprocess
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
_PS1 = REPO / "scripts" / "vram_free.ps1"

# headroom (GB free) to require before loading each model size = model footprint + margin,
# and never let usable free drop under the FLOOR.
FREE_FLOOR = 1.5
NEED_FREE = {"0.5B": 4.0, "1.5B": 7.0, "3B": 11.0}


def gpu_free_gb():
    """Free VRAM in GB, or None if it can't be read."""
    try:
        out = subprocess.run(["powershell.exe", "-NoProfile", "-File", str(_PS1)],
                             capture_output=True, text=True, timeout=25)
        return float(out.stdout.strip().replace(",", "."))
    except Exception:  # noqa: BLE001
        return None


def ensure_free(min_gb, wait_s=900, poll=15, label=""):
    """Block until >= min_gb VRAM is free; raise if it never clears within wait_s."""
    min_gb = max(min_gb, FREE_FLOOR)
    t0 = time.time()
    while True:
        f = gpu_free_gb()
        if f is None:
            print(f"[gpu_guard] {label}: cannot read VRAM — proceeding cautiously", flush=True)
            return
        if f >= min_gb:
            print(f"[gpu_guard] {label}: {f}GB free (>= {min_gb}) OK", flush=True)
            return
        if time.time() - t0 > wait_s:
            raise RuntimeError(f"[gpu_guard] {label}: only {f}GB free (< {min_gb}) after {wait_s}s — aborting (GPU busy)")
        print(f"[gpu_guard] {label}: {f}GB free (< {min_gb}) — waiting {poll}s...", flush=True)
        time.sleep(poll)


def ensure_free_for(size, label=""):
    ensure_free(NEED_FREE.get(size, 4.0), label=label or size)


def release(*objs):
    """Drop model refs and force GC so DirectML VRAM is reclaimed before process exit."""
    for o in objs:
        del o
    gc.collect()
    try:
        import torch
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
    except Exception:  # noqa: BLE001
        pass
    time.sleep(1)
    f = gpu_free_gb()
    if f is not None:
        print(f"[gpu_guard] released -> {f}GB free", flush=True)
