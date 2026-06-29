---
title: Preview local upload comportement divergent
summary: L'avatar en preview local Unity et le comportement post-upload dans VRChat diffèrent souvent; des constraints, scripts SDK et syncs ne s'activent qu'une fois uploadé.
type: lesson
links:
  - "[[mirror-test-local-remote-comportement]]"
  - "[[animation-clip-binding-chemin-exact]]"
  - "[[physbones-et-fx-layer-font]]"
  - "[[synced-vs-unsynced-parametres-difference]]"
---
Le play mode Unity simule l'animator mais pas le runtime VRChat complet: pas de sync réseau réel, pas de PhysBones optimisés, pas de VRCConstraints actives comme en jeu. Ce qui marche parfait en preview peut être silencieusement cassé une fois uploadé. Le vrai test c'est toujours l'upload en world private avec un second compte.
