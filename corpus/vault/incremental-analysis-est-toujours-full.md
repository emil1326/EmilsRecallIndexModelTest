---
title: Incremental analysis est toujours > full rebuild
summary: Analyser seulement les fichiers qui ont vraiment changé et leurs dépendants est toujours plus rapide qu'un full rebuild, même si le code d'orchestration est plus complexe à écrire.
type: lesson
links:
  - "[[dependency-graph-colonne-vertebrale-du]]"
  - "[[invalidation-partielle-evite-le-full]]"
  - "[[le-lazy-rebuild-se-declenche]]"
  - "[[cascade-invalidation-quand-un-leaf]]"
---
Le full rebuild c'est facile à implémenter et ça marche — pour cinq minutes sur un petit projet. Dès que le codebase grossit ou que l'outil doit donner du feedback en quasi-realtime, l'incremental devient non-négociable. L'effort supplémentaire de setup le dependency graph et l'invalidation partielle paie énormément à long terme.
