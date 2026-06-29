---
title: git add -p pour staging chirurgical
summary: git add -p (patch mode) permet de stageer seulement certains hunks d'un fichier, utile quand t'as mélangé deux changements logiquement distincts dans les mêmes fichiers.
type: reference
links:
  - "[[un-commit-une-seule-idee]]"
  - "[[stash-buffer-temporaire-pas-un]]"
  - "[[wip-commits-a-squasher-avant]]"
  - "[[interactive-rebase-cleanup-avant-pr]]"
  - "[[conventional-commits-format-feat-fix]]"
---
Tu fais git add -p et git te montre chaque hunk de diff un à la fois — tu réponds y (stage), n (skip), s (split le hunk), e (edit manuellement). C'est un peu lent quand t'as beaucoup de changements mais c'est la seule façon propre de sortir des commits atomiques à partir d'un mess de modifications. Souvent j'aurais dû faire deux branches séparées mais bon, c'est la vie.
