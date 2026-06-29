---
title: Health check avec timestamp pour debugger
summary: Mon /health retourne le timestamp serveur en plus du statut — pratique pour vérifier si le serveur est à jour ou si c'est un vieux process qui traîne.
type: reference
links:
  - "[[le-endpoint-ping-pour-verifier]]"
  - "[[pm2-pour-auto-restart-apres]]"
  - "[[logs-en-fichier-pas-juste]]"
  - "[[uptime-check-avec-un-script]]"
---
Le uptime m'aide à voir si le serveur a redémarré récemment, pis le timestamp me confirme que c'est bien le bon process qui répond. Ça prend genre 3 lignes de plus que le /ping basique pis ça vaut le coup. Sans timestamp, t'as aucun moyen de savoir si le restart a ben marché.
