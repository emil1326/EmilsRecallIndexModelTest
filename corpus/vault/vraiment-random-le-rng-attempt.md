---
title: Vraiment random? Le RNG attempt raté
summary: J'ai essayé de faire un 'truly random' number generator mais j'ai failed — parce que dans un environnement déterministe comme JavaScript, c'est pratiquement impossible.
type: journal
links:
  - "[[boredom-driven-dev-les-meilleurs]]"
  - "[[la-classe-image-custom-pourquoi]]"
  - "[[javascript-pur-vs-typescript-le]]"
  - "[[from-scratch-builds-le-vrai]]"
---
L'idée c'était d'utiliser du entropy externe pour dépasser `Math.random()` — timing, mouse position, whatever — mais le résultat était pas vraiment plus random, just plus compliqué. Sad xD. J'ai appris que "pseudo-random" c'est un compromis volontaire, pas une limitation technique à corriger avec du bricolage.
