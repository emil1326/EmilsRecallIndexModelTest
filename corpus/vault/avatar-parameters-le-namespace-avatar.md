---
title: Avatar parameters — le namespace /avatar/parameters/
summary: Tous les custom params d'avatar sont accessibles via l'address OSC /avatar/parameters/{NomExact}, case-sensitive, pis le nom doit matcher exactement ce qui est dans l'animator.
type: reference
links:
  - "[[types-de-params-osc-vrchat]]"
  - "[[avatar-swap-reset-tous-les]]"
  - "[[config-json-osc-par-avatar]]"
  - "[[avatar-expressions-vs-custom-params]]"
---
Le path exact c'est /avatar/parameters/ suivi du nom du param EXACTEMENT comme dans l'Animator Controller de l'avatar — case-sensitive, espaces inclus s'il y en a dans le nom. Faut pas confondre avec les built-in VRChat params qui ont leurs propres paths séparés. La façon la plus rapide de trouver les noms exacts c'est de lire le config JSON que VRChat génère automatiquement.
