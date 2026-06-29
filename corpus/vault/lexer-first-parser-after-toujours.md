---
title: Lexer first, parser after, toujours
summary: Dans un interpréteur custom, le lexer tokenize le texte brut pis le parser consomme ces tokens — l'ordre est pas négociable, même si c'est tentant.
type: lesson
links:
  - "[[l-interpreteur-custom-architecture-de]]"
  - "[[grammar-design-pour-un-langage]]"
  - "[[parsing-expressions-recursion-descent-marche]]"
  - "[[error-handling-dans-un-interpreteur]]"
  - "[[le-moment-ou-l-interpreteur]]"
  - "[[boredom-vers-rabbit-hole-le]]"
---
J'ai essayé une fois de parser directement le raw string sans tokenizer... tata. T'as pas de fun à debugger ça. Le lexer transforme `while x > 5` en tokens propres genre `[KEYWORD, IDENT, GT, NUMBER]`, pis là le parser a quelque chose de sensé à travailler avec. Deux passes séparées, ça change tout.
