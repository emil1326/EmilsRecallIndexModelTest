---
title: Undo.RecordObject avant toute modification editor
summary: Toujours appeler Undo.RecordObject juste avant de modifier un objet dans un editor tool — sinon Ctrl+Z marche pas et les users vont haïr ton outil.
type: reference
links:
  - "[[beginchangecheck-pattern-pour-eviter-dirty]]"
  - "[[prefab-instances-pis-serializedproperty-le]]"
  - "[[aac-applicator-le-probleme-que]]"
  - "[[feature-locker-ne-d-un]]"
---
C'est le genre de chose qu'on oublie quand on prototype vite pis qui revient nous hanter. Si ton tool modifie des composants sans enregistrer l'undo, les users peuvent pas revenir en arrière pis ça crée de la méfiance envers l'outil. Dans EmilsWork tous les applicators ont leur Undo.RecordObject — c'est non-négociable.
