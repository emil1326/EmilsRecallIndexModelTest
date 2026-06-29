---
title: RRF: l'algorithme de fusion des ranks
summary: Reciprocal Rank Fusion fusionne des ranked lists sans normaliser les scores bruts — score RRF = somme de 1/(k+rank_i) pour chaque retriever, k=60 par défaut.
type: reference
links:
  - "[[hybrid-fusion-dense-plus-sparse]]"
  - "[[score-normalization-avant-hybrid-fusion]]"
  - "[[hybrid-fusion-weight-ratio-dense]]"
  - "[[reranking-quand-ca-vaut-vraiment]]"
---
L'avantage de RRF c'est que tu n'as pas à calibrer les scores entre BM25 et cosine, qui sont sur des échelles complètement différentes. Tu prends juste le rang, t'appliques la formule, tu sommes. Simple, robuste, marche bien en pratique. Le k=60 c'est empirique mais stable.
