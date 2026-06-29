---
title: Burst compiler pour les loops heavy
summary: Le Burst compiler de Unity transforme du C# IL en native code optimisé (SIMD, vectorisation) — plusieurs fois plus rapide que le C# managé pour des math loops.
type: reference
links:
  - "[[struct-layout-pis-cache-locality]]"
  - "[[les-gc-allocs-causent-des]]"
  - "[[cpu-bottleneck-pis-gpu-bottleneck]]"
  - "[[micro-benchmark-le-piege-du]]"
---
C'est pas magique pour tout, mais pour du traitement batch de vertices, des calculs physiques custom ou des pathfinding loops, le speedup est genre 5x-20x pour vrai. Faut utiliser des structs blittables et des NativeArrays — pas de managed refs dans du Burst code, sinon erreur compile. Le Job System va souvent de pair pour paralleliser sur plusieurs cores en même temps.
