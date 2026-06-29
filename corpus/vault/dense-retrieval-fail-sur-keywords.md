---
title: dense retrieval fail sur keywords exacts
summary: Le modèle dense tend à rater les requêtes ultra-spécifiques — noms de fonctions, numéros de version, acronymes — parce qu'il généralise sémantiquement au lieu de matcher exact.
type: lesson
links:
  - "[[bm25-still-slaps-pour-keywords]]"
  - "[[hybrid-fusion-dense-plus-sparse]]"
  - "[[e5-small-choisi-pour-le]]"
  - "[[recall-k-vs-precision-trade]]"
---
J'ai vu e5 sortir un doc sur 'state machines en général' quand je cherchais un FSM précis avec un nom de classe spécifique. Ça fait mal. C'est pas un bug, c'est by design, le modèle compresse la sémantique. Pour ça, BM25 est juste meilleur.
