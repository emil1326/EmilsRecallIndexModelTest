---
title: Puppet menu hold behavior gotcha
summary: Le Puppet menu exige de tenir le contrôle ouvert pour ajuster; relâcher ferme le menu mais la valeur reste figée là où elle était, c'est voulu mais contre-intuitif.
type: lesson
links:
  - "[[radial-puppet-float-continu-expression]]"
  - "[[expression-menu-limite-a-8]]"
  - "[[sub-menu-nesting-profondeur-expression]]"
  - "[[synced-vs-unsynced-parametres-difference]]"
---
Pour les gens qui découvrent ça la première fois, ça semble buggy que le menu ferme dès qu'on relâche le joystick. Mais c'est le design: hold pour ajuster, release pour confirmer et fermer. Si tu veux une valeur persistante que tu tweakes souvent, assure-toi que ton Float est bien synced pour qu'il reste entre sessions.
