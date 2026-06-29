---
title: Sleep() dans les tests: code smell immédiat
summary: Mettre un sleep() pour attendre qu'un effet se produise c'est fragile pis ça ralentit tout le test suite — préfère des wait conditions explicites.
type: lesson
links:
  - "[[tests-flaky-ils-pourrissent-tout]]"
  - "[[tests-async-et-le-false]]"
  - "[[datetime-et-random-sources-de]]"
  - "[[test-isolation-chaque-test-son]]"
---
J'ai vu des test suites qui prenaient 15 minutes à cause de sleeps partout — un wait de 500ms par-ci, 2 secondes par-là, ça s'accumule vite. Le fix c'est wait_until() avec une condition, des callbacks, ou des events — pas sleep(5000) pis espérer que ça fit dans la fenêtre. Pis c'est pas juste une question de vitesse: les sleeps causent des flaky tests sur des machines lentes ou sous charge.
