---
title: CPU bottleneck pis GPU bottleneck c'est different
summary: Quand le frametime est haut, faut d'abord identifier si c'est le CPU ou le GPU qui stall, parce que les fixes sont complètement orthogonaux.
type: lesson
links:
  - "[[ma-heuristique-d-optim-le]]"
  - "[[gpu-overdraw-pis-fill-rate]]"
  - "[[renderdoc-pour-debug-le-gpu]]"
  - "[[draw-calls-le-vrai-cost]]"
---
Le CPU attend que le GPU finisse (ou vice versa) pis le profiler va te dire lequel des deux est le goulot. Si ton CPU time est bas mais ton frametime est quand même haut, t'es GPU-bound — optimiser le C# va rien changer. C'est une des premières choses à checker avant de tomber dans le rabbit hole d'optim. Genre, vérifier ça prend 30 secondes et ça sauve des heures de debug inutile.
