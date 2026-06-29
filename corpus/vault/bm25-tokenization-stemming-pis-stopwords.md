---
title: BM25 tokenization stemming pis stopwords
summary: BM25 dépend fortement du tokenizer en amont — enlever stopwords et appliquer stemming change significativement les scores, surtout pour des requêtes courtes en franglais.
type: lesson
links:
  - "[[bm25-still-slaps-pour-keywords]]"
  - "[[bm25-k1-et-b-les]]"
  - "[[bm25-fail-sur-semantique-et]]"
  - "[[hybrid-fusion-dense-plus-sparse]]"
  - "[[tokenizer-outside-du-split-pas]]"
---
Pour du contenu franglais, le stemming standard anglais va mal gérer les mots français, tsu. C'est un tradeoff: soit tu tokenizes raw (plus simple, perd le stemming), soit tu fais un tokenizer custom mixed. Pour mon daemon, j'ai gardé ça simple avec whitespace+lowercase, pis ça fit correct.
