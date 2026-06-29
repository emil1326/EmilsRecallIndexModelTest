---
title: Variables d'env ROCm pour debug GPU
summary: Setter AMD_LOG_LEVEL=7 et HSA_OVERRIDE_GFX_VERSION permet de debugger le ROCm stack verbosement pis de forcer des workarounds temporaires quand ton GPU est pas encore officiellement supporté.
type: reference
links:
  - "[[hsa-override-gfx-version-workaround]]"
  - "[[rocm-6-4-2-pas]]"
  - "[[ollama-logs-ou-chercher-le]]"
  - "[[hip-target-et-les-gpu]]"
---
AMD_LOG_LEVEL=4 ou 7 donne des logs beaucoup plus verbeux sur ce que le runtime fait — utile pour voir si ton GPU est détecté. ROCR_VISIBLE_DEVICES permet de forcer quel GPU ROCm voit si t'en as plusieurs ou pour isoler. HSA_OVERRIDE_GFX_VERSION c'est le hack pour spoofer l'architecture. Ces variables-là, garde-les dans ta tête pour le prochain GPU pas-encore-supporté.
