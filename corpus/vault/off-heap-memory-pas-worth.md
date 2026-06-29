---
title: Off-heap memory pas worth it Arrow
summary: J'ai évalué stocker les données Arrow off-heap avec `sun.misc.Unsafe` ou ByteBuffer direct pour réduire la GC pressure, pis j'ai conclu que c'était pas worth it.
type: lesson
links:
  - "[[in-memory-store-bati-sur]]"
  - "[[microbenchmarks-java-pas-reliable-pantoute]]"
  - "[[refactor-arrow-savoir-quand-arreter]]"
  - "[[replication-factor-3-comme-defaut]]"
---
`sun.misc.Unsafe` c'est pas public API, ça peut break à chaque Java version, et gérer manuellement la mémoire en Java c'est demander des segfaults. La GC pressure avec `ConcurrentHashMap` est gérable pour les volumes d'Arrow. On est pas Netflix ici tsu, l'over-engineering serait du pure waste.
