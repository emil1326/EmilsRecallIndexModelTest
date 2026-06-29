---
title: Bool Int Float choisir bon type paramètre
summary: Bool coûte 1 bit, Int et Float coûtent 8 bits chacun; choisir le mauvais type pis ça gaspille des bits dans le budget synced pour rien du tout.
type: reference
links:
  - "[[budget-parametres-vrchat-limite-256]]"
  - "[[radial-puppet-float-continu-expression]]"
  - "[[synced-vs-unsynced-parametres-difference]]"
  - "[[avatar-parameter-driver-changer-params]]"
---
Pour les toggles simples, Bool c'est la go-to: 1 bit, rien de plus efficace. Int sert pour les multi-states genre 0/1/2/3 (outfit selection), Float pour les valeurs continues comme les Radial Puppets. Overkill d'utiliser un Float pour un toggle on/off basique, tsu — ça gaspille 7 bits pour rien.
