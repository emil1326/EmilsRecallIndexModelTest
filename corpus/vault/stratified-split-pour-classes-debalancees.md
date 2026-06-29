---
title: Stratified split pour classes débalancées
summary: Un stratified split préserve la proportion de chaque classe dans chaque fold, crucial quand ton dataset est imbalancé pour éviter un test set sans exemples d'une classe.
type: reference
links:
  - "[[shuffle-avant-le-split-toujours]]"
  - "[[proportions-80-10-10-vs]]"
  - "[[cross-val-ou-held-out]]"
  - "[[held-out-set-intouchable-en]]"
---
Avec sklearn, `train_test_split(..., stratify=y)` c'est suffisant pour un split simple. Pour la cross-validation, `StratifiedKFold` est le choix par défaut. Si t'as genre 1% de classe positive, un split random pourrait facilement te donner 0% dans ton val set — là tes métriques sont n'importe quoi pis tu le réalises même pas. C'est un bug silencieux le plus souvent, faut checker les distributions après chaque split.
