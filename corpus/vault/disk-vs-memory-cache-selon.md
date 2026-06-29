---
title: Disk vs memory cache selon la taille du projet
summary: Cache mémoire = ultra-rapide mais volatil; cache disque = persistant mais ajoute I/O — pour un gros codebase les deux en layers c'est la bonne réponse.
type: reference
links:
  - "[[serialisation-cache-json-lisible-vs]]"
  - "[[cache-hit-rate-la-vraie]]"
  - "[[cache-warming-au-startup-nice]]"
  - "[[hot-path-analyser-les-fichiers]]"
---
Le pattern two-level cache: un hot cache en mémoire pour les fichiers récemment analysés, pis un cold cache sur disque pour la persistance entre sessions. Quand la mémoire est pleine, tu evict vers le disque (LRU ou LFU). Pour un outil d'analyse léger, disk-only avec bon indexing c'est souvent suffisant et bien moins compliqué à gérer.
