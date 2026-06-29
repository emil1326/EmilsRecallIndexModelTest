---
title: Transitive deps: le vrai rabbit hole du graph
summary: Tracker les dépendances directes c'est facile, mais les transitive deps (A importe B qui importe C) sont ce qui rend l'invalidation cache vraiment complexe sur des projets réels.
type: journal
links:
  - "[[dependency-graph-colonne-vertebrale-du]]"
  - "[[cascade-invalidation-quand-un-leaf]]"
  - "[[expiration-anticipee-sur-imports-transitifs]]"
  - "[[multi-file-dependency-tracking-c]]"
  - "[[propagation-dans-le-graph-ordre]]"
---
Le problème c'est que les transitive deps peuvent exploser en nombre — un fichier utilitaire importé partout rend tout le monde dépendant de lui. Faut décider si tu veux la full transitive closure dans le graph (précis mais expensive à calculer) ou juste les direct deps (rapide mais peut rater des invalidations). Mon opinion: full transitive closure pour les security rules, direct seulement pour le reste.
