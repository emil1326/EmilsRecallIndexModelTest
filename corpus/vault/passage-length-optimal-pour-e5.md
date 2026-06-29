---
title: passage length optimal pour e5-small
summary: E5-small a un context window de 512 tokens — les passages trop longs sont tronqués, les trop courts diluent le signal sémantique, genre 100-200 tokens c'est le sweet spot.
type: reference
links:
  - "[[prefix-passage-pour-indexer-les]]"
  - "[[e5-small-choisi-pour-le]]"
  - "[[cosine-similarity-pas-dot-product]]"
  - "[[embedding-caching-pour-eviter-recalcul]]"
---
Chunker tes documents trop finement (genre phrases individuelles) donne des embeddings pauvres en contexte. Trop large (pages entières) et t'as de la dilution plus troncation. Pour des notes de second brain, des chunks de 150-250 tokens avec un overlap de 20-30 tokens marchent bien.
