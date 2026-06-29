---
title: EditorPrefs: global, pas project-scoped
summary: EditorPrefs c'est machine-wide, pas project-scoped — des settings EmilsWork peuvent spiller entre projets si on préfixe pas les keys avec le nom du projet.
type: reference
links:
  - "[[scriptableobject-comme-backend-pour-editor]]"
  - "[[theme-manager-scriptableobject-configs-par]]"
  - "[[branding-emilswork-dans-chaque-fenetre]]"
  - "[[emilswork-suite-de-tools-modulaires]]"
---
J'avais des settings qui se mélangeaient entre projets différents parce que EditorPrefs c'est vraiment global à la machine, pas isolé par projet. Le workaround c'est de préfixer chaque key avec Application.productName, mais honnêtement pour n'importe quoi de non-trivial un ScriptableObject dans Assets c'est clairement mieux. C'est plate tbh mais c'est ça.
