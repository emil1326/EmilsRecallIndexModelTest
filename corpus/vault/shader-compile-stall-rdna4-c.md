---
title: Shader compile stall RDNA4 c'est brutal
summary: RDNA4 a un comportement de shader compile différent des archs précédentes, pis les stalls que ça génère peuvent causer des hitches visibles directement en gameplay.
type: lesson
links:
  - "[[shader-warmup-avant-gameplay-previent]]"
  - "[[async-shader-compilation-evite-les]]"
  - "[[rdna4-wave-size-32-ou]]"
  - "[[frametime-en-ms-plus-utile]]"
  - "[[renderdoc-pour-investiguer-le-render]]"
---
Sur RDNA4 (RX 9000 series), le pipeline de shader compilation a changé versus RDNA2/3. Le driver compile les PSO (pipeline state objects) de façon plus aggressive pis si t'as pas warmé tes shaders avant, t'as des hitches de 50-200ms qui pop au pire moment. J'ai galéré à comprendre pourquoi mon frame budget explosait sur une scène pourtant simple — c'était pas l'overdraw, c'était le shader compile. T'as vraiment besoin d'une warmup strategy solide sur cette arch-là.
