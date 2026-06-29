---
title: Sérialisation cache: JSON lisible vs binaire rapide
summary: JSON c'est debuggable facilement mais slow à parser sur de grosses entrées cache; binaire (MessagePack, protobuf) c'est rapide mais opaque — le trade-off dépend de la fréquence des reads.
type: reference
links:
  - "[[versioning-du-cache-schema-sinon]]"
  - "[[disk-vs-memory-cache-selon]]"
  - "[[debug-mode-devrait-bypass-le]]"
  - "[[rollback-automatique-si-cache-corrompu]]"
---
En dev, JSON c'est vraiment nice parce que tu peux ouvrir le fichier cache et voir exactement ce qui est dedans. En prod avec des fichiers de cache de 50MB, le parse time commence à compter. MessagePack c'est mon pick personnel — binaire mais pas trop opaque, et les libs sont disponibles partout. Peu importe le format, inclus toujours un schema version.
