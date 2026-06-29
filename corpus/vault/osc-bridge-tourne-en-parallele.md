---
title: OSC bridge tourne en parallèle du HTTP
summary: Le OSC listener et le serveur HTTP sont deux listeners séparés sur des ports différents — ils partagent le même process Node.js mais ne se bloquent pas mutuellement.
type: reference
links:
  - "[[pourquoi-osc-plutot-que-websocket]]"
  - "[[port-mapping-dev-3000-prod]]"
  - "[[le-backend-bridge-unity-vers]]"
  - "[[pm2-pour-auto-restart-apres]]"
---
Unity envoie des messages OSC sur le port 9000 pendant que le HTTP continue de répondre sur 8080. J'ai essayé de merger les deux dans un seul système une fois, c'était une mauvaise idée xD. Deux listeners, deux responsabilités, pis ça fit correctement.
