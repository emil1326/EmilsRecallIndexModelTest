---
title: Avatar swap reset tous les custom params
summary: Un avatar swap dans VRChat reset tous les params à leur valeur default — ton app desktop doit détecter ça et réenvoyer ses états pour rester sync.
type: lesson
links:
  - "[[avatar-parameters-le-namespace-avatar]]"
  - "[[sync-au-spawn-le-timing]]"
  - "[[config-json-osc-par-avatar]]"
  - "[[types-de-params-osc-vrchat]]"
---
Quand tu switch d'avatar, VRChat réinitialise tous les params à leurs valeurs par défaut définies dans l'animator. Ton app desktop qui maintenait un état se retrouve donc désync après un swap, sans prévenir. La solution: écouter l'event /avatar/change que VRChat envoie en OSC et réenvoyer tout l'état de ton app à ce moment-là.
