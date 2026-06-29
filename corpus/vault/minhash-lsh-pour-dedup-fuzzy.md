---
title: MinHash LSH pour dedup fuzzy
summary: Le dedup fuzzy avec MinHash + LSH détecte des near-duplicates quasi-identiques qui passent à travers un dedup exact sur hash — essentiel pour du web-scraped text.
type: reference
links:
  - "[[dedup-exact-sur-hash-md5]]"
  - "[[normaliser-le-texte-avant-dedup]]"
  - "[[sources-cachees-de-leakage-insidieux]]"
  - "[[ordre-dedup-split-ca-change]]"
---
Le principe: tu génères une MinHash signature par texte basée sur les n-grams, pis tu bucket les signatures similaires avec LSH. Datasketch en Python c'est la lib standard pour ça. Le threshold de similarité typique c'est 0.8 à 0.9 de Jaccard similarity. C'est way plus lent qu'un hash exact mais genre indispensable quand t'as des paraphrases ou du contenu dupliqué légèrement reworded — les near-dupes entre train et test c'est du leakage déguisé.
