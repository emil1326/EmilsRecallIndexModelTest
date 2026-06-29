---
title: Handles.BeginGUI pour mixer 3D pis 2D SceneView
summary: Handles.BeginGUI/EndGUI dans OnSceneGUI permet de draw du GUI 2D overlay dans la SceneView — utile pour labels, boutons, infos contextuelles en world space.
type: reference
links:
  - "[[onscenegui-pis-les-handles-pour]]"
  - "[[pourquoi-imgui-reste-le-choix]]"
  - "[[customeditor-vs-editorwindow-quand-choisir]]"
  - "[[emilswork-suite-de-tools-modulaires]]"
  - "[[depth-prepass-quand-ca-vaut]]"
---
C'est comme un petit HUD dans ta SceneView — t'ouvres le bloc Handles.BeginGUI, tu draw tes GUILayout calls normaux, t'as un panel 2D qui vit dans la vue 3D. Le coordinate system est en screen pixels depuis le coin top-left de la SceneView. Pour le 3D GUI dans EmilsWork ça a vraiment changé comment je pense les outils de placement.
