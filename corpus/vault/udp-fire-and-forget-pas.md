---
title: UDP fire-and-forget — pas de guarantee de delivery
summary: OSC roule sur UDP donc tes messages peuvent drop silencieusement sous heavy load ou port conflict, pis VRChat va juste ignorer le paquet perdu, zéro feedback.
type: lesson
links:
  - "[[latence-osc-en-dessous-de]]"
  - "[[port-deja-occupe-erreur-silencieuse]]"
  - "[[rate-limiting-osc-vrchat-throttle]]"
  - "[[sync-au-spawn-le-timing]]"
---
UDP c'est fire-and-forget — tu envoies, tu pries, le paquet arrive ou pas. Sous charge ou avec des port conflicts, des messages peuvent disparaître sans aucun avertissement ni erreur côté code. C'est pour ça que l'approche 'envoyer seulement les changements d'état' est plus safe que du polling continu — si un paquet drop, le prochain changement le corrige de toute façon.
