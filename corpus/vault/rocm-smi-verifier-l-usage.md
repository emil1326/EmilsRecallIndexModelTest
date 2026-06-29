---
title: rocm-smi: vérifier l'usage GPU live
summary: rocm-smi est l'outil AMD équivalent à nvidia-smi pour monitorer l'usage GPU, la mémoire et la température en temps réel sous ROCm, utile pour diagnostiquer les fallbacks.
type: reference
links:
  - "[[detecter-si-ollama-run-sur]]"
  - "[[ollama-fallback-cpu-silencieux-danger]]"
  - "[[variables-d-env-rocm-pour]]"
  - "[[tester-son-gpu-setup-apres]]"
---
watch -n 0.5 rocm-smi te donne un refresh toutes les demi-secondes — pendant une inférence Ollama tu devrais voir GPU use grimper. Si ça bouge pas, ton model tourne sur CPU. Commande simple mais c'est souvent la première chose à check quand quelque chose feel lent. Garde ça dans ta toolbox AMD.
