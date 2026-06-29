---
title: Chain-of-Thought Sans Extended Thinking
summary: Ajouter "pense étape par étape" dans le prompt trigger le chain-of-thought sur les non-reasoning models sans avoir besoin du mode extended thinking payant.
type: lesson
links:
  - "[[think-false-reasoning-models-reponse]]"
  - "[[think-extended-pour-maths-raisonnement]]"
  - "[[reasoning-budget-cout-eleve-gain]]"
  - "[[zero-shot-simple-few-shot]]"
  - "[[context-window-compter-tokens-avant]]"
---
Juste écrire "think step by step" ou "break this down" dans le user turn améliore souvent la qualité du raisonnement de façon significative — c'est gratuit en termes de feature, juste des tokens extra. C'est pas aussi puissant que le extended thinking d'un o1, mais pour 80% des tâches de raisonnement medium c'est sufficient. J'utilise ça avant d'upgrader au reasoning model pour voir si c'est nécessaire, pis souvent ça l'est pas.
