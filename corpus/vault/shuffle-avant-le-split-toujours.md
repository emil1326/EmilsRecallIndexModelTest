---
title: Shuffle avant le split, toujours
summary: Si tes données ont un ordre naturel — temporel, par classe, par source — shuffler avant de splitter est critique pour éviter des splits biaisés pas représentatifs.
type: reference
links:
  - "[[time-based-split-vs-random]]"
  - "[[stratified-split-pour-classes-debalancees]]"
  - "[[seed-fixe-pour-reproductibilite-totale]]"
  - "[[ordre-dedup-split-ca-change]]"
---
Genre si tes données sont sorted par label, un split 80/20 naïf te donne un train avec surtout les premières classes pis un test avec les dernières — ça fit pas pantoute. Pareil si les données viennent de sources différentes groupées ensemble. `sklearn.utils.shuffle(X, y, random_state=42)` avant `train_test_split` c'est l'habitude à avoir. Exception notable: les données temporelles où le shuffle introduirait justement du leakage — là on shuffe pas, tsé.
