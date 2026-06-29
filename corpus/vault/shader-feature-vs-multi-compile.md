---
title: shader_feature vs multi_compile le stripping qui sauve
summary: Utiliser shader_feature au lieu de multi_compile permet à Unity de stripper automatiquement les variants non utilisées dans ton projet — essentiel pour contrôler l'explosion du nombre de variants.
type: reference
links:
  - "[[shader-variant-explosion-ca-compile]]"
  - "[[shader-warmup-avant-gameplay-previent]]"
  - "[[async-shader-compilation-evite-les]]"
  - "[[shader-compile-stall-rdna4-c]]"
  - "[[material-count-pis-draw-calls]]"
---
`multi_compile` génère TOUTES les combinaisons peu importe si elles sont utilisées. `shader_feature` génère seulement les variants pour lesquelles une keyword est activée sur au moins un material dans le projet. La différence peut être de centaines de variants. La règle: `multi_compile` pour les keywords globales (qualité settings, platform features), `shader_feature` pour les features qui dépendent des materials.
