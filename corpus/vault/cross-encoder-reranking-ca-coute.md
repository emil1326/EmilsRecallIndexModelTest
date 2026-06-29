---
title: cross-encoder reranking ça coûte cher
summary: Le cross-encoder reranking est bien plus précis que bi-encoder mais fait une passe complète pour chaque (query, doc) pair — O(n) forward passes, pas scalable sur gros sets.
type: lesson
links:
  - "[[reranking-quand-ca-vaut-vraiment]]"
  - "[[e5-small-choisi-pour-le]]"
  - "[[recall-k-vs-precision-trade]]"
  - "[[retrieval-pipeline-l-ordre-des]]"
  - "[[metadata-per-ligne-dans-le]]"
  - "[[temperature-haute-plus-prompt-precis]]"
---
Le bi-encoder comme e5 encode query et doc séparément, donc tu peux précalculer les doc embeddings. Le cross-encoder prend la paire concaténée, impossible de précalculer. Pour du reranking, tu l'appliques juste sur le top-k (genre 20-50 docs) après le retrieval initial.
