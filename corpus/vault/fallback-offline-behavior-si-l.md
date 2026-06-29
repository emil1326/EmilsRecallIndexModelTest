---
title: Fallback offline: behavior si l'API répond pas
summary: Si l'API cloud est down ou unreachable, l'OSC app a un comportement de fallback clair: expirer le cache local et gate tout par défaut, pas laisser passer.
type: lesson
links:
  - "[[la-logique-de-gate-fallback]]"
  - "[[osc-app-le-middleware-local]]"
  - "[[feature-checker-service-cloud-pas]]"
  - "[[api-rate-limiting-sur-les]]"
---
L'OSC app garde le dernier état connu en cache local avec un TTL. Si l'API répond pas pendant plus d'un certain temps, elle expire le cache et gate tout. Oui c'est annoying si le serveur plante, mais c'est way mieux que de laisser du lewd content passer parce que le backend avait des problèmes.
