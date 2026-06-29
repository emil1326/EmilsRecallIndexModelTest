---
title: Frametime > Perf Rank pour les Avatars
summary: Le perf rank VRChat c'est des seuils arbitraires pas une mesure de perf réelle; le frametime dans le Unity Profiler dit la vraie vérité.
type: lesson
links:
  - "[[very-poor-avatar-peut-outperformer]]"
  - "[[unity-profiler-vs-vrchat-in]]"
  - "[[unity-stats-window-premier-tool]]"
  - "[[budget-realiste-moins-de-24]]"
  - "[[renderer-count-dans-le-perf]]"
---
Le perf rank c'est nice pour avoir une idée rapide, mais genre, un avatar Very Poor ben optimisé peut avoir un meilleur frametime qu'un Good avec 15 materials et des shaders de fou. Faut ouvrir le Profiler pis regarder les ms réels, pas se fier aux étoiles. Le rank compte les seuils de bones/renderers/etc de façon isolée, mais c'est le combo de tout ça ensemble qui kill le frametime pour vrai.
