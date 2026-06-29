---
title: Hot reload vs full rebuild, le vrai coût
summary: Le hot reload accélère l'itération mais introduit des états corrompus subtils qui sont souvent plus longs à debugger que le temps économisé.
type: lesson
links:
  - "[[lazy-rebuild-declenche-on-demand]]"
  - "[[cache-invalidation-strategy-le-probleme]]"
  - "[[sync-vs-async-dans-les]]"
  - "[[savoir-quand-killer-un-rabbit]]"
---
Quand le hot reload marche bien, c'est magique — tu changes un chiffre, tu vois le résultat direct. Mais dès que t'as du state qui persiste entre les reloads, tu peux te retrouver à debugger un comportement qui existe juste dans cette session particulière. J'ai appris à avoir un "full restart" shortcut rapide aussi pour reset quand quelque chose feel off. Le hot reload c'est un tool, pas un remplacement au full rebuild.
