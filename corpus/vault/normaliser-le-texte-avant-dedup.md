---
title: Normaliser le texte avant dedup
summary: Avant de hasher pour le dedup, normaliser le texte — strip, lowercase, collapse whitespace, unicode normalization — évite de garder des doublons qui diffèrent seulement par la forme.
type: reference
links:
  - "[[dedup-exact-sur-hash-md5]]"
  - "[[minhash-lsh-pour-dedup-fuzzy]]"
  - "[[ordre-dedup-split-ca-change]]"
  - "[[sources-cachees-de-leakage-insidieux]]"
---
Un texte avec un espace en trop ou un accent encodé différemment va générer un hash différent et passer le dedup exact sans normalisation, tsé. Genre `unicodedata.normalize("NFC", text).strip().lower()` c'est le minimum absolu. Pour du texte web-scraped, des patterns de nettoyage plus agressifs (balises HTML, URLs) avant de normaliser c'est souvent nécessaire. Le niveau de normalisation dépend du domaine, mais plus c'est agressif, plus le dedup est efficace.
