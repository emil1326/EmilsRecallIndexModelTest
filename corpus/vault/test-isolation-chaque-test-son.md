---
title: Test isolation: chaque test son propre univers
summary: Un test qui dépend du state laissé par un autre c'est une bombe à retardement qui explose exactement quand t'as pas le temps.
type: lesson
links:
  - "[[datetime-et-random-sources-de]]"
  - "[[fixtures-setup-partage-attention-au]]"
  - "[[setup-teardown-garder-ca-minimal]]"
  - "[[tests-flaky-ils-pourrissent-tout]]"
---
Reset ton state entre chaque test, pas juste entre les test suites — ça veut dire pas de state global mutable, pas de singletons partagés, des fresh fixtures à chaque run. En pratique, un test qui dépend de l'ordre d'exécution va passer en local dans ton IDE pis fail en CI où l'ordre est différent. Ça prend un peu plus de setup time mais le debug évité après vaut chaque minute.
