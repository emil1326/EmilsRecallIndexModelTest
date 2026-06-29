---
title: JSON Schema System Exemple User Turn
summary: Mettre le JSON schema dans le system prompt et les exemples concrets dans le user turn réduit la repetition de tokens et clarifie beaucoup le debugging en prod.
type: reference
links:
  - "[[json-force-avec-schema-inline]]"
  - "[[few-shot-ordering-exemples-recents]]"
  - "[[system-prompt-loi-du-monde]]"
  - "[[xml-tags-pour-delimiter-sections]]"
  - "[[zero-shot-simple-few-shot]]"
---
Pas besoin de repeater le schema à chaque user message s'il est stable — il va dans le system prompt une fois, fin. Les exemples concrets pour le few-shot vont dans le user turn parce que c'est là que le model les voit en contexte avec la vraie task. Ce split rend aussi le debugging plus simple: si le format est wrong, tu sais immédiatement où aller chercher. Genre, separation of concerns mais pour les prompts.
