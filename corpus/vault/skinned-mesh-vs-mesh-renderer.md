---
title: Skinned Mesh vs Mesh Renderer CPU Cost
summary: Les skinned mesh renderers font un recalcul CPU à chaque frame pour les bones, contrairement aux mesh renderers statiques qui sont ben moins chers.
type: reference
links:
  - "[[armature-merging-moins-de-bones]]"
  - "[[seuil-critique-150-bones-actifs]]"
  - "[[physbones-chains-complexes-saignent-le]]"
  - "[[blendshapes-coutent-memoire-meme-a]]"
---
Tout mesh avec des bones associés dans l'armature devient un skinned mesh renderer automatiquement dans Unity, même si le mesh bouge pas vraiment. Les accessoires statiques (oreilles rigides, épaulettes fixes) devraient idéalement être des mesh renderers normaux si c'est faisable. C'est pas toujours possible avec le setup VRChat, mais c'est à garder en tête quand tu design l'avatar dès le départ.
