---
title: Augmentation et leakage, combo subtil
summary: Faire de la data augmentation sur le full dataset avant de splitter introduit du leakage si des exemples augmentés du test set se retrouvent dans le train set.
type: lesson
links:
  - "[[leakage-train-test-le-vrai]]"
  - "[[sources-cachees-de-leakage-insidieux]]"
  - "[[ordre-dedup-split-ca-change]]"
  - "[[tokenizer-outside-du-split-pas]]"
---
Genre si tu génères des rotations ou flips d'images sur tout le dataset pis ensuite tu splittes, un exemple du test set pourrait être une rotation d'un exemple du train set — là ton modèle a techniquement "vu" le test set. L'augmentation doit se faire après le split, seulement sur le train set, jamais sur val ou test. C'est logique une fois qu'on y pense, mais c'est un bug facile à faire quand tu build ton pipeline vite de même.
