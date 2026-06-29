---
title: Depth prepass quand ça vaut vraiment la peine
summary: Un depth prepass réduit l'overdraw en opaque geometry, mais ça coûte un draw call additionnel par mesh — ça fit surtout quand t'as vraiment beaucoup d'overlap.
type: lesson
links:
  - "[[overdraw-accumule-les-pixel-invocations]]"
  - "[[render-pipeline-stages-les-cles]]"
  - "[[gpu-bound-vs-cpu-bound]]"
  - "[[renderdoc-pour-investiguer-le-render]]"
  - "[[frametime-en-ms-plus-utile]]"
---
Le depth prepass render la geometry en depth-only d'abord, pis le early-z rejection coupe les pixel shader invocations inutiles dans le color pass. Sur des scènes simples avec peu d'overlap, ça coûte plus que ça rapporte. Là où c'est une win c'est dans des scènes avec beaucoup de mesh qui se chevauchent — genre une jungle dense ou de l'architecture complexe.
