---
title: State sync: timing entre world join et avatar load
summary: Y'a un edge case timing: le world join event et l'avatar load sont pas synchrones, ce qui cause une brief window où le toggle est pas gaté.
type: lesson
links:
  - "[[osc-app-le-middleware-local]]"
  - "[[osc-le-seul-bridge-temps]]"
  - "[[vrchat-api-instance-type-source]]"
  - "[[api-rate-limiting-sur-les]]"
---
Quand le user join un world, VRChat charge l'avatar en parallèle — si l'OSC app réagit au world join event et envoie le gate message avant que l'avatar soit fully loaded, le message se perd dans le vide. Faut soit retry avec un delay, soit écouter un avatar-loaded event. Pas super documenté.
