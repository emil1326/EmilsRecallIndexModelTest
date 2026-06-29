---
title: BM25 fail sur sémantique et paraphrase
summary: BM25 est aveugle aux synonymes et paraphrases — 'rapide' et 'fast' sont deux tokens différents pour lui, ce que le dense retrieval gère naturellement.
type: lesson
links:
  - "[[bm25-still-slaps-pour-keywords]]"
  - "[[hybrid-fusion-dense-plus-sparse]]"
  - "[[dense-retrieval-fail-sur-keywords]]"
  - "[[bm25-tokenization-stemming-pis-stopwords]]"
  - "[[system-prompt-loi-du-monde]]"
---
Si tu notes quelque chose en français mais tu queries en anglais (ou vice versa), BM25 va juste pas find ça. Dense embedding, par contre, si le modèle a vu les deux langues, il peut faire le lien sémantique. Pour du contenu franglais, ça justifie encore plus le hybrid.
