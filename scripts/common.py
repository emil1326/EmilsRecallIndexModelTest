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


# --- Vault loader (parse <slug>.md flat frontmatter) -------------------------
def load_vault(vault_dir=None):
    """Return {slug: {title, summary, body, type, links:[slug,...]}} from a dir of
    <slug>.md notes. Mirrors build_corpus.mjs's parser."""
    vault = Path(vault_dir) if vault_dir else path("corpus_dir")
    notes = {}
    for p in sorted(vault.glob("*.md")):
        slug = p.stem
        text = p.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
        if not m:
            continue
        fm, body = m.group(1), m.group(2).strip()
        rec = {"title": "", "summary": "", "type": "", "links": [], "body": body}
        in_links = False
        for line in fm.split("\n"):
            kv = re.match(r"^(\w+):\s*(.*)$", line.rstrip())
            if kv and kv.group(1) in ("title", "summary", "type", "links"):
                in_links = kv.group(1) == "links"
                if in_links:
                    one = re.search(r"\[\[([^\]]+)\]\]", kv.group(2))
                    if one:
                        rec["links"].append(one.group(1).strip())
                else:
                    rec[kv.group(1)] = kv.group(2).strip()
            elif in_links:
                lm = re.search(r"\[\[([^\]]+)\]\]", line)
                if lm:
                    rec["links"].append(lm.group(1).strip())
        notes[slug] = rec
    return notes


# --- Ollama client (local, no data leaves the machine) ----------------------
def ollama_generate(prompt, model=None, system=None, options=None, fmt=None,
                    think=False, retries=3, timeout=180):
    import urllib.request
    host = CONFIG["ollama"]["host"]
    model = model or CONFIG["ollama"]["gen_model"]
    opts = dict(CONFIG["ollama"].get("options", {}))
    if options:
        opts.update(options)
    # think=False matters for reasoning models (qwen3.5): otherwise hidden
    # reasoning eats the num_predict budget and the answer comes back empty.
    payload = {"model": model, "prompt": prompt, "stream": False,
               "think": think, "options": opts}
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


def extract_json(text):
    """Pull the first JSON object/array out of an LLM response, tolerating
    ```json fences and surrounding prose. Returns the parsed value or raises."""
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z]*\n?", "", text)
        text = re.sub(r"\n?```$", "", text).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    # fall back: find the outermost {...} or [...]
    for open_c, close_c in (("{", "}"), ("[", "]")):
        i, j = text.find(open_c), text.rfind(close_c)
        if 0 <= i < j:
            try:
                return json.loads(text[i:j + 1])
            except json.JSONDecodeError:
                continue
    raise ValueError(f"No parseable JSON in: {text[:300]!r}")


def ollama_json(prompt, model=None, system=None, options=None, think=False,
                retries=4, timeout=240):
    """Generate with format=json and return the parsed object. Retries on both
    transport and parse failures."""
    last_err = None
    for attempt in range(retries):
        try:
            raw = ollama_generate(prompt, model=model, system=system,
                                  options=options, fmt="json", think=think,
                                  retries=1, timeout=timeout)
            return extract_json(raw)
        except Exception as e:  # noqa: BLE001
            last_err = e
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"Ollama JSON failed after {retries} tries: {last_err}")
