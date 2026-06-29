---
title: embedding caching pour éviter recalcul
summary: Cacher les embeddings à l'indexation est essentiel — recalculer les embeddings à chaque query serait un nonsense total vu le cost computationnel, même avec e5-small.
type: reference
links:
  - "[[incremental-indexing-juste-les-nouveaux]]"
  - "[[lazy-rebuild-on-demand-vs]]"
  - "[[onnx-runtime-pour-embedding-rapide]]"
  - "[[daemon-tourne-en-background-process]]"
---
L'embedding d'un document se fait une fois à l'ingestion, tu persistes ça sur disk (numpy array ou sqlite blob), pis au query time tu loads juste ce qui est nécessaire. Le seul recalcul c'est pour les nouveaux documents ou les modifiés. Sinon ton daemon serait juste pas viable.
