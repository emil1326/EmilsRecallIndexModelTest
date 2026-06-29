---
title: Logger les timestamps pour les bugs intermittents
summary: Pour les bugs intermittents, des timestamps précis dans les logs permettent de corréler avec d'autres événements système pis de trouver le pattern caché.
type: reference
links:
  - "[[race-condition-impossible-a-repro]]"
  - "[[l-heisenbug-qui-disparait-quand]]"
  - "[[log-quality-over-quantity-tse]]"
  - "[[un-log-sans-contexte-est]]"
---
Un bug qui arrive 'des fois' a souvent un pattern caché — toutes les X secondes, quand un autre thread fait quelque chose, quand la mémoire atteint un threshold. Sans timestamps dans les logs, t'as aucun moyen de voir ces patterns. Ça change tout, vraiment.
