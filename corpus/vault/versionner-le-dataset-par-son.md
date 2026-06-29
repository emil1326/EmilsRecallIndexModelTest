---
title: Versionner le dataset par son hash
summary: Calculer un hash global du dataset pis le logger dans les expériences garantit la reproductibilité — si quelqu'un modifie les données, le hash change et t'es alerté.
type: reference
links:
  - "[[reproductibilite-end-to-end-du]]"
  - "[[logger-le-split-avec-seed]]"
  - "[[metadata-per-ligne-dans-le]]"
  - "[[dedup-exact-sur-hash-md5]]"
---
Si quelqu'un modifie le fichier de données ou si les lignes changent d'ordre, le hash change — t'as une détection automatique sans rien faire de fancy. `hashlib.md5(open("data.jsonl","rb").read()).hexdigest()` pour les petits fichiers, ou un hash incrémental ligne par ligne pour les gros. C'est plate à setup mais genre indispensable quand plusieurs personnes travaillent sur le même projet pis que quelqu'un "juste nettoie le dataset un peu" à 3h du mat sans rien dire.
