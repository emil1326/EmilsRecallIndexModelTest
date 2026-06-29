---
title: Sync vs async dans les tool pipelines
summary: Les pipelines sync sont plus simples à debugger et à raisonner, mais l'async devient nécessaire dès qu'un step peut bloquer l'UI ou durer plus de quelques secondes.
type: reference
links:
  - "[[lazy-rebuild-declenche-on-demand]]"
  - "[[hot-reload-vs-full-rebuild]]"
  - "[[cache-invalidation-strategy-le-probleme]]"
  - "[[frametime-beats-fps-pour-decider]]"
---
Le mistake c'est souvent d'aller async trop vite parce que "ça pourrait être long". Si ton step prend 200ms, sync c'est fine — le overhead de coordonner l'async dépasse le bénéfice. Le threshold que j'utilise en pratique: si ça peut bloquer le thread principal pour plus d'une frame à 60fps (soit ~16ms), pense async. Pis dès que tu vas async, assure-toi d'avoir un cancellation token dès le départ, pas en retrofit.
