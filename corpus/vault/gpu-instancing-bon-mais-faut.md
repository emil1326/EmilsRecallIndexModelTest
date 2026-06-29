---
title: GPU Instancing bon mais faut atteindre le threshold
summary: Le GPU Instancing est efficace seulement quand t'as suffisamment d'instances identiques par draw call — en dessous d'un certain nombre, l'overhead annule le gain.
type: lesson
links:
  - "[[srp-batcher-batch-automatique-si]]"
  - "[[static-batching-vs-dynamic-batching-2]]"
  - "[[draw-call-budget-selon-la]]"
  - "[[material-count-pis-draw-calls]]"
  - "[[lod-groups-differents-materials-cassent]]"
---
En pratique, GPU Instancing commence à payer autour de 20-30+ instances du même mesh+material. En dessous de ça, le overhead du constant buffer instancing dépasse ce que tu gagnes. Sur RDNA4, le threshold exact va dépendre du mesh complexity pis du shader, mais la règle de 20 minimum c'est un bon point de départ. C'est pas une solution magique pour quelques arbres épars sur une map.
