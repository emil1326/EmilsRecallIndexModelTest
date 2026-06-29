---
title: L'entropie hardware comme vrai source de random
summary: Du vrai aléatoire en programmation faut de l'entropie physique, genre le bruit thermique d'un CPU ou des mouvements de souris, pas juste une formule mathématique.
type: reference
links:
  - "[[le-rng-qui-a-failed]]"
  - "[[pseudo-random-vs-truly-random]]"
  - "[[la-failure-du-rng-comme]]"
---
Pour du vrai aléatoire, les OS collectent de l'entropie hardware en background: mouvements de souris, timing du clavier, disk I/O, bruit thermique. Tout ça va dans un entropy pool que les programmes peuvent tapper. C'est pour ça que /dev/random existe sur Linux. Fetcher ça manuellement dans un programme basic c'est pas trivial, pis c'est exactement là que j'ai flopped.
