---
title: think=false Reasoning Models Réponse Rapide
summary: Désactiver le extended thinking sur les reasoning models quand la task est simple évite de payer cher en tokens pour du raisonnement complètement inutile.
type: lesson
links:
  - "[[think-extended-pour-maths-raisonnement]]"
  - "[[reasoning-budget-cout-eleve-gain]]"
  - "[[context-window-compter-tokens-avant]]"
  - "[[max-tokens-strict-controler-output]]"
  - "[[zero-shot-simple-few-shot]]"
---
Les reasoning models peuvent spend des milliers de tokens à "penser" avant de répondre — sur une task triviale c'est du cash jeté dans le vide, smh. Avec think=false ou en coupant le budget à 0, tu gardes la qualité du model sans le overhead de reasoning. J'utilise ça pour tout ce qui est classification, formatting, extraction simple. Garde think=extended pour les vraies puzzles.
