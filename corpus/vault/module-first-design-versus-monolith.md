---
title: Module-first design versus monolith: la leçon
summary: Partir avec des modules indépendants c'est mieux qu'un gros monolith — plus facile à debug, à versionner, pis sortir un module sans casser les autres c'est inestimable.
type: lesson
links:
  - "[[assembly-definition-pour-separer-code]]"
  - "[[emilswork-suite-de-tools-modulaires]]"
  - "[[far-plan-emilswork-gros-tool]]"
  - "[[branding-emilswork-dans-chaque-fenetre]]"
  - "[[createur-liability-pourquoi-le-gate]]"
---
Au début j'aurais pu tout mettre dans un gros EditorWindow avec des tabs — ça aurait été "plus simple". Mais dès qu'un tool break il break tout le reste avec lui. Les modules séparés dans EmilsWork ont leur propre assembly, leur propre lifecycle, pis je peux sortir l'un sans toucher aux autres — ça vaut vraiment son pesant de gold.
