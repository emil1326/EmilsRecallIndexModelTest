---
title: score normalization avant hybrid fusion
summary: Avant de fusionner scores BM25 et cosine, il faut les ramener sur la même échelle — min-max normalization ou z-score, sinon un des deux retrievers domine arbitrairement.
type: reference
links:
  - "[[rrf-l-algorithme-de-fusion]]"
  - "[[hybrid-fusion-dense-plus-sparse]]"
  - "[[hybrid-fusion-weight-ratio-dense]]"
  - "[[cosine-similarity-pas-dot-product]]"
---
BM25 sort des scores entre 0 et genre 20+, cosine entre -1 et 1. Si tu les sommes direct, BM25 écrase tout. Min-max normalisation sur le batch de résultats ramène les deux à [0,1]. Alternative: utiliser RRF qui bypass complètement le problème de scale.
