---
title: La bisection coupe le debug en deux
summary: Diviser le code ou les commits en deux récursivement pour localiser un bug est way plus efficace que lire line-by-line, genre toujours.
type: lesson
links:
  - "[[git-bisect-pour-les-regressions]]"
  - "[[une-hypothese-a-la-fois]]"
  - "[[changer-une-seule-variable-par]]"
  - "[[symptome-vs-cause-racine-pas]]"
---
Le principe c'est simple: tu commentes ou désactives la moitié du suspected code, tu checks si le bug est encore là, pis tu continues dans la bonne moitié. C'est O(log n) au lieu de O(n), tsu. Ça paraît évident mais dans le moment de stress on oublie ça pis on scroll dans tout le fichier comme un tata.
