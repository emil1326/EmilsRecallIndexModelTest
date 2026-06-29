---
title: Monorepo vs multi-repo pour tools internes
summary: Le monorepo simplifie le refactor cross-package mais le build time augmente, tandis que le multi-repo garde les tools isolés mais le sharing devient douloureux.
type: reference
links:
  - "[[build-by-need-pas-by]]"
  - "[[forker-une-library-vs-la]]"
  - "[[custom-editor-window-vs-inspector]]"
  - "[[rebuild-from-scratch-vs-refactor]]"
---
Pour des tools internes d'un seul dev, le monorepo c'est presque toujours mieux — tu refactores sans avoir à bumper 4 versions séparées. Le multi-repo fait du sens quand les tools ont des owners différents ou des release cycles vraiment indépendants. J'ai essayé les deux pis le overhead de synchroniser les versions entre repos est sous-estimé genre. La complexité du monorepo c'est visible, celle du multi-repo c'est cachée dans le coordination cost.
