---
title: Budget Réaliste: moins de 24 Draw Calls
summary: Viser moins de 24 draw calls par avatar est un target communautaire raisonnable; au-delà, le coût collectif dans une instance peuplée commence à dégringoler.
type: reference
links:
  - "[[material-slots-brisent-le-gpu]]"
  - "[[atlas-texture-reduit-draw-calls]]"
  - "[[renderer-count-dans-le-perf]]"
  - "[[static-batching-marche-pas-sur]]"
---
24 draw calls c'est pas un chiffre officiel VRChat, c'est un best practice qui circule dans la communauté d'optimisation. En dessous de ça, ton avatar est relativement safe même dans des instances à 40 personnes. Au-dessus, ça dépend — 30 draw calls bien optimisés peuvent valoir mieux que 20 draw calls avec des shaders ultra-lourds, tsé.
