---
title: Geler le code qui marche, toucher à rien
summary: Une fois que quelque chose marche après une galère, tu gèles ça et tu changes rien, don't touch what works c'est une règle d'or dans mon flow.
type: identity
links:
  - "[[savoir-quand-arreter-de-debug]]"
  - "[[refactor-quand-ca-bloque-pas]]"
  - "[[committer-du-code-que-tu]]"
  - "[[documenter-dans-ta-tete-vs]]"
---
Le réflexe de "tant qu'à être là, laisse moi cleaner ça un peu" après une fix qui a pris deux heures c'est dangereux. Tu risques de re-briser ce que tu venais de fixer. Le bon move c'est: ça marche? Commit tout de suite. Clean up dans un commit séparé si vraiment nécessaire.
