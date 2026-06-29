---
title: Cache poisoning si les inputs sont pas validés
summary: Si n'importe quoi peut écrire dans le cache sans validation, un fichier malicieux peut empoisonner les entrées et faire croire à l'outil que du code dangereux est safe.
type: lesson
links:
  - "[[stale-cache-bugs-silencieux-dangereux]]"
  - "[[reapply-des-security-rules-apres]]"
  - "[[lock-sur-le-cache-write]]"
  - "[[versioning-du-cache-schema-sinon]]"
---
C'est un vecteur d'attaque réel pour les outils de sécurité — si un attaquant peut écrire dans le répertoire de cache, il peut pre-populate des résultats falsifiés. Signe tes entrées cache avec un HMAC, ou garde le cache dans un répertoire avec permissions strictes. Pour un outil local dev-only, c'est moins critique, mais pour un CI tool ça compte vraiment.
