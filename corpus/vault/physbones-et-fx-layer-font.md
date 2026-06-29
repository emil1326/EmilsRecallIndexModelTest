---
title: PhysBones et FX layer font mal ensemble
summary: PhysBones exposent IsGrabbed et Stretch comme paramètres mais ils sont locaux; leur timing avec le FX layer crée des glitches visuels chez les autres joueurs.
type: lesson
links:
  - "[[contact-receiver-toggle-sans-menu]]"
  - "[[layer-order-contraintes-animator-critique]]"
  - "[[fx-layer-regne-sur-quasi]]"
  - "[[mirror-test-local-remote-comportement]]"
---
Le problème c'est que les PhysBones parameters (IsGrabbed, Angle, Stretch) sont locaux par défaut, donc l'animation déclenche chez toi mais les autres la voient avec du lag ou pas du tout. Pour des interactions physiques visibles par tous, mieux vaut passer par un Contact Receiver synced. C'est plate tbh mais c'est la réalité du networking VRChat.
