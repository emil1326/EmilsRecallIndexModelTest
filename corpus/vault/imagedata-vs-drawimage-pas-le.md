---
title: ImageData vs drawImage: pas le même deal
summary: `ImageData` te donne un accès raw aux bytes du canvas, alors que `drawImage` est une black box optimisée que le browser contrôle — deux outils très différents.
type: reference
links:
  - "[[canvas-pixel-by-pixel-le]]"
  - "[[la-classe-image-custom-pourquoi]]"
  - "[[pixel-loop-performance-le-frametime]]"
  - "[[coordinate-system-canvas-0-0]]"
---
Quand j'ai découvert `ImageData`, j'étais genre... attends, je peux écrire directement dans la mémoire vidéo? Kind of? Ça hit different. `drawImage` c'est pour les cas normaux, mais si tu veux du contrôle total pixel par pixel, c'est `getImageData`/`putImageData` que t'utilises, pis c'est lent mais instructif.
