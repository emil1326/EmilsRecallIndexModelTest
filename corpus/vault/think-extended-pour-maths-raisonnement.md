---
title: think=extended Pour Maths Raisonnement Complexe
summary: Le mode extended thinking est vraiment worth it uniquement pour les tâches où le raisonnement multi-étapes change vraiment le résultat: maths, code complexe, puzzles logiques.
type: lesson
links:
  - "[[think-false-reasoning-models-reponse]]"
  - "[[reasoning-budget-cout-eleve-gain]]"
  - "[[chain-of-thought-sans-extended]]"
  - "[[context-window-compter-tokens-avant]]"
  - "[[zero-shot-simple-few-shot]]"
---
J'ai testé think=extended sur des tasks de summarization, formatting, extraction — le delta de qualité vs think=false est quasi nul, mais le coût en tokens explose. Là où ça paie vraiment c'est les algorithmes complexes, le debugging multi-step, les proofs mathématiques. Tsu, le extended thinking c'est pas un "mode premium" universel — c'est un outil pour des reasoning tasks spécifiques. Budget tes tokens en conséquence.
