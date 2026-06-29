---
title: Color handling: RGBA ou HSLA, faut choisir
summary: RGBA c'est natif Canvas mais HSLA est way plus intuitif pour les gradients — faut convertir entre les deux pis c'est là que les math arrivent.
type: reference
links:
  - "[[canvas-pixel-by-pixel-le]]"
  - "[[coordinate-system-canvas-0-0]]"
  - "[[la-classe-image-custom-pourquoi]]"
  - "[[pixel-loop-performance-le-frametime]]"
---
Quand je voulais faire des effets smooth — genre du color cycling ou des gradients — RGBA c'est painful. Tourner juste le Hue en HSL pis garder S et L constant, c'est beaucoup plus lisible comme intent. La conversion HSL vers RGB c'est pas compliqué mais faut la savoir.
