---
title: GPU-bound test simple freeze la caméra
summary: Pour tester rapidement si tu es GPU-bound ou CPU-bound, freeze la caméra — si le framerate augmente, le GPU travaillait moins, donc t'étais GPU-bound.
type: lesson
links:
  - "[[gpu-bound-vs-cpu-bound]]"
  - "[[frametime-en-ms-plus-utile]]"
  - "[[overdraw-accumule-les-pixel-invocations]]"
  - "[[renderdoc-pour-investiguer-le-render]]"
  - "[[draw-call-budget-selon-la]]"
---
C'est le test le plus quick and dirty: tu mets la caméra à regarder un mur vide (ou tu disable le rendering complètement). Si ton frametime drop significativement, ton bottleneck était dans le render — GPU-bound ou fill-rate bound. Si le frametime change pas, le problème vient du CPU (game logic, physics, etc.). Pas parfait mais ça donne une direction en 10 secondes.
