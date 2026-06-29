---
title: Ollama logs: où chercher le GPU failure
summary: Les logs Ollama au démarrage (journalctl ou stdout) indiquent quel device a été détecté — cherche 'GPU' ou 'compute' pour confirmer que ROCm a bien pickup ton chip.
type: reference
links:
  - "[[detecter-si-ollama-run-sur]]"
  - "[[le-silent-failure-pattern-des]]"
  - "[[variables-d-env-rocm-pour]]"
  - "[[ollama-fallback-cpu-silencieux-danger]]"
---
journalctl -u ollama -f ou juste ollama serve en foreground — t'as les logs direct dans ton terminal. Les lignes importantes sont autour de l'initialisation, genre 'found 1 compatible GPU' ou au contraire absence totale de mention GPU. Quand Ollama fallback sur CPU silencieusement, les logs sont quand même là pour te le dire si tu sais où regarder.
