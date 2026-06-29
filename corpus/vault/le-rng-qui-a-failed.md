---
title: Le RNG qui a failed faute d'entropie réelle
summary: J'ai essayé de builder un truly random number generator et ça a pas marché parce que l'entropie réelle c'est un beast à capturer.
type: journal
links:
  - "[[pseudo-random-vs-truly-random]]"
  - "[[l-entropie-hardware-comme-vrai]]"
  - "[[la-failure-du-rng-comme]]"
  - "[[boredom-vers-rabbit-hole-le]]"
  - "[[un-projet-ne-d-un]]"
---
J'ai décidé un jour de builder un truly random number generator, pas un PRNG, un VRAI. Ça a pas marché. Le problème c'est que sur un ordinateur classique, t'as pas accès à de l'entropie réelle juste comme ça, faut aller la chercher ailleurs pis c'est pas simple du tout. J'ai galéré un bon moment là-dessus, pis j'ai abandonné. Mais au moins j'avais appris pourquoi c'est hard, tsu.
