---
title: e5-small choisi pour le bon trade-off
summary: E5-small offre une qualité sémantique suffisante pour du retrieval personnel avec un footprint minimal — pas besoin de large pour ce use case.
type: reference
links:
  - "[[e5-small-vs-e5-large]]"
  - "[[daemon-tourne-en-background-process]]"
  - "[[onnx-runtime-pour-embedding-rapide]]"
  - "[[batch-size-affecte-throughput-embedding]]"
---
Le modèle large c'est tentant mais pour un daemon qui tourne en background, e5-small est assez bon. La différence de qualité entre small et large est là mais franchement pour des notes perso c'est marginal. Pis le latency gap, lui, il est bien réel.
