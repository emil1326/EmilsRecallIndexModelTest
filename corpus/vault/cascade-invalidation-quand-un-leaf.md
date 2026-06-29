---
title: Cascade invalidation quand un leaf node change
summary: Quand un fichier de base du dependency graph change, il faut invalider tous ses dépendants en cascade — sinon les résultats d'analyse upstream restent wrongos silencieusement.
type: lesson
links:
  - "[[dependency-graph-colonne-vertebrale-du]]"
  - "[[le-lazy-rebuild-se-declenche]]"
  - "[[invalidation-partielle-evite-le-full]]"
  - "[[propagation-dans-le-graph-ordre]]"
  - "[[transitive-deps-le-vrai-rabbit]]"
---
Le piège c'est que l'invalidation cascade peut être expensive si le graph est deep. Faut marquer les nodes comme dirty sans nécessairement rebuilder tout de suite — lazy evaluation au rescue. J'ai vu des systèmes invalider des centaines de fichiers pour un changement dans un helper commun, c'est là que le lazy rebuild devient essentiel.
