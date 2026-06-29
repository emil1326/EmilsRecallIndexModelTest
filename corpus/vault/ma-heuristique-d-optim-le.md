---
title: Ma heuristique d'optim: le frametime, pas le rank
summary: Pour juger si un avatar est bien optimise, je lance le Unity debugger pis je regarde le frametime direct: au-dessus de 4-6ms overall, c'est vraiment pas good.
type: lesson
links:
  - "[[cpu-bottleneck-pis-gpu-bottleneck]]"
  - "[[les-gc-allocs-causent-des]]"
  - "[[profiler-beginsample-pour-isoler-les]]"
---
Le perf rank officiel ment, mais le frametime ment pas. Je me fie au vrai temps par frame dans le debugger Unity plutot qu'au ranking. En haut de ~4-6ms, faut optimiser, peu importe ce que le rank raconte.
