---
title: Convention de nommage des routes EmilsWork
summary: Les routes de mon API suivent le pattern /emilswork/<tool>/<action> — verbeux mais jamais ambigu, pis ça fit avec le branding.
type: reference
links:
  - "[[api-key-dans-le-header]]"
  - "[[ajouter-un-endpoint-decision-intentionnelle]]"
  - "[[le-backend-bridge-unity-vers]]"
  - "[[response-format-json-meme-pour]]"
---
Genre /emilswork/aac/status ou /emilswork/featurelocker/toggle. C'est plus long que /api/v1/... mais quand t'as plein d'outils différents sur le même serveur, t'as pas le choix de garder ça organisé. Pas de versioning pour l'instant parce que c'est juste moi qui consomme l'API.
