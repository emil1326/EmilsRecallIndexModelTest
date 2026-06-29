---
title: batch size affecte throughput embedding
summary: En CPU, l'optimal batch size pour l'embedding avec e5-small se situe souvent entre 16 et 64 — trop petit et t'as du overhead, trop grand et la mémoire swap.
type: reference
links:
  - "[[onnx-runtime-pour-embedding-rapide]]"
  - "[[e5-small-choisi-pour-le]]"
  - "[[embedding-caching-pour-eviter-recalcul]]"
  - "[[lazy-rebuild-on-demand-vs]]"
---
C'est pas linéaire, tsu. Batch de 1 c'est le pire pour throughput. Batch de 32 c'est souvent le sweet spot en CPU pour e5-small, tu parallelizes les matrix multiplications. Au-dessus de 64 les gains sont marginaux et tu risques le memory pressure. À tuner sur ta machine.
