---
title: Conventional commits: format feat/fix/chore
summary: Le format Conventional Commits (feat:, fix:, chore:, etc.) donne une structure lisible à l'historique pis permet l'auto-génération de changelogs sans trop d'effort.
type: reference
links:
  - "[[message-de-commit-a-l]]"
  - "[[un-commit-une-seule-idee]]"
  - "[[tags-semantiques-sur-chaque-release]]"
  - "[[wip-commits-a-squasher-avant]]"
  - "[[pr-review-c-est-plus]]"
  - "[[quand-le-test-coute-plus]]"
---
La syntaxe c'est: type(scope): description — genre 'feat(auth): add OAuth2 login' ou 'fix(ui): correct button alignment'. C'est pas obligatoire dans tous les projets mais une fois que t'y goûtes tu veux plus t'en passer. Ça aide aussi à comprendre d'un seul coup d'oeil l'impact d'un commit sans avoir à lire le diff au complet.
