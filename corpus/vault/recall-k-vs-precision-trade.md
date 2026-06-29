---
title: recall@k vs precision trade-off retrieval
summary: En retrieval, recall@k mesure combien de docs pertinents tu catches dans le top-k — pour alimenter un reranker ou LLM, préférer recall élevé sur precision, quitte à avoir du bruit.
type: lesson
links:
  - "[[reranking-quand-ca-vaut-vraiment]]"
  - "[[cross-encoder-reranking-ca-coute]]"
  - "[[hybrid-fusion-dense-plus-sparse]]"
  - "[[retrieval-pipeline-l-ordre-des]]"
---
C'est contre-intuitif mais pour un système qui passe les résultats à un LLM, tu veux pas rater des docs pertinents. Quelques faux positifs dans le top-20 c'est less bad que rater le meilleur doc. Augmente ton k au retrieval, laisse le reranker ou le LLM filter. Genre recall@20 > precision@5.
