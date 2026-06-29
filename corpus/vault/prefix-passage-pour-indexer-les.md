---
title: prefix passage: pour indexer les docs
summary: Chaque chunk de document doit être préfixé avec 'passage:' avant l'embedding — c'est la contrepartie du prefix query: pour l'alignement du modèle e5.
type: reference
links:
  - "[[prefix-query-obligatoire-avec-e5]]"
  - "[[passage-length-optimal-pour-e5]]"
  - "[[embedding-caching-pour-eviter-recalcul]]"
  - "[[retrieval-pipeline-l-ordre-des]]"
---
C'est simple mais facile à oublier côté indexing si tu sépares le pipeline. Le prefix 'passage:' va avec chaque chunk au moment de l'ingestion, pas au query time. Si t'oublies ça, tes embeddings sont dans un espace légèrement différent pis le retrieval souffre silencieusement.
