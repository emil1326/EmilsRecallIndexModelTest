---
title: Parsing expressions: recursion descent marche
summary: Recursive descent parsing, c'est la meilleure approche pour un interpréteur hobby — chaque règle de grammaire devient une fonction, c'est lisible pis ça just marche.
type: lesson
links:
  - "[[lexer-first-parser-after-toujours]]"
  - "[[grammar-design-pour-un-langage]]"
  - "[[l-interpreteur-custom-architecture-de]]"
  - "[[le-moment-ou-l-interpreteur]]"
  - "[[error-handling-dans-un-interpreteur]]"
---
J'ai pas eu à comprendre toute la théorie des compilateurs pour faire marcher ça. Tu lis sur recursive descent, t'écris `parseExpression()`, `parseTerm()`, `parseFactor()`, pis ça handle la précédence naturellement via la call stack. Le Aha moment quand t'as pigé ça, c'est clean.
