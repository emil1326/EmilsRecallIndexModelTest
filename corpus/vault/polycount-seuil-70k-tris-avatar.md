---
title: Polycount Seuil 70k Tris Avatar PC
summary: Le polycount safe pour un avatar PC VRChat est autour de 70k tris, mais c'est honnêtement pas le bottleneck le plus critique comparé aux draw calls.
type: lesson
links:
  - "[[frametime-perf-rank-pour-les]]"
  - "[[very-poor-avatar-peut-outperformer]]"
  - "[[material-slots-brisent-le-gpu]]"
  - "[[budget-realiste-moins-de-24]]"
---
VRChat classe les avatars Very Poor si le polycount dépasse 70k sur PC, mais en 2024-2025 avec des GPUs modernes, les tris c'est rarement le vrai bottleneck. Un avatar à 120k tris avec 2 materials et des shaders légers peut performer mieux qu'un avatar à 40k tris avec 20 materials et Poiyomi full features. Fais confiance au frametime, pas au rank.
