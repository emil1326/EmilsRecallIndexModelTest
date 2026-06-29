---
title: Versioning du cache schema, sinon corruption garantie
summary: Chaque changement de structure de données cachées nécessite un bump de schema version — sinon le code lit un format incompatible pis ça explose cryptiquement en prod.
type: lesson
links:
  - "[[serialisation-cache-json-lisible-vs]]"
  - "[[rollback-automatique-si-cache-corrompu]]"
  - "[[fingerprint-de-fichier-comme-cache]]"
  - "[[cache-key-doit-inclure-la]]"
  - "[[config-yaml-avec-override-par]]"
---
J'inclus toujours un champ `cache_version` dans chaque entrée, et au load si la version match pas la version courante, on invalide et on rebuilde. Ça semble obvious mais c'est le genre de truc qu'on oublie en early dev pis qu'on paie cher plus tard. Un migration path clean c'est overkill pour un outil d'analyse — invalider et rebuilder c'est suffisant.
