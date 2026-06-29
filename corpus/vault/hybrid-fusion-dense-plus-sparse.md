---
title: hybrid fusion dense plus sparse: pourquoi
summary: Le hybrid retrieval combine le meilleur de BM25 (keyword exact) et dense (sémantique) — aucun seul approach ne gagne sur tous les types de requêtes, c'est juste la réalité.
type: lesson
links:
  - "[[bm25-still-slaps-pour-keywords]]"
  - "[[dense-retrieval-fail-sur-keywords]]"
  - "[[rrf-l-algorithme-de-fusion]]"
  - "[[score-normalization-avant-hybrid-fusion]]"
  - "[[hybrid-fusion-weight-ratio-dense]]"
---
C'est pas juste une mode, les benchmarks sont clairs là-dessus. Dense est meilleur sur les questions paraphrasées, BM25 sur les termes précis. Hybrid gagne sur les deux en moyenne. Le trick c'est de bien fusionner les scores, pis là c'est là que RRF entre en jeu.
