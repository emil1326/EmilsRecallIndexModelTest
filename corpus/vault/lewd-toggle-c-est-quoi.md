---
title: Lewd toggle: c'est quoi concrètement sur un avatar
summary: Un lewd toggle c'est typiquement un parameter d'animation VRChat qui active/désactive des mesh objects ou swap des textures pour passer en mode non-SFW sur un avatar.
type: reference
links:
  - "[[feature-checker-gate-les-toggles]]"
  - "[[osc-le-seul-bridge-temps]]"
  - "[[state-sync-timing-entre-world]]"
  - "[[granularite-conditionnelle-feature-par-feature]]"
---
Dans VRChat, les avatars ont des parameters qui contrôlent les animation layers — le lewd toggle c'est juste un bool ou un int qui trigger une state machine transition pour cacher ou montrer des meshes. Rien de fancy techniquement, mais c'est ce que tout le monde veut gate.
