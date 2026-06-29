---
title: Streaming JSONL pour gros datasets
summary: Avec des datasets qui fittent pas en RAM, streamer le JSONL ligne par ligne c'est la solution simple avant de sortir les gros guns comme HuggingFace datasets.
type: reference
links:
  - "[[jsonl-le-format-de-base]]"
  - "[[append-atomique-au-jsonl-sans]]"
  - "[[metadata-per-ligne-dans-le]]"
  - "[[jsonl-vs-csv-pour-ml]]"
---
Un simple `for line in open("data.jsonl"): json.loads(line)` te donne un générateur pratiquement gratuit en mémoire. C'est parfait pour les pipelines de preprocessing où tu transformes exemple par exemple avant d'écrire dans un nouveau JSONL. Pandas `read_json(lines=True, chunksize=N)` marche aussi si t'as besoin de batch processing. HuggingFace `datasets.load_dataset("json", streaming=True)` c'est la version fancy avec les features en plus quand le projet grossit.
