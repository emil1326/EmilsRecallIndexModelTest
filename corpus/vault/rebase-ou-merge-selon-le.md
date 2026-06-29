---
title: Rebase ou merge selon le contexte
summary: Rebase pour garder un historique linéaire propre sur ta feature branch, merge pour les intégrations publiques où l'historique de fusion a de la valeur.
type: lesson
links:
  - "[[interactive-rebase-cleanup-avant-pr]]"
  - "[[force-push-interdit-sur-branches]]"
  - "[[squash-commits-avant-merge-dans]]"
  - "[[main-branch-doit-rester-deployable]]"
  - "[[sync-avec-main-souvent-pas]]"
---
La règle de base: tu rebase ta feature branch sur main avant d'ouvrir une PR, mais tu merge dans main (ou tu laisses GitHub faire le squash merge). Rebaser une branch que quelqu'un d'autre a aussi checkout c'est une recette pour le chaos — golden rule: rebase only your own local stuff. Ça fait des mois que je fais ça comme ça pis c'est mf clean.
