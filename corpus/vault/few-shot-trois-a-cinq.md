---
title: Few-Shot Trois À Cinq Exemples Sweet Spot
summary: Trois à cinq exemples few-shot c'est généralement optimal — en dessous c'est trop ambiguë, au-dessus ça eat du context inutilement sans améliorer le behavior.
type: reference
links:
  - "[[few-shot-ordering-exemples-recents]]"
  - "[[negative-few-shot-pour-casser]]"
  - "[[zero-shot-simple-few-shot]]"
  - "[[json-schema-system-exemple-user]]"
  - "[[context-window-compter-tokens-avant]]"
---
Un seul exemple c'est souvent insuffisant — le model peut pas vraiment inférer le pattern de façon reliée. Dix exemples c'est du gaspillage de context window et ça peut même confuse le model si les exemples ont de la variance entre eux. Si tu trouves que 5 exemples suffisent pas, le problème c'est probablement la qualité ou la consistance des exemples, pas la quantité — checke ça en premier.
