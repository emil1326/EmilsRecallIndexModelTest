---
title: Mesh diff: vertex comparison pis les pièges float
summary: Comparer deux meshes implique vertex positions, normals, UVs, triangles — mais l'égalité exacte de floats c'est une mauvaise idée, faut absolument un epsilon de tolérance.
type: lesson
links:
  - "[[module-first-design-versus-monolith]]"
  - "[[assetdatabase-refresh-bloque-l-editor]]"
  - "[[tests-editor-tools-manual-bat]]"
  - "[[emilswork-suite-de-tools-modulaires]]"
  - "[[archi-feature-checker-api-osc]]"
---
Pour le mesh diff dans EmilsWork j'ai appris que comparer des floats exactement donne des faux positifs partout — faut un epsilon de tolérance. Le vrai problème c'est quand l'ordre des vertices change entre deux imports du même mesh: techniquement différent mais visuellement identique. Ça a pris quelques itérations pour avoir un diff qui sort juste les vraies différences. C'est un rabbit hole tsu.
