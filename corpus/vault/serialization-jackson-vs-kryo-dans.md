---
title: Serialization Jackson vs Kryo dans Arrow
summary: J'ai choisi Jackson pour la serialization dans Arrow plutôt que Kryo parce que la lisibilité du format compte plus que la perf raw pour ce use case.
type: lesson
links:
  - "[[in-memory-store-bati-sur]]"
  - "[[distributed-data-arrow-sans-consensus]]"
  - "[[microbenchmarks-java-pas-reliable-pantoute]]"
  - "[[arrow-outil-java-ne-d]]"
---
Kryo est plus rapide mais le format binaire c'est un pain à debug, genre t'as aucune idée ce qui est sérialisé si ça break. Jackson avec JSON c'est un peu plus verbose mais au moins je peux ouvrir le fichier pis voir ce qui se passe. Pour du distributed in-memory, la debuggabilité > la perf brute.
