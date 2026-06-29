---
title: Occlusion culling: le setup coûte avant de saver
summary: L'occlusion culling bake un volume data file pis fait des ray queries runtime — dans des petites scènes ou open worlds, le cost dépasse parfois le gain.
type: lesson
links:
  - "[[draw-calls-le-vrai-cost]]"
  - "[[gpu-overdraw-pis-fill-rate]]"
  - "[[le-good-enough-en-perf]]"
  - "[[lod-group-le-setup-correct]]"
---
Le bake est une opération longue et le résultat dépend de comment tu setup les occluders et occludees — mal configuré, ça cull rien d'utile. Si ta scène a peu de gros objets solides, l'occlusion save pas grand chose et le query overhead traîne pour rien. Frustum culling est automatique de toute façon — l'occlusion c'est un extra pour des scènes denses et fermées seulement.
