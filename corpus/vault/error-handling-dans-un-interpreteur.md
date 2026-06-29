---
title: Error handling dans un interpréteur naïf
summary: Un interpréteur naïf sans error recovery, c'est soit ça marche, soit ça crash brutalement — instructif pour apprendre, mais le debugging devient vite un enfer.
type: lesson
links:
  - "[[l-interpreteur-custom-architecture-de]]"
  - "[[lexer-first-parser-after-toujours]]"
  - "[[grammar-design-pour-un-langage]]"
  - "[[le-moment-ou-l-interpreteur]]"
---
Mon evaluator throwait juste des JS errors quand quelque chose allait mal. Pas de line numbers, pas de message humain. Genre tu catches ça dans une try/catch pis tu printes le message... qui est souvent garbage. C'est correct pour apprendre la mécanique de base, mais dès que tu veux vraiment utiliser ton langage, ça devient douloureux.
