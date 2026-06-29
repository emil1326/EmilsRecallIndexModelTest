---
title: Setup/teardown: garder ça minimal pis explicite
summary: Les beforeEach qui font trop de choses créent des tests opaques où on sait plus c'est quoi le state de départ, pis déboguer ça c'est une horreur.
type: reference
links:
  - "[[fixtures-setup-partage-attention-au]]"
  - "[[test-isolation-chaque-test-son]]"
  - "[[test-data-hardcode-ca-scale]]"
  - "[[tests-flaky-ils-pourrissent-tout]]"
---
Plus ton setup est gros, plus c'est dur de comprendre pourquoi un test spécifique fail. Idéalement les dépendances critiques d'un test devraient être visibles dans le test lui-même, pas cachées dans un beforeEach qui fait 80 lignes. Garde le setup pour le boilerplate pur — database connection, mock server — pis laisse les détails business dans les tests.
