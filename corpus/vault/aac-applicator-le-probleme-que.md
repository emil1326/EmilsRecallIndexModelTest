---
title: AAC Applicator: le problème que ça règle
summary: L'AAC Applicator automatise l'application de configurations sur des avatars VRChat — sans ça c'est du copy-paste manuel sur des dizaines de composants à chaque update.
type: journal
links:
  - "[[undo-recordobject-avant-toute-modification]]"
  - "[[assetdatabase-refresh-bloque-l-editor]]"
  - "[[feature-locker-ne-d-un]]"
  - "[[emilswork-suite-de-tools-modulaires]]"
---
Le problème c'est que configurer un avatar VRChat avec de l'AAC c'est répétitif: les mêmes settings sur les mêmes composants, avatar après avatar. L'Applicator prend un template, trouve les composants matching dans la scène, pis applique tout en un click. Undo.RecordObject partout — parce que sinon une mauvaise application c'est catastrophique.
