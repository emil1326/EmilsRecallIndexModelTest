---
title: EmilsWork branding dans les modules Arrow
summary: Les packages Java d'Arrow utilisent `emilswork.arrow` comme namespace, jamais d'abréviation `ew`, parce que ça read comme yucky et c'est plate.
type: identity
links:
  - "[[arrow-outil-java-ne-d]]"
  - "[[gradle-multi-module-structure-de]]"
  - "[[picocli-pour-le-cli-arrow]]"
  - "[[feature-flags-comme-roadmap-tracker]]"
---
Le package root c'est `emilswork.arrow.core`, `emilswork.arrow.net`, etc. Le nom du projet dans le Gradle c'est `EmilsArrow` dans les metadata, pis le CLI affiche "Emil's Arrow" dans le help text. L'abréviation `EW` a été bannie immédiatement, genre j'allais pas avoir un namespace qui sonne comme une réaction de dégoût smh.
