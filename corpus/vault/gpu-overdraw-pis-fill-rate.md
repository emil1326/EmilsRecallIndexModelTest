---
title: GPU overdraw pis fill rate: souvent oublié
summary: Chaque pixel dessiné plusieurs fois (transparent objects, particles, UI stacked) contribue à l'overdraw — et ça peut saturer le fill rate du GPU facilement.
type: lesson
links:
  - "[[cpu-bottleneck-pis-gpu-bottleneck]]"
  - "[[draw-calls-le-vrai-cost]]"
  - "[[shader-variants-une-explosion-silencieuse]]"
  - "[[renderdoc-pour-debug-le-gpu]]"
---
Sur mobile ou VR, le fill rate est souvent le bottleneck, pas le vertex count — une réalité que beaucoup de devs ignorent. Unity a un overdraw scene view mode qui montre les zones rouges clairement. Les particules sont les coupables classiques: un particle system avec soft particles pis additive blending, ça bouffe le GPU fast.
