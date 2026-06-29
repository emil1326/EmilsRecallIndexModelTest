---
title: Dynamic Bones dead, PhysBones only maintenant
summary: VRChat a migré vers leur système PhysBones natif — les Dynamic Bones scripts marchent encore mais c'est deprecated pis tout nouveau projet devrait partir direct en PhysBones.
type: journal
links:
  - "[[sdk2-mort-sdk3-only-maintenant]]"
  - "[[performance-rank-cible-pour-avatars]]"
  - "[[physbones-collision-test-avec-plusieurs]]"
  - "[[reducing-build-time-avec-asset]]"
  - "[[vcc-remplace-le-sdk-unity]]"
---
La bonne nouvelle c'est que PhysBones c'est mieux optimisé — les autres players peuvent disable tes dynamics pour sauver du performance sans que ça crashe rien. La mauvaise c'est que migrer un rig existant c'est du re-tune manual, les valeurs se mappent pas 1-to-1. Mais genre, c'est le futur tsu, autant partir de là.
