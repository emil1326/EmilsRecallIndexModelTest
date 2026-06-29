---
title: Held-out set intouchable en dev
summary: Le test set final doit être mis de côté dès le début pis jamais regardé pendant le dev, sinon tu te fais un modèle biaisé vers ton test set par inadvertance.
type: lesson
links:
  - "[[leakage-train-test-le-vrai]]"
  - "[[cross-val-ou-held-out]]"
  - "[[proportions-80-10-10-vs]]"
  - "[[logger-le-split-avec-seed]]"
---
C'est un des pièges les plus classiques: tu tunes des hyperparams, tu check le test set, tu tunes encore... là tu fais juste overfitter sur ton test set à la main sans t'en rendre compte. Le held-out set c'est pour la mesure finale une seule fois, c'est ça le deal. Garde un val set séparé pour tout ton dev pis le tuning. Si t'as pas assez de données pour trois splits, cross-validation sur le train pis un seul held-out shot.
