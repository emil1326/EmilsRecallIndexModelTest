---
title: Dedup exact sur hash MD5
summary: Le dedup exact consiste à hasher chaque exemple (MD5 ou SHA1 sur le texte normalisé) pis à garder seulement les hashes uniques avant tout split.
type: reference
links:
  - "[[normaliser-le-texte-avant-dedup]]"
  - "[[minhash-lsh-pour-dedup-fuzzy]]"
  - "[[ordre-dedup-split-ca-change]]"
  - "[[sources-cachees-de-leakage-insidieux]]"
---
T'as juste à faire `hashlib.md5(text.encode()).hexdigest()` pis tu droppe les doublons dans un set — c'est O(n) en temps, pratiquement gratuit. Le piège c'est de hasher le texte brut sans normaliser d'abord: deux exemples identiques avec juste des espaces différents vont passer à travers. Genre fais ton `strip().lower()` avant de hasher, tsé. Pour les datasets vraiment larges, SHA1 est à peine plus lent mais les collisions sont astronomiquement moins probables.
