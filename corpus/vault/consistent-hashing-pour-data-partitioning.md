---
title: Consistent hashing pour data partitioning Arrow
summary: Arrow distribue les keys entre nodes via consistent hashing sur un virtual ring, ce qui minimise le reshuffling des données quand un node join ou quitte le cluster.
type: reference
links:
  - "[[in-memory-store-bati-sur]]"
  - "[[replication-factor-3-comme-defaut]]"
  - "[[distributed-data-arrow-sans-consensus]]"
  - "[[netty-vs-raw-sockets-pour]]"
---
L'anneau virtuel a 360 virtual nodes par défaut pour une distribution plus uniforme même avec peu de nodes physiques. Chaque key est hashée avec MurmurHash3 pis assignée au node suivant clockwise sur le ring. C'est le même principe que Cassandra, genre j'ai pas réinventé la roue.
