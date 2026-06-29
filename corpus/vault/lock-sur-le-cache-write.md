---
title: Lock sur le cache write pour éviter race conditions
summary: Sans lock sur les écritures cache, deux workers qui analysent le même fichier en parallèle peuvent corrompre l'entrée — file lock ou mutex selon le contexte, c'est non-négociable.
type: reference
links:
  - "[[rollback-automatique-si-cache-corrompu]]"
  - "[[serialisation-cache-json-lisible-vs]]"
  - "[[versioning-du-cache-schema-sinon]]"
  - "[[incremental-analysis-est-toujours-full]]"
  - "[[les-coroutines-unity-le-overhead]]"
---
Le pattern classique c'est read-check-write sans lock, pis tu te retrouves avec deux analyses qui écrivent en même temps et une entrée cache à moitié écrite. Sur un outil single-threaded c'est moins un enjeu, mais dès que t'as du parallel processing, le lock devient critique. Préfère un write-then-atomic-rename plutôt qu'écrire directement dans le fichier final.
