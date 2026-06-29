---
title: Abstraction layers coûtent cher à changer
summary: Plus une abstraction est profonde dans l'architecture, plus le coût de la changer est élevé, les mauvaises abstractions basses sont les dettes les plus chères.
type: lesson
links:
  - "[[quand-abstraire-vs-quand-hardcoder]]"
  - "[[rebuild-from-scratch-vs-refactor]]"
  - "[[build-by-need-pas-by]]"
  - "[[premature-optimization-vs-good-enough]]"
---
Y'a une asymétrie cruelle: une abstraction haute (un wrapper, un helper) est facile à jeter. Une abstraction basse (le data model, le protocol de communication entre systèmes) devient une fondation que tout le reste assume. Changer ça plus tard c'est souvent un refactor de plusieurs jours. C'est pour ça que je rush moins sur les abstractions basses pis que je laisse le design émerger avec du vrai usage avant de setter les interfaces core.
