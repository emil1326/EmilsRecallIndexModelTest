---
title: Le serveur a crashé pendant une session live
summary: Une fois mon Express server a crashé en plein milieu d'une session de dev parce qu'une unhandled promise rejection a tout tué — une erreur de rookie.
type: journal
links:
  - "[[pm2-pour-auto-restart-apres]]"
  - "[[logs-en-fichier-pas-juste]]"
  - "[[garder-le-server-lean-sans]]"
  - "[[uptime-check-avec-un-script]]"
---
Je savais même pas que ça pouvait crasher de même tsu, j'avais pas de process.on('unhandledRejection'). PM2 l'aurait redémarré mais j'avais pas encore PM2. Depuis ce jour-là, j'add un global error handler pis PM2 dès le début, jamais en retard.
