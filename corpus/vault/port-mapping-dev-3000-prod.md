---
title: Port mapping dev 3000 prod 8080 OSC 9000
summary: J'ai standardisé mes ports: 3000 pour le dev local, 8080 pour la prod sur ma machine, 9000 pour le bridge OSC Unity — tout ça vient du .env.
type: reference
links:
  - "[[osc-bridge-tourne-en-parallele]]"
  - "[[env-local-jamais-committe-jamais]]"
  - "[[pourquoi-osc-plutot-que-websocket]]"
  - "[[le-backend-bridge-unity-vers]]"
---
Ça évite les conflits quand j'ai les deux environnements qui tournent en même temps. La valeur vient du .env alors je change jamais ça hardcodé dans le code. Le 9000 pour OSC c'est un peu arbitraire mais maintenant c'est établi pis je touche pas à ça.
