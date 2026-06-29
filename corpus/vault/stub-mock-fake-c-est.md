---
title: Stub, mock, fake: c'est vraiment pas pareil
summary: Un stub retourne des données canned, un mock vérifie des interactions, un fake est une vraie implémentation allégée — mélanger ça cause des tests fragiles pis confus.
type: reference
links:
  - "[[mocks-qui-masquent-le-vrai]]"
  - "[[tests-flaky-ils-pourrissent-tout]]"
  - "[[un-test-qui-peut-jamais]]"
  - "[[fixtures-setup-partage-attention-au]]"
---
La confusion classique c'est d'utiliser un mock quand t'as besoin d'un stub, pis de se retrouver à vérifier des appels de méthodes qui sont pas le point du test. Un stub retourne des données canned sans s'intéresser à comment c'est appelé; un mock vérifie que les bonnes interactions ont eu lieu; un fake est une vraie implémentation allégée genre in-memory DB. Chaque type a sa place, mélanger ça crée des tests fragiles.
