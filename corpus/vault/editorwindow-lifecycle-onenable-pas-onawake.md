---
title: EditorWindow lifecycle: OnEnable pas OnAwake
summary: Dans Unity editor, OnEnable se call à chaque reload de scripts ou recompile — c'est là qu'on initialize les SerializedObjects, pas dans le constructeur.
type: lesson
links:
  - "[[serializedproperty-path-syntax-pour-nested]]"
  - "[[beginchangecheck-pattern-pour-eviter-dirty]]"
  - "[[scriptableobject-comme-backend-pour-editor]]"
  - "[[emilswork-suite-de-tools-modulaires]]"
---
Tsa, j'ai passé une heure à debug pourquoi mes références se perdaient après une recompile — c'est parce que j'initializais dans le constructeur comme un cave. OnEnable c'est le vrai entry point pour les EditorWindows, pis faut penser à cleanup dans OnDisable si t'as des callbacks enregistrés. Le lifecycle Unity editor c'est vraiment pas le même que le runtime.
