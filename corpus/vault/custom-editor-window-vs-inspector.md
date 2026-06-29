---
title: Custom editor window vs Inspector extension
summary: Une custom editor window donne un contrôle total sur l'UX mais coûte beaucoup plus de code qu'une simple Inspector extension pour le même feature.
type: reference
links:
  - "[[custom-parser-vs-json-yaml]]"
  - "[[hard-coded-vs-data-driven]]"
  - "[[scriptableobject-vs-monobehaviour-le-vrai]]"
  - "[[quand-abstraire-vs-quand-hardcoder]]"
---
L'Inspector extension c'est le 80/20 pour la plupart des tools — tu adds un bouton, tu overrides un field display, ça fit dans le workflow existant. Mais quand tu as un vrai workflow multi-step ou des données trop complexes pour l'Inspector, la custom window est le seul vrai choix. La règle que j'utilise: si ça prend plus de 3 scrolls dans l'Inspector pour voir tout le feature, c'est signe qu'il faut une window. Le coût du custom window c'est surtout le docking et la serialization de l'état.
