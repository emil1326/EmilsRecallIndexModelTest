---
title: Latence OSC — en-dessous de 50ms en local
summary: La latence OSC de ton app vers VRChat est genre 5–20ms en local, mais la latence perçue in-game dépend surtout du animator update rate, pas du OSC.
type: lesson
links:
  - "[[udp-fire-and-forget-pas]]"
  - "[[impact-perf-osc-overhead-sur]]"
  - "[[rate-limiting-osc-vrchat-throttle]]"
  - "[[osc-dans-vrchat-protocole-de]]"
---
En pratique OSC lui-même ajoute quelques ms sur loopback, c'est rien. La latence que tu perçois in-game c'est surtout l'animator update qui se fait à un rate fixe et pas à chaque frame. Donc même si tu envoies un message instantanément, le param visuellement bouge pas plus vite que le cycle d'update de l'animator — c'est un problème de game loop, pas de networking.
