---
title: Les GC allocs causent des hitches imprévisibles
summary: Chaque allocation managed en C# build up la heap jusqu'au prochain GC collect — qui freeze le main thread pour quelques ms, genre sans prévenir.
type: lesson
links:
  - "[[object-pooling-pour-eviter-les]]"
  - "[[struct-layout-pis-cache-locality]]"
  - "[[string-concat-dans-un-hot]]"
  - "[[profiler-beginsample-pour-isoler-les]]"
---
Les hitches de GC sont vicieuses parce qu'elles apparaissent pas dans ton frametime moyen — juste comme des spikes aléatoires qui rendent le truc feel janky. Le Unity Profiler montre les allocs per frame dans la timeline, pis faut viser zéro alloc dans les hot paths. Le fix classique c'est l'object pooling ou repenser le layout de données en structs.
