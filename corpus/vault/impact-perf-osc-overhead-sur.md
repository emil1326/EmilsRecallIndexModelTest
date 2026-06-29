---
title: Impact perf — OSC overhead sur le framerate VRChat
summary: L'overhead OSC sur le framerate VRChat est négligeable en pratique — c'est du UDP local sur loopback, c'est l'animator et les shaders qui kill ta perf, pas ça.
type: lesson
links:
  - "[[latence-osc-en-dessous-de]]"
  - "[[rate-limiting-osc-vrchat-throttle]]"
  - "[[udp-fire-and-forget-pas]]"
  - "[[osc-dans-vrchat-protocole-de]]"
---
OSC roule sur loopback UDP, donc y'a virtuellement zéro overhead réseau. Le CPU que ça consomme sur l'app desktop c'est négligeable. La vraie perf concern dans VRChat c'est l'animator complexity, le shader compile, les audio sources — pas le OSC. Soyons honnêtes, si ton VRChat lag c'est pas la faute à OSC, arrête de chercher là.
