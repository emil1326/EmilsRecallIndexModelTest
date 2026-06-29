---
title: Mesh Read/Write Enabled Double la VRAM
summary: Cocher Read/Write Enabled sur un mesh dans Unity en double la présence mémoire, une copie CPU et une copie GPU; à désactiver si inutile pour les avatars.
type: reference
links:
  - "[[textures-4k-et-vram-budget]]"
  - "[[vram-budget-en-instance-de]]"
  - "[[blendshapes-coutent-memoire-meme-a]]"
  - "[[unity-stats-window-premier-tool]]"
---
Unity garde un mesh en VRAM pour le GPU, et si Read/Write est activé, il garde aussi une copie en RAM CPU pour que le code puisse la lire et modifier. Sur les avatars VRChat, t'as généralement pas besoin de ça après upload. Check les import settings de chaque mesh et désactive Read/Write si t'as pas de runtime deformation — c'est un quick win souvent overlooked.
