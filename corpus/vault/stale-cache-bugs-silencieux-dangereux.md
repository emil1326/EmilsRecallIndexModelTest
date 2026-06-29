---
title: Stale cache = bugs silencieux dangereux
summary: Un cache pas invalidé au bon moment retourne des résultats d'analyse outdatés sans avertir — le pire scénario parce que tu vois pas le bug jusqu'à un audit.
type: lesson
links:
  - "[[fingerprint-de-fichier-comme-cache]]"
  - "[[reapply-des-security-rules-apres]]"
  - "[[ttl-vs-event-based-expiration]]"
  - "[[cache-key-doit-inclure-la]]"
---
Sur un outil d'analyse de sécurité, stale cache peut vouloir dire une vulnérabilité détectée correctement avant qui disparaît des résultats parce que le cache est pas refreshé. C'est plate tbh parce que tout le monde assume que les résultats sont fresh. Toujours inclure un timestamp et une version dans les entrées de cache pour pouvoir détecter le staleness.
