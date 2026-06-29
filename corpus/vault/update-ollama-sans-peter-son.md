---
title: Update Ollama sans péter son setup ROCm
summary: Updater Ollama sur Linux se fait proprement via curl install script — il replace le binaire mais garde les models et la config en place sans drama.
type: reference
links:
  - "[[ollama-0-30-11-fix]]"
  - "[[tester-son-gpu-setup-apres]]"
  - "[[quand-arreter-de-debug-et]]"
  - "[[ollama-logs-ou-chercher-le]]"
---
curl -fsSL https://ollama.com/install.sh | sh — le script détecte ton hardware, télécharge la bonne version avec le bon ROCm bundlé, et replace l'install sans toucher à ~/.ollama/models. Pas besoin de re-pull tous tes models. J'avais peur de tout péter en updatant mais ça s'est passé clean. Garde juste ton service arrêté pendant l'install.
