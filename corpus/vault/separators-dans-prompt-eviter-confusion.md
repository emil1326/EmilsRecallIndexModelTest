---
title: Separators Dans Prompt Éviter Confusion Contexte
summary: Utiliser des séparateurs clairs entre context, exemples et task évite que le model mélange les sections et suive des instructions au mauvais endroit du prompt.
type: reference
links:
  - "[[xml-tags-pour-delimiter-sections]]"
  - "[[instruction-fin-de-prompt-meilleur]]"
  - "[[system-prompt-sweet-spot-cinq]]"
  - "[[json-schema-system-exemple-user]]"
  - "[[prompt-injection-trust-jamais-l]]"
---
Un prompt flat sans structure c'est une recipe pour que le model "perde" des sections ou applique des instructions à la mauvaise partie. Les séparateurs visuels — triple dash, ###, ou XML tags — signalent au model les frontières entre les sections. Sur les longs prompts surtout, ça fait une différence notable dans le comportement. C'est du basic mais beaucoup de prompts en prod ont pas ça pis ça paraît dans les outputs.
