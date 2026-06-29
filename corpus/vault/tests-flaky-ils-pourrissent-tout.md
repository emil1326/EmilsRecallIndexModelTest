---
title: Tests flaky: ils pourrissent tout le CI
summary: Un test qui passe 70% du temps est pire qu'un test absent parce qu'il tue la confiance de toute l'équipe dans les résultats du CI.
type: lesson
links:
  - "[[ci-vs-local-l-environnement]]"
  - "[[datetime-et-random-sources-de]]"
  - "[[test-isolation-chaque-test-son]]"
  - "[[quand-delete-un-test-moins]]"
  - "[[sleep-dans-les-tests-code]]"
---
Dès qu'un test commence à fail intermittently, quarantine-le right away — pending, fix, ou sacre-le dehors, mais laisse-le pas live dans le CI. Un flaky test c'est comme un smoke detector qui sonne pour rien: tout le monde l'ignore pis là y'a un vrai feu. Smh. La confiance dans le test suite c'est fragile, pis un seul test flaky peut la détruire.
