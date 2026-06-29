---
title: Sources cachées de leakage insidieux
summary: Y'a des formes de leakage moins évidentes que le scaler fitté sur full data: feature engineering sur stats globales, preprocessing avec labels, ou duplicates entre splits.
type: lesson
links:
  - "[[leakage-train-test-le-vrai]]"
  - "[[augmentation-et-leakage-combo-subtil]]"
  - "[[tokenizer-outside-du-split-pas]]"
  - "[[dedup-exact-sur-hash-md5]]"
---
Exemples concrets: calculer la fréquence d'un mot sur tout le corpus incluant le test set puis l'utiliser comme feature — c'est du leakage stat. Ou encore utiliser le label pour imputer des missing values avant de splitter, tsé. Pis évidemment les duplicates entre train et test c'est le grand classique qu'on oublie quand même. La règle d'or: tout ce qui est fitté ou calculé sur les données doit être fait sur le train set only, point.
