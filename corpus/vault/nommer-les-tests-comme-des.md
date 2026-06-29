---
title: Nommer les tests comme des specs de comportement
summary: test_returns_true dit rien; user_cannot_purchase_without_verified_email explique le comportement attendu pis ça devient de la documentation gratis quand ça fail à 3h du matin.
type: reference
links:
  - "[[regression-tests-ecrire-le-test]]"
  - "[[un-test-qui-peut-jamais]]"
  - "[[repro-minimal-avant-de-toucher]]"
  - "[[smoke-tests-lancer-le-happy]]"
---
Quand un test fail à 3h du matin en CI, le nom du test c'est ta première info sans avoir à lire le code. 'test_function_returns_true' ça dit rien; 'user_cannot_purchase_without_verified_email' ça te dit exactement quoi était censé se passer. Un bon nom de test c'est de la documentation gratis qui se maintient automatiquement parce qu'il est couplé au test lui-même.
