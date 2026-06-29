---
title: cosine: normaliser vecteurs au préalable
summary: Si tu normalises L2 tous tes embeddings à l'indexation, le cosine similarity devient un simple dot product — plus rapide à calculer, surtout avec numpy ou FAISS.
type: reference
links:
  - "[[cosine-similarity-pas-dot-product]]"
  - "[[embedding-caching-pour-eviter-recalcul]]"
  - "[[retrieval-pipeline-l-ordre-des]]"
  - "[[onnx-runtime-pour-embedding-rapide]]"
---
C'est une petite optimisation mais propre: au moment d'indexer, tu divises chaque embedding par sa norme L2. Après, cosine(a,b) = dot(a,b) puisque ||a||=||b||=1. Ça simplifie le query path et ça fit mieux avec FAISS IndexFlatIP. Une normalisation à l'indexation, zéro overhead au query time.
