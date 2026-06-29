---
title: Leakage train/test, le vrai danger
summary: Le leakage c'est quand des informations du test set influencent le training, ce qui donne des métriques fantastiques en lab mais des résultats pitoyables en prod.
type: lesson
links:
  - "[[held-out-set-intouchable-en]]"
  - "[[sources-cachees-de-leakage-insidieux]]"
  - "[[augmentation-et-leakage-combo-subtil]]"
  - "[[tokenizer-outside-du-split-pas]]"
  - "[[ordre-dedup-split-ca-change]]"
---
Le cas classique c'est d'appliquer un scaler ou un tokenizer fitté sur le full dataset avant de splitter — là t'as du leakage pis tu le sais même pas, tsu. Ton modèle a "vu" les stats du test set via la normalisation. Le vrai fix c'est de fitter tous tes preprocessors sur le train set seulement, puis transformer train/val/test séparément. C'est plate à refactorer après coup smh, mais c'est ça ou des métriques qui mentent.
