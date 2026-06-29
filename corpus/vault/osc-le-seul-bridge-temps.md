---
title: OSC: le seul bridge temps-réel avec VRChat
summary: OSC (Open Sound Control) c'est le protocole qu'utilise VRChat pour communiquer en temps réel avec des apps externes — c'est la seule option viable pour toggle des features avatar live.
type: reference
links:
  - "[[osc-app-le-middleware-local]]"
  - "[[archi-feature-checker-api-osc]]"
  - "[[state-sync-timing-entre-world]]"
  - "[[osc-vs-websocket-pourquoi-osc]]"
---
VRChat supporte OSC nativement, ce qui permet d'envoyer et recevoir des messages localement vers l'avatar. C'est genre du UDP sur localhost, donc super rapide mais un peu finicky sur la config des ports. Sans OSC y'aurait zéro moyen de toggle quoi que ce soit sur l'avatar depuis l'extérieur.
