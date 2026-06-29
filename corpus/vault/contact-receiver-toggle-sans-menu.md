---
title: Contact Receiver toggle sans menu possible
summary: Un Contact Receiver peut setter un Bool paramètre automatiquement quand quelqu'un touche une zone; parfait pour des toggles proximity-triggered sans passer par le menu du tout.
type: reference
links:
  - "[[synced-vs-unsynced-parametres-difference]]"
  - "[[avatar-parameter-driver-changer-params]]"
  - "[[physbones-et-fx-layer-font]]"
  - "[[bool-int-float-choisir-bon]]"
---
Se configure avec un VRCContactReceiver component, un collision tag, pis le nom d'un Bool paramètre à setter. Le paramètre doit être synced pour que les autres joueurs voient l'effet. C'est un pattern cool pour des interactions immersives genre quelqu'un qui pette un animal sur ton avatar.
