---
title: Unit tests et integration tests: les deux nécessaires
summary: Les unit tests vérifient les pièces, les integration tests vérifient l'assemblage — avoir 500 unit tests verts pis zéro integration test c'est une fausse sécurité.
type: reference
links:
  - "[[smoke-tests-lancer-le-happy]]"
  - "[[mocks-qui-masquent-le-vrai]]"
  - "[[ci-vs-local-l-environnement]]"
  - "[[code-coverage-la-metrique-qui]]"
---
Le mistake classique c'est d'avoir 500 unit tests verts pis zéro integration test — tes composants fonctionnent chacun séparément mais parlent pas ensemble correctly en prod. Genre t'as testé chaque vis séparément mais jamais le moteur assemblé, tsu. Les unit tests donnent du feedback rapide pis précis, les integration tests donnent de la confiance sur le système complet. Les deux.
