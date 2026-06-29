---
title: Radial Puppet float continu expression menu
summary: Le Radial Puppet dans l'expression menu contrôle un Float paramètre via un wheel rotatif; idéal pour des valeurs continues genre taille, intensité ou blend entre deux états.
type: reference
links:
  - "[[direct-blend-tree-toggle-sans]]"
  - "[[expression-menu-limite-a-8]]"
  - "[[bool-int-float-choisir-bon]]"
  - "[[puppet-menu-hold-behavior-gotcha]]"
---
Le Float va de 0.0 à 1.0 selon la position du wheel, et dans le FX layer un Blend Tree lit ce Float pour interpoler entre deux animation clips. Excellent pour les avatars qui ont des options de personnalisation smooth genre taille de queue ou intensité de glow. Combine bien avec un Direct Blend Tree.
