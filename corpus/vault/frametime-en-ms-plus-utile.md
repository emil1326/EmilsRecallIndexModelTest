---
title: Frametime en ms plus utile que le FPS
summary: Travailler en frametime (ms) plutôt qu'en FPS est crucial pour évaluer le GPU time et détecter les hitches — le FPS moyen masque les spikes.
type: lesson
links:
  - "[[gpu-bound-vs-cpu-bound]]"
  - "[[gpu-bound-test-simple-freeze]]"
  - "[[shader-compile-stall-rdna4-c]]"
  - "[[shader-warmup-avant-gameplay-previent]]"
  - "[[renderdoc-pour-investiguer-le-render]]"
---
60fps = 16.67ms par frame. Si ton game tourne 'en moyenne' à 60fps mais que t'as des spikes à 50ms aux 10 secondes, le joueur le voit mais le FPS affiché dit toujours '60'. Le frametime graph (ou pire case frametime) c'est ce qui matter vraiment pour le feel. En profiling, regarde toujours le GPU time en ms par stage, pas juste le FPS global.
