---
title: Avatar Parameter Driver changer params en state
summary: Avatar Parameter Driver est un state behavior qui set, add, random ou copy des paramètres quand un state est activé; idéal pour déclencher des effets en cascade.
type: reference
links:
  - "[[contact-receiver-toggle-sans-menu]]"
  - "[[bool-int-float-choisir-bon]]"
  - "[[budget-parametres-vrchat-limite-256]]"
  - "[[anystate-transition-boucle-infinie-piege]]"
---
Tu le mets directement sur un animator state comme un State Behavior, pis quand l'animator entre dans ce state, le driver s'exécute. Parfait pour des one-shots: genre entrer dans un état 'explosion' trigger aussi un Bool de particules. Beaucoup de gens connaissent pas ça pis font des workarounds compliqués dans leur animator pour rien.
