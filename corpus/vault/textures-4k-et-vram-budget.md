---
title: Textures 4K et VRAM Budget par Avatar
summary: Des textures 4K non-compressées sur un avatar peuvent bouffer 50 à 100MB de VRAM chacune, pis personne check ça dans le perf rank officiel.
type: reference
links:
  - "[[vram-budget-en-instance-de]]"
  - "[[dxt-vs-astc-compression-texture]]"
  - "[[mesh-read-write-enabled-double]]"
  - "[[atlas-texture-reduit-draw-calls]]"
---
Le perf rank VRChat check pas la VRAM usage du tout, c'est un angle mort majeur tsu. Une texture 4096×4096 RGBA32 non-compressée ça fait 64MB rien que pour une texture. En instance à 40 personnes avec des avatars lourds en textures, tu peux vite dépasser la VRAM d'une 3060 juste avec les avatars.
