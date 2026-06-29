"""DirectML GPU smoke-test — run BEFORE trusting the device for training.

Confirms torch-directml sees the RX 9070 XT, that a real matmul runs on-device and
matches CPU, and records the working version set to results/directml_env.json.

Run with the DirectML venv:  .venv-dml/Scripts/python scripts/setup_directml.py
"""
import json
import time
from pathlib import Path

import torch
import torch_directml as dml

REPO = Path(__file__).resolve().parent.parent


def main():
    n = dml.device_count()
    dev = dml.device()
    print(f"torch {torch.__version__} | directml devices: {n} | device: {dev}")
    print(f"device name: {dml.device_name(0) if n else 'NONE'}")

    # correctness: matmul on device vs cpu
    torch.manual_seed(0)
    a = torch.randn(512, 512)
    b = torch.randn(512, 512)
    ref = a @ b
    got = (a.to(dev) @ b.to(dev)).cpu()
    max_err = (ref - got).abs().max().item()
    ok = max_err < 1e-2
    print(f"matmul max abs err vs CPU: {max_err:.2e} -> {'OK' if ok else 'MISMATCH'}")

    # rough throughput
    x = torch.randn(2048, 2048).to(dev)
    y = torch.randn(2048, 2048).to(dev)
    for _ in range(3):
        _ = x @ y
    t0 = time.time()
    iters = 50
    for _ in range(iters):
        z = x @ y
    _ = z.cpu()
    dt = time.time() - t0
    gflops = 2 * 2048**3 * iters / dt / 1e9
    print(f"2048^3 matmul x{iters}: {dt:.2f}s (~{gflops:.0f} GFLOP/s)")

    out = {
        "torch": torch.__version__,
        "directml_device_count": n,
        "device_name": dml.device_name(0) if n else None,
        "matmul_max_err": max_err,
        "matmul_ok": ok,
        "matmul_gflops": round(gflops, 1),
    }
    try:
        import transformers, peft  # noqa
        out["transformers"] = transformers.__version__
        out["peft"] = peft.__version__
    except Exception:  # noqa: BLE001
        pass
    (REPO / "results" / "directml_env.json").write_text(
        json.dumps(out, indent=2), encoding="utf-8")
    print("->", REPO / "results" / "directml_env.json")
    if not ok:
        raise SystemExit("DirectML matmul mismatch — do NOT train on this device")


if __name__ == "__main__":
    main()
