---
title: Quand abstraire vs quand hardcoder directement
summary: L'abstraction prématurée coûte plus cher que le hardcode à long terme si l'abstraction s'avère fausse, et on peut rarement prédire le bon seam au départ.
type: lesson
links:
  - "[[build-by-need-pas-by]]"
  - "[[premature-optimization-vs-good-enough]]"
  - "[[ecs-vs-oop-pour-les]]"
  - "[[abstraction-layers-coutent-cher-a]]"
  - "[[slf4j-comme-logging-facade-arrow]]"
---
Le worst case c'est quand tu abstrais pour le mauvais seam — tu mets une interface au mauvais endroit et là tous tes futurs changes doivent travailler against cette abstraction. J'essaie de laisser le code se répéter trois fois avant d'abstraire, pas deux. Ça semble long mais les patterns qui méritent une abstraction se clarifient vraiment à la troisième répétition. L'abstraction trop tôt c'est parier sur un futur qu'on connaît pas encore.
