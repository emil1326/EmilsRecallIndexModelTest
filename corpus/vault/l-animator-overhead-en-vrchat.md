---
title: L'animator overhead en VRChat c'est réel
summary: Un Animator Controller complexe avec beaucoup de layers et transitions coûte des ms de CPU time chaque frame, indépendamment du nombre de bones.
type: lesson
links:
  - "[[les-perf-rankings-vrchat-sont]]"
  - "[[ma-heuristique-d-optim-le]]"
  - "[[cpu-bottleneck-pis-gpu-bottleneck]]"
  - "[[skinnedmeshrenderer-expensive-af-cote-cpu]]"
---
Le perf ranking VRChat dit "excellent" si l'animator tourne en 6ms — mais 6ms juste pour l'animator, c'est énorme quand ton budget total est genre 16ms à 60fps. Les layers disabled n'arrêtent pas complètement le calcul selon comment c'est configuré. Faut vraiment profiler rather que se fier au rank, ça c'est clair.
