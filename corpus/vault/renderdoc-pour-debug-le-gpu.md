---
title: RenderDoc pour debug le GPU pour vrai
summary: RenderDoc capture un frame complet et te montre chaque drawcall, les textures bindées, les shader inputs/outputs — bien plus précis que le Unity Profiler côté GPU.
type: reference
links:
  - "[[gpu-overdraw-pis-fill-rate]]"
  - "[[cpu-bottleneck-pis-gpu-bottleneck]]"
  - "[[shader-variants-une-explosion-silencieuse]]"
  - "[[draw-calls-le-vrai-cost]]"
---
Le Unity Profiler te donne le GPU time total par category, mais RenderDoc te montre exactement quel draw call prend combien de ms et pourquoi il est là. C'est là que tu réalises que ton overdraw vient de trois passes de particules qui draw au même endroit en alpha blend. Setup un peu rough au début, mais une fois que tu sais t'en servir, t'es dépendant — smh.
