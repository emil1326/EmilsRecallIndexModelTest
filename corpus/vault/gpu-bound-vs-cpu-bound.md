---
title: GPU-bound vs CPU-bound détecter le vrai bottleneck
summary: Distinguer si le bottleneck est GPU ou CPU, c'est la première chose à faire avant de toucher à ton render pipeline, sinon t'optimises dans le vide.
type: reference
links:
  - "[[gpu-bound-test-simple-freeze]]"
  - "[[frametime-en-ms-plus-utile]]"
  - "[[renderdoc-pour-investiguer-le-render]]"
  - "[[draw-call-budget-selon-la]]"
  - "[[overdraw-accumule-les-pixel-invocations]]"
---
La distinction change tout — si t'es CPU-bound, réduire les draw calls aide. Si t'es GPU-bound, faut regarder l'overdraw, les texture samples, la complexité des pixel shaders. Utilise le GPU profiler de ton engine (Frame Debugger en Unity, RenderDoc) pis checke si le GPU time dépasse ton frame budget ou si c'est le main thread CPU qui attend.
