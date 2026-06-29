---
title: DXT vs ASTC: Compression Texture PC VRChat
summary: Sur PC VRChat, DXT5 ou BC7 pour les textures avec alpha c'est le sweet spot; ASTC c'est pour Quest et l'utiliser sur PC c'est une erreur inutile.
type: reference
links:
  - "[[textures-4k-et-vram-budget]]"
  - "[[atlas-texture-reduit-draw-calls]]"
  - "[[shader-variants-poiyomi-et-compile]]"
  - "[[vram-budget-en-instance-de]]"
---
Unity te laisse choisir le format de compression dans les texture import settings. DXT1 pour les textures sans alpha (diffuse), DXT5 ou BC5 pour les normalmaps, BC7 pour qualité maximale. ASTC c'est un format mobile que les GPUs PC supportent pas nativement de façon optimale — aucune raison de l'utiliser si tu target pas Quest.
