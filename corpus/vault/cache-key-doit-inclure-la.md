---
title: Cache key doit inclure la version des règles actives
summary: La cache key d'une analyse doit combiner le fingerprint du fichier ET la version des security rules — sinon changer les règles réutilise des analyses faites avec l'ancienne version.
type: reference
links:
  - "[[fingerprint-de-fichier-comme-cache]]"
  - "[[early-expiration-sur-changement-de]]"
  - "[[versioning-du-cache-schema-sinon]]"
  - "[[reapply-des-security-rules-apres]]"
---
En pratique: `cache_key = hash(file_content) + '_' + rules_version`. Dès que les règles updatent, toutes les clés changent automatiquement — invalidation par construction, pas besoin de tracking explicite. Le seul downside c'est que ça force un full rebuild quand les règles changent, même pour les fichiers où la règle modifiée ne s'applique pas. Trade-off acceptable.
