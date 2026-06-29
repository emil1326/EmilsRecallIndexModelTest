---
title: VSync pis la stabilité du frametime
summary: VSync force le GPU à attendre le vblank — le frametime devient un multiple du refresh interval (16.6ms, 33.3ms) plutôt qu'une valeur continue.
type: lesson
links:
  - "[[ma-heuristique-d-optim-le]]"
  - "[[cpu-bottleneck-pis-gpu-bottleneck]]"
  - "[[les-gc-allocs-causent-des]]"
  - "[[le-good-enough-en-perf]]"
---
Le problème c'est que si ton frame prend 17ms au lieu de 16ms, tu drop à 30fps d'un coup — pas de 60 à 59, c'est binaire. En VR, c'est encore plus brutal parce que le headset a son propre timewarp et la moindre hésitation se sent physiquement. Avoir un frametime stable en dessous du target c'est plus important qu'une moyenne basse avec des spikes occasionnels.
