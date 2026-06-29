---
title: Repro minimal avant de toucher au fix
summary: Jamais fixer un bug sans d'abord écrire le test minimal qui le reproduce — sinon tu fixes le mauvais truc pis le bug revient.
type: lesson
links:
  - "[[regression-tests-ecrire-le-test]]"
  - "[[un-test-qui-peut-jamais]]"
  - "[[smoke-tests-lancer-le-happy]]"
  - "[[nommer-les-tests-comme-des]]"
---
Le réflexe c'est de patch direct, mais 9 fois sur 10 tu fixes le mauvais truc ou tu rajoutes du code autour du vrai problème. Whip up un test minimal qui reproduce le comportement attendu-vs-réel, pis là tu sais exactement quoi toucher. Ça prend genre 10 minutes mais ça sauve des heures de debug dans le vide.
