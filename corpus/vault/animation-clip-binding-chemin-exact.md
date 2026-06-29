---
title: Animation clip binding chemin exact obligatoire
summary: Le path dans une animation clip doit correspondre exactement à la hiérarchie depuis la racine; une typo ou un rename d'objet pis l'animation ne fait plus rien.
type: lesson
links:
  - "[[write-defaults-on-off-vraie]]"
  - "[[layer-order-contraintes-animator-critique]]"
  - "[[preview-local-upload-comportement-divergent]]"
  - "[[fx-layer-regne-sur-quasi]]"
---
Si tu renommes un GameObject après avoir créé le clip, le binding break silencieusement — l'animation joue mais anime absolument rien. Faut aller dans l'Animation window, clicker sur le binding cassé, pis fixer le path manuellement. Pro tip: finalise tes noms d'objets avant de recorder des animations, sinon c'est une corvée.
