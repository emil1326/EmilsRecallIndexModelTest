---
title: ROCm version pinning: blessing ou nightmare
summary: Pinner une version ROCm évite les breaking changes, mais ça te fait manquer les nouveaux GPU supports — gfx1201 case illustre bien ce double tranchant.
type: lesson
links:
  - "[[rocm-6-4-2-pas]]"
  - "[[rocm-v7-1-changelog-support]]"
  - "[[ollama-0-30-11-fix]]"
  - "[[amd-driver-compatibility-et-rocm]]"
---
Si tu pins ROCm 6.4.2 pour la stabilité tu rates le support gfx1201 de v7.1. Si tu always-latest tu risques des regressions sur d'autres trucs. C'est le tradeoff classique de version management mais dans le GPU compute c'est particulièrement douloureux parce que les fallbacks sont silencieux. Faut au moins rester aware des changelogs de ROCm quand t'as du hardware récent.
