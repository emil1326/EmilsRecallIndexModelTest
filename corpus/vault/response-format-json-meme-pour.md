---
title: Response format JSON même pour les erreurs
summary: Mon API retourne toujours du JSON même pour les erreurs — un objet error avec un code plutôt qu'une HTML error page qui brise le client.
type: reference
links:
  - "[[convention-de-nommage-des-routes]]"
  - "[[api-key-dans-le-header]]"
  - "[[les-tools-emilswork-pingent-le]]"
  - "[[cors-m-a-pris-une]]"
---
Un client qui parse du JSON s'attend à du JSON — lui retourner du HTML sur une 404 ça crash le JSON.parse et là t'as un error dans l'error handler, c'est une mauvaise journée. J'ai un middleware global d'error handling qui transforme tout en JSON propre avant d'envoyer. Simple pis ça évite des heures de debug inutile.
