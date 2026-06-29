---
title: Write Defaults ON OFF vraie différence
summary: Write Defaults ON reset les propriétés auto quand l'état est inactif; OFF faut gérer chaque état à la main sinon les propriétés se stuck quelque part de random.
type: lesson
links:
  - "[[fx-layer-regne-sur-quasi]]"
  - "[[direct-blend-tree-toggle-sans]]"
  - "[[layer-weight-a-0-par]]"
  - "[[animation-clip-binding-chemin-exact]]"
---
La communauté penche vers Write Defaults OFF pour les avatars complexes parce que c'est plus prévisible et moins magique. Avec WD ON, la valeur par défaut de l'idle state peut entrer en conflit avec d'autres layers et créer des surprises. Si tu mixes ON et OFF dans le même animator, prépare-toi à debug longtemps — c'est un classique.
