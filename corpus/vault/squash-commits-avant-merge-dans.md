---
title: Squash commits avant merge dans main
summary: Le squash merge sur la PR condense tous les commits de la feature branch en un seul commit propre dans main, ce qui garde l'historique lisible sans sacrifier le détail local.
type: lesson
links:
  - "[[rebase-ou-merge-selon-le]]"
  - "[[interactive-rebase-cleanup-avant-pr]]"
  - "[[wip-commits-a-squasher-avant]]"
  - "[[main-branch-doit-rester-deployable]]"
  - "[[un-commit-une-seule-idee]]"
---
GitHub a l'option 'Squash and merge' qui fait exactement ça — tu gardes ton historique de dev messy sur ta branch, pis main reçoit un seul commit bien nommé. La contrepartie c'est que git blame perd un peu de granularité, mais pour la majorité des projets c'est le bon trade-off. J'utilise ça par défaut sur mes repos perso, sauf quand les commits individuels ont vraiment de la valeur pour l'historique.
