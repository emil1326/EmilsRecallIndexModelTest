---
title: Direct Blend Tree toggle sans transitions
summary: Un Direct Blend Tree dans le FX layer permet de gérer plusieurs toggles en parallèle sans créer de transitions; plus clean pis plus performant que des states individuels.
type: reference
links:
  - "[[write-defaults-on-off-vraie]]"
  - "[[radial-puppet-float-continu-expression]]"
  - "[[bool-int-float-choisir-bon]]"
  - "[[layer-weight-a-0-par]]"
---
Le principe: chaque Bool ou Float paramètre contrôle le weight d'un child blend tree directement, sans passer par des transitions. Zéro transition delay, zéro exit time à configurer, ça just works. C'est la méthode recommandée pour les avatars avec beaucoup de toggles indépendants parce que ça scale vraiment bien.
