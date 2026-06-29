---
title: API rate limiting sur les calls VRChat publics
summary: L'API VRChat a des rate limits pas documentés, donc le feature checker doit être smart sur la fréquence de ses checks pour pas se faire throttle.
type: lesson
links:
  - "[[vrchat-api-instance-type-source]]"
  - "[[state-sync-timing-entre-world]]"
  - "[[osc-app-le-middleware-local]]"
  - "[[archi-feature-checker-api-osc]]"
---
C'est un peu un rabbit hole de trouver les vrais rate limits de VRChat — leur doc est sparse là-dessus. En pratique le feature checker poll pas en continu; il check à des moments clés (world join, avatar change) pis cache le résultat. Ça évite de hammer l'API pour rien.
