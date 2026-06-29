---
title: HIP target et les GPU non-officiels ROCm
summary: ROCm compile ses kernels HIP pour des cibles gfx précises — si ton GPU est pas dans la liste officielle, t'as zero garantie que ça va run correctement.
type: reference
links:
  - "[[rocm-6-4-2-pas]]"
  - "[[hsa-override-gfx-version-workaround]]"
  - "[[hipblaslt-et-gfx1201-en-rocm]]"
  - "[[gpu-support-officiel-vs-community]]"
---
HIP c'est le CUDA analogue d'AMD — portable GPU programming, but avec ses propres quirks. Quand tu build pour gfx1201 et que ROCm 6.4.x a pas ce target dans sa liste, soit ça fallback, soit ça crash, soit ça run mal. C'est pour ça que le support 'officiel' d'un GPU dans ROCm est pas juste cosmétique — ça change concrètement ce qui est compilé.
