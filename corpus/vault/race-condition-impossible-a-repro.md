---
title: Race condition: impossible à repro, faut analyser
summary: Les race conditions sont par définition timing-dependent et disparaissent souvent quand on les observe — le seul vrai fix c'est l'analyse statique du code.
type: reference
links:
  - "[[l-heisenbug-qui-disparait-quand]]"
  - "[[logger-les-timestamps-pour-les]]"
  - "[[le-repro-minimal-first-thing]]"
  - "[[isoler-systeme-vs-app-avant]]"
---
Une race condition c'est quand deux threads ou coroutines accèdent au même état dans un ordre non-déterministe. Le fait de logger ou d'attacher un debugger change le timing, ce qui peut masquer le bug complètement. Pas le choix: faut analyser le code pour les accès concurrents, pas juste attendre que ça repro.
