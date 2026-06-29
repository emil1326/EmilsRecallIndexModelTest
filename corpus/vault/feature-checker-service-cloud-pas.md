---
title: Feature checker: service cloud, pas script local
summary: Faire du feature checker un service cloud plutôt qu'un script local permet des updates de logique de gate sans que le user ait à rien réinstaller.
type: journal
links:
  - "[[archi-feature-checker-api-osc]]"
  - "[[osc-app-le-middleware-local]]"
  - "[[api-auth-qui-a-le]]"
  - "[[fallback-offline-behavior-si-l]]"
---
Si la logique de gate était hardcodée dans l'OSC app locale, chaque changement de règle nécessiterait une mise à jour de l'app. Avec un service cloud, on peut tweaker les règles côté serveur pis tout le monde bénéficie automatiquement. Ça vaut l'overhead d'avoir à gérer un backend.
