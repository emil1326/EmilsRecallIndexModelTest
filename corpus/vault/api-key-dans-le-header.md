---
title: API key dans le header Authorization
summary: J'envoie l'API key dans le header Authorization plutôt qu'en query param pour éviter qu'elle finisse dans les logs ou l'historique browser.
type: reference
links:
  - "[[env-local-jamais-committe-jamais]]"
  - "[[convention-de-nommage-des-routes]]"
  - "[[ajouter-un-endpoint-decision-intentionnelle]]"
  - "[[response-format-json-meme-pour]]"
  - "[[port-deja-occupe-erreur-silencieuse]]"
---
Les query params c'est tsu pratique mais elles apparaissent dans les access logs du serveur et dans le cache du browser. Header Authorization: Bearer <key>, c'est deux secondes de plus à implémenter pis c'est la bonne façon. Même pour des tools persos, les bonnes pratiques ça reste des bonnes pratiques.
