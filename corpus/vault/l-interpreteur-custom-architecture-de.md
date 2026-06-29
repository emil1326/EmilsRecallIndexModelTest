---
title: L'interpréteur custom: architecture de base
summary: Un interpréteur walk-through simple comprend trois étapes: lexer (tokens), parser (AST), evaluator (exécution) — trivial à dire, moins trivial à debugger quand ça plante.
type: reference
links:
  - "[[lexer-first-parser-after-toujours]]"
  - "[[grammar-design-pour-un-langage]]"
  - "[[parsing-expressions-recursion-descent-marche]]"
  - "[[error-handling-dans-un-interpreteur]]"
  - "[[le-moment-ou-l-interpreteur]]"
---
Mon setup était simple: un lexer qui crache des tokens, un recursive descent parser qui build un AST, pis un evaluator qui walk l'arbre. Rien de fancy, pas de bytecode, pas de compilation. C'est le genre d'archi que tu comprends vraiment une fois que t'as fait, pis after that les "vrais" langages font way plus de sens.
