---
title: Seeds différents par librairie, attention
summary: Chaque librairie a sa propre source de random indépendante, pis setter la seed dans une seule change rien aux autres — faut toutes les setter explicitement.
type: lesson
links:
  - "[[seed-fixe-pour-reproductibilite-totale]]"
  - "[[reproductibilite-end-to-end-du]]"
  - "[[shuffle-avant-le-split-toujours]]"
  - "[[logger-le-split-avec-seed]]"
---
Genre tu peux avoir `random.seed(42)` mais si sklearn utilise NumPy en interne, ses shuffles vont quand même varier si t'as pas set `np.random.seed(42)`. Pareil pour PyTorch versus NumPy — complètement découplés. Le fix propre c'est un wrapper `set_all_seeds(seed)` que t'appelles en début de script avant tout. Ça semble tata mais c'est la raison numéro un des "why can't I reproduce my results" smh.
