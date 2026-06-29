---
title: File-based vs database pour persister l'état
summary: Les fichiers flat (JSON, binary) sont plus simples à debugger et à versionner, mais une database gagne quand tu as des queries ou des relations complexes.
type: reference
links:
  - "[[custom-parser-vs-json-yaml]]"
  - "[[hard-coded-vs-data-driven]]"
  - "[[cache-invalidation-strategy-le-probleme]]"
  - "[[build-by-need-pas-by]]"
---
Pour les tools d'un seul dev, les fichiers JSON c'est souvent la meilleure option — tu peux les ouvrir dans un éditeur, les committer, les diff. Dès que tu te retrouves à faire des "queries" avec du LINQ sur un JSON chargé en mémoire, c'est le signal pour switcher. SQLite c'est le sweet spot entre les deux — file-based mais avec des vraies queries. J'ai over-engineered une fois avec PostgreSQL pour un tool solo, c'était clairement overkill smh.
