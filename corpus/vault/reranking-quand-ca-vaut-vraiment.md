---
title: reranking: quand ça vaut vraiment le shot
summary: Le reranking vaut la latency cost seulement si ton retrieval initial a un recall suffisant — reranker un mauvais top-20 reste un mauvais top-5.
type: lesson
links:
  - "[[cross-encoder-reranking-ca-coute]]"
  - "[[recall-k-vs-precision-trade]]"
  - "[[hybrid-fusion-dense-plus-sparse]]"
  - "[[retrieval-pipeline-l-ordre-des]]"
---
C'est le piège classique: mettre un reranker pour cacher un retrieval médiocre. Si ton recall@20 est shit, le reranker peut pas inventer des bons docs. Fix le retrieval d'abord, ajoute le reranker après comme polish. Pour un daemon perso avec peu de docs, le reranker est souvent overkill anyway.
