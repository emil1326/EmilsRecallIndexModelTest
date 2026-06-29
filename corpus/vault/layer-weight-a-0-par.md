---
title: Layer weight à 0 par défaut piège
summary: Les nouvelles layers dans l'animator ont un weight de 0 par défaut; oublier de le setter à 1 pis la layer fait rien du tout, c'est le bug classique.
type: lesson
links:
  - "[[write-defaults-on-off-vraie]]"
  - "[[fx-layer-regne-sur-quasi]]"
  - "[[gesture-layer-hand-signs-tracking]]"
  - "[[action-layer-pour-emotes-et]]"
---
C'est un des bugs les plus frustrants parce que tout semble correct: les states existent, les transitions sont là, les paramètres sont bons — mais la layer est mute à 0. Va dans l'Animator window, sélectionne la layer, mets le weight à 1. Fais ça immédiatement en créant chaque nouvelle layer.
