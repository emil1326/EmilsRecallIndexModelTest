---
title: Proportions 80/10/10 vs 70/15/15
summary: Les proportions 80/10/10 (train/val/test) sont le standard de facto, mais avec peu de données 70/15/15 donne des val et test sets plus stables statistiquement.
type: reference
links:
  - "[[stratified-split-pour-classes-debalancees]]"
  - "[[held-out-set-intouchable-en]]"
  - "[[cross-val-ou-held-out]]"
  - "[[shuffle-avant-le-split-toujours]]"
---
Avec 100k exemples, 10k en val et 10k en test c'est largement suffisant pour des estimations stables. Avec 10k total, 1k en test c'est serré — tes métriques vont varier beaucoup entre seeds pis tu peux pas trop te fier aux résultats. Dans ce cas 1.5k ou 2k en test donne des intervalles de confiance plus raisonnables. Y'a pas de règle universelle, c'est une question de combien de variance tu tolères dans ton estimation de perf.
