---
title: Action layer pour emotes et overrides
summary: Le Action layer est pour les emotes et animations full-body qui overrident le rig humanoid complet; il blend via le paramètre built-in VRCActionWeight.
type: reference
links:
  - "[[fx-layer-regne-sur-quasi]]"
  - "[[gesture-layer-hand-signs-tracking]]"
  - "[[layer-weight-a-0-par]]"
  - "[[layer-order-contraintes-animator-critique]]"
---
Quand le Action layer est actif, il prend le dessus sur les autres layers pour le rig humanoid — c'est pour ça que les emotes bloquent les hand gestures pendant qu'elles jouent. Le weight du Action layer est contrôlé via le paramètre built-in VRCActionWeight. FX layer continue de rouler en parallèle parce qu'il touche pas au rig.
