---
title: Netty vs raw sockets pour Arrow
summary: Arrow utilise Netty pour son network layer plutôt que des raw Java sockets parce que gérer le non-blocking IO manuellement c'était trop de pain pour les gains.
type: lesson
links:
  - "[[distributed-data-arrow-sans-consensus]]"
  - "[[gradle-multi-module-structure-de]]"
  - "[[replication-factor-3-comme-defaut]]"
  - "[[consistent-hashing-pour-data-partitioning]]"
---
J'ai commencé avec `ServerSocket` basic pis c'était un mess de threads pour chaque connexion. Netty avec son event loop model gère ça proprement, pis le pipeline de handlers est extensible. L'overhead d'apprendre Netty valait le coup vu que c'est utilisé dans un bunch de gros projets donc ya de la doc.
