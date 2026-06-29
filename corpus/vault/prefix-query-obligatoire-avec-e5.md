---
title: prefix query: obligatoire avec e5
summary: Sans le prefix 'query:' sur les requêtes, e5 produit des embeddings mal alignés avec les passages — les scores cosine drop significativement, c'est pas optionnel.
type: lesson
links:
  - "[[prefix-passage-pour-indexer-les]]"
  - "[[e5-small-choisi-pour-le]]"
  - "[[cosine-similarity-pas-dot-product]]"
  - "[[retrieval-pipeline-l-ordre-des]]"
---
E5 a été fine-tuned avec des paires (query:, passage:), tsu, enlever ça c'est pas juste une perte marginale. Genre j'ai testé sans et les résultats étaient vraiment bizarres, des docs non-pertinents qui sortaient en top-1. Mets le prefix, c'est juste une string concat.
