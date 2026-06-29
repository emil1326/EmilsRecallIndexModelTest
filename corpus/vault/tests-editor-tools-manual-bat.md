---
title: Tests editor tools: manual bat l'automatisé
summary: Les editor tools Unity sont quasi-impossibles à unit tester proprement — les tests manuels dans l'editor sur des projets réels restent la seule approche vraiment fiable.
type: lesson
links:
  - "[[module-first-design-versus-monolith]]"
  - "[[aac-applicator-le-probleme-que]]"
  - "[[mesh-diff-vertex-comparison-pis]]"
  - "[[feature-locker-ne-d-un]]"
---
Unity a un framework de test EditMode mais c'est lourd à setup pis les tests deviennent fragiles dès qu'ils touchent des assets ou le scene graph. Pour EmilsWork j'ai abandonné les automated tests sur les editor tools — je teste manuellement sur des projets VRChat réels pis je note les edge cases. C'est pas parfait mais c'est pragmatique.
