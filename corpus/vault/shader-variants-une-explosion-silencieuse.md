---
title: Shader variants: une explosion silencieuse
summary: Chaque keyword combinaison dans un shader génère une variant séparée — des centaines de variants peuvent exploser le compile time et la VRAM.
type: reference
links:
  - "[[gpu-overdraw-pis-fill-rate]]"
  - "[[texture-streaming-pis-vram-bandwidth]]"
  - "[[static-batching-vs-dynamic-batching]]"
  - "[[renderdoc-pour-debug-le-gpu]]"
---
Le problème c'est que t'en aperçois pas au dev time, juste au build ou quand le shader stall compile in-game pour la première fois avec un freeze d'une seconde. Stripping les variants non-utilisées dans les graphics settings est essentiel. shader_feature vs multi_compile c'est pas juste du style — shader_feature strip automatiquement les keywords désactivés, multi_compile les garde tous.
