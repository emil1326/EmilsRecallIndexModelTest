---
title: git bisect pour trouver le commit coupable
summary: git bisect fait une binary search dans l'historique pour identifier quel commit a introduit un bug — beaucoup plus efficace que de regarder les diffs manuellement.
type: reference
links:
  - "[[un-commit-une-seule-idee]]"
  - "[[git-reflog-comme-filet-de]]"
  - "[[main-branch-doit-rester-deployable]]"
  - "[[rebase-ou-merge-selon-le]]"
  - "[[sync-avec-main-souvent-pas]]"
---
git bisect start, git bisect bad (commit actuel buggé), git bisect good SHA (dernier commit où ça marchait) — pis git te checkout automatiquement des commits pour que tu testes. Tu réponds good ou bad à chaque fois, pis en O(log n) commits il trouve le coupable. J'ai utilisé ça une fois pour traquer un bug de regression dans un projet Unity et c'était magique, j'aurais passé des heures autrement.
