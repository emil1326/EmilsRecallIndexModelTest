---
title: ROCm v7.1 changelog: support gfx1201 officiel
summary: ROCm v7.1 a officiellement ajouté gfx1201 dans sa liste de targets supportées, ce qui débloque les GPU RDNA4 pour l'inférence AI sans hacks.
type: reference
links:
  - "[[ollama-0-30-11-fix]]"
  - "[[rocm-6-4-2-pas]]"
  - "[[rdna4-gfx1201-encore-trop-neuf]]"
  - "[[hip-target-et-les-gpu]]"
---
C'était LE changement qui faisait qu'Ollama pouvait enfin utiliser mon GPU correctement. ROCm v7.1 a élargi la liste des architectures supportées, gfx1201 inclus. Avant ça, fallait soit patcher, soit setter des variables d'environnement bancales. Maintenant c'est propre, officiel, pis ça marche out of the box avec Ollama 0.30.11+.
