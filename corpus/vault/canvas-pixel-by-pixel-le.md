---
title: Canvas pixel-by-pixel: le vrai coût
summary: Manipuler chaque pixel manuellement via `putImageData` coûte cher en perfs, tsu, mais t'apprends exactement comment le browser gère son rendering.
type: lesson
links:
  - "[[imagedata-vs-drawimage-pas-le]]"
  - "[[pixel-loop-performance-le-frametime]]"
  - "[[la-classe-image-custom-pourquoi]]"
  - "[[animation-canvas-requestanimationframe-ou-rien]]"
  - "[[color-handling-rgba-ou-hsla]]"
---
Chaque pixel, c'est 4 bytes dans le array — R, G, B, A — et tu loop à travers tout ça à chaque frame si t'animes. C'est genre super satisfaisant de voir une image apparaître que t'as construite byte par byte, mais ça scale vraiment pas. Pour du static c'est parfait, pour de l'animation t'as besoin de smarter patterns.
