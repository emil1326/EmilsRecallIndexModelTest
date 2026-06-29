---
title: Trust hierarchy: instance type prime sur user age
summary: Quand les deux conditions entrent en jeu, l'instance type (public) overrides tout — même si aucun underage user est détecté, un public world gate quand même.
type: lesson
links:
  - "[[vrchat-api-instance-type-source]]"
  - "[[underage-detection-aucun-signal-magique]]"
  - "[[private-world-toggle-libre-peu]]"
  - "[[la-logique-de-gate-fallback]]"
  - "[[float-params-osc-quantizes-en]]"
---
C'est la règle la plus importante du feature checker: public world = gate, no exceptions. L'underage check ajoute juste une couche supplémentaire pour les edge cases en private. L'ordre de priorité c'était une décision design consciente pour garder la logique simple et pas full of edge cases.
