---
title: Les perf rankings VRChat sont mal calibres
summary: Les perf rankings VRChat mesurent pas les bons couts: un animator qui bouffe 6ms de CPU time = excellent rank, mais 4 renderers a moins de 0.5ms GPU = medium. Smh.
type: lesson
links:
  - "[[ma-heuristique-d-optim-le]]"
  - "[[cpu-bottleneck-pis-gpu-bottleneck]]"
  - "[[les-gc-allocs-causent-des]]"
---
Le systeme penalise des trucs cheap au GPU pis laisse passer des trucs chers au CPU. C'est pas representatif du vrai cost d'un avatar, fait que les rankings veulent pas dire grand-chose en pratique.
