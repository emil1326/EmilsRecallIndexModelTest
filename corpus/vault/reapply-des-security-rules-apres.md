---
title: Reapply des security rules après chaque cache miss
summary: Un cache miss sur un fichier de sécurité doit toujours déclencher un reapply complet des règles actives, jamais retourner les derniers résultats cached sans revalider.
type: lesson
links:
  - "[[early-expiration-sur-changement-de]]"
  - "[[cache-key-doit-inclure-la]]"
  - "[[stale-cache-bugs-silencieux-dangereux]]"
  - "[[audit-trail-des-cache-misses]]"
---
C'est tentant de retourner le cache même si la règle a changé légèrement, mais en sécurité c'est non. Un cache miss sur quoi que ce soit lié aux security rules = reanalyse full, point final. J'ai vu un bug où une règle updatée continuait à retourner des faux positifs cached pendant des heures. Pas le genre d'erreur qu'on fait deux fois.
