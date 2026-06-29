---
title: Test data: hardcode ça scale jamais
summary: Des données hardcodées dans chaque test ça va ben pour 5 tests, mais passé ça faut des factory functions — changer un schema sinon c'est 2h de patch.
type: reference
links:
  - "[[fixtures-setup-partage-attention-au]]"
  - "[[setup-teardown-garder-ca-minimal]]"
  - "[[regression-tests-ecrire-le-test]]"
  - "[[test-isolation-chaque-test-son]]"
---
Quand tes test data sont en hardcodé partout pis que tu changes un schema, tu passes 2h à patcher chaque test à la mano. Une factory function qui crée les objets de test avec des defaults sensés pis des override optionnels, ça change la vie. C'est du setup up front mais genre 20 minutes investies qui en sauvent 10 par mise à jour de schema.
