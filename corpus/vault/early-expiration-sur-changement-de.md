---
title: Early expiration sur changement de règle critique
summary: Quand une security rule change, invalider immédiatement toutes les entrées cache liées — attendre le TTL pour un outil de sécurité c'est inacceptable, pas juste suboptimal.
type: lesson
links:
  - "[[cache-key-doit-inclure-la]]"
  - "[[ttl-vs-event-based-expiration]]"
  - "[[reapply-des-security-rules-apres]]"
  - "[[expiration-anticipee-sur-imports-transitifs]]"
---
L'approche: chaque entrée cache stocke la liste des rule IDs dont elle dépend. Quand une règle est updatée, on fait un scan des entrées et on invalide tout ce qui référence ce rule ID. Oui c'est un peu expensive comme opération, mais ça arrive pas souvent et c'est le bon tradeoff. Rule version dans la cache key aide aussi à rendre ça automatique.
