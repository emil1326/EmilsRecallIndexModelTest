---
title: Frametime comme preuve que le GPU travaille
summary: En inférence locale, un bon proxy pour savoir si le GPU est actif c'est de comparer les tokens par seconde — CPU c'est lent, GPU c'est notable.
type: lesson
links:
  - "[[rocm-smi-verifier-l-usage]]"
  - "[[detecter-si-ollama-run-sur]]"
  - "[[cpu-inference-lent-mais-au]]"
  - "[[ollama-fallback-cpu-silencieux-danger]]"
---
GPU sur Ollama tu peux voir genre 30-80+ tokens/sec selon le model, CPU ça traîne sous 5-10 t/s facilement. La différence est assez grosse pour être felt empiriquement. C'est pas aussi précis que rocm-smi mais c'est un gut-check rapide. Si ton llama3 génère du texte à la vitesse d'un humain qui tape lentement, y'a un problème.
