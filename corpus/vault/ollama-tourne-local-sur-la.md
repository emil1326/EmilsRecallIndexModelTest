---
title: Ollama tourne local sur la machine
summary: Emil roule Ollama localement pour accéder à des LLMs sans envoyer ses données dans le cloud, le GPU AMD s'occupe de l'inference.
type: user
links:
  - "[[gpu-amd-pour-l-inference]]"
  - "[[rocm-sur-amd-la-galere]]"
  - "[[choisir-le-bon-modele-ollama]]"
  - "[[ollama-offline-aucune-donnee-qui]]"
  - "[[windows-pour-dev-pas-parfait]]"
---
Ollama c'est le setup le plus simple pour rouler des modèles genre Mistral ou Llama localement, juste `ollama run` pis c'est parti. La vitesse dépend du VRAM du GPU et du quantization level du modèle choisi, faut trouver le bon balance. C'est pas aussi rapide que les API cloud mais privacy-wise c'est imbattable.
