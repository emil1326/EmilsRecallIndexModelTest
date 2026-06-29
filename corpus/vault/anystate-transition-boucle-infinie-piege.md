---
title: AnyState transition boucle infinie piège
summary: Une transition depuis AnyState sans condition bien définie peut créer une boucle infinie où l'animator se ré-entre dans le même state constamment; l'avatar lag au complet.
type: lesson
links:
  - "[[transition-exit-time-desactiver-immediatement]]"
  - "[[avatar-parameter-driver-changer-params]]"
  - "[[fx-layer-regne-sur-quasi]]"
  - "[[write-defaults-on-off-vraie]]"
---
AnyState c'est puissant pour des transitions globales genre 'quitter n'importe quel état pour aller en idle', mais faut des conditions strictes. La configuration safe: 'Can Transition to Self' = false, plus une condition paramètre explicite. Sans ça, l'animator peut se ré-entrer dans le même state en boucle et lag l'avatar au complet.
