---
title: XML Tags Pour Délimiter Sections Prompt
summary: Utiliser des XML tags comme instructions, examples, context pour séparer les sections d'un long prompt améliore le recall des instructions sur les Anthropic models.
type: reference
links:
  - "[[separators-dans-prompt-eviter-confusion]]"
  - "[[system-prompt-loi-du-monde]]"
  - "[[system-prompt-sweet-spot-cinq]]"
  - "[[json-schema-system-exemple-user]]"
  - "[[instruction-fin-de-prompt-meilleur]]"
---
Anthropic a clairement entraîné leurs modèles à respecter la structure XML dans les prompts — Claude suit les instructions dans `<instructions>` de façon plus fiable que dans un block de texte plat. C'est documenté dans leurs guides et c'est real en pratique. Pour les gros prompts multi-sections, les XML tags c'est presque mandatory pour que ça soit pas un chaos. OpenAI models sont moins sensibles à ça mais ça nuit pas.
