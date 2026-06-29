---
title: Static batching vs dynamic batching le vrai tradeoff
summary: Static batching merge les meshes en RAM pour une draw call, dynamic batching le fait CPU-side chaque frame — le tradeoff c'est mémoire vs CPU time.
type: reference
links:
  - "[[srp-batcher-batch-automatique-si]]"
  - "[[gpu-instancing-bon-mais-faut]]"
  - "[[draw-call-budget-selon-la]]"
  - "[[lod-groups-differents-materials-cassent]]"
  - "[[material-count-pis-draw-calls]]"
---
Static batching c'est la meilleure option pour les objets qui bougent jamais — Unity merge les meshes en un gros mesh, un draw call, mais ça prend de la mémoire pour stocker les mesh combinés. Dynamic batching fonctionne en temps réel mais Unity doit re-combiner les vertices chaque frame, pis ça marche seulement pour des petits meshes (moins de ~300 vertices selon Unity). Sur des scènes avec beaucoup d'objets statiques, le static batching + SRP Batcher c'est le combo gagnant.
