---
title: AssetDatabase.Refresh bloque l'editor - éviter dans loops
summary: Appeler AssetDatabase.Refresh() force un reimport synchrone qui freeze l'editor — dans un loop sur plusieurs assets c'est facilement 30 secondes de gel.
type: lesson
links:
  - "[[editorapplication-delaycall-pour-ops-async]]"
  - "[[aac-applicator-le-probleme-que]]"
  - "[[editorwindow-lifecycle-onenable-pas-onawake]]"
  - "[[assembly-definition-pour-separer-code]]"
---
J'ai fait l'erreur avec un tool qui processait des prefabs en batch: un Refresh() par asset et l'editor était frozen une minute et demie, smh. La fix c'est de batcher toutes les modifs pis caller Refresh() une seule fois à la fin, ou utiliser AssetDatabase.StartAssetEditing() / StopAssetEditing() pour wrapper le batch. Leçon apprise de façon pénible.
