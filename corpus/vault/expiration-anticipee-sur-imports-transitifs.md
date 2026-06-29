---
title: Expiration anticipée sur imports transitifs modifiés
summary: Quand C change et que A importe B qui importe C, l'entrée cache de A doit expirer même sans import direct — les deps transitives font partie du contrat d'invalidation correcte.
type: lesson
links:
  - "[[transitive-deps-le-vrai-rabbit]]"
  - "[[dependency-graph-colonne-vertebrale-du]]"
  - "[[early-expiration-sur-changement-de]]"
  - "[[cascade-invalidation-quand-un-leaf]]"
  - "[[multi-file-dependency-tracking-c]]"
---
C'est la subtilité qui distingue un cache d'analyse correct d'un qui génère des false negatives. Si ton outil analyse les types ou les side effects d'un import, un changement transitif peut invalider les résultats même sans changement du fichier source direct. En pratique: stocker la transitive closure des deps dans chaque entrée cache, ou propager les invalidations correctement via le graph.
