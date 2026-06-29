---
title: Uptime check avec un script cron simple
summary: Un cron job qui ping mon /health toutes les 5 minutes et m'envoie un message si le serveur répond pas — simple, pas fancy, mais ça marche.
type: reference
links:
  - "[[health-check-avec-timestamp-pour]]"
  - "[[pm2-pour-auto-restart-apres]]"
  - "[[heberger-chez-moi-plutot-que]]"
  - "[[le-serveur-a-crashe-pendant]]"
---
C'est pas du monitoring de niveau production tsu, c'est un script bash de 10 lignes. Mais quand ma machine a rebooté et que PM2 avait pas survécu pour une raison X, j'ai été notifié en genre 5 minutes. Pour un usage solo, c'est amplement suffisant.
