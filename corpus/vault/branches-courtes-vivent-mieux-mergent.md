---
title: Branches courtes vivent mieux mergent mieux
summary: Plus une feature branch dure longtemps, plus les merge conflicts s'accumulent pis le review devient complexe — idéalement une branch dure quelques jours max.
type: lesson
links:
  - "[[sync-avec-main-souvent-pas]]"
  - "[[rebase-ou-merge-selon-le]]"
  - "[[branch-naming-feature-hotfix-chore]]"
  - "[[draft-pr-pour-early-feedback]]"
  - "[[squash-commits-avant-merge-dans]]"
---
Une branch qui traine depuis trois semaines c'est un merge conflict guaranteed pis un review que personne veut faire parce que c'est trop de changements d'un coup. La solution c'est de découper les features en plus petits incréments deployables — c'est pas toujours évident mais ça force à mieux designer. Feature flags peuvent aider si t'as besoin de merger du code incomplet sans l'exposer aux users.
