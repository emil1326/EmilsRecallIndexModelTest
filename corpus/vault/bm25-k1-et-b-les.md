---
title: BM25 k1 et b les paramètres clés
summary: BM25 a deux hyperparamètres: k1 contrôle la saturation du term frequency (défaut 1.5), b contrôle la normalisation par longueur de document (défaut 0.75).
type: reference
links:
  - "[[bm25-tokenization-stemming-pis-stopwords]]"
  - "[[bm25-still-slaps-pour-keywords]]"
  - "[[passage-length-optimal-pour-e5]]"
  - "[[hybrid-fusion-weight-ratio-dense]]"
---
k1=1.5 veut dire qu'un terme qui apparaît 3x vs 1x donne plus de score, mais avec diminishing returns. b=0.75 pénalise les longs documents qui contiendraient plus de termes par chance. Pour des notes courtes, b peut être réduit à genre 0.5. Vaut la peine de tuner sur ton corpus.
