---
title: Unity side: integration point clean pour le créateur
summary: Le côté Unity du feature checker c'est pensé pour être propre et simple — le créateur doit pas comprendre l'archi backend pour setup son avatar avec le gate.
type: reference
links:
  - "[[archi-feature-checker-api-osc]]"
  - "[[website-dashboard-de-config-pour]]"
  - "[[lewd-toggle-c-est-quoi]]"
  - "[[osc-app-le-middleware-local]]"
---
L'idée c'est que le Unity package expose juste ce qu'il faut: un component à mettre sur l'avatar, quelques champs à remplir (quel parameter OSC correspond à quel toggle). Tout le reste est abstracted away. Branding EmilsWork sur le package, obviously.
