---
title: Cross-val ou held-out: faut choisir
summary: Cross-validation donne une meilleure estimation de variance avec peu de données, mais un held-out unique est plus honnête si les données temporelles ou la taille le permettent.
type: lesson
links:
  - "[[held-out-set-intouchable-en]]"
  - "[[stratified-split-pour-classes-debalancees]]"
  - "[[proportions-80-10-10-vs]]"
  - "[[reproductibilite-end-to-end-du]]"
---
Avec un petit dataset (moins de 10k exemples), la cross-val est souvent préférable parce que tu maximises l'utilisation des données pour estimer les perfs. Avec un gros dataset, un single held-out split suffit pis c'est beaucoup moins cher computationnellement. Le trap c'est de faire de la cross-val ET un held-out puis de choisir le meilleur résultat — là t'as juste rajouté un niveau de test set leakage, smh. Faut choisir l'un ou l'autre avant de commencer.
