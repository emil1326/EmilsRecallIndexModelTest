---
title: Smoke tests: lancer le happy path d'abord
summary: Avant de tester les edge cases, lancer le main flow d'abord — si ça casse là, les autres tests ont zero valeur.
type: lesson
links:
  - "[[valider-le-test-loop-en]]"
  - "[[tests-flaky-ils-pourrissent-tout]]"
  - "[[unit-tests-et-integration-tests]]"
  - "[[repro-minimal-avant-de-toucher]]"
---
Le smoke test c'est genre ton canary dans la mine, tsu. Si le main flow passe même pas, t'as un problème bien plus gros à régler avant de s'inquiéter des corner cases. C'est basic mais ça prend 2 minutes pis ça filtre un LOT de bruit avant de plonger plus profond.
