---
title: Rollback automatique si cache corrompu
summary: Si une entrée cache est corrompue ou illisible au load, il faut toujours fallback gracieusement sur un rebuild plutôt que crasher ou retourner des données partielles.
type: lesson
links:
  - "[[lock-sur-le-cache-write]]"
  - "[[versioning-du-cache-schema-sinon]]"
  - "[[serialisation-cache-json-lisible-vs]]"
  - "[[debug-mode-devrait-bypass-le]]"
  - "[[dedup-exact-sur-hash-md5]]"
---
Le pattern c'est: try { load cache } catch { log warning, invalider, rebuild }. Jamais laisser une corruption de cache crasher l'outil — c'est du code d'infrastructure, il doit être resilient. Sur disque, un write partiel (power cut, kill -9) peut laisser un fichier cache dans un état invalide. Le write-then-rename atomic guard contre ça la plupart du temps.
