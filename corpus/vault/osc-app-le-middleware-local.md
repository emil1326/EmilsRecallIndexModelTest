---
title: OSC app: le middleware local sur la machine
summary: L'OSC app tourne en local sur la machine du user et fait le bridge entre l'API cloud et VRChat en écoutant et envoyant des messages OSC.
type: reference
links:
  - "[[osc-le-seul-bridge-temps]]"
  - "[[archi-feature-checker-api-osc]]"
  - "[[state-sync-timing-entre-world]]"
  - "[[fallback-offline-behavior-si-l]]"
---
L'OSC app c'est le seul morceau qui tourne sur le PC du user pendant qu'il est dans VRChat. Elle poll l'API pour savoir l'état courant (public? underage?) pis elle envoie les bons OSC messages à VRChat pour forcer ou débloquer les toggles. C'est le middleware obligatoire.
