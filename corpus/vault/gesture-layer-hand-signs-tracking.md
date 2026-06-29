---
title: Gesture layer hand signs tracking
summary: Le Gesture layer est dédié aux animations de mains et lit GestureLeft et GestureRight (Int 0-7) pour déclencher des hand signs sur le rig humanoid.
type: reference
links:
  - "[[fx-layer-regne-sur-quasi]]"
  - "[[action-layer-pour-emotes-et]]"
  - "[[write-defaults-on-off-vraie]]"
  - "[[transition-exit-time-desactiver-immediatement]]"
---
Les valeurs GestureLeft et GestureRight vont de 0 (Neutral) à 7 (ThumbsUp) et correspondent aux hand poses définies dans le SDK VRChat. Ce layer devrait rester séparé du FX parce qu'il touche directement au rig humanoid des mains. Si t'as un finger tracking fancy, c'est ici que les animations de doigts se setup.
