---
title: SerializedProperty path syntax pour nested objects
summary: Le path d'un SerializedProperty pour un champ nested c'est "parent.child.field" avec des dots, pis les arrays Unity s'écrivent "list.Array.data[0]" — pas intuitif du tout.
type: reference
links:
  - "[[editorwindow-lifecycle-onenable-pas-onawake]]"
  - "[[beginchangecheck-pattern-pour-eviter-dirty]]"
  - "[[prefab-instances-pis-serializedproperty-le]]"
  - "[[undo-recordobject-avant-toute-modification]]"
---
La première fois que j'ai essayé d'éditer un champ dans une liste via SerializedProperty j'ai pogné une null ref pendant genre trente minutes. Le path "Array.data[i]" c'est une des affaires Unity que t'apprends en faisant ça crash ou en lisant le source. Super utile dans les CustomDrawers des tools EmilsWork mais ça se mémorise mal, faut garder une note.
