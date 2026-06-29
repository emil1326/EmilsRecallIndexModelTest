---
title: OnSceneGUI pis les Handles pour 3D GUI
summary: OnSceneGUI dans un CustomEditor draw des Handles directement dans la SceneView — le vrai entry point pour manipulation 3D custom sans passer par les Gizmos.
type: reference
links:
  - "[[handles-begingui-pour-mixer-3d]]"
  - "[[customeditor-vs-editorwindow-quand-choisir]]"
  - "[[pourquoi-imgui-reste-le-choix]]"
  - "[[emilswork-suite-de-tools-modulaires]]"
---
Pour le 3D GUI dans EmilsWork, OnSceneGUI c'est le entry point — tu overrides ça dans ton CustomEditor pis t'as accès aux Handles API pour des position handles, des arcs, des labels en world space. Le tricky c'est que ça require un CustomEditor attaché à un MonoBehaviour même si l'outil est conceptuellement standalone. Faut aussi appeler HandleUtility.Repaint() quand le state change sinon la SceneView update pas.
