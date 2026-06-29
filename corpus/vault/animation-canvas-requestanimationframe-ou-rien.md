---
title: Animation canvas: requestAnimationFrame ou rien
summary: Pour animer dans un Canvas, `requestAnimationFrame` est le seul vrai choix — `setInterval` est moins fiable, syncs pas avec le refresh rate pis mange du CPU inutilement.
type: reference
links:
  - "[[canvas-pixel-by-pixel-le]]"
  - "[[pixel-loop-performance-le-frametime]]"
  - "[[la-classe-image-custom-pourquoi]]"
  - "[[imagedata-vs-drawimage-pas-le]]"
---
J'ai commencé avec `setInterval` parce que c'est plus intuitif — tu mets un délai en ms pis c'est parti. Mais le frametime est jamais clean, t'as du tearing, pis ça tourne même si la page est pas visible. `requestAnimationFrame` pause quand l'onglet est en background, ça c'est smarter.
