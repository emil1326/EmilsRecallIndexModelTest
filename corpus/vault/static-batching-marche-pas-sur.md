---
title: Static Batching Marche Pas sur Avatars VRChat
summary: Le static batching Unity s'applique pas aux avatars VRChat parce qu'ils bougent; le dynamic batching a des contraintes trop strictes pour être utile sur des avatars complexes.
type: reference
links:
  - "[[material-slots-brisent-le-gpu]]"
  - "[[atlas-texture-reduit-draw-calls]]"
  - "[[budget-realiste-moins-de-24]]"
  - "[[renderer-count-dans-le-perf]]"
---
Le static batching dans Unity batch des meshes qui bougent pas ensemble pour réduire les draw calls — mais les avatars bougent, donc ça s'applique pas. Le dynamic batching c'est possible mais avec des contraintes strictes (mesh pas trop gros, même material, etc.) qui sont rarement remplies sur des avatars complexes. Pour les avatars VRChat, la réduction de draw calls passe par le texture atlas et le material merging, pas les systèmes de batching Unity standard.
