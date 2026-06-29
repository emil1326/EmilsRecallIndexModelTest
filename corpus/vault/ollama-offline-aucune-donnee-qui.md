---
title: Ollama offline, aucune donnée qui leak
summary: Ollama local signifie que toutes les requêtes LLM restent sur la machine d'Emil, zéro donnée envoyée sur internet, zéro dépendance à un service externe.
type: user
links:
  - "[[ollama-tourne-local-sur-la]]"
  - "[[gpu-amd-pour-l-inference]]"
  - "[[choisir-le-bon-modele-ollama]]"
  - "[[rocm-sur-amd-la-galere]]"
  - "[[windows-pour-dev-pas-parfait]]"
---
Pour des projets ou du code qui est sensible ou pas encore public, l'aspect offline est crucial, pas de risque de retrouver son code dans un training dataset. Ça marche aussi sans connexion internet, ce qui est un bonus pour les fois où le wifi est douteux. C'est pas juste une question de coût API, c'est une question de contrôle.
