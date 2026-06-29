---
title: Dependency graph = colonne vertébrale du cache
summary: Sans dependency graph précis, l'invalidation cache devient du guessing — tu sais pas quels fichiers impactent lesquels, pis tu finis par invalider trop ou pas assez.
type: reference
links:
  - "[[transitive-deps-le-vrai-rabbit]]"
  - "[[cascade-invalidation-quand-un-leaf]]"
  - "[[propagation-dans-le-graph-ordre]]"
  - "[[multi-file-dependency-tracking-c]]"
  - "[[le-lazy-rebuild-se-declenche]]"
---
Le graph représente les relations entre fichiers: A dépend de B, B dépend de C, etc. Quand C change, faut remonter le graph pour invalider A et B aussi. Sans ça, t'as des résultats stale qui traînent pis ça finit par causer des bugs de sécurité silencieux. C'est vraiment la pièce centrale de tout système de cache sérieux.
