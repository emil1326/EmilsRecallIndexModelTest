---
title: Float params OSC quantizés en network sync
summary: Les float params VRChat sont quantizés 8-bit pour le network sync — ton app OSC envoie du float32 propre, mais les autres players voient des steps discrets de 1/255.
type: lesson
links:
  - "[[types-de-params-osc-vrchat]]"
  - "[[avatar-parameters-le-namespace-avatar]]"
  - "[[latence-osc-en-dessous-de]]"
  - "[[udp-fire-and-forget-pas]]"
---
Localement (sur ton propre client) les float params sont full precision, mais pour les autres joueurs dans la room c'est quantizé en 256 valeurs discrètes pour le network sync. Concrètement un pas de ~0.004. Pour la plupart des use cases visuels ça change rien, mais si tu fais du positional tracking ou quelque chose de continu et précis, c'est un détail à garder en tête.
