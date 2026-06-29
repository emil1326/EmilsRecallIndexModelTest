---
title: Force push interdit sur branches partagées
summary: git push --force sur une branch que quelqu'un d'autre a checkout, c'est réécrire l'histoire sous les pieds des autres — utilise --force-with-lease si tu dois vraiment.
type: lesson
links:
  - "[[rebase-ou-merge-selon-le]]"
  - "[[interactive-rebase-cleanup-avant-pr]]"
  - "[[main-branch-doit-rester-deployable]]"
  - "[[git-reflog-comme-filet-de]]"
  - "[[draft-pr-pour-early-feedback]]"
---
--force-with-lease vérifie que la remote branch est exactement comme tu t'y attendais avant de pusher, ce qui protège contre l'écrasement de commits que quelqu'un d'autre aurait pushé entre temps. Sur main/master, le force push devrait être carrément désactivé via les branch protection rules sur GitHub. Sur ta propre feature branch que personne d'autre touche, force push c'est fine, mais dès que t'as un co-reviewer qui pull ta branch, check avant.
