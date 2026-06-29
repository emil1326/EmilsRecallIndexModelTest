---
title: Metadata per-ligne dans le JSONL
summary: Stocker la metadata — source, date de collection, split assignment, version — directement dans chaque ligne JSONL permet de filtrer pis d'auditer le pipeline sans fichiers séparés.
type: reference
links:
  - "[[jsonl-le-format-de-base]]"
  - "[[streaming-jsonl-pour-gros-datasets]]"
  - "[[logger-le-split-avec-seed]]"
  - "[[versionner-le-dataset-par-son]]"
---
Genre `{"text": "...", "label": 1, "source": "reddit", "collected_at": "2024-01-15", "split": "train", "dataset_version": "v2.1"}`. Ça rend chaque exemple auto-documenté pis tu peux rebuild n'importe quel split juste avec un `jq` filter. La colonne `split` dans chaque ligne est particulièrement utile pour reconstruire exactement les mêmes splits plus tard sans re-runner le split script. Overhead négligeable en storage, win énorme en auditabilité.
