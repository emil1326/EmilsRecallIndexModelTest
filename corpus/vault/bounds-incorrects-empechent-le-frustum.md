---
title: Bounds Incorrects Empêchent le Frustum Culling
summary: VRChat peut culler les avatars hors du frustum seulement si leurs bounds sont correctement dimensionnés; des bounds trop larges gardent l'avatar rendu même quand il est caché.
type: reference
links:
  - "[[skinned-mesh-vs-mesh-renderer]]"
  - "[[unity-profiler-vs-vrchat-in]]"
  - "[[vram-budget-en-instance-de]]"
  - "[[frametime-perf-rank-pour-les]]"
---
Les bounds d'un skinned mesh renderer définissent la bounding box pour le frustum culling. Si les bounds sont calculés trop larges (ce qui arrive avec des animations qui dépassent beaucoup le root), l'avatar sera rarement culled même quand il est hors caméra. Unity a une option Update When Offscreen sur les skinned mesh renderers — à désactiver si pas nécessaire pour éviter de render hors-écran inutilement.
