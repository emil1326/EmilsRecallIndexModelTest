---
title: Invalidation partielle évite le full rebuild
summary: Invalider seulement les entrées cache affectées par un changement plutôt que tout vider réduit massivement le travail de rebuild sur les gros projets.
type: lesson
links:
  - "[[dependency-graph-colonne-vertebrale-du]]"
  - "[[le-lazy-rebuild-se-declenche]]"
  - "[[cascade-invalidation-quand-un-leaf]]"
  - "[[incremental-analysis-est-toujours-full]]"
  - "[[cache-hit-rate-la-vraie]]"
---
Pour ça il te faut absolument un dependency graph — sans ça tu peux pas savoir quoi invalider précisément. Le naive approach c'est de tout invalider dès qu'un fichier change, mais sur un projet de 10k fichiers c'est inutilisable. Invalidation partielle plus lazy rebuild = la combo qui rend le cache réellement utile.
