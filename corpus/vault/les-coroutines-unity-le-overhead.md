---
title: Les coroutines Unity: le overhead mal compris
summary: Les coroutines Unity ne sont pas des vrais threads — elles tournent sur le main thread entre les frames, avec un petit overhead d'allocation à chaque yield.
type: lesson
links:
  - "[[les-gc-allocs-causent-des]]"
  - "[[object-pooling-pour-eviter-les]]"
  - "[[profiler-beginsample-pour-isoler-les]]"
  - "[[string-concat-dans-un-hot]]"
---
Chaque yield return new WaitForSeconds() alloue un objet managed sur la heap si tu le new à chaque fois — le fix classique c'est de cacher l'instruction dans une variable membre et de la réutiliser. Le vrai problème des coroutines c'est pas leur overhead per se, c'est quand elles substituent du code qui devrait être dans l'Update proprement schedulé pis que personne sait plus ce qui tourne quand.
