---
title: Stash: buffer temporaire pas un storage
summary: Le stash c'est fait pour switcher de contexte vite fait quand t'as du travail en cours — c'est pas un stockage long terme, les stashes orphelins c'est un enfer à retrouver.
type: reference
links:
  - "[[git-add-p-pour-staging]]"
  - "[[hotfix-branch-part-toujours-de]]"
  - "[[branches-courtes-vivent-mieux-mergent]]"
  - "[[wip-commits-a-squasher-avant]]"
  - "[[branch-naming-feature-hotfix-chore]]"
---
git stash push -m 'description utile' parce que git stash list avec dix entrées du genre 'stash@{0}: WIP on main' c'est inutilisable. Le stash c'est genre: quelqu'un a besoin d'un hotfix là là, tu stash, tu règles, tu pop. Mais si t'as besoin de garder du travail plus longtemps, une branch draft c'est mille fois mieux.
