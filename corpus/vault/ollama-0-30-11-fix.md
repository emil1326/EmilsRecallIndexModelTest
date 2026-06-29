---
title: Ollama 0.30.11 fix: ROCm v7.1 embarqué
summary: La version Ollama 0.30.11 ship avec ROCm v7.1 qui supporte enfin gfx1201, ce qui règle le fallback CPU pour les GPU RDNA4 d'un coup.
type: lesson
links:
  - "[[rocm-6-4-2-pas]]"
  - "[[rocm-v7-1-changelog-support]]"
  - "[[quand-arreter-de-debug-et]]"
  - "[[tester-son-gpu-setup-apres]]"
---
Le fix était simple dans les faits — juste updater Ollama. Mais encore fallait-il savoir que c'était un problème de version et pas autre chose. ROCm v7.1 a ajouté le support officiel de gfx1201, pis Ollama 0.30.11 a packagé ça. Un update de rien qui fait passer de 'ça rame sur CPU' à 'GPU full blast'.
