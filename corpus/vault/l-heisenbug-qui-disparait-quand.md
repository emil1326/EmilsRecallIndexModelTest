---
title: L'heisenbug qui disparaît quand tu regardes
summary: Certains bugs disparaissent quand on ajoute des logs ou qu'on attache un debugger — c'est souvent un timing issue masqué par l'outil lui-même.
type: reference
links:
  - "[[race-condition-impossible-a-repro]]"
  - "[[logger-les-timestamps-pour-les]]"
  - "[[log-quality-over-quantity-tse]]"
  - "[[isoler-systeme-vs-app-avant]]"
---
Le terme 'heisenbug' vient du principe d'Heisenberg: observer change le comportement. En pratique c'est souvent une race condition masquée par la latence du logging, ou un memory issue que le debugger alloue différemment. Si ton bug disparaît avec le debugger, suspect le timing immediately — c'est le signal classique.
