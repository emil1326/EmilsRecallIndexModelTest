---
title: Build un bridge desktop — architecture app OSC
summary: Une app desktop OSC VRChat c'est au minimum un UDP listener sur 9001 et un sender vers 9000, avec une UI pour mapper et contrôler les params d'avatar.
type: journal
links:
  - "[[ports-9000-9001-le-handshake]]"
  - "[[osc-dans-vrchat-protocole-de]]"
  - "[[lib-osc-existante-vs-implementation]]"
  - "[[rate-limiting-osc-vrchat-throttle]]"
  - "[[monitoring-params-en-live-workflow]]"
---
L'architecture de base: un thread UDP listener sur 127.0.0.1:9001 pour recevoir de VRChat, un sender vers 127.0.0.1:9000, et un dictionnaire params->valeurs courantes pour maintenir l'état. La UI peut être n'importe quoi — Electron, WPF, même un terminal. Le tricky c'est la gestion du state et le resync après un avatar swap, pas la partie networking qui est triviale.
