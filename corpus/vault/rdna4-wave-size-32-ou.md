---
title: RDNA4 wave size 32 ou 64 impact occupancy
summary: RDNA4 supporte le wave size 32 ou 64 threads — le choix impact l'occupancy GPU, pis sur des shaders register-heavy, wave32 peut être plus efficace.
type: reference
links:
  - "[[shader-compile-stall-rdna4-c]]"
  - "[[renderdoc-pour-investiguer-le-render]]"
  - "[[async-shader-compilation-evite-les]]"
  - "[[gpu-bound-vs-cpu-bound]]"
  - "[[overdraw-accumule-les-pixel-invocations]]"
---
Sur RDNA4 (architecture Navi 4x), le hardware supporte native wave32 et wave64. Wave64 donne plus d'occupancy théorique mais si ton shader utilise beaucoup de registres (high register pressure), wave64 va réduire l'occupancy réelle parce que chaque wavefront prend plus de registres. Dans ce cas wave32 peut être plus efficace. Le driver AMD choisit souvent automatiquement, mais dans des shaders custom HLSL tu peux hint avec `[WaveSize(32)]`.
