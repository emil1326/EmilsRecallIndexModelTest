---
title: Choisir le bon modèle Ollama
summary: Pour Ollama local, le choix du modèle dépend du VRAM disponible, des modèles trop gros fittent pas en mémoire GPU et tombent sur le CPU.
type: reference
links:
  - "[[ollama-tourne-local-sur-la]]"
  - "[[gpu-amd-pour-l-inference]]"
  - "[[rocm-sur-amd-la-galere]]"
  - "[[ollama-offline-aucune-donnee-qui]]"
---
Les modèles 7B quantisés en Q4 ou Q5 sont généralement le sweet spot pour un GPU mid-range, assez capable, assez rapide. Un modèle qui tombe sur le CPU c'est dix fois plus lent, c'est pas viable pour du usage quotidien. Faut checker la taille du `.gguf` avant de pull pour pas avoir de mauvaise surprise.
