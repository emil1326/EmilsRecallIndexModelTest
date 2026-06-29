---
title: Async shader compilation évite les stalls RDNA4
summary: L'async shader compilation d'Unity permet de compiler les PSO en background, affichant un placeholder shader pendant ce temps — ça évite les stalls visibles mais faut gérer le placeholder.
type: reference
links:
  - "[[shader-compile-stall-rdna4-c]]"
  - "[[shader-warmup-avant-gameplay-previent]]"
  - "[[shader-variant-explosion-ca-compile]]"
  - "[[rdna4-wave-size-32-ou]]"
  - "[[frametime-en-ms-plus-utile]]"
---
En pratique, le placeholder shader (souvent un magenta ou un flat color selon le setup) apparaît pendant que le vrai shader compile async. C'est acceptable en editing mais faut s'assurer que ça arrive pas en gameplay. La solution propre c'est de combiner l'async compile avec un ShaderVariantCollection warmup au load — tu compiles tout ce qui est critique de façon synchrone au loading screen.
