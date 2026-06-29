---
title: In-memory store bâti sur ConcurrentHashMap
summary: Le core store d'Arrow est un `ConcurrentHashMap` wrappé dans une classe custom qui gère les versioned entries pis le TTL automatiquement.
type: reference
links:
  - "[[lazy-rebuild-arrow-se-declenche]]"
  - "[[distributed-data-arrow-sans-consensus]]"
  - "[[consistent-hashing-pour-data-partitioning]]"
  - "[[replication-factor-3-comme-defaut]]"
---
`ConcurrentHashMap` pour le thread-safety out of the box, pas besoin de synchronized blocks partout. Le wrapper ajoute le version tracking pour détecter les conflits de write concurrent, pis le TTL est géré par un `ScheduledExecutorService` qui clean les entries expirées. Simple mais ça marche.
