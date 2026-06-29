---
title: Shader compile au premier build, toujours douloureux
summary: Le premier build d'un projet VRChat avec des shaders custom prend un eternal parce qu'Unity doit compiler tous les shader variants from scratch — c'est pas un freeze.
type: lesson
links:
  - "[[reducing-build-time-avec-asset]]"
  - "[[private-build-avant-tout-upload]]"
  - "[[vcc-remplace-le-sdk-unity]]"
  - "[[performance-rank-cible-pour-avatars]]"
  - "[[blueprint-id-controle-quel-avatar]]"
---
J'ai galéré avec ça genre plusieurs fois — tu penses que le build est stuck, mais non, c'est juste Unity qui compile à mort en background. La solution c'est de garder ton dossier Library/ShaderCache intact et de pas cleaner ton projet trop souvent. Une fois le cache chaud c'est raisonnable, mais le cold start c'est vraiment plate tbh.
