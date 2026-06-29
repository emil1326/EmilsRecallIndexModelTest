---
title: cosine similarity pas dot product
summary: Avec des vecteurs e5 non-normalisés, cosine similarity est plus robuste que dot product parce qu'elle neutralise la norme — les documents longs sinon dominent artificiellement.
type: reference
links:
  - "[[cosine-normaliser-vecteurs-au-prealable]]"
  - "[[e5-small-choisi-pour-le]]"
  - "[[passage-length-optimal-pour-e5]]"
  - "[[score-normalization-avant-hybrid-fusion]]"
---
Dot product c'est plus rapide mais si tes embeddings ont des normes variables, tu vas avoir du biais vers les passages longs ou répétitifs. Cosine divise par les normes, donc ça compare juste la direction. Ou t'as juste à normaliser L2 tes vecteurs à l'indexation, alors dot product == cosine.
