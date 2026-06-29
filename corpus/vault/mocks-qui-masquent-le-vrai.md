---
title: Mocks qui masquent le vrai bug en prod
summary: Si tu mock trop, tu testes ton mock setup plutôt que ton code — j'ai eu un test suite green complet avec un feature broken en prod.
type: lesson
links:
  - "[[stub-mock-fake-c-est]]"
  - "[[fixtures-setup-partage-attention-au]]"
  - "[[code-coverage-la-metrique-qui]]"
  - "[[tests-flaky-ils-pourrissent-tout]]"
---
J'ai déjà eu un test suite complet au vert pis le feature était broken en prod parce que les mocks retournaient des données parfaites que le vrai service retournait jamais. Les mocks sont parfaits pour isoler une unité, mais si tu mock trop, tu testes ton setup plutôt que ton code. C'est plate tbh, pis ça donne une fausse sécurité pire qu'aucun test.
