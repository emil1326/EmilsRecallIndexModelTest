---
title: Shader Variants Poiyomi et Compile Time Lag
summary: Les shaders comme Poiyomi ou lilToon génèrent des milliers de shader variants qui causent un lag notable au premier chargement de l'avatar dans VRChat.
type: reference
links:
  - "[[dxt-vs-astc-compression-texture]]"
  - "[[material-slots-brisent-le-gpu]]"
  - "[[unity-profiler-vs-vrchat-in]]"
  - "[[frametime-perf-rank-pour-les]]"
---
Poiyomi Toon c'est le shader de facto pour les avatars anime VRChat mais il a des centaines de features toggleables, chacune crée des variants compilés. La première fois que quelqu'un load ton avatar, leur VRChat doit compiler ces variants — ça cause un freeze momentané pour eux. Poiyomi a une option Lock In qui bake les settings et réduit les variants drastiquement, c'est à faire avant tout upload.
