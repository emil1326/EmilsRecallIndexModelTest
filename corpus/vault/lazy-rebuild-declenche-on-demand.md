---
title: Lazy rebuild déclenché on-demand vs eager
summary: Choisir lazy rebuild évite de recomputer inutilement, mais ajoute de la complexité dans la gestion des dirty flags et des dépendances.
type: lesson
links:
  - "[[cache-invalidation-strategy-le-probleme]]"
  - "[[quand-abstraire-vs-quand-hardcoder]]"
  - "[[sync-vs-async-dans-les]]"
  - "[[build-by-need-pas-by]]"
---
L'approche eager c'est simple — tu rebuild à chaque change, tu sais que c'est à jour. Mais à scale, ça devient un goulot d'étranglement réel. Le lazy c'est plus smart mais tsu, tu dois tracker ce qui est dirty correctement sinon tu sers des stale results sans t'en rendre compte. Le bug le plus plate c'est un dirty flag qui se reset trop tôt.
