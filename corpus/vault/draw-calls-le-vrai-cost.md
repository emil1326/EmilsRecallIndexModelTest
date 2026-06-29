---
title: Draw calls: le vrai cost sur CPU
summary: Chaque draw call stresse le CPU — c'est le driver qui submit la commande au GPU, pis ça coûte quelques microsecondes chacun, qui s'accumulent vite.
type: reference
links:
  - "[[cpu-bottleneck-pis-gpu-bottleneck]]"
  - "[[static-batching-vs-dynamic-batching]]"
  - "[[gpu-overdraw-pis-fill-rate]]"
  - "[[les-perf-rankings-vrchat-sont]]"
---
Dans VRChat par exemple, un avatar avec 20+ materials différents peut facilement manger 20+ draw calls juste pour lui. Batcher ou réduire les materials c'est souvent plus impactant que d'optimiser le shader lui-même. Le GPU, lui, attend souvent que le CPU finisse de tout soumettre — c'est un bottleneck CPU déguisé en problème GPU.
