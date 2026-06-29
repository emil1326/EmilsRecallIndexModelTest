---
title: HIPBLASLT et gfx1201 en ROCm 6.x
summary: hipBLASLt, la librairie AMD pour les matrix operations accélérées, avait pas de kernels compilés pour gfx1201 dans ROCm 6.x — grosse partie du problème perf.
type: reference
links:
  - "[[hip-target-et-les-gpu]]"
  - "[[rocm-6-4-2-pas]]"
  - "[[rocm-v7-1-changelog-support]]"
  - "[[rdna4-architecture-amd-move-fast]]"
---
hipBLASLt c'est super important pour les LLMs parce que les attention layers et les matrix multiplications passent par là. Sans kernels pour ton GPU target, ROCm fallback soit sur des implémentations génériques lentes, soit sur CPU. C'est une des raisons techniques pourquoi gfx1201 performait pas bien avant ROCm v7.1. Le support officiel inclut les bons kernels compilés.
