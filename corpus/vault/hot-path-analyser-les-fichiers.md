---
title: Hot path: analyser les fichiers chauds en premier
summary: Prioriser l'analyse des fichiers modifiés récemment ou fréquemment maximise l'utilité perçue de l'outil — l'user voit des résultats fresh là où il travaille activement.
type: reference
links:
  - "[[cache-warming-au-startup-nice]]"
  - "[[le-lazy-rebuild-se-declenche]]"
  - "[[cache-hit-rate-la-vraie]]"
  - "[[disk-vs-memory-cache-selon]]"
---
Tracker les fichiers par fréquence d'accès ou de modification donne une heuristique simple pour décider quoi analyser en premier. En pratique, les fichiers ouverts dans l'éditeur right now sont les candidats évidents pour le hot path. C'est aussi une bonne idée de revalider le cache sur les hot files plus agressivement que sur les fichiers qui changent rarement.
