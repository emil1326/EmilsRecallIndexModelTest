---
title: Logger le split avec seed et date
summary: Logger la seed utilisée, la date du split pis les tailles des sets dans un fichier de metadata garantit de retrouver exactement quel split a été utilisé six mois plus tard.
type: reference
links:
  - "[[seed-fixe-pour-reproductibilite-totale]]"
  - "[[versionner-le-dataset-par-son]]"
  - "[[metadata-per-ligne-dans-le]]"
  - "[[reproductibilite-end-to-end-du]]"
---
Genre un fichier `split_info.json` avec `{"seed": 42, "date": "2024-01-15", "train_size": 80000, "val_size": 10000, "test_size": 10000, "dataset_hash": "abc123"}`. Ça prend 5 minutes à ajouter au script pis ça sauve des heures de "mais quel split t'avais utilisé là?" six mois plus tard. Couplé à la metadata per-ligne dans chaque exemple JSONL, t'as un audit trail complet du pipeline sans effort.
