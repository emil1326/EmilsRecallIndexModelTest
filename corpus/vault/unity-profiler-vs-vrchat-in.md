---
title: Unity Profiler vs VRChat In-Game: Divergence
summary: Le frametime mesuré dans le Unity Profiler en mode preview est jamais exactement le même qu'in-game VRChat à cause du SDK overhead et du networking layer.
type: lesson
links:
  - "[[frametime-perf-rank-pour-les]]"
  - "[[unity-stats-window-premier-tool]]"
  - "[[shader-variants-poiyomi-et-compile]]"
  - "[[very-poor-avatar-peut-outperformer]]"
  - "[[cpu-bottleneck-pis-gpu-bottleneck]]"
---
Le Unity Profiler local te donne une bonne idée relative (A est plus lourd que B), mais les chiffres absolus in-game VRChat vont être différents. Il y a du overhead VRChat SDK, des syncs réseau, d'autres avatars qui tournent en même temps, tout ça change le picture. Utilise le Profiler pour comparer des versions d'un même avatar, pas pour prédire le frametime exact in-game.
