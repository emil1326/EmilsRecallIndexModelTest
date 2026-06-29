---
title: Memory bandwidth: le bottleneck que personne regarde
summary: Même si le CPU pis le GPU semblent idle, la bandwidth mémoire peut être le bottleneck — et les profilers classiques le montrent rarement directement.
type: reference
links:
  - "[[texture-streaming-pis-vram-bandwidth]]"
  - "[[gpu-overdraw-pis-fill-rate]]"
  - "[[struct-layout-pis-cache-locality]]"
  - "[[renderdoc-pour-debug-le-gpu]]"
---
Quand tu lis des textures 4K non-compressées, du vertex data non-interleaved ou des buffers scattered en mémoire, tu peux saturer le bus mémoire sans que le GPU soit à 100%. Les formats de texture compressés (BC7, ASTC) réduisent pas juste la VRAM — ils reducent aussi la bandwidth nécessaire à chaque sample. C'est un des rabbit holes les plus obscurs en GPU perf, honnêtement.
