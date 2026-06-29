---
title: WIP commits à squasher avant push
summary: Les commits WIP ('work in progress: blah') sont utiles pour sauvegarder l'état localement, mais ils doivent absolument être squashés en quelque chose de propre avant de pusher.
type: lesson
links:
  - "[[git-add-p-pour-staging]]"
  - "[[interactive-rebase-cleanup-avant-pr]]"
  - "[[un-commit-une-seule-idee]]"
  - "[[squash-commits-avant-merge-dans]]"
  - "[[git-reflog-comme-filet-de]]"
---
Je fais souvent des 'wip: checkpoint avant de tout casser' quand j'expérimente — c'est clean comme stratégie pour pas perdre de travail. Mais pousser des WIP commits sur une remote branch partagée c'est le genre de truc qui pollue l'historique pour tout le monde. Un git rebase -i HEAD~N pour squash/fixup les WIPs en commits propres avant le push, c'est deux minutes qui valent la peine.
