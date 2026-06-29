---
title: ECS vs OOP pour les systèmes game
summary: ECS donne un cache locality et une composabilité réelle, mais le mental model shift coûte du temps et OOP reste souvent good enough pour les projets mid-size.
type: reference
links:
  - "[[frametime-beats-fps-pour-decider]]"
  - "[[build-by-need-pas-by]]"
  - "[[premature-optimization-vs-good-enough]]"
  - "[[quand-abstraire-vs-quand-hardcoder]]"
---
L'argument ECS c'est toujours les benchmarks de data-oriented design — ok, c'est réel pour des milliers d'entités. Mais pour un jeu indie avec quelques centaines d'objets, OOP avec un peu de discipline c'est souvent plus rapide à ship. J'ai switché à ECS une fois par curiosité, pas par besoin, pis j'ai regretté le overhead de setup. Le fit dépend du scale, pas des trends.
