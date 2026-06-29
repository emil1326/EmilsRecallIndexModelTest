---
title: Testing sans public world: galère complète
summary: Tester le feature checker en conditions réelles c'est difficile parce que recréer un vrai public world avec un user underage c'est juste pas possible normalement.
type: journal
links:
  - "[[api-rate-limiting-sur-les]]"
  - "[[underage-detection-aucun-signal-magique]]"
  - "[[state-sync-timing-entre-world]]"
  - "[[osc-app-le-middleware-local]]"
---
Pour tester, faut soit avoir deux comptes VRChat (un underage, un normal), soit mock les responses d'API en local. En vrai testing en public world c'est chiant parce que y'a du monde random partout. J'ai fini par tester avec des mock data et un peu de foi. Pas glorieux mais ça fit.
