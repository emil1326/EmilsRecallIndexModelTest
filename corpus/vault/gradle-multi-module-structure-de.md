---
title: Gradle multi-module structure de base Arrow
summary: Arrow est structuré en multi-module Gradle avec un root project pis des submodules pour le core, le network et le CLI, c'est propre.
type: reference
links:
  - "[[gradle-dependency-locking-evite-surprises]]"
  - "[[gradle-build-cache-game-changer]]"
  - "[[picocli-pour-le-cli-arrow]]"
  - "[[arrow-outil-java-ne-d]]"
---
Le root `build.gradle` gère les dépendances communes, chaque submodule override ce qu'il a besoin. C'est le setup standard mais ça prend du temps à configurer right au début. Le module `arrow-core` contient toute la logique de data, `arrow-net` gère le networking, `arrow-cli` wrappe picocli.
