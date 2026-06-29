---
title: Addressables vs Asset Bundle, le regret
summary: Addressables simplifie le workflow par rapport aux raw Asset Bundles, mais ajoute une complexité de runtime et un build pipeline qui peut vite devenir opaque.
type: lesson
links:
  - "[[forker-une-library-vs-la]]"
  - "[[custom-parser-vs-json-yaml]]"
  - "[[savoir-quand-killer-un-rabbit]]"
  - "[[build-by-need-pas-by]]"
---
Les raw Asset Bundles c'est verbose à setup mais tu comprends exactement ce qui se passe. Les Addressables cachent beaucoup de la complexité... jusqu'à ce que quelque chose broke, pis là tu debugs dans un système que tu comprends pas vraiment. J'ai switché à Addressables par FOMO et j'ai passé deux jours à comprendre pourquoi mes bundles se chargeaient pas dans le bon ordre. Pour un projet solo mid-size, les raw bundles avec un petit wrapper custom c'est souvent way plus clair.
