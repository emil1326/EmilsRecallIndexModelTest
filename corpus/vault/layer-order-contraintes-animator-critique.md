---
title: Layer order contraintes animator critique
summary: L'ordre des layers dans l'animator détermine qui gagne quand deux layers touchent la même propriété; layer du haut a priorité plus haute, pis ça peut vraiment surprendre.
type: lesson
links:
  - "[[fx-layer-regne-sur-quasi]]"
  - "[[action-layer-pour-emotes-et]]"
  - "[[animation-clip-binding-chemin-exact]]"
  - "[[transition-exit-time-desactiver-immediatement]]"
  - "[[frametime-perf-rank-pour-les]]"
---
Si deux layers touchent la même propriété, la layer du dessus dans la liste gagne sur celle du dessous. Ça s'applique aussi aux activations de constraints: si FX layer active une contrainte et une autre layer la désactive, c'est l'ordre qui tranche. J'ai perdu du temps à comprendre ça, pas de mensonges xD.
