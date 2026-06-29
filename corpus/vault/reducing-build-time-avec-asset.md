---
title: Reducing build time avec Asset Bundle Cache
summary: Activer le Asset Bundle caching dans les VRChat SDK settings réduit massivement le rebuild time — le lazy rebuild se déclenche only pour les assets modifiés.
type: lesson
links:
  - "[[vcc-remplace-le-sdk-unity]]"
  - "[[shader-compile-au-premier-build]]"
  - "[[blueprint-id-controle-quel-avatar]]"
  - "[[private-build-avant-tout-upload]]"
  - "[[dynamic-bones-dead-physbones-only]]"
---
Ça passe de genre 5-10 minutes à 30-60 secondes pour les petits changements, c'est pas rien. C'est activé par défaut normalement mais ça vaut la peine de checker dans les SDK settings. Si tu cleanes ton projet trop souvent t'invalides le cache pis tu repars à zero — à faire avec parcimonie.
