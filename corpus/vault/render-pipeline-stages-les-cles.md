---
title: Render pipeline stages les clés à connaître
summary: Les stages principaux du render pipeline moderne — vertex, rasterization, fragment/pixel, puis output merger — chacun a ses propres bottlenecks pis son propre profiling à faire.
type: reference
links:
  - "[[renderdoc-pour-investiguer-le-render]]"
  - "[[overdraw-accumule-les-pixel-invocations]]"
  - "[[depth-prepass-quand-ca-vaut]]"
  - "[[gpu-bound-vs-cpu-bound]]"
  - "[[rdna4-wave-size-32-ou]]"
---
Vertex stage: transforme les positions, skinning si t'as de l'animation. Rasterization: convertit triangles en fragments. Fragment/pixel stage: exécute le pixel shader pour chaque fragment — c'est souvent là que le coût est le plus gros. Output merger: depth test, blending, write au render target. Savoir dans quel stage ton GPU time va te dire quoi optimiser — RenderDoc et Radeon GPU Profiler peuvent breakdown le temps par stage.
