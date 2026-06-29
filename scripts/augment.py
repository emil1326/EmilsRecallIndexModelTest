"""Augmentation — the generalization lever.

For each NON-held-out training note, generate K paraphrase queries (varying vocabulary
toward the question/symptom side, not just the summary words) with the local LLM on GPU,
and add them to train. This teaches the router to map *novel phrasings* -> slug rather
than memorizing the summary string.

Validity (NON-NEGOTIABLE):
  * Only notes whose summary group is in TRAIN are augmented (held-out notes get only their
    title anchor — their summary/assoc stay a clean novel-phrasing test).
  * Every augmented query is normalized-deduped against the held-out + multi-gold queries
    (no leak) and against existing train queries. Dropped collisions are reported.

Resumable: appends to data/augment.jsonl as it goes. Then merges -> data/train_aug.jsonl.

Usage: python scripts/augment.py [--k 8]
"""
import argparse
import json
from pathlib import Path

import common

CFG = common.config()
DATA = common.path("data_dir")


def gen_paraphrases(title, summary, k, model):
    prompt = f"""Un user cherche UNE note précise dans sa mémoire perso. Voici la note:
Titre: {title}
Résumé: {summary}

Génère EXACTEMENT {k} reformulations DIFFÉRENTES de la requête qu'un user taperait pour
retrouver CETTE note. FRANGLAIS (français + termes techniques anglais). Varie le vocabulaire
vers le côté QUESTION / SYMPTÔME / problème vécu (pas juste recopier le résumé). Courtes,
naturelles, variées (questions, mots-clés, formulation orale).

JSON: {{"queries": ["...", "..."]}}"""
    try:
        out = common.ollama_json(prompt, model=model,
                                 options={"num_predict": 40 + 22 * k, "temperature": 0.9})
        qs = out.get("queries", []) if isinstance(out, dict) else (out if isinstance(out, list) else [])
        return [str(q).strip() for q in qs if str(q).strip()]
    except Exception as e:  # noqa: BLE001
        print(f"  paraphrase failed for '{title[:40]}': {e}", flush=True)
        return []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, default=CFG["augment"]["k_per_note"])
    ap.add_argument("--model", default=CFG["augment"]["model"])
    args = ap.parse_args()
    common.set_seed()

    notes = common.load_vault()
    train = common.read_jsonl(DATA / "train.jsonl")
    heldout = common.read_jsonl(DATA / "heldout.jsonl")
    multigold = common.read_jsonl(DATA / "multigold.jsonl") if (DATA / "multigold.jsonl").exists() else []

    heldout_sources = {p["source"] for p in heldout}          # notes whose summary group is held out
    forbidden = {common.normalize_query(p["query"]) for p in heldout}
    forbidden |= {common.normalize_query(p["query"]) for p in multigold}
    existing = {common.normalize_query(p["query"]) for p in train}

    targets = [s for s in sorted(notes) if s not in heldout_sources]
    print(f"augmenting {len(targets)} non-held-out notes (K={args.k}) on {args.model}", flush=True)

    out_path = DATA / "augment.jsonl"
    done = set()
    if out_path.exists():
        for r in common.read_jsonl(out_path):
            done.add(r["source"])
        print(f"resuming: {len(done)} notes already augmented", flush=True)

    added, dropped = 0, 0
    seen = set(existing)
    f = open(out_path, "a", encoding="utf-8")
    try:
        for i, slug in enumerate(targets):
            if slug in done:
                continue
            n = notes[slug]
            for q in gen_paraphrases(n["title"], n["summary"], args.k, args.model):
                nq = common.normalize_query(q)
                if not nq or nq in forbidden or nq in seen:
                    dropped += 1
                    continue
                seen.add(nq)
                f.write(json.dumps({"query": q, "slug": slug, "kind": "augment",
                                    "source": slug}, ensure_ascii=False) + "\n")
                added += 1
            if (i + 1) % 25 == 0:
                f.flush()
                print(f"  {i+1}/{len(targets)} notes | +{added} aug | {dropped} dropped", flush=True)
    finally:
        f.close()

    # merge train + augment -> train_aug.jsonl
    aug = common.read_jsonl(out_path)
    common.write_jsonl(DATA / "train_aug.jsonl", train + aug)
    report = {"k": args.k, "model": args.model, "augmented_notes": len(targets),
              "augment_pairs": len(aug), "dropped_collisions": dropped,
              "train_pairs": len(train), "train_aug_pairs": len(train) + len(aug)}
    (common.path("results_dir") / "augment_report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2), flush=True)


if __name__ == "__main__":
    main()
