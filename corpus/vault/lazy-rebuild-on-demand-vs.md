---
title: lazy rebuild on-demand vs eager rebuild
summary: Le lazy rebuild déclenche l'indexation seulement quand une query arrive ou qu'un threshold de nouveaux docs est atteint — mieux qu'un eager rebuild qui bloque constamment.
type: lesson
links:
  - "[[incremental-indexing-juste-les-nouveaux]]"
  - "[[embedding-caching-pour-eviter-recalcul]]"
  - "[[daemon-tourne-en-background-process]]"
  - "[[batch-size-affecte-throughput-embedding]]"
  - "[[versionner-le-dataset-par-son]]"
---
Pour un daemon personnel, eager rebuild (indexer dès qu'un doc change) c'est overkill et ça mange des ressources pour rien. Lazy rebuild avec un dirty flag par document, ça fit mieux. Quand une query arrive, tu checks si l'index est stale, tu rebuildes juste ce qui a changé.
