---
title: Cache warming au startup, nice to have
summary: Pre-remplir le cache au démarrage de l'outil sur les fichiers les plus utilisés évite les misses coûteux au début, mais c'est du polish — implémente ça en dernier.
type: lesson
links:
  - "[[le-lazy-rebuild-se-declenche]]"
  - "[[hot-path-analyser-les-fichiers]]"
  - "[[disk-vs-memory-cache-selon]]"
  - "[[incremental-analysis-est-toujours-full]]"
---
Le warming fait du sens si l'outil a une phase de startup claire comme un LSP server, où tu peux analyser les fichiers ouverts en background pendant que l'user setup son affaire. Pour un outil one-shot comme un linter CLI, le warming pre-run est inutile. Priorise le lazy rebuild correctement avant même de penser au warming.
