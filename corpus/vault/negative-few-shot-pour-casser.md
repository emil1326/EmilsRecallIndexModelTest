---
title: Negative Few-Shot Pour Casser Pattern Indésirable
summary: Inclure des exemples négatifs labelés explicitement dans le few-shot prompt est parfois plus efficace qu'ajouter des exemples positifs pour corriger un pattern récurrent.
type: lesson
links:
  - "[[few-shot-ordering-exemples-recents]]"
  - "[[few-shot-trois-a-cinq]]"
  - "[[franglais-prompt-output-franglais-garanti]]"
  - "[[persona-system-prompt-stay-in]]"
  - "[[zero-shot-simple-few-shot]]"
---
Si le model insiste à répondre d'une façon que tu veux pas — trop formel, trop long, mauvaise structure — des contre-exemples explicites ("❌ PAS ça: ...") peuvent reset le behavior plus vite que 3 exemples positifs supplémentaires. C'est contre-intuitif mais des fois montrer ce qu'il faut éviter est plus clair que montrer ce qu'il faut faire. À utiliser avec parcimonie parce que trop de négatifs dans le prompt confuse le model smh.
