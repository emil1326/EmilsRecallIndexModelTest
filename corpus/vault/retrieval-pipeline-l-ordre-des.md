---
title: retrieval pipeline l'ordre des étapes
summary: L'ordre du pipeline est fixe: chunk → embed avec prefix passage: → index BM25+dense → au query time: embed query avec prefix query: → retrieval hybrid → rerank optionnel.
type: reference
links:
  - "[[prefix-query-obligatoire-avec-e5]]"
  - "[[prefix-passage-pour-indexer-les]]"
  - "[[hybrid-fusion-dense-plus-sparse]]"
  - "[[reranking-quand-ca-vaut-vraiment]]"
  - "[[embedding-caching-pour-eviter-recalcul]]"
---
Mélanger les étapes ou oublier les prefixes à la bonne étape c'est le genre d'erreur qui se voit pas tout de suite mais qui dégrade silencieusement la qualité. Fais-toi des fonctions nommées claires genre embed_query() vs embed_passage(). Ça aide vraiment à pas se mélanger.
