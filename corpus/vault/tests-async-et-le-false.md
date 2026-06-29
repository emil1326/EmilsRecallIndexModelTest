---
title: Tests async et le false positive silencieux
summary: Un test async qui await pas correctement peut passer même avec du code broken — c'est le worst kind of false positive, le test dit green pis c'est cassé.
type: lesson
links:
  - "[[sleep-dans-les-tests-code]]"
  - "[[tests-flaky-ils-pourrissent-tout]]"
  - "[[un-test-qui-peut-jamais]]"
  - "[[ci-vs-local-l-environnement]]"
---
J'ai vu des test suites entiers avec des assertions qui tournaient après que le test était déjà passé — le test dit 'green' parce que l'assertion a jamais eu le temps de run correctement. Faut toujours s'assurer que ton async se résout before d'assert, pis que tes assertions elles-mêmes sont dans le bon scope. Un test async qui peut pas fail correctement c'est pire qu'aucun test.
