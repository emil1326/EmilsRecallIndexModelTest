---
title: Isoler système vs app avant tout
summary: Avant de debug ton code, valider que c'est pas l'OS, le driver ou la lib externe qui cause le problème sauve des heures de rabbit hole.
type: lesson
links:
  - "[[valider-l-environnement-avant-de]]"
  - "[[le-bug-est-parfois-dans]]"
  - "[[le-repro-minimal-first-thing]]"
  - "[[symptome-vs-cause-racine-pas]]"
---
J'ai déjà passé deux heures à debug un soi-disant bug dans mon shader pipeline qui était en fait un driver GPU outdated. C'est humiliant mais ça arrive. Le quick check: est-ce que le même comportement arrive sur une autre machine ou avec une version différente de la dépendance? Si oui, c'est probablement pas toi.
