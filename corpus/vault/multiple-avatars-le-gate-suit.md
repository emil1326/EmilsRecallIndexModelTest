---
title: Multiple avatars: le gate suit le user, pas l'avatar
summary: Le feature checker gate selon le contexte du user (world type, âge déclaré), pas selon quel avatar spécifique est équipé — le tracking est user-level, pas avatar-level.
type: reference
links:
  - "[[vrchat-api-instance-type-source]]"
  - "[[osc-app-le-middleware-local]]"
  - "[[state-sync-timing-entre-world]]"
  - "[[lewd-toggle-c-est-quoi]]"
---
Ça simplifie pas mal le tracking: l'OSC app a besoin de savoir "dans quel type de world est CE user" et "est-ce qu'il est underage". Pas besoin de tracker chaque avatar séparément. Si le user change d'avatar dans un public world, le gate s'applique quand même. Logique.
