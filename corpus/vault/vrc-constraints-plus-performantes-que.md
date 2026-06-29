---
title: VRC Constraints plus Performantes que Unity Constraints
summary: Les VRC Constraints introduites par VRChat sont plus performantes que les Unity Constraints de base, pis la migration vaut le coup sur les avatars avec beaucoup de constraints.
type: reference
links:
  - "[[armature-merging-moins-de-bones]]"
  - "[[seuil-critique-150-bones-actifs]]"
  - "[[physbones-chains-complexes-saignent-le]]"
  - "[[frametime-perf-rank-pour-les]]"
---
VRChat a sorti ses propres VRC Constraints pour remplacer les Unity built-in Constraints (Parent, Rotation, Position, etc.) qui sont notoriously pas bien optimisés. Les VRC Constraints ont le même behavior fonctionnel mais sont exécutées dans un job system plus efficace. Si t'as un vieil avatar avec plein de Unity Constraints, migrer vers VRC Constraints c'est une win de perf facile avec peu d'effort.
