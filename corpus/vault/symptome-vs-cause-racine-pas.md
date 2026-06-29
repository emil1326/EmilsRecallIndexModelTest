---
title: Symptôme vs cause racine: pas la même affaire
summary: Fixer le symptôme sans trouver la cause racine garantit que le bug revient ailleurs ou plus tard — distinguer les deux c'est fondamental.
type: lesson
links:
  - "[[la-bisection-coupe-le-debug]]"
  - "[[les-assumptions-non-validees-causent]]"
  - "[[lire-le-message-d-erreur]]"
  - "[[stack-trace-lire-du-bas]]"
---
Le NullPointerException c'est le symptôme; la vraie cause c'est peut-être une assumption sur l'ordre d'initialisation. Si tu null-check juste pour faire taire l'erreur sans comprendre pourquoi c'est null, t'as rien fixé, t'as juste reporté. Ça, c'est plate tbh.
