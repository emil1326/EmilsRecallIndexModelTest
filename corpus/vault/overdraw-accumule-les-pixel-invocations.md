---
title: Overdraw accumule les pixel invocations inutilement
summary: L'overdraw, c'est quand plusieurs fragments sont rendus pour le même pixel à cause d'overlap de geometry, pis chaque invocation du pixel shader supplémentaire c'est du GPU time gaspillé.
type: lesson
links:
  - "[[depth-prepass-quand-ca-vaut]]"
  - "[[render-pipeline-stages-les-cles]]"
  - "[[gpu-bound-vs-cpu-bound]]"
  - "[[renderdoc-pour-investiguer-le-render]]"
  - "[[atlas-textures-reduit-les-material]]"
---
Sur mobile c'est critique mais sur PC avec RDNA4 c'est still notable si tes pixel shaders sont complexes. Le pire c'est les particules et les UI avec beaucoup de layers transparents — là t'accumules du fill rate cost pour rien. Unity a un overdraw visualization mode dans le Scene View pour voir ça visuellement, pis RenderDoc montre le depth complexity par pixel.
