---
title: ROCm sur AMD, la galère Windows
summary: ROCm, le stack GPU d'AMD pour le machine learning, est officiellement supporté que sur Linux, sur Windows c'est une vraie galère à setup.
type: lesson
links:
  - "[[ollama-tourne-local-sur-la]]"
  - "[[gpu-amd-pour-l-inference]]"
  - "[[choisir-le-bon-modele-ollama]]"
  - "[[windows-pour-dev-pas-parfait]]"
  - "[[ollama-offline-aucune-donnee-qui]]"
---
Ollama sur Windows avec AMD GPU passe par une implémentation Vulkan au lieu de ROCm propre, ça marche, mais c'est pas optimal. Si Emil avait un GPU NVIDIA, CUDA ferait ça sans douleur, mais bon, il a ce qu'il a. La morale: AMD GPU pour du ML local sur Windows c'est faisable mais faut pas s'attendre à du plug-and-play.
