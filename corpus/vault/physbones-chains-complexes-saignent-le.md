---
title: PhysBones Chains Complexes Saignent le CPU
summary: VRChat PhysBones sont plus optimisés que l'ancien Dynamic Bones, mais des chains complexes avec trop de colliders pis de transforms font encore saigner le CPU.
type: lesson
links:
  - "[[seuil-critique-150-bones-actifs]]"
  - "[[skinned-mesh-vs-mesh-renderer]]"
  - "[[armature-merging-moins-de-bones]]"
  - "[[frametime-perf-rank-pour-les]]"
---
Le vrai coût des PhysBones c'est proportionnel au nombre de transforms dans chaque chain et au nombre de colliders qui interagissent. Genre, une queue avec 20 bones pis 8 colliders c'est way plus cher qu'une queue avec 8 bones pis 2 colliders. Merger les bones de PhysBones ou réduire les colliders c'est souvent la première chose à faire sur un avatar de VTuber anime chargé.
