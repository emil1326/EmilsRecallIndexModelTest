---
title: Atlas textures réduit les material swaps entre draws
summary: Regrouper plusieurs textures dans un atlas permet à plusieurs objects d'utiliser le même material, réduisant les material changes coûteux entre draw calls.
type: lesson
links:
  - "[[material-count-pis-draw-calls]]"
  - "[[material-unique-setpass-call-coute]]"
  - "[[srp-batcher-batch-automatique-si]]"
  - "[[gpu-instancing-bon-mais-faut]]"
  - "[[draw-call-budget-selon-la]]"
---
Le principe c'est simple: si deux objets utilisent le même material (donc la même texture atlas), ils peuvent être batchés ensemble ou au moins éviter un SetPass call. Faut juste UV-mapper tes objets pour pointer vers la bonne region de l'atlas. Le tradeoff c'est que t'as moins de contrôle sur le mipmapping par texture individuelle pis ça peut introduire du bleeding aux bords des tiles.
