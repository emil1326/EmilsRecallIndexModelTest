---
title: Premature optimization vs good enough threshold
summary: Optimiser avant d'avoir mesuré le problème réel c'est souvent du travail jeté, mais ignorer la perf complètement au design c'est aussi une erreur.
type: lesson
links:
  - "[[frametime-beats-fps-pour-decider]]"
  - "[[ecs-vs-oop-pour-les]]"
  - "[[build-by-need-pas-by]]"
  - "[[quand-abstraire-vs-quand-hardcoder]]"
---
Le nuance que j'ai appris: y'a des décisions architecturales qui rendent la perf future beaucoup plus difficile — comme choisir un data layout qui garantit des cache misses. Celles-là méritent d'être pensées tôt même sans profiler. Mais les micro-optimizations de code? Jamais avant d'avoir un profiler ouvert avec un vrai problème visible. "It's probably slow" est pas un bon point de départ pour optimiser.
