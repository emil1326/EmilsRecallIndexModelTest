---
title: Le endpoint /ping pour vérifier si online
summary: Le /ping est le premier endpoint que j'ajoute à tout serveur — une réponse 200 avec alive:true suffit pour savoir si le backend répond.
type: reference
links:
  - "[[les-tools-emilswork-pingent-le]]"
  - "[[health-check-avec-timestamp-pour]]"
  - "[[response-format-json-meme-pour]]"
  - "[[latence-acceptable-pour-des-tools]]"
---
Simple, bête, mais genre le /ping m'a sauvé tsu combien de fois quand je savais pas si c'était le client ou le serveur qui déconnait. Je l'ajoute avant même d'écrire la vraie logique, c'est le premier truc qui marche. Les tools EmilsWork l'utilisent pour afficher un petit indicateur de connexion dans l'UI.
