---
title: Light probes vs realtime lights: le vrai cost
summary: Une realtime light recalcule les shadow maps chaque frame et affect le batching — les light probes bake la lumière une fois, zéro cost runtime pour les objets dynamic.
type: lesson
links:
  - "[[draw-calls-le-vrai-cost]]"
  - "[[gpu-overdraw-pis-fill-rate]]"
  - "[[les-perf-rankings-vrchat-sont]]"
  - "[[ma-heuristique-d-optim-le]]"
---
Chaque realtime light qui cast des shadows ajoute des shadow map passes au render, ce qui multiplie les draw calls pour tous les objets dans son range. Dans VRChat, les realtime lights custom sont souvent la première chose à couper pour récupérer du frametime meaningful. Les light probes sont pas parfaits visuellement mais ça fit pour des perfs raisonnables sans trop sacrifier l'ambiance.
