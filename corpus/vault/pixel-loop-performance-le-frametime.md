---
title: Pixel loop performance: le frametime ment pas
summary: Looper sur chaque pixel à chaque frame en JavaScript pur plafonne vite — le frametime spike est immédiat passé quelques centaines de pixels wide.
type: lesson
links:
  - "[[canvas-pixel-by-pixel-le]]"
  - "[[animation-canvas-requestanimationframe-ou-rien]]"
  - "[[imagedata-vs-drawimage-pas-le]]"
  - "[[la-classe-image-custom-pourquoi]]"
---
J'ai mesuré ça direct dans Chrome DevTools pis whoa. Une image 512x512 animée frame par frame en JS pur, t'as déjà des drops. Tu peux optimiser le inner loop, mais y'a un ceiling. Pour de vrai performance t'as besoin de WebGL ou d'une autre stratégie — la brute force a ses limites, tsu.
