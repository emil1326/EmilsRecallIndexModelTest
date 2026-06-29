---
title: Avatar expressions vs custom params — la différence clé
summary: Les Expression Params sont les params custom définis par le créateur d'avatar — à distinguer des built-ins VRChat (Viseme, GestureLeft, etc.) qui sont aussi exposés en OSC.
type: reference
links:
  - "[[avatar-parameters-le-namespace-avatar]]"
  - "[[types-de-params-osc-vrchat]]"
  - "[[config-json-osc-par-avatar]]"
  - "[[format-d-un-message-osc]]"
---
Les Expression Parameters c'est le vrai contenu intéressant pour les devs — c'est ce que le creator a mis dans son avatar pour le contrôler. Les built-in VRChat params (Viseme, GestureLeft, GestureRight, VelocityX, etc.) sont exposés automatiquement pour tout le monde en OSC peu importe l'avatar. Deux catégories très différentes dans leurs usages — faut pas les mélanger dans son code ou son mapping.
