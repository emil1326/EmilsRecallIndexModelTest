---
title: GPU support officiel vs community patches
summary: Attendre le support officiel d'un GPU dans ROCm est presque toujours mieux que des community patches — moins de risque de regression, pis c'est maintenu.
type: lesson
links:
  - "[[hip-target-et-les-gpu]]"
  - "[[rocm-v7-1-changelog-support]]"
  - "[[rdna4-gfx1201-encore-trop-neuf]]"
  - "[[hsa-override-gfx-version-workaround]]"
---
Les community patches pour ajouter un GPU non-supporté dans ROCm existent — forks de hipBLASLt, patches de compilation, etc. Mais à chaque update t'as le merge hell. Le support officiel dans ROCm v7.1 pour gfx1201 c'est beaucoup plus propre: kernels compilés et testés par AMD, maintenus dans les futures versions. La patience paye, même si c'est plate d'attendre.
