---
title: Texture streaming pis VRAM bandwidth
summary: Les textures trop grosses saturent la VRAM et forcent des swaps avec la RAM système — une latence catastrophique pour le frametime.
type: reference
links:
  - "[[shader-variants-une-explosion-silencieuse]]"
  - "[[gpu-overdraw-pis-fill-rate]]"
  - "[[static-batching-vs-dynamic-batching]]"
  - "[[memory-bandwidth-le-bottleneck-que]]"
---
Le bottleneck VRAM se voit pas toujours dans le CPU/GPU time directement, mais comme des stalls et des hitches quand les textures load. Texture streaming dans Unity mipmap les textures on-demand, mais le streaming budget par défaut est trop bas pour des scènes denses — faut l'ajuster manuellement. En VR, la VRAM est précieuse: chaque texture 4K non-compressée c'est genre 85MB juste là.
