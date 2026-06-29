---
title: ScriptableObject comme backend pour editor tools
summary: Utiliser des ScriptableObjects comme config backend pour les editor tools c'est bien mieux qu'EditorPrefs — sérialisé proprement, versionnable avec git, partageable dans l'équipe.
type: lesson
links:
  - "[[editorprefs-global-pas-project-scoped]]"
  - "[[theme-manager-scriptableobject-configs-par]]"
  - "[[editorwindow-lifecycle-onenable-pas-onawake]]"
  - "[[far-plan-emilswork-gros-tool]]"
  - "[[gpu-instancing-bon-mais-faut]]"
  - "[[overdraw-accumule-les-pixel-invocations]]"
---
Pour le theme manager dans EmilsWork j'ai switché d'EditorPrefs vers un ScriptableObject et c'est clairement la bonne call — les settings sont dans git pis les autres qui ouvrent le projet ont les mêmes configs. Le seul downside c'est de gérer le cas où l'asset existe pas encore, mais un find-or-create au OnEnable c'est trivial.
