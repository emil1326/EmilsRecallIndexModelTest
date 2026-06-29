---
title: Context Window Compter Tokens Avant Tout
summary: Estimer le token count avant de whip up un prompt complexe évite les surprises de truncation ou de coût excessif qui arrivent toujours au pire moment en prod.
type: reference
links:
  - "[[system-prompt-sweet-spot-cinq]]"
  - "[[think-false-reasoning-models-reponse]]"
  - "[[max-tokens-strict-controler-output]]"
  - "[[reasoning-budget-cout-eleve-gain]]"
  - "[[json-schema-system-exemple-user]]"
---
Tokenizer les inputs au runtime c'est une étape que beaucoup de gens skip jusqu'à ce que leur app crash parce que le context est full. La règle rough: 1 token ≈ 4 caractères en anglais, un peu moins en français. Si ton prompt + context + expected output dépasse la context window, le model va truncate l'input de façon pas nécessairement intelligente. Pis ça coûte cher les gros contexts — autant le savoir avant le premier appel en prod.
