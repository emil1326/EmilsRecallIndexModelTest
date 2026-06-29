---
title: Refactor Arrow savoir quand arrêter
summary: La leçon la plus utile sur Arrow c'est que les refactors peuvent spiral infiniment, pis à un moment il faut ship le truc même si c'est pas parfait.
type: lesson
links:
  - "[[serialization-jackson-vs-kryo-dans]]"
  - "[[arrow-roadmap-evolue-par-besoin]]"
  - "[[arrow-outil-java-ne-d]]"
  - "[[microbenchmarks-java-pas-reliable-pantoute]]"
---
J'ai réécrit le module de serialization trois fois parce que j'étais jamais satisfied, mais la troisième version est genre 10% mieux que la première. Maintenant je me fixe un timeboxing: si le refactor prend plus de 2h pis le gain est marginal, j'arrête. Arrow est un outil, pas un projet d'art.
