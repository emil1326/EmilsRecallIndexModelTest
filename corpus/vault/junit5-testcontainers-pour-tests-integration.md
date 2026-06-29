---
title: JUnit5 Testcontainers pour tests intégration Arrow
summary: Arrow utilise JUnit5 pour les unit tests pis Testcontainers pour les tests d'intégration réseau, ce qui permet de tester les nodes Arrow dans de vrais containers Docker locaux.
type: reference
links:
  - "[[netty-vs-raw-sockets-pour]]"
  - "[[distributed-data-arrow-sans-consensus]]"
  - "[[replication-factor-3-comme-defaut]]"
  - "[[slf4j-comme-logging-facade-arrow]]"
---
Testcontainers spin up des containers Docker on-the-fly pendant les tests pis les kill après. Pour Arrow, j'ai un `ArrowClusterContainer` helper qui spawn 3 nodes en réseau isolé. C'est lent mais ça catch des bugs de networking qu'un mock aurait jamais trouvé.
