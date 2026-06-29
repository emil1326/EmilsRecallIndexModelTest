---
title: HSA_OVERRIDE_GFX_VERSION: workaround ou piège
summary: Setter HSA_OVERRIDE_GFX_VERSION peut forcer ROCm à traiter ton GPU comme un chip supporté, mais ça reste un hack fragile qui peut peter n'importe quand.
type: lesson
links:
  - "[[rocm-6-4-2-pas]]"
  - "[[rdna4-gfx1201-encore-trop-neuf]]"
  - "[[variables-d-env-rocm-pour]]"
  - "[[hip-target-et-les-gpu]]"
  - "[[overdraw-accumule-les-pixel-invocations]]"
---
L'idée c'est de spoofer le GPU version identifier pour que le ROCm stack se comporte comme si ton hardware était supporté officiellement. Genre HSA_OVERRIDE_GFX_VERSION=11.0.0 pour faire passer gfx1201 pour quelque chose de connu. Ça marche... parfois. Performance pas garantie, pis certaines ops peuvent crash. Vaut mieux attendre le support officiel, ou updater Ollama.
