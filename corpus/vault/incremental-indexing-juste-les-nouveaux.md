---
title: incremental indexing juste les nouveaux docs
summary: L'indexation incrémentale recompute les embeddings et BM25 stats seulement pour les documents nouveaux ou modifiés — évite de rebuilder l'index complet inutilement.
type: lesson
links:
  - "[[lazy-rebuild-on-demand-vs]]"
  - "[[embedding-caching-pour-eviter-recalcul]]"
  - "[[bm25-k1-et-b-les]]"
  - "[[bm25-tokenization-stemming-pis-stopwords]]"
---
Pour BM25 c'est un peu plus complexe parce que les IDF stats dépendent du corpus entier. Un incremental update partiel peut drift légèrement vs un rebuild complet. Pour un daemon perso avec quelques milliers de notes, rebuilder le BM25 index complet reste rapide — l'embedding c'est l'étape coûteuse.
