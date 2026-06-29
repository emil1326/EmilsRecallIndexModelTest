---
title: Rebuild from scratch vs refactor, le flip
summary: Le rebuild from scratch semble libérateur mais reproduit souvent les mêmes problèmes avec du polish en plus, le refactor incrémental est presque toujours meilleur.
type: lesson
links:
  - "[[build-by-need-pas-by]]"
  - "[[abstraction-layers-coutent-cher-a]]"
  - "[[forker-une-library-vs-la]]"
  - "[[quand-abstraire-vs-quand-hardcoder]]"
---
La deuxième version d'un système tend à reproduire les bugs cachés de la première parce que les contraintes du domaine restent les mêmes. Tu penses que c'était l'architecture le problème, mais c'est souvent la compréhension du domaine. Le signe que tu dois vraiment rebuilder c'est quand les assumptions fondamentales du système sont fausses, pas juste quand le code est messy. Messy code ça se refactor, des fausses assumptions ça se rebuild.
