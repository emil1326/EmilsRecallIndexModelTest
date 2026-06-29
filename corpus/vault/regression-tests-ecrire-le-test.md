---
title: Regression tests: écrire le test avant le fix
summary: Quand t'as un bug, écrire le test qui le reproduce avant de le fixer garantit que le bug reviendra pas en silence dans 3 mois.
type: lesson
links:
  - "[[repro-minimal-avant-de-toucher]]"
  - "[[un-test-qui-peut-jamais]]"
  - "[[nommer-les-tests-comme-des]]"
  - "[[code-coverage-la-metrique-qui]]"
---
Le workflow c'est: bug report → failing test qui reproduce → fix → test passes. Pas l'inverse. Si tu fixes d'abord, t'as jamais prouvé que ton test aurait catch le bug — peut-être que ton test est mauvais pis il aurait passé de toute façon. Pis le bug va revenir dans 6 mois, pis là tu vas vouloir te battre contre ton passé-toi.
