---
title: Debug mode devrait bypass le cache complètement
summary: Un flag --no-cache pour bypass complet en debug est essentiel — sans ça tu passes des heures à chasser des fantômes de cache stale pis c'est épuisant.
type: lesson
links:
  - "[[cache-hit-rate-la-vraie]]"
  - "[[audit-trail-des-cache-misses]]"
  - "[[stale-cache-bugs-silencieux-dangereux]]"
  - "[[rollback-automatique-si-cache-corrompu]]"
  - "[[dedup-exact-sur-hash-md5]]"
---
C'est le genre de feature qu'on implémente après avoir perdu 3 heures à debugger un 'bug' qui existait pas — le cache retournait les vieux résultats. Un --no-cache flag plus du verbose logging sur les cache hits/misses = indispensable pour le sanity. J'ajoute aussi un --cache-stats pour voir le hit rate live pendant le debug.
