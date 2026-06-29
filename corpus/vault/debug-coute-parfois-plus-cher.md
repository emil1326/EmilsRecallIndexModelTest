---
title: Debug coûte parfois plus cher que réécrire
summary: Sur du code legacy opaque, évaluer si réécrire la section serait plus rapide que continuer à debug est une décision d'ingénierie complètement valide.
type: journal
links:
  - "[[savoir-quand-drop-le-debug]]"
  - "[[debug-fatigue-tourner-en-rond]]"
  - "[[le-repro-minimal-first-thing]]"
  - "[[symptome-vs-cause-racine-pas]]"
---
C'est tabou de dire ça mais c'est réel. Si tu es à 3 heures de debug sur un module de 200 lignes qui a pas de tests et que personne comprend plus, le ROI de comprendre ce code vs juste le réécrire proprement peut basculer. Faut juste être honnête avec soi-même pis pas utiliser ça comme excuse pour éviter la vraie work.
