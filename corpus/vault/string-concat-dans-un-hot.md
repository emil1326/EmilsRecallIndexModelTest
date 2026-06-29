---
title: String concat dans un hot loop: bad idea
summary: Chaque string concat en C# alloue une nouvelle string sur la managed heap — dans un hot loop, c'est des GC allocs guaranteed à chaque frame.
type: lesson
links:
  - "[[les-gc-allocs-causent-des]]"
  - "[[object-pooling-pour-eviter-les]]"
  - "[[profiler-beginsample-pour-isoler-les]]"
  - "[[micro-benchmark-le-piege-du]]"
---
Le fix le plus simple c'est StringBuilder si tu build une string progressivement, ou string.Format/interpolation quand c'est one-shot. Le vrai fix c'est de se demander pourquoi on manipule des strings dans un hot path genre — c'est souvent du debug logging qui aurait dû être désactivé en non-editor. Ça paraît obvious mais je l'ai vu brûler du frametime pour vrai.
