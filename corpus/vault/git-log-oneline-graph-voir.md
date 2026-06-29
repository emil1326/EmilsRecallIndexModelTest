---
title: git log --oneline --graph voir l'histoire
summary: git log --oneline --decorate --graph --all donne une visualisation ASCII de l'historique des branches — utile pour voir le lay of the land avant un rebase ou un merge compliqué.
type: reference
links:
  - "[[rebase-ou-merge-selon-le]]"
  - "[[interactive-rebase-cleanup-avant-pr]]"
  - "[[git-reflog-comme-filet-de]]"
  - "[[squash-commits-avant-merge-dans]]"
  - "[[sync-avec-main-souvent-pas]]"
  - "[[regression-tests-ecrire-le-test]]"
---
J'ai ça en alias: bindé sur 'git lg' dans mon .gitconfig, une commande. Ça montre les branches, les tags, pis la structure de merge en quelques lignes au lieu d'un wall of text. Avant de faire un rebase ou de merger quelque chose de compliqué, un coup de git lg pour voir où tout le monde est dans l'arbre ça m'a sauvé plusieurs fois de faire des bêtises.
