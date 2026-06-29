---
title: Pack Bool en Int économiser budget
summary: Remplacer plusieurs Bools mutuellement exclusifs par un seul Int peut simplifier la gestion; un Int gère jusqu'à 255 valeurs pour 8 bits, autant que 8 Bools séparés.
type: lesson
links:
  - "[[budget-parametres-vrchat-limite-256]]"
  - "[[bool-int-float-choisir-bon]]"
  - "[[synced-vs-unsynced-parametres-difference]]"
  - "[[osc-pour-controle-externe-parametres]]"
---
Si t'as genre 5 options mutuellement exclusives (outfit A/B/C/D/E), un Int 0-4 c'est plus clean que 5 Bools à 1 bit chacun — même coût de 8 bits mais un seul paramètre à gérer. Par contre si les options sont combinables (toggle A ET B simultanément), faut rester avec des Bools séparés. Pense à ta logique avant de pack.
