---
title: Cache invalidation strategy, le problème dur
summary: Choisir une stratégie de cache invalidation upfront évite des bugs de stale data subtils qui sont parmi les plus longs à tracker down.
type: reference
links:
  - "[[lazy-rebuild-declenche-on-demand]]"
  - "[[file-based-vs-database-pour]]"
  - "[[hot-reload-vs-full-rebuild]]"
  - "[[sync-vs-async-dans-les]]"
---
Y'a deux erreurs classiques: invalider trop souvent (tu perds le bénéfice du cache) ou invalider trop rarement (tu sers des stale results qui feel comme des bugs random). La stratégie la plus robuste que j'ai trouvée c'est content-hash based — le cache key inclut un hash du contenu, si ça change le cache miss automatiquement. Ça coûte du compute upfront mais ça élimine toute une classe de bugs. Time-to-live c'est bien pour les données externes, pas pour les artifacts internes.
