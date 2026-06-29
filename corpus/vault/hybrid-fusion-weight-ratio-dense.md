---
title: hybrid fusion weight ratio dense vs sparse
summary: Le ratio de pondération entre dense et BM25 dans le hybrid score est un hyperparamètre à tuner sur tes données — souvent 0.7 dense / 0.3 sparse comme baseline raisonnable.
type: reference
links:
  - "[[rrf-l-algorithme-de-fusion]]"
  - "[[score-normalization-avant-hybrid-fusion]]"
  - "[[hybrid-fusion-dense-plus-sparse]]"
  - "[[bm25-k1-et-b-les]]"
  - "[[wikilinks-pour-tisser-le-graphe]]"
---
Y'a pas de ratio universel, ça dépend de ton corpus et tes query patterns. Pour du contenu technique avec beaucoup de keywords spécifiques, BM25 mérite plus de poids. Pour des notes conversationnelles et sémantiques, monte le dense. Ou utilise RRF qui évite ce headache complètement.
