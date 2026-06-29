---
title: Replication factor 3 comme défaut Arrow
summary: Arrow réplique chaque entry sur 3 nodes par défaut, parce que c'est le sweet spot tolérance aux pannes vs overhead réseau pour la plupart des use cases raisonnables.
type: lesson
links:
  - "[[consistent-hashing-pour-data-partitioning]]"
  - "[[api-fluent-builder-pattern-arrow]]"
  - "[[distributed-data-arrow-sans-consensus]]"
  - "[[junit5-testcontainers-pour-tests-integration]]"
---
Avec replication factor 3, Arrow peut tolérer 1 node down sans perte de données dans un cluster de 3 nodes et plus. C'est configurable à la baisse pour les envs de dev où tu veux pas spawner 3 containers. Le factor de réplication est un param du builder comme n'importe quel autre setting.
