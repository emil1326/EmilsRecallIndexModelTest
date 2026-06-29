---
title: Prefab instances pis SerializedProperty: le piège
summary: Modifier une prefab instance via SerializedProperty sans checker si c'en est une peut silently casser le lien avec le prefab parent — PrefabUtility.IsPartOfPrefabInstance() en premier.
type: lesson
links:
  - "[[serializedproperty-path-syntax-pour-nested]]"
  - "[[undo-recordobject-avant-toute-modification]]"
  - "[[aac-applicator-le-probleme-que]]"
  - "[[beginchangecheck-pattern-pour-eviter-dirty]]"
---
Si tu modify via SerializedObject directement sur une instance sans passer par les APIs prefab, tu risques de créer des overrides accidentelles ou de casser la connexion au parent. PrefabUtility.IsPartOfPrefabInstance() avant de toucher quoi que ce soit, c'est le réflexe à avoir. Ça m'a coûté un prefab entier à re-setup une fois — je vais pas oublier ça.
