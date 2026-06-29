---
title: System Prompt Sweet Spot Cinq Cents Tokens
summary: Un system prompt entre 300 et 600 tokens c'est le sweet spot: assez précis pour contraindre le model sans diluer les instructions critiques dans du verbose.
type: reference
links:
  - "[[system-prompt-loi-du-monde]]"
  - "[[context-window-compter-tokens-avant]]"
  - "[[instruction-fin-de-prompt-meilleur]]"
  - "[[system-prompt-versioning-comme-du]]"
  - "[[separators-dans-prompt-eviter-confusion]]"
---
Passé ~800 tokens dans le system prompt, les instructions en début ou en fin du block perdent du recall sur certains modèles — le "lost in the middle" problem s'applique au system prompt lui-même, pas juste au context. Si ton system prompt est un roman, le model va skip des chunks entiers. Garde ça dense et opinionated, pas verbeux.
