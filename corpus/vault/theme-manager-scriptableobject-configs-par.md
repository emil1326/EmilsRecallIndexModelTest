---
title: Theme manager: ScriptableObject configs par projet
summary: Le theme manager EmilsWork stocke des palettes couleur par projet dans des ScriptableObjects — versionnable git, partageable en équipe, pas perdu comme un EditorPref machine-wide.
type: reference
links:
  - "[[scriptableobject-comme-backend-pour-editor]]"
  - "[[editorprefs-global-pas-project-scoped]]"
  - "[[textmesh-wrapper-pourquoi-wrapper-tmp]]"
  - "[[emilswork-suite-de-tools-modulaires]]"
---
Chaque projet VRChat a son aesthetic, pis gérer les couleurs des materials pis shaders à la main c'est error-prone. Le theme manager c'est un ScriptableObject avec les couleurs principales du projet pis des Apply() par catégorie. Sauvé dans le repo git donc moi plus tard (ou l'équipe) retrouve les mêmes themes sans repartir de zéro.
