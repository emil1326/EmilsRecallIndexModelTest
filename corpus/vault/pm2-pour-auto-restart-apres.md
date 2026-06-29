---
title: PM2 pour auto-restart après un crash
summary: PM2 manage mon serveur Express en prod — il auto-restart après un crash, garde les logs, pis il peut démarrer avec le système si je le configure.
type: reference
links:
  - "[[le-serveur-a-crashe-pendant]]"
  - "[[logs-en-fichier-pas-juste]]"
  - "[[uptime-check-avec-un-script]]"
  - "[[heberger-chez-moi-plutot-que]]"
---
pm2 start server.js --name emilswork-api et c'est à peu près tout ce qu'il faut savoir pour commencer. Le ecosystem.config.js c'est utile si t'as plusieurs apps mais pour un serveur solo, la commande directe fit. Je save la config avec pm2 save pour qu'il survive un reboot machine.
