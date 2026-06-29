---
title: Armature Merging: Moins de Bones, Plus Rapide
summary: Merger les bones d'accessoires dans l'armature principale réduit le nombre de GameObjects Unity à processer chaque frame et allège le CPU skinning overhead.
type: reference
links:
  - "[[seuil-critique-150-bones-actifs]]"
  - "[[skinned-mesh-vs-mesh-renderer]]"
  - "[[physbones-chains-complexes-saignent-le]]"
  - "[[vrc-constraints-plus-performantes-que]]"
---
Quand tu add un hat ou des ailes à un avatar, la bonne pratique c'est de merger l'armature de l'accessoire dans l'armature principale dans Blender avant d'importer. Ça réduit le nombre total d'objects dans la hiérarchie Unity et peut aider le skinning à être plus efficace. C'est une best practice standard en VRChat avatar creation, mais les gens l'oublient quand ils rush leur setup.
