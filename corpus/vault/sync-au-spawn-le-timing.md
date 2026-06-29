---
title: Sync au spawn — le timing du premier message
summary: Au spawn ou rejoin, VRChat prend quelques secondes avant d'accepter des messages OSC — envoyer trop tôt cause des drops silencieux, faut attendre l'avatar load complet.
type: lesson
links:
  - "[[avatar-swap-reset-tous-les]]"
  - "[[udp-fire-and-forget-pas]]"
  - "[[enable-osc-dans-vrchat-settings]]"
  - "[[config-json-osc-par-avatar]]"
---
J'ai eu ce bug plusieurs fois — j'envoyais des params OSC dès que mon app détectait que VRChat était ouvert, mais les premiers messages disparaissaient. VRChat prend quelques secondes après le spawn pour que l'avatar soit fully loaded et que les params soient prêts à recevoir. Un delay de 2-3 secondes après la détection du launch règle le problème pour l'instant, c'est pas élégant mais ça fit.
