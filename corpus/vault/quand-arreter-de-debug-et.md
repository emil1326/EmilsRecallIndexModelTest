---
title: Quand arrêter de debug et juste updater
summary: Avant de rabbit hole dans les configs et les hacks ROCm, check juste si une nouvelle version de l'outil règle le problème — souvent c'est ça la vraie fix.
type: lesson
links:
  - "[[ollama-0-30-11-fix]]"
  - "[[hsa-override-gfx-version-workaround]]"
  - "[[rocm-version-pinning-blessing-ou]]"
  - "[[driver-pimax-40h-de-debug]]"
  - "[[rdna4-wave-size-32-ou]]"
---
J'ai passé du temps à debug les variables HSA, à lire des posts de forum de 2023 sur les workarounds gfx1100... alors qu'Ollama 0.30.11 avec ROCm v7.1 fix tout ça proprement. Lesson: quand un tool AI marche pas avec ton GPU, la première chose à faire c'est vérifier si la version du tool est récente. GitHub releases > StackOverflow pour ce genre de truc.
