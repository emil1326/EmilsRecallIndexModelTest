---
title: Rate limiting OSC — VRChat throttle tes sends
summary: VRChat throttle les messages OSC entrants à haute fréquence — faut envoyer seulement les changements d'état, pas un continuous stream, sinon les params lag ou droppent.
type: lesson
links:
  - "[[latence-osc-en-dessous-de]]"
  - "[[udp-fire-and-forget-pas]]"
  - "[[impact-perf-osc-overhead-sur]]"
  - "[[build-un-bridge-desktop-architecture]]"
---
Si tu spam des messages OSC vers VRChat trop rapidement, le jeu commence à en ignorer — le rate exact est pas documenté officiellement mais ça se voit en pratique. L'approche correcte c'est un delta-check avant chaque envoi: si la valeur a pas changé, t'envoies pas. Ça réduit le traffic à quasi-rien pour la plupart des use cases et élimine le throttling.
