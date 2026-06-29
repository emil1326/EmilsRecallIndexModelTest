---
title: BM25 still slaps pour keywords exacts
summary: BM25 reste imbattable pour les requêtes avec termes techniques précis, acronymes, ou noms propres que le dense retrieval va sémantiquement rater complètement.
type: lesson
links:
  - "[[bm25-fail-sur-semantique-et]]"
  - "[[hybrid-fusion-dense-plus-sparse]]"
  - "[[bm25-tokenization-stemming-pis-stopwords]]"
  - "[[dense-retrieval-fail-sur-keywords]]"
  - "[[spaced-repetition-integre-au-second]]"
---
Genre si tu cherches 'EmilsWork FSM State' ou un nom de fonction précis, e5 va peut-être te sortir un doc sémantiquement proche mais pas celui qui a les vrais mots. BM25 lui, il cherche exactement ça. C'est pour ça que hybrid existe.
