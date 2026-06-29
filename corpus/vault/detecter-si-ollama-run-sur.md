---
title: Détecter si Ollama run sur GPU ou CPU
summary: Pour savoir si Ollama use vraiment le GPU, faut checker rocm-smi en live ou lire les logs au démarrage du service, pas attendre la lenteur.
type: reference
links:
  - "[[rocm-smi-verifier-l-usage]]"
  - "[[ollama-fallback-cpu-silencieux-danger]]"
  - "[[ollama-logs-ou-chercher-le]]"
  - "[[rocm-6-4-2-pas]]"
---
La commande watch -n 0.5 rocm-smi te montre si le GPU est actif pendant une inférence. Aussi, les logs Ollama au startup mentionnent quel device il a détecté — si tu vois pas ton GPU là, c'est red flag immediate. Deux façons de voir le même problème, mais la deuxième est plus pratique pour un diagnostic rapide.
