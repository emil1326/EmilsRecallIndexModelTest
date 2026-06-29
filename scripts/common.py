"""Shared utilities: config, HF-cache redirect, seeding, slug helpers, Ollama client.

IMPORTANT: importing this module sets HF_HOME/HF_HUB_CACHE to a folder on F:
*before* transformers/sentence-transformers get a chance to read them. C: only has
~32 GB free; e5 + 0.5-3B base models would blow it. So always `import common` first.
"""
import os
import re
import json
import time
import hashlib
import unicodedata
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# --- HF cache redirect (must happen before any HF import) -------------------
_cfg_path = REPO_ROOT / "configs" / "experiment.json"
with open(_cfg_path, "r", encoding="utf-8") as _f:
    CONFIG = json.load(_f)

_hf_cache = (REPO_ROOT / CONFIG["paths"]["hf_cache"]).resolve()
_hf_cache.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("HF_HOME", str(_hf_cache))
os.environ.setdefault("HF_HUB_CACHE", str(_hf_cache / "hub"))
os.environ.setdefault("SENTENCE_TRANSFORMERS_HOME", str(_hf_cache / "sbert"))
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")


def config():
    return CONFIG


def path(key):
    """Resolve a configured path (under paths.*) to an absolute Path."""
    return (REPO_ROOT / CONFIG["paths"][key]).resolve()


def set_seed(seed=None):
    seed = CONFIG["seed"] if seed is None else seed
    import random
    random.seed(seed)
    try:
        import numpy as np
        np.random.seed(seed)
    except ImportError:
        pass
    try:
        import torch
        torch.manual_seed(seed)
    except ImportError:
        pass
    return seed


# --- Slug helpers -----------------------------------------------------------
def slugify(text, maxlen=60):
    """kebab-case ascii slug. Deterministic."""
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    return text[:maxlen].strip("-")


def stable_hash(s):
    """Deterministic hash in [0,1) — used for held-out splitting (not Python's
    salted hash())."""
    h = hashlib.sha256(s.encode("utf-8")).hexdigest()
    return int(h[:16], 16) / float(1 << 64)


def normalize_query(q):
    """Canonical form for leak-detection / dedup (case + whitespace + punctuation
    folded)."""
    q = unicodedata.normalize("NFKD", q).encode("ascii", "ignore").decode("ascii")
    q = q.lower()
    q = re.sub(r"[^a-z0-9]+", " ", q)
    return re.sub(r"\s+", " ", q).strip()


# --- JSONL helpers ----------------------------------------------------------
def read_jsonl(p):
    out = []
    with open(p, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def write_jsonl(p, rows):
    p = Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


# --- Ollama client (local, no data leaves the machine) ----------------------
def ollama_generate(prompt, model=None, system=None, options=None, fmt=None,
                    retries=3, timeout=180):
    import urllib.request
    host = CONFIG["ollama"]["host"]
    model = model or CONFIG["ollama"]["gen_model"]
    opts = dict(CONFIG["ollama"].get("options", {}))
    if options:
        opts.update(options)
    payload = {"model": model, "prompt": prompt, "stream": False, "options": opts}
    if system:
        payload["system"] = system
    if fmt:
        payload["format"] = fmt  # "json" or a JSON schema dict
    data = json.dumps(payload).encode("utf-8")
    last_err = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                host + "/api/generate", data=data,
                headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                body = json.loads(resp.read().decode("utf-8"))
                return body.get("response", "")
        except Exception as e:  # noqa: BLE001
            last_err = e
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"Ollama generate failed after {retries} tries: {last_err}")
