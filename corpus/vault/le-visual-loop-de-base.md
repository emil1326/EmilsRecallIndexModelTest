---
title: Le visual loop de base derrière l'app oiseaux
summary: L'animation des oiseaux dans l'app c'était un simple loop qui repositionnait chaque oiseau de droite à gauche sur un interval fixe.
type: reference
links:
  - "[[l-app-d-oiseaux-qui]]"
  - "[[l-autoclicker-cache-dans-l]]"
  - "[[quand-un-projet-pivot-a]]"
---
L'animation des oiseaux c'était simple: chaque oiseau avait une position X qui decrementait frame par frame, pis quand il sortait du bord gauche il reapparaissait à droite. C'est le loop le plus basique pour un sprite qui bouge. Ce qui est drôle c'est que c'est ce même loop qui triggait les clicks automatiques.
