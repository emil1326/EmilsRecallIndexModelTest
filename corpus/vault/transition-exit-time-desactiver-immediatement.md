---
title: Transition exit time désactiver immédiatement
summary: Exit Time force la fin de l'animation avant de changer d'état; faut le désactiver pour des toggles réactifs et se fier uniquement aux conditions de paramètres.
type: reference
links:
  - "[[anystate-transition-boucle-infinie-piege]]"
  - "[[direct-blend-tree-toggle-sans]]"
  - "[[layer-order-contraintes-animator-critique]]"
  - "[[gesture-layer-hand-signs-tracking]]"
---
Par défaut Unity active Exit Time à 1.0, ce qui veut dire que le state va jouer jusqu'au bout avant de transitionner. Pour un toggle on/off instantané: Has Exit Time = unchecked, Transition Duration = 0, condition = paramètre. Sinon ton toggle répond avec un delay de la durée complète du clip, c'est horrible.
