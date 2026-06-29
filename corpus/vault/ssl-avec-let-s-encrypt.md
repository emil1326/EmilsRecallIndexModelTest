---
title: SSL avec Let's Encrypt qui renouvèle tout seul
summary: Pour HTTPS sur mon serveur j'utilise Let's Encrypt avec certbot en auto-renew — le certificat se renouvèle tout seul, j'y pense plus après le premier setup.
type: reference
links:
  - "[[env-local-jamais-committe-jamais]]"
  - "[[heberger-chez-moi-plutot-que]]"
  - "[[uptime-check-avec-un-script]]"
  - "[[api-key-dans-le-header]]"
---
certbot --nginx ou certbot --standalone selon le setup, pis un cron job que certbot installe lui-même pour le renouvèlement automatique. La première fois c'est un peu de setup pour pointer le domain, mais après c'est set and forget. HTTPS sur un serveur perso c'est pas overkill, c'est juste correct.
