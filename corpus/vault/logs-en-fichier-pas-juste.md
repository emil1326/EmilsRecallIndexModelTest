---
title: Logs en fichier pas juste la console
summary: Les logs du serveur vont dans un fichier avec rotation — relire la console après un crash c'est pas une stratégie, les fichiers de logs c'en est une.
type: reference
links:
  - "[[pm2-pour-auto-restart-apres]]"
  - "[[le-serveur-a-crashe-pendant]]"
  - "[[health-check-avec-timestamp-pour]]"
  - "[[uptime-check-avec-un-script]]"
---
PM2 gère les logs automatiquement en fichier, mais j'add aussi Winston pour logger les événements importants avec des niveaux info, warn, error. Après un crash inattendu, c'est les logs qui m'ont dit ce qui s'était passé. La console c'est pour le dev, les fichiers c'est pour la prod.
