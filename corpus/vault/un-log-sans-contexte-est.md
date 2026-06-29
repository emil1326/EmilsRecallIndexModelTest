---
title: Un log sans contexte est un log inutile
summary: Un log qui dit juste 'Error: null' sans dire quel objet, quelle fonction, quel état du system est aussi utile que rien, literally.
type: lesson
links:
  - "[[log-quality-over-quantity-tse]]"
  - "[[logger-les-timestamps-pour-les]]"
  - "[[valider-l-environnement-avant-de]]"
  - "[[l-heisenbug-qui-disparait-quand]]"
---
Best practice que j'applique maintenant: chaque log inclut (1) l'identifier de l'entity concernée, (2) l'état attendu vs l'état observé, (3) l'action qui était en cours. Ça paraît verbose mais quand tu cherches à 2h du matin dans un log file de prod, tu vas bénir ton passé toi-même.
