---
title: RenderDoc pour investiguer le render pipeline
summary: RenderDoc est l'outil de référence pour capturer et analyser frame-by-frame ce qui se passe dans le render pipeline — draw calls, états, textures, temps GPU par stage.
type: reference
links:
  - "[[shader-compile-stall-rdna4-c]]"
  - "[[gpu-bound-vs-cpu-bound]]"
  - "[[render-pipeline-stages-les-cles]]"
  - "[[rdna4-wave-size-32-ou]]"
  - "[[overdraw-accumule-les-pixel-invocations]]"
---
T'attaches RenderDoc au process, tu captures un frame, pis t'as accès à chaque draw call avec les bindings, les shaders, les render targets. C'est là que tu vois vraiment pourquoi tes draw calls sont pas batchés, ou quel pass coûte le plus cher. Sur RDNA4 avec les AMD tools en plus (Radeon GPU Profiler), t'as des données de timing par wave encore plus précises.
