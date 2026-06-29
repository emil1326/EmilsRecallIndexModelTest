---
title: Frametime beats FPS pour décider la perf
summary: Le frametime en ms donne une vérité plus honnête que le FPS, surtout quand les spikes sont le vrai problème à investiguer.
type: reference
links:
  - "[[premature-optimization-vs-good-enough]]"
  - "[[savoir-quand-killer-un-rabbit]]"
  - "[[shader-variant-baking-upfront-ou]]"
  - "[[ecs-vs-oop-pour-les]]"
---
Un jeu à 60 FPS "stable" peut avoir des spikes à 80ms qui font feel le stuttering tsu. Regarder le FPS moyen c'est se mentir à soi-même. Le frametime expose les outliers directement, pis c'est ça qui compte pour le ressenti joueur. J'utilise ça comme premier filtre avant même de profiler en profondeur.
