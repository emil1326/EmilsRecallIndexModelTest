---
title: Material Slots Brisent le GPU Batching
summary: Chaque material slot unique sur un avatar génère un draw call séparé, pis ça casse le GPU batching même si les meshes sont simples.
type: lesson
links:
  - "[[atlas-texture-reduit-draw-calls]]"
  - "[[budget-realiste-moins-de-24]]"
  - "[[unity-stats-window-premier-tool]]"
  - "[[renderer-count-dans-le-perf]]"
  - "[[static-batching-marche-pas-sur]]"
---
Un avatar avec 3 meshes mais 12 materials différentes c'est 12 draw calls minimum, tsé. L'impact c'est multiplicatif en instance: 40 personnes × 12 draw calls, ça commence à faire mal au GPU collectif. La solution c'est de merger les materials et faire un texture atlas, c'est le move le plus high-impact per effort ratio.
