---
title: Cache hit rate: la vraie métrique qui compte
summary: Le cache hit rate dit si ton cache vaut quelque chose — sous 70% sur usage normal, ta stratégie d'invalidation invalide trop agressivement pis tu gaspilles du CPU.
type: journal
links:
  - "[[fingerprint-de-fichier-comme-cache]]"
  - "[[audit-trail-des-cache-misses]]"
  - "[[invalidation-partielle-evite-le-full]]"
  - "[[stale-cache-bugs-silencieux-dangereux]]"
---
J'ai eu un cache avec un hit rate de 23% parce que j'invalidais à chaque edit même si le contenu avait pas changé — un fingerprint sur le contenu ça aurait réglé ça tout de suite. Logge toujours hits vs misses avec du contexte (quel fichier, quelle règle) pour pouvoir diagnostiquer. Un hit rate élevé avec des résultats wrongos c'est encore pire que pas de cache pantoute.
