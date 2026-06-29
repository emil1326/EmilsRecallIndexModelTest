---
title: API design de la classe Image: ergonomie first
summary: Une classe Image custom doit exposer un API naturel — `setPixel(x, y, color)` plutôt que manipuler le raw ImageData array partout dans son code.
type: lesson
links:
  - "[[la-classe-image-custom-pourquoi]]"
  - "[[canvas-pixel-by-pixel-le]]"
  - "[[coordinate-system-canvas-0-0]]"
  - "[[imagedata-vs-drawimage-pas-le]]"
---
J'ai fait l'erreur de faire une classe où tu touchais encore le array interne direct pour certaines ops. Un design inconsistant comme ça, c'est le worst. L'interface publique devrait isoler complètement les détails d'implémentation — c'est vrai pour n'importe quelle classe mais encore plus quand c'est just toi qui l'utilises, parce que y'a personne pour t'arrêter.
