---
title: Synced vs Unsynced paramètres différence clé
summary: Les paramètres synced sont visibles par les autres joueurs et consomment du budget; les unsynced sont local-only et gratuits en bits, mais invisibles au réseau.
type: lesson
links:
  - "[[budget-parametres-vrchat-limite-256]]"
  - "[[osc-pour-controle-externe-parametres]]"
  - "[[contact-receiver-toggle-sans-menu]]"
  - "[[mirror-test-local-remote-comportement]]"
  - "[[dxt-vs-astc-compression-texture]]"
---
Utilise des paramètres unsynced pour la logique interne pis les états intermédiaires que personne d'autre a besoin de voir. Les autres joueurs voient seulement ce qui est synced, donc un toggle visible par tous doit absolument être synced. La confusion entre les deux cause des bugs de sync vraiment hardcore à debug.
