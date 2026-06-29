---
title: Tester son GPU setup après chaque update
summary: Après n'importe quel update qui touche au driver AMD ou Ollama, lancer un quick inference test pis vérifier rocm-smi devrait être un réflexe automatique.
type: lesson
links:
  - "[[rocm-smi-verifier-l-usage]]"
  - "[[detecter-si-ollama-run-sur]]"
  - "[[update-ollama-sans-peter-son]]"
  - "[[frametime-comme-preuve-que-le]]"
---
ollama run llama3:8b 'write a haiku' pis watch -n 0.5 rocm-smi dans un autre terminal — si le GPU use spike durant la génération, t'es bon. Si ça bouge pas, quelque chose a changé. Ça prend 30 secondes et ça évite de découvrir trois jours plus tard que t'as tourné sur CPU sans le savoir. Fais-toi un alias pour ça.
