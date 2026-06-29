---
title: Datetime et random: sources de non-déterminisme
summary: Les tests qui font intervenir datetime.now() ou random() sans les contrôler vont finir par fail dans les conditions les moins attendues.
type: reference
links:
  - "[[tests-flaky-ils-pourrissent-tout]]"
  - "[[test-isolation-chaque-test-son]]"
  - "[[sleep-dans-les-tests-code]]"
  - "[[ci-vs-local-l-environnement]]"
---
Inject le temps comme dépendance, seed le random, ou mock-le — les tests doivent pas dépendre de l'heure du serveur CI qui tourne dans un timezone différent. Ça c'est du vécu: un test de 'vérifier que c'est pas expiré' qui fail mystérieusement parce que le serveur est à UTC pis ta date hardcodée était relative à EST. Date et random sont les premiers suspects quand un test est mysteriously flaky.
