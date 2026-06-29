---
title: Hot reload Java pas si simple
summary: Arrow n'a pas de hot reload des data schemas pour l'instant parce que Java ClassLoader pas conçu pour ça easy, pis les workarounds sont tous fragiles.
type: lesson
links:
  - "[[refactor-arrow-savoir-quand-arreter]]"
  - "[[in-memory-store-bati-sur]]"
  - "[[serialization-jackson-vs-kryo-dans]]"
  - "[[arrow-roadmap-evolue-par-besoin]]"
---
J'ai regardé des trucs genre OSGi ou des custom ClassLoaders pour hot-swap des schema classes, mais c'est genre 500 lignes de code brittle pour un feature nice-to-have. Pour l'instant Arrow requiert un restart pour les schema changes. C'est plate mais honest tbh.
