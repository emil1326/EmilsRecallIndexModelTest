---
title: Pseudo-random vs truly random: pas la même affaire
summary: Les PRNGs sont des formules mathématiques déterministes, pas du vrai hasard; pour du truly random faut de l'entropie physique externe.
type: lesson
links:
  - "[[le-rng-qui-a-failed]]"
  - "[[l-entropie-hardware-comme-vrai]]"
  - "[[la-failure-du-rng-comme]]"
  - "[[builder-une-image-class-from]]"
---
Un PRNG c'est juste une formule mathématique déterministe qui a l'air aléatoire si tu connais pas le seed de départ. Genre Math.random() c'est prévisible si tu sais comment ça marche en dessous. Moi je voulais du random qui dépend pas d'une formule, qui vient de quelque chose de physiquement imprévisible. Spoiler: c'est pas un truc que tu whip up en une soirée.
