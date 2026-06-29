---
title: Le backend bridge Unity vers les outils web
summary: Mon serveur agit comme bridge entre Unity qui envoie via OSC et les outils web EmilsWork — c'est lui le hub central qui garde l'état cohérent.
type: reference
links:
  - "[[osc-bridge-tourne-en-parallele]]"
  - "[[convention-de-nommage-des-routes]]"
  - "[[pourquoi-osc-plutot-que-websocket]]"
  - "[[les-tools-emilswork-pingent-le]]"
---
Quand Unity toggle un feature, le message passe par le serveur qui met à jour l'état pis notifie les autres clients si y'en a. C'est pas vraiment du microservices tsu, c'est juste un point central. Simple mais ça fait exactement ce que j'ai besoin.
