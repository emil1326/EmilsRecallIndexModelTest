---
title: Display string vs code identifier séparés
summary: La séparation display string/code identifier c'est pas juste une convention — c'est une nécessité technique pis un principe de design à internaliser tôt.
type: reference
links:
  - "[[convention-emils-vs-emil-s]]"
  - "[[emil-s-apostrophe-seulement-en]]"
  - "[[class-names-emils-sans-apostrophe]]"
  - "[[window-titles-affichent-emil-s]]"
  - "[[identifiers-code-sans-espaces-ni]]"
---
Une class peut s'appeler EmilsApplicatorWindow pis avoir un champ title = "Emil's Applicator" — c'est normal pis c'est le bon pattern. Le code identifier suit les contraintes du compilateur, le display string suit les contraintes de l'humain. Les mélanger c'est la source de bugs chiants.
