---
title: Underage detection: aucun signal magique
summary: Vérifier si un user est underage c'est flou — VRChat expose un flag d'âge mais c'est self-reported, donc le feature checker doit traiter l'incertitude comme un risk à mitiger.
type: lesson
links:
  - "[[feature-checker-gate-les-toggles]]"
  - "[[false-positive-underage-on-erre]]"
  - "[[trust-hierarchy-instance-type-prime]]"
  - "[[la-logique-de-gate-fallback]]"
---
Y'a pas de vrai vérification d'âge dans VRChat, le flag underage c'est juste ce que l'user a rentré à l'inscription. Donc le feature checker part du principe que si le flag dit underage, c'est underage, point. Errer du côté safe même si c'est potentiellement faux, tsu.
