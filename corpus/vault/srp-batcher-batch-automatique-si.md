---
title: SRP Batcher batch automatique si CBUFFER compatible
summary: Le SRP Batcher d'Unity réduit les SetPass calls en batchant les draw calls des objects qui partagent un même shader, à condition que les propriétés soient dans un CBUFFER.
type: reference
links:
  - "[[material-count-pis-draw-calls]]"
  - "[[material-unique-setpass-call-coute]]"
  - "[[gpu-instancing-bon-mais-faut]]"
  - "[[static-batching-vs-dynamic-batching-2]]"
  - "[[materialpropertyblock-evite-de-casser-le]]"
---
Le SRP Batcher marche pas avec les shaders legacy — faut que toutes les propriétés du material soient dans un CBUFFER nommé `UnityPerMaterial`. Si c'est le cas, Unity batche automatiquement tous les objets qui utilisent ce shader ensemble. Le catch c'est que ça batche par shader, pas par material, donc avoir 50 materials différents avec le même shader c'est still batchable. Pratiquement c'est une win facile.
