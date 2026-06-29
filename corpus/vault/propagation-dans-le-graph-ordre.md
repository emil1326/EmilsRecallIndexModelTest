---
title: Propagation dans le graph: ordre BFS > DFS
summary: Pour propager les invalidations dans un dependency graph, BFS est généralement préférable à DFS parce qu'il invalide les nodes proches du changement en premier.
type: reference
links:
  - "[[dependency-graph-colonne-vertebrale-du]]"
  - "[[cascade-invalidation-quand-un-leaf]]"
  - "[[transitive-deps-le-vrai-rabbit]]"
  - "[[invalidation-partielle-evite-le-full]]"
  - "[[logger-le-split-avec-seed]]"
---
DFS va deep dans une branche avant de revenir, ce qui peut invalider des nodes lointains avant des nodes intermédiaires — ça change rien fonctionnellement mais c'est moins intuitif à debugger. Avec BFS, les nodes à un hop du changement sont invalidés avant ceux à deux hops, ce qui correspond mieux à l'ordre dans lequel on va probablement avoir besoin de rebuilder. Pas un dealbreaker, mais BFS is cleaner.
