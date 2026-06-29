---
title: Append atomique au JSONL sans corruption
summary: Écrire dans un JSONL de façon atomique — une ligne complète par write suivi d'un flush — évite la corruption du fichier si le process crash mid-write.
type: reference
links:
  - "[[jsonl-le-format-de-base]]"
  - "[[streaming-jsonl-pour-gros-datasets]]"
  - "[[versionner-le-dataset-par-son]]"
  - "[[metadata-per-ligne-dans-le]]"
---
Le pattern safe c'est d'écrire la ligne complète + `\n` dans un seul `write()` call, jamais en plusieurs calls sans lock. Sur la plupart des OS, un `write()` de moins de PIPE_BUF bytes (4096 sur Linux) est atomique. Pour les pipelines multi-process qui écrivent dans le même fichier, faut soit un lock, soit des fichiers séparés par worker mergés à la fin. Un JSONL corrompu avec une ligne tronquée fait crasher ton loader à cet endroit précis — sympa pour débugger.
