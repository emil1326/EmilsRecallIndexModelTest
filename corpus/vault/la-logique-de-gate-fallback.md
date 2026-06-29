---
title: La logique de gate: fallback sur safe
summary: Le comportement par défaut du feature checker quand il sait pas (API down, edge case) c'est de bloquer le toggle lewd, always fail closed, pas open.
type: lesson
links:
  - "[[feature-checker-gate-les-toggles]]"
  - "[[fallback-offline-behavior-si-l]]"
  - "[[underage-detection-aucun-signal-magique]]"
  - "[[vrchat-api-instance-type-source]]"
---
C'est une décision de design claire: si on est dans le doute, on gate. Ça veut dire que si l'API plante ou que l'OSC répond pas, le toggle reste bloqué. C'est peut-être annoying pour le user parfois, mais l'alternative c'est leak du lewd content en public, pis ça c'est pire.
