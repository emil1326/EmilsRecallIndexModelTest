---
title: Interactive rebase cleanup avant PR
summary: Un git rebase -i avant d'ouvrir ta PR pour squasher les WIP commits pis reworder les messages en quelque chose qui a du sens, c'est du respect pour les reviewers.
type: lesson
links:
  - "[[rebase-ou-merge-selon-le]]"
  - "[[wip-commits-a-squasher-avant]]"
  - "[[force-push-interdit-sur-branches]]"
  - "[[pr-review-c-est-plus]]"
  - "[[un-commit-une-seule-idee]]"
---
git rebase -i HEAD~N te donne un éditeur où tu peux pick, squash, fixup, reword — tsu, le full control sur ton historique local. Le truc c'est de faire ça avant de pusher pour éviter d'avoir à force push sur une branche déjà partagée. Moi je le fais systématiquement avant chaque PR, ça prend genre deux minutes pis ça change toute la qualité du review.
