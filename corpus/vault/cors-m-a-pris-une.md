---
title: CORS m'a pris une heure pour rien
summary: J'ai perdu une heure à debugger une CORS error qui venait juste du fait que j'avais oublié d'inclure Authorization dans les allowed headers.
type: journal
links:
  - "[[api-key-dans-le-header]]"
  - "[[garder-le-server-lean-sans]]"
  - "[[env-local-jamais-committe-jamais]]"
  - "[[ajouter-un-endpoint-decision-intentionnelle]]"
---
allowedOrigin '*' était là, allowedMethods aussi, mais le header Authorization était pas dans allowedHeaders pis le browser bloquait silencieusement. Depuis ce temps-là j'add un CORS config template que je colle dès le début du projet. Smh.
