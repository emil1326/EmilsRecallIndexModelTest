---
title: Types de params OSC VRChat: float, bool, int
summary: VRChat supporte trois types de params via OSC: float (0.0–1.0), bool (true/false), et int (0–255), pis chaque type mappe différemment selon l'avatar.
type: reference
links:
  - "[[float-params-osc-quantizes-en]]"
  - "[[avatar-parameters-le-namespace-avatar]]"
  - "[[format-d-un-message-osc]]"
  - "[[avatar-expressions-vs-custom-params]]"
---
Float va de 0.0 à 1.0 côté API mais est quantizé en 8-bit en interne pour le network sync. Bool c'est simple. Int peut aller de 0 à 255. La confusion entre float et int est la source de beaucoup de bugs silencieux — tsu si ton param répond pas ou donne des valeurs étranges, check le type en premier avant de chercher ailleurs.
