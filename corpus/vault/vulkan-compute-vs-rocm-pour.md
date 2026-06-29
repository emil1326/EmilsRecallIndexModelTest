---
title: Vulkan compute vs ROCm pour inférence locale
summary: Vulkan compute peut run de l'inférence AI sur GPU AMD sans ROCm du tout — c'est une alternative viable quand ROCm supporte pas encore ton GPU.
type: lesson
links:
  - "[[rocm-6-4-2-pas]]"
  - "[[rdna4-gfx1201-encore-trop-neuf]]"
  - "[[hsa-override-gfx-version-workaround]]"
  - "[[gpu-support-officiel-vs-community]]"
---
Tools comme llama.cpp avec le backend Vulkan peuvent tirer du GPU même sur des architectures pas encore dans ROCm. Performance généralement en dessous de ROCm natif, mais infiniment mieux que CPU pure. Pour un GPU RDNA4 en attente de support ROCm, c'est une vraie option de survie. Utile de savoir que le ROCm path est pas le seul chemin.
