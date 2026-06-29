---
title: Un test qui peut jamais fail
summary: Si ton assertion pourrait jamais être false dans ce context, t'as écrit du code décoratif, pas un test — introduis un bug volontaire pour vérifier.
type: lesson
links:
  - "[[code-coverage-la-metrique-qui]]"
  - "[[regression-tests-ecrire-le-test]]"
  - "[[mocks-qui-masquent-le-vrai]]"
  - "[[nommer-les-tests-comme-des]]"
---
Un bon test doit avoir au moins un path où il fail si le code est broken. Si tu trouves pas de façon de faire fail ton test, soit l'assertion est trop weak, soit tu check pas la bonne chose. Prends 30 secondes à introduire un bug volontaire dans ton code pour valider que le test le catch — ça c'est la sanity check ultime.
