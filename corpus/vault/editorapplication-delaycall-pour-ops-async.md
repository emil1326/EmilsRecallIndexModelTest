---
title: EditorApplication.delayCall pour ops async editor
summary: EditorApplication.delayCall diffère du code à la prochaine frame editor — le safe way pour trigger des opérations depuis des callbacks qui s'exécutent pendant un repaint.
type: reference
links:
  - "[[editorwindow-lifecycle-onenable-pas-onawake]]"
  - "[[assetdatabase-refresh-bloque-l-editor]]"
  - "[[guirepaint-loop-si-ongui-throttle]]"
  - "[[aac-applicator-le-probleme-que]]"
---
Si t'essaies de modifier des assets ou de reload des windows pendant un OnGUI callback, Unity throw souvent une exception parce que t'es mid-draw. DelayCall c'est la solution propre pour dire "fais ça après le frame actuel". Genre un bouton qui doit close la window pis reload quelque chose — c'est là que delayCall brille.
