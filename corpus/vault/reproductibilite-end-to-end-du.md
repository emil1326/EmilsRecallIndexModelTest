---
title: Reproductibilité end-to-end du pipeline
summary: Pour reproduire exactement un run ML, faut locker la version du code, le hash du dataset, toutes les seeds, les versions des librairies pis les hyperparamètres.
type: lesson
links:
  - "[[seed-fixe-pour-reproductibilite-totale]]"
  - "[[seeds-differents-par-librairie-attention]]"
  - "[[versionner-le-dataset-par-son]]"
  - "[[logger-le-split-avec-seed]]"
---
Un `requirements.txt` avec des versions pinnées (pas juste `>=`), un hash du dataset, un `seed=42` partout pis un config file versionné dans git — c'est le minimum absolu. Le problème c'est que même avec tout ça, des non-déterminismes GPU (CUDA) peuvent faire varier les résultats au dernier décimal. Pour du vrai reproductible, faut soit désactiver les ops non-déterministes avec `torch.use_deterministic_algorithms(True)`, soit accepter une variance epsilon et documenter que c'est voulu.
