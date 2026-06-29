---
title: GUIRepaint loop si OnGUI throttlé mal
summary: Appeler Repaint() sans condition à chaque OnGUI frame crée une boucle infinie de repaints qui pousse le CPU de l'editor à fond pour rien.
type: lesson
links:
  - "[[beginchangecheck-pattern-pour-eviter-dirty]]"
  - "[[uitoolkit-vs-imgui-le-vrai]]"
  - "[[editorwindow-lifecycle-onenable-pas-onawake]]"
  - "[[pourquoi-imgui-reste-le-choix]]"
---
J'ai eu ça avec un module qui avait un animated spinner — j'appelais Repaint() unconditionally dans OnGUI pis le fan du laptop montait au max smh. La fix: Repaint() seulement quand quelque chose a vraiment changé, ou pour les animations utiliser EditorApplication.update avec un timer. Le profiler editor existe pour ces bugs-là mais faut penser à l'ouvrir.
