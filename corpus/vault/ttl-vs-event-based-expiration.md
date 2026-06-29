---
title: TTL vs event-based expiration: faut pas mixer naïvement
summary: TTL est simple à implémenter mais expire des caches encore valides, event-based est précis mais complexe — mixer les deux sans stratégie claire cause des races confuses.
type: reference
links:
  - "[[stale-cache-bugs-silencieux-dangereux]]"
  - "[[early-expiration-sur-changement-de]]"
  - "[[expiration-anticipee-sur-imports-transitifs]]"
  - "[[le-lazy-rebuild-se-declenche]]"
---
Un TTL de 5 minutes sur un fichier qui change aux 30 secondes, c'est du gaspillage. Event-based invalidation avec un file watcher c'est mieux mais ça ajoute de la complexité et des edge cases sur Windows notamment. La combo gagnante c'est souvent event-based comme stratégie principale plus TTL comme safety net pour les cas où les events se perdent.
