---
title: Lazy rebuild Arrow se déclenche on-demand
summary: Le lazy rebuild dans Arrow se déclenche on-demand seulement quand les données sont accessed, pas au startup, ce qui coupe le temps de boot significativement.
type: lesson
links:
  - "[[in-memory-store-bati-sur]]"
  - "[[arrow-outil-java-ne-d]]"
  - "[[gradle-build-cache-game-changer]]"
  - "[[microbenchmarks-java-pas-reliable-pantoute]]"
---
Au début j'initialisais tout à l'avance pis le startup time était atroce. J'ai switché vers un lazy init pattern genre `computeIfAbsent` sur le store principal. Maintenant Arrow boot en quelques ms pis reconstruit les structures seulement quand quelqu'un les demande, ce qui fait du sens tbh.
