---
title: Blendshapes Coûtent Mémoire Même à Zéro
summary: Chaque blendshape sur un mesh existe en mémoire et génère un léger overhead même quand sa valeur est à zéro, pis les avatars anime en ont souvent 200+.
type: reference
links:
  - "[[skinned-mesh-vs-mesh-renderer]]"
  - "[[textures-4k-et-vram-budget]]"
  - "[[unity-profiler-vs-vrchat-in]]"
  - "[[armature-merging-moins-de-bones]]"
---
Unity stocke tous les blendshapes du mesh en mémoire, actives ou pas. Un avatar anime bien thicc en expressions faciales peut avoir facilement 200-300 blendshapes, c'est un chunk de RAM non-négligeable. Si des blendshapes servent à rien (vieux vestige du modèle original), les delete dans le mesh directement c'est une win facile et propre.
