---
title: Hard-coded vs data-driven config, quand basculer
summary: Hardcoder au début accélère l'itération, mais dès que la même valeur apparaît à deux endroits, c'est le signal de basculer vers data-driven.
type: lesson
links:
  - "[[custom-editor-window-vs-inspector]]"
  - "[[scriptableobject-vs-monobehaviour-le-vrai]]"
  - "[[quand-abstraire-vs-quand-hardcoder]]"
  - "[[build-by-need-pas-by]]"
---
La règle des deux occurences: si je me retrouve à hardcoder le même magic number à deux places, je le mets dans un config. C'est pas une règle de propreté, c'est une règle de survie pour éviter les bugs de désync. Le data-driven prématuré c'est du overhead pour rien — genre avoir un JSON pour une valeur qui changera jamais. Le sweet spot c'est: hardcode d'abord, extrait quand ça fait mal.
