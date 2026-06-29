---
title: Le lazy rebuild se déclenche on-demand seulement
summary: Le lazy rebuild attend qu'on demande les résultats pour reanalyser un fichier, pas juste parce qu'il a changé — ça sauve énormément de CPU.
type: lesson
links:
  - "[[cascade-invalidation-quand-un-leaf]]"
  - "[[dependency-graph-colonne-vertebrale-du]]"
  - "[[incremental-analysis-est-toujours-full]]"
  - "[[hot-path-analyser-les-fichiers]]"
---
En pratique, si personne ouvre le fichier X, son analyse reste stale pis c'est correct. Le problème arrive quand un module dépend de X — là faut détecter que X est dirty pis rebuild on-the-fly avant de retourner les résultats. J'ai pogné ça à la dure avec un pipeline qui rebuilait TOUT à chaque keystroke, smh.
