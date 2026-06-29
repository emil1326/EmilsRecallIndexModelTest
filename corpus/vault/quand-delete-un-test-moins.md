---
title: Quand delete un test: moins peut être mieux
summary: Un test qui fail pour de mauvaises raisons plus souvent qu'il catch des vrais bugs, c'est mieux de le sacrer dehors que de le garder par principe.
type: lesson
links:
  - "[[tests-flaky-ils-pourrissent-tout]]"
  - "[[code-coverage-la-metrique-qui]]"
  - "[[snapshot-tests-quick-win-qui]]"
  - "[[quand-le-test-coute-plus]]"
---
Le dogme 'plus de tests = mieux' marche pas si les tests sont shit. Un test qui fait perdre confiance dans le CI parce qu'il est flaky, ou qui teste une implémentation plutôt qu'un comportement, vaut mieux le sacrer dehors. Marie Kondo tes tests: est-ce que ce test spark joy (ou en tout cas catch des vrais bugs)? Non? Bye.
