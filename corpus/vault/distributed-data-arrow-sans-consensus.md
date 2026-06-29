---
title: Distributed data Arrow sans consensus protocol
summary: Arrow fait du distributed in-memory data sans implementer un vrai consensus protocol genre Raft, ce qui est un trade-off assumé de simplicité sur la consistency garantie.
type: lesson
links:
  - "[[in-memory-store-bati-sur]]"
  - "[[consistent-hashing-pour-data-partitioning]]"
  - "[[replication-factor-3-comme-defaut]]"
  - "[[arrow-outil-java-ne-d]]"
  - "[[serialization-jackson-vs-kryo-dans]]"
---
Raft ou Paxos c'est un rabbit hole infernal que j'avais pas envie de descendre. Arrow utilise une eventual consistency loose avec des vector clocks pour détecter les conflits, pis en cas de conflit c'est last-write-wins. C'est pas parfait mais ça fit pour les use cases visés.
