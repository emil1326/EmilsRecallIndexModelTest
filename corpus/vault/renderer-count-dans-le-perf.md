---
title: Renderer Count dans le Perf Rank VRChat
summary: VRChat compte le nombre de renderers dans le perf rank, mais 10 renderers bien optimisés peuvent avoir moins d'impact réel que 3 renderers avec 20 materials chacun.
type: lesson
links:
  - "[[very-poor-avatar-peut-outperformer]]"
  - "[[material-slots-brisent-le-gpu]]"
  - "[[budget-realiste-moins-de-24]]"
  - "[[frametime-perf-rank-pour-les]]"
---
C'est une des limites du système de ranking VRChat: il compte les objets pas leur coût réel. Un renderer avec une material simple c'est un draw call; un renderer avec 15 materials c'est 15 draw calls. Le rank voit deux renderers différents mais le GPU, lui, il voit pas la même chose pantoute.
