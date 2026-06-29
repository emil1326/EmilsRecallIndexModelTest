---
title: LOD groups différents materials cassent le batching
summary: Utiliser des materials différents par niveau de LOD casse le batching entre instances — garder le même material per-LOD te permet de les batcher ensemble.
type: lesson
links:
  - "[[gpu-instancing-bon-mais-faut]]"
  - "[[static-batching-vs-dynamic-batching-2]]"
  - "[[material-count-pis-draw-calls]]"
  - "[[draw-call-budget-selon-la]]"
  - "[[materialpropertyblock-evite-de-casser-le]]"
---
C'est un piège classique — tu mets un material haute-qualité sur LOD0 pis un 'cheap' sur LOD2 pour 'optimiser', pis en fait t'as créé deux buckets séparés qui peuvent plus être batchés ensemble. Si la différence visuelle entre les LOD levels justifie pas des materials distincts, utilise le même material avec des mesh simplifiés. Profite du LOD pour réduire la poly count, pas pour switcher de material si tu peux l'éviter.
