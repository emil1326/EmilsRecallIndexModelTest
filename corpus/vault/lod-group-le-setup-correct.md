---
title: LOD Group: le setup correct pour vraiment saver
summary: Un LOD Group mal configuré économise des triangles mais augmente parfois le draw call count — faut que les LODs partagent le même material pour batcher.
type: reference
links:
  - "[[draw-calls-le-vrai-cost]]"
  - "[[static-batching-vs-dynamic-batching]]"
  - "[[skinnedmeshrenderer-expensive-af-cote-cpu]]"
  - "[[le-good-enough-en-perf]]"
---
Le switch LOD déclenche un recalcul chaque frame based on screen percentage, ce qui a un petit cost CPU. Si les seuils sont trop agressifs, tu vois le popping partout et ça rend le truc feel cheap. En VRChat, les LODs marchent pas vraiment côté avatar dans tous les contextes anyway, tsu — faut vérifier dans le context réel.
