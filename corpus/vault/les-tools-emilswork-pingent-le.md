---
title: Les tools EmilsWork pingent le serveur au startup
summary: Chaque tool EmilsWork fait un /ping au démarrage et affiche un indicateur visuel de connexion — l'utilisateur sait tout de suite si le backend est up ou pas.
type: reference
links:
  - "[[le-endpoint-ping-pour-verifier]]"
  - "[[le-backend-bridge-unity-vers]]"
  - "[[convention-de-nommage-des-routes]]"
  - "[[latence-acceptable-pour-des-tools]]"
  - "[[monitoring-params-en-live-workflow]]"
---
C'est une petite LED verte ou rouge dans le coin de l'UI. Si le serveur est down, les features qui en dépendent se disabled automatiquement plutôt que de fail silencieusement. J'ai appris que fail silently c'est la pire chose qu'un tool peut faire.
