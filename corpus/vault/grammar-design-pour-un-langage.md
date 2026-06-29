---
title: Grammar design pour un langage custom
summary: Définir la grammaire d'un langage custom avant de coder — même juste informellement sur papier — sauve énormément de refactors douloureux dans le parser après.
type: lesson
links:
  - "[[l-interpreteur-custom-architecture-de]]"
  - "[[lexer-first-parser-after-toujours]]"
  - "[[parsing-expressions-recursion-descent-marche]]"
  - "[[error-handling-dans-un-interpreteur]]"
---
Mon langage avait des statements simples: assignments, if/else, while loops, print. Rien de crazy. Mais même avec ça, si t'as pas pensé à la précédence des opérateurs d'avance, ton parser va pas être heureux. BNF ou même juste un pseudocode rough, ça force à réfléchir les edge cases avant.
