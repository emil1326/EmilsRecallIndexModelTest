---
title: Ports 9000/9001 — le handshake OSC VRChat
summary: VRChat écoute sur le port 9000 (reçoit tes messages OSC) et envoie ses données sur le 9001, pis ça se configure pas vraiment autrement.
type: reference
links:
  - "[[osc-dans-vrchat-protocole-de]]"
  - "[[port-deja-occupe-erreur-silencieuse]]"
  - "[[build-un-bridge-desktop-architecture]]"
  - "[[udp-fire-and-forget-pas]]"
---
Port 9000 = VRChat écoute, port 9001 = VRChat envoie. Si un autre process occupe le 9001 avant VRChat, tu vas recevoir strictement rien pis galérer longtemps avant de comprendre pourquoi. Classique port conflict silencieux, smh — toujours la première chose à vérifier.
