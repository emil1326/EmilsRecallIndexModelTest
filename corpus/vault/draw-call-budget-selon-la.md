---
title: Draw call budget selon la plateforme
summary: Le budget draw calls acceptable varie énormément selon la plateforme cible — PC tolère beaucoup plus que mobile, pis les consoles ont leurs propres quirks.
type: reference
links:
  - "[[gpu-bound-vs-cpu-bound]]"
  - "[[material-count-pis-draw-calls]]"
  - "[[srp-batcher-batch-automatique-si]]"
  - "[[frametime-en-ms-plus-utile]]"
  - "[[static-batching-vs-dynamic-batching-2]]"
---
Sur PC moderne (including RDNA4), 2000-4000 draw calls per frame c'est raisonnable sans trop de problèmes. Sur mobile (iOS/Android), vise 100-200 max si tu veux pas chauffer le device. Sur console, ça dépend du titre et du target frame rate. Ces chiffres sont des starting points, pas des absolus — faut toujours profiler sur le hardware cible réel.
