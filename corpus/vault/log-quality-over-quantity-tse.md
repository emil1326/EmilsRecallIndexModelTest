---
title: Log quality over quantity, tsé
summary: Avoir mille logs inutiles c'est pire qu'en avoir dix bons — un log utile dit QUOI, OÙ, pis dans quel état l'app était.
type: lesson
links:
  - "[[un-log-sans-contexte-est]]"
  - "[[logger-les-timestamps-pour-les]]"
  - "[[l-heisenbug-qui-disparait-quand]]"
  - "[[garder-un-journal-des-hypotheses]]"
---
J'ai déjà eu une codebase avec des console.log partout pis j'arrivais pas à trouver quoi que ce soit dans le noise. Un bon log c'est: contexte clair, valeur de la variable suspecte, pis l'état du système à ce moment-là. Le reste c'est du bruit qui cache l'information.
