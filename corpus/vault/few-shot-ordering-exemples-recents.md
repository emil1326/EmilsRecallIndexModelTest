---
title: Few-Shot Ordering Exemples Récents Win
summary: Dans un few-shot prompt, les exemples placés en fin juste avant la task ont plus d'influence sur l'output que ceux placés en début de context.
type: lesson
links:
  - "[[zero-shot-simple-few-shot]]"
  - "[[negative-few-shot-pour-casser]]"
  - "[[few-shot-trois-a-cinq]]"
  - "[[instruction-fin-de-prompt-meilleur]]"
  - "[[json-schema-system-exemple-user]]"
---
C'est lié au recency bias des LLMs — le dernier exemple vu avant de générer a plus de pull sur le comportement. Si t'as un exemple un peu weird que tu veux overrider, mets le bon pattern en dernier. Tsu, ça change le vibe de l'output de façon assez notable pour que tu changes ton ordre d'exemples intentionnellement.
