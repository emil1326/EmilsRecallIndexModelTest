---
title: Reasoning Budget Coût Élevé Gain Marginal
summary: Au-delà d'un certain budget de reasoning tokens, le gain de qualité sur les reasoning models devient marginal pis le coût explose de façon vraiment non-linéaire.
type: lesson
links:
  - "[[think-false-reasoning-models-reponse]]"
  - "[[think-extended-pour-maths-raisonnement]]"
  - "[[context-window-compter-tokens-avant]]"
  - "[[max-tokens-strict-controler-output]]"
  - "[[chain-of-thought-sans-extended]]"
---
Les reasoning models facturent les thinking tokens au même taux que les output tokens, et ces tokens peuvent s'accumuler vite. J'ai vu des runs où le model a spend 8000 tokens de reasoning pour un output de 200 tokens — pour une task qui needed probablement 500 tokens de thinking max. Setter un thinking_budget raisonnable selon la complexité évite les factures surprises. Y'a pas de corrélation linéaire entre thinking tokens et qualité, c'est plate tbh.
