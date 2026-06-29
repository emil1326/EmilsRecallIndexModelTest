---
title: GPU AMD pour l'inference locale
summary: Emil utilise son GPU AMD pour accélérer l'inference Ollama, c'est fondamentalement plus rapide que le CPU pur, mais AMD demande plus de configuration que NVIDIA pour ça.
type: reference
links:
  - "[[ollama-tourne-local-sur-la]]"
  - "[[rocm-sur-amd-la-galere]]"
  - "[[choisir-le-bon-modele-ollama]]"
  - "[[ollama-offline-aucune-donnee-qui]]"
  - "[[windows-pour-dev-pas-parfait]]"
---
Le GPU AMD fait rouler les LLMs via Vulkan dans Ollama sur Windows, c'est pas aussi propre que CUDA mais ça accélère quand même significativement. Le VRAM est le vrai bottleneck: plus le modèle est gros, plus il risque de spiller sur le RAM système et tout ralentir drastiquement. Connaître le VRAM exact de son GPU c'est non-négociable pour choisir ses modèles.
