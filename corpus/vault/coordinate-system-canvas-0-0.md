---
title: Coordinate system canvas: (0,0) en haut-gauche
summary: Canvas a (0,0) en top-left pis Y qui augmente vers le bas — le contraire du repère mathématique, source de bugs de flip pas évidents à catch.
type: reference
links:
  - "[[canvas-pixel-by-pixel-le]]"
  - "[[la-classe-image-custom-pourquoi]]"
  - "[[api-design-de-la-classe]]"
  - "[[color-handling-rgba-ou-hsla]]"
---
Ça paraît trivial mais quand tu build ta propre classe Image, t'as le choix de transformer ou pas le coordinate system. J'ai laissé le Canvas natif (Y down) pis ça m'a causé des headaches quand je drawais des shapes qui étaient upside down. Genre tu sais c'est ça mais tu l'oublies anyway smh.
