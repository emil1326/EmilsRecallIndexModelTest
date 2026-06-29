---
title: Valider le test loop en petit d'abord
summary: Avant d'écrire 50 tests, valider que le runner, la config pis le premier test basique fonctionnent — un green loop minimal, pis on scale après.
type: lesson
links:
  - "[[smoke-tests-lancer-le-happy]]"
  - "[[ci-vs-local-l-environnement]]"
  - "[[un-test-qui-peut-jamais]]"
  - "[[quand-le-test-coute-plus]]"
---
Y'a rien de plus frustrant que de réaliser après avoir écrit une tonne de tests que ton test setup était cassé depuis le début. Premier test simple, il passe, le loop est vert — pis là on scale. C'est pas sexy mais c'est ce qui évite de jeter des heures de travail à la poubelle.
