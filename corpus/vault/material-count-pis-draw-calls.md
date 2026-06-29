---
title: Material count pis draw calls c'est pas pareil
summary: Avoir 100 materials c'est pas automatiquement 100 draw calls — la distinction est cruciale pour savoir où optimiser dans ton render pipeline.
type: lesson
links:
  - "[[material-unique-setpass-call-coute]]"
  - "[[srp-batcher-batch-automatique-si]]"
  - "[[gpu-bound-vs-cpu-bound]]"
  - "[[draw-call-budget-selon-la]]"
  - "[[materialpropertyblock-evite-de-casser-le]]"
---
Un draw call c'est un appel GPU pour render une geometry. Un material change (SetPass call) c'est ce qui coûte cher côté CPU. T'as beau batcher tes draw calls, si tes materials sont tous différents, le CPU choke quand même à setup chaque state. Faut penser aux deux séparément si tu veux vraiment comprendre ton bottleneck.
