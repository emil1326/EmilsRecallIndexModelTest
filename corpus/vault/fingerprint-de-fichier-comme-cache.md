---
title: Fingerprint de fichier comme cache key robuste
summary: Hasher le contenu du fichier pour la cache key est plus fiable qu'un timestamp parce que les timestamps peuvent mentir après un git checkout ou un build.
type: reference
links:
  - "[[cache-key-doit-inclure-la]]"
  - "[[stale-cache-bugs-silencieux-dangereux]]"
  - "[[versioning-du-cache-schema-sinon]]"
  - "[[dependency-graph-colonne-vertebrale-du]]"
---
SHA-256 du contenu, ou même juste les premiers N bytes plus la taille, ça fit pour la plupart des cas. Le timestamp c'est tentant parce que c'est cheap à lire, mais genre, git rebase ou un simple touch peuvent le rendre inutile. Cache key = hash du contenu + version des règles, au minimum.
