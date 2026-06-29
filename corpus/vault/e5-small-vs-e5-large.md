---
title: e5-small vs e5-large le vrai test
summary: E5-large est nettement meilleur sur les benchmarks MTEB mais pour un retrieval sur corpus personnel de quelques milliers de docs, la différence pratique est souvent décevante.
type: lesson
links:
  - "[[e5-small-choisi-pour-le]]"
  - "[[passage-length-optimal-pour-e5]]"
  - "[[onnx-runtime-pour-embedding-rapide]]"
  - "[[recall-k-vs-precision-trade]]"
---
J'ai testé les deux sur mes propres notes pis honnêtement, e5-small était juste fine. La vraie différence se voit sur des requêtes ambiguës complexes, mais dans un second brain bien structuré tes queries sont souvent assez directes. Le latency et memory cost de large, eux, sont bien réels.
