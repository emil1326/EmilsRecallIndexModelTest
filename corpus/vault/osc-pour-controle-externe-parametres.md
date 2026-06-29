---
title: OSC pour contrôle externe paramètres
summary: VRChat supporte l'OSC pour set des paramètres d'avatar depuis des apps externes; pratique pour automatiser des effets ou intégrer des outils comme VRCOSC en runtime.
type: reference
links:
  - "[[synced-vs-unsynced-parametres-difference]]"
  - "[[bool-int-float-choisir-bon]]"
  - "[[mirror-test-local-remote-comportement]]"
  - "[[budget-parametres-vrchat-limite-256]]"
---
Les messages OSC arrivent sur le port 9000 et peuvent lire/écrire tous les paramètres synced de l'avatar en runtime. Des outils comme VRCOSC ou ThumbParams exploitent ça pour des intégrations fancy: heart rate, Spotify, gestures custom. C'est un rabbit hole mais un fun rabbit hole — t'as été prévenu.
