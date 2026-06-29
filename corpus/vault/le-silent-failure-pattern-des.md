---
title: Le silent failure pattern des AI tools
summary: Beaucoup d'outils AI comme Ollama dégradent gracefully vers le CPU sans t'alerter — c'est pratique pour l'UX mais catastrophique pour debugger tes perfs.
type: lesson
links:
  - "[[ollama-fallback-cpu-silencieux-danger]]"
  - "[[detecter-si-ollama-run-sur]]"
  - "[[rocm-smi-verifier-l-usage]]"
  - "[[le-cout-reel-du-fallback]]"
---
Le design choice est genre 'au moins ça marche', mais du point de vue dev c'est frustrant parce que tu sais jamais si t'es dans le happy path ou le fallback path. Ollama, PyTorch, même des jeux avec Vulkan — tous peuvent silencieusement drop down vers une implem moins performante. La leçon: toujours vérifier avec un outil externe genre rocm-smi, pas juste feel-based.
