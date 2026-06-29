---
title: Time-based split vs random split
summary: Pour les données temporelles, faut splitter par date — train = passé, test = futur — et jamais aléatoirement, sinon tu simules un oracle qui connaît le futur.
type: lesson
links:
  - "[[shuffle-avant-le-split-toujours]]"
  - "[[leakage-train-test-le-vrai]]"
  - "[[sources-cachees-de-leakage-insidieux]]"
  - "[[reproductibilite-end-to-end-du]]"
---
Un modèle de prédiction de prix entraîné sur 2020-2023 et testé sur des données de 2021 mélangées dans le train, c'est du look-ahead leakage — dans la réalité, t'as pas accès au futur au moment de la prédiction. Le time-based split simule correctement le deployment scenario. Donc pas de shuffle avant de splitter dans ce cas-là — l'ordre temporel c'est de l'information précieuse, tsé. C'est un des rares cas où "shuffle toujours" est la mauvaise règle.
