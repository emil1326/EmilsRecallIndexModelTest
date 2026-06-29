---
title: UIToolkit vs IMGUI: le vrai trade-off
summary: UIToolkit c'est l'avenir mais l'écosystème IMGUI est tellement plus mature et documenté que switcher coûte plus cher que ça rapporte pour des tools utilitaires.
type: lesson
links:
  - "[[pourquoi-imgui-reste-le-choix]]"
  - "[[guirepaint-loop-si-ongui-throttle]]"
  - "[[editorwindow-lifecycle-onenable-pas-onawake]]"
  - "[[module-first-design-versus-monolith]]"
---
J'ai essayé UIToolkit pour un module EmilsWork et honnêtement le data binding, UXML, USS — c'est une courbe d'apprentissage énorme pour pas grand chose de plus. Le vrai avantage de UIToolkit c'est pour des UIs complexes avec du layout dynamique, mais pour des tools utilitaires genre les miens c'est overkill live. Je reste sur IMGUI jusqu'à ce que Unity force la migration.
