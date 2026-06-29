---
title: Shader variant explosion ça compile forever
summary: Chaque keyword actif dans un shader peut doubler ou multiplier le nombre de variants à compiler, pis ça dégénère vite en temps de compile absurdes.
type: lesson
links:
  - "[[shader-feature-vs-multi-compile]]"
  - "[[shader-warmup-avant-gameplay-previent]]"
  - "[[async-shader-compilation-evite-les]]"
  - "[[shader-compile-stall-rdna4-c]]"
  - "[[material-count-pis-draw-calls]]"
---
Genre, 10 keywords = potentiellement 1024 variants si c'est tous des `multi_compile`. C'est là que le shader warmup devient un cauchemar pis que les temps de build explosent. La solution c'est d'utiliser `shader_feature` au lieu de `multi_compile` quand c'est possible — Unity va stripper les variants inutilisées. J'avais un shader avec 8 keywords multi_compile pour 'flexibilité' pis le compile prenait 4 minutes. Tata.
