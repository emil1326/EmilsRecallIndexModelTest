---
title: JSONL: le format de base ML
summary: JSONL (JSON Lines) c'est une ligne par exemple, facile à streamer pis à append sans charger tout en mémoire, tsu c'est le standard de facto ML.
type: reference
links:
  - "[[streaming-jsonl-pour-gros-datasets]]"
  - "[[jsonl-vs-csv-pour-ml]]"
  - "[[append-atomique-au-jsonl-sans]]"
  - "[[metadata-per-ligne-dans-le]]"
---
Chaque ligne est un JSON valide indépendant, genre `{"text": "...", "label": 0}`. Ça stream parfaitement avec un simple `for line in f` en Python, zero overhead. Pas besoin de loader tout le dataset dans un DataFrame avant de savoir si le format est correct — c'est ça la beauté. Comparé à CSV, t'as le typage natif pis les champs arbitraires sans te battre avec les quotes mal escapées.
