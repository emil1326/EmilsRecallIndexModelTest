---
title: Unity Stats Window: Premier Tool Avant Upload
summary: Le Unity Stats window en mode Game montre les draw calls, tris et verts en temps réel; c'est le premier tool à ouvrir avant d'upload un avatar VRChat.
type: reference
links:
  - "[[frametime-perf-rank-pour-les]]"
  - "[[unity-profiler-vs-vrchat-in]]"
  - "[[budget-realiste-moins-de-24]]"
  - "[[material-slots-brisent-le-gpu]]"
  - "[[renderdoc-pour-investiguer-le-render]]"
---
Le Stats window c'est dans l'éditeur Unity, tu le toggle dans le coin du Game view, pis ça te donne un breakdown live de la frame. Tu peux voir immédiatement si tu as 5 draw calls ou 50, et voir les batches séparément. C'est pas aussi détaillé que le Profiler, mais pour un sanity check rapide avant d'upload, c'est parfait et ça prend 3 secondes.
