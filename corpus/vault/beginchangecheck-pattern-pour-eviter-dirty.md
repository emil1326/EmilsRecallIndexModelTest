---
title: BeginChangeCheck pattern pour éviter dirty states
summary: Wrapper les GUI calls dans EditorGUI.BeginChangeCheck/EndChangeCheck détecte exactement quand une valeur change — on agit seulement à ce moment-là, pas à chaque repaint frame.
type: reference
links:
  - "[[undo-recordobject-avant-toute-modification]]"
  - "[[serializedproperty-path-syntax-pour-nested]]"
  - "[[editorwindow-lifecycle-onenable-pas-onawake]]"
  - "[[guirepaint-loop-si-ongui-throttle]]"
---
Sans ça, t'as tendance à appliquer des effets à chaque frame OnGUI ce qui est wasteful pis peut causer des bugs de dirty state. Le pattern c'est: BeginChangeCheck, draw tes controls, EndChangeCheck retourne true si quelque chose a changé, là t'appliques. Hyper utile dans les tools EmilsWork où une modification UI trigger une opération sur des assets.
