---
title: Physics FixedUpdate: le cost caché des rigidbodies
summary: Chaque Rigidbody actif force un step de simulation physique dans FixedUpdate, pis multiplier les colliders complexes explose le CPU time de PhysX.
type: reference
links:
  - "[[cpu-bottleneck-pis-gpu-bottleneck]]"
  - "[[profiler-beginsample-pour-isoler-les]]"
  - "[[les-gc-allocs-causent-des]]"
  - "[[ma-heuristique-d-optim-le]]"
---
Le FixedUpdate tourne à taux fixe (default 50Hz) indépendamment du framerate, donc si ça prend 5ms, ça prend 5ms à chaque step, pas juste quand ça collide. Les colliders mesh sont les plus expensive — toujours préférer primitives ou convex hull. Mettre les rigidbodies kinematic quand ils bougent pas coûte rien et save du compute pour vrai.
