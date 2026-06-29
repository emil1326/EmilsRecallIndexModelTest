---
title: daemon tourne en background process
summary: Le retrieval daemon tourne comme processus background avec une socket ou pipe IPC — les queries arrivent, il répond, zéro cold start à chaque appel contrairement à un script one-shot.
type: reference
links:
  - "[[onnx-runtime-pour-embedding-rapide]]"
  - "[[embedding-caching-pour-eviter-recalcul]]"
  - "[[lazy-rebuild-on-demand-vs]]"
  - "[[retrieval-pipeline-l-ordre-des]]"
---
Un script one-shot qui load le modèle à chaque query c'est nul — le cold start de e5-small même en ONNX c'est quelques secondes. Daemon persistant = modèle loadé une fois en mémoire, queries servies en millisecondes après. IPC simple via stdin/stdout ou un local socket Unix-style.
