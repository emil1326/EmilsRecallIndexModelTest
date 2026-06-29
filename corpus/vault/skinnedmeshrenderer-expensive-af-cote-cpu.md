---
title: SkinnedMeshRenderer: expensive AF côté CPU
summary: Les SkinnedMeshRenderer recalculent les vertex positions chaque frame sur CPU — avec un gros mesh, ça peut manger plusieurs ms sans que tu le voies venir.
type: lesson
links:
  - "[[cpu-bottleneck-pis-gpu-bottleneck]]"
  - "[[les-perf-rankings-vrchat-sont]]"
  - "[[draw-calls-le-vrai-cost]]"
  - "[[l-animator-overhead-en-vrchat]]"
---
Unity peut GPU-skin à la place, mais c'est pas activé partout par défaut et le support varie selon le pipeline. Pour les avatars VRChat avec des meshes body séparés en tonnes de parties, c'est souvent là que le CPU time disparaît. Merger les meshes en un seul SkinnedMesh réduit drastiquement le coût — moins de renderers, moins d'évaluation de bones redondante.
