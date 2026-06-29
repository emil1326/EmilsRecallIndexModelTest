---
title: RDNA4 architecture: AMD move fast, ecosystem slow
summary: AMD sort une nouvelle archi GPU et le reste de l'écosystème — ROCm, PyTorch, outils AI — a besoin de plusieurs mois pour suivre correctement.
type: journal
links:
  - "[[rdna4-gfx1201-encore-trop-neuf]]"
  - "[[rocm-6-4-2-pas]]"
  - "[[gpu-support-officiel-vs-community]]"
  - "[[hipblaslt-et-gfx1201-en-rocm]]"
  - "[[extensions-vs-code-qui-changent]]"
---
C'est pas propre à AMD, NVIDIA fait pareil — mais le problème avec AMD c'est que ROCm est déjà en retard sur CUDA niveau ecosystem maturity, donc le double délai hardware+software c'est plus douloureux. RDNA4/gfx1201 c'est un bel exemple: archi excellente, mais des mois à galère pour l'AI tooling. Si t'es pas prêt à être un beta tester de facto, attends 6 mois après le GPU launch.
