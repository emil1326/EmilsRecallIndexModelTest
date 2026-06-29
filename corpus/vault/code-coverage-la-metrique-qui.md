---
title: Code coverage: la métrique qui ment souvent
summary: 100% de coverage dit juste que chaque ligne a été executée, ça dit pas que le comportement est correct — c'est du théâtre de testing.
type: lesson
links:
  - "[[un-test-qui-peut-jamais]]"
  - "[[mocks-qui-masquent-le-vrai]]"
  - "[[quand-delete-un-test-moins]]"
  - "[[regression-tests-ecrire-le-test]]"
---
T'as beau avoir 100% coverage si tes assertions sont nulles ou inexistantes — j'ai vu du coverage parfait avec des tests genre 'assert result is not None' sur des choses qui pourraient jamais être None. Le coverage dit que le code a été exécuté, pas que le comportement est correct. C'est du théâtre de testing, pis c'est plus dangereux qu'un coverage de 40% avec de bons tests.
