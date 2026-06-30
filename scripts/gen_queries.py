"""Run 2 — generate the CLEAN query sets (the fix for the eval confounds in EXPERIMENTPRECISIONS.md).

The held-out eval must contain ZERO note-verbatim text. So we LLM-generate two query kinds
per note (franglais, symptom/second-hop vocabulary, never the title/summary words), split a
disjoint slice to held-out (never trained), and add the rest to train as augmentation:

  symptom : a problem/symptom-vocabulary question for note N (gold = N). Tests the cause↔symptom
            vocab gap embedding cosine struggles with — NOT a verbatim match.
  assoc   : a genuine SECOND-HOP question. Given N links [[B]] (B is the relevant note when you
            hit N's situation), a question someone facing N would ask whose ANSWER is B, phrased
            WITHOUT quoting N. gold = B, source = N (excluded at scoring, see eval.py).

Outputs: data/heldout.jsonl (clean eval), data/augment.jsonl (train queries),
data/train_aug.jsonl (anchors + train queries). Verified: held-out query text never in train.

Usage: python scripts/gen_queries.py [--per-note 5] [--heldout 0.2]
"""
import argparse
import json
import random
from pathlib import Path

import common

CFG = common.config()
DATA = common.path("data_dir")
MANIFEST = common.path("corpus_dir").parent / "manifest.json"


def gen_symptom(note, k, model):
    prompt = f"""Note de mémoire d'un dev (franglais). Titre: {note['title']}
Résumé: {note['summary']}
Détail: {note.get('body','')[:300]}

Écris {k} questions DIFFÉRENTES qu'un user taperait pour retrouver CETTE note — mais formulées
côté SYMPTÔME / problème vécu, PAS avec les mots du titre. FRANGLAIS (français + termes techniques
anglais). Vocabulaire de la galère réelle ("pourquoi X foire", "comment debug Y"), zéro recopie du titre.

JSON: {{"queries": ["...", "..."]}}"""
    try:
        out = common.ollama_json(prompt, model=model, options={"num_predict": 40 + 26 * k, "temperature": 0.9})
        return [str(q).strip() for q in out.get("queries", []) if str(q).strip()]
    except Exception:  # noqa: BLE001
        return []


def gen_assoc(src, tgt, model):
    prompt = f"""Deux notes reliées dans une mémoire de dev.
NOTE SOURCE (le problème/contexte): {src['title']} — {src['summary'][:120]}
NOTE CIBLE (la réponse/principe lié): {tgt['title']} — {tgt['summary'][:120]}

Écris UNE question FRANGLAIS qu'un user taperait en faisant face au contexte de la SOURCE, et dont
la MEILLEURE réponse est la note CIBLE. INTERDIT de citer les mots spécifiques de la source ou de la
cible — formule un vrai besoin d'info de second niveau (le principe général, pas le cas précis).

JSON: {{"query": "..."}}"""
    try:
        out = common.ollama_json(prompt, model=model, options={"num_predict": 70, "temperature": 0.85})
        q = str(out.get("query", "")).strip()
        return q or None
    except Exception:  # noqa: BLE001
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-note", type=int, default=5)
    ap.add_argument("--max-links", type=int, default=2, help="second-hop queries per note")
    ap.add_argument("--heldout", type=float, default=0.2)
    ap.add_argument("--model", default=CFG["augment"]["model"])
    args = ap.parse_args()
    common.set_seed()
    rng = random.Random(CFG["seed"] + 23)

    notes = json.loads(MANIFEST.read_text(encoding="utf-8"))["notes"]
    slugs = sorted(notes)
    anchors = common.read_jsonl(DATA / "train.jsonl")
    anchor_q = {common.normalize_query(p["query"]) for p in anchors}

    out_path = DATA / "queries_raw.jsonl"
    done_sources = set()
    if out_path.exists():
        for r in common.read_jsonl(out_path):
            done_sources.add(r["_src"])
        print(f"resuming: {len(done_sources)} notes done", flush=True)

    f = open(out_path, "a", encoding="utf-8")
    try:
        for i, s in enumerate(slugs):
            if s in done_sources:
                continue
            n = notes[s]
            rows = []
            for q in gen_symptom(n, args.per_note, args.model):
                rows.append({"query": q, "gold": [s], "kind": "symptom", "source": s, "_src": s})
            for t in n["links"][: args.max_links]:
                if t in notes:
                    q = gen_assoc(n, notes[t], args.model)
                    if q:
                        rows.append({"query": q, "gold": [t], "kind": "assoc", "source": s, "_src": s})
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
            f.flush()
            if (i + 1) % 25 == 0:
                print(f"  {i+1}/{len(slugs)} notes", flush=True)
    finally:
        f.close()

    # ---- split train/eval with NO leak ----
    raw = common.read_jsonl(out_path)
    seen, uniq = set(), []
    for r in raw:
        nq = common.normalize_query(r["query"])
        if not nq or nq in anchor_q or nq in seen:
            continue
        seen.add(nq)
        uniq.append(r)
    rng.shuffle(uniq)
    heldout, aug = [], []
    eval_q = set()
    for r in uniq:
        nq = common.normalize_query(r["query"])
        to_eval = rng.random() < args.heldout
        rec = {"query": r["query"], "kind": r["kind"], "gold": r["gold"], "source": r["source"]}
        if to_eval:
            heldout.append(rec)
            eval_q.add(nq)
        else:
            aug.append({"query": r["query"], "slug": r["gold"][0], "kind": r["kind"], "source": r["source"]})
    # final guard: drop any train query whose text collides with an eval query
    aug = [a for a in aug if common.normalize_query(a["query"]) not in eval_q]

    common.write_jsonl(DATA / "heldout.jsonl", heldout)
    common.write_jsonl(DATA / "augment.jsonl", aug)
    common.write_jsonl(DATA / "train_aug.jsonl", anchors + aug)

    leak = sum(1 for h in heldout if common.normalize_query(h["query"]) in anchor_q)
    by = lambda rows, key: {k: sum(1 for r in rows if r.get("kind") == k) for k in ("symptom", "assoc")}
    report = {"notes": len(slugs), "raw_queries": len(raw), "unique": len(uniq),
              "heldout": len(heldout), "heldout_by_kind": by(heldout, "kind"),
              "train_queries": len(aug), "train_aug_total": len(anchors) + len(aug),
              "leak_into_anchors": leak}
    (common.path("results_dir") / "queries_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
