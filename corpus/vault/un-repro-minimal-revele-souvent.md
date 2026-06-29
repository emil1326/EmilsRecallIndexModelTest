---
title: Un repro minimal révèle souvent la vraie cause
summary: Le processus de créer un repro minimal est lui-même du debug actif — en éliminant l'inutile, on trouve souvent la cause avant de finir.
type: lesson
links:
  - "[[le-repro-minimal-first-thing]]"
  - "[[les-assumptions-non-validees-causent]]"
  - "[[symptome-vs-cause-racine-pas]]"
  - "[[isoler-systeme-vs-app-avant]]"
---
C'est presque méta: t'essaies de build le repro minimal pis à un moment tu enlèves quelque chose et le bug disparaît — et là tu réalises que c'est CETTE chose qui causait le problème. J'ai vécu ça tellement de fois que c'est devenu ma stratégie principale pour les bugs complexes.
