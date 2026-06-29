---
title: MaterialPropertyBlock évite de casser le batching
summary: MaterialPropertyBlock permet de modifier des propriétés shader per-object sans créer un nouveau material instance, ce qui préserve le batching contrairement à material.SetFloat().
type: reference
links:
  - "[[srp-batcher-batch-automatique-si]]"
  - "[[material-count-pis-draw-calls]]"
  - "[[gpu-instancing-bon-mais-faut]]"
  - "[[static-batching-vs-dynamic-batching-2]]"
  - "[[material-unique-setpass-call-coute]]"
---
Si tu fais `renderer.material.SetFloat(...)`, Unity crée implicitement un nouveau material instance — ça casse le batching. Avec `MaterialPropertyBlock`, tu push les données directement dans le constant buffer per-object sans toucher au material. C'est la way to go pour des variations de couleur/scale sur des objets batchés. Le seul catch: ça marche pas avec le SRP Batcher, qui a son propre system de per-instance data.
