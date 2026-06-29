---
title: JSONL vs CSV pour ML
summary: JSONL gagne sur CSV pour le ML parce que t'as le typage natif, des champs arbitraires par ligne, pis un streaming trivial — CSV c'est pour les tableaux propres et rien d'autre.
type: reference
links:
  - "[[jsonl-le-format-de-base]]"
  - "[[streaming-jsonl-pour-gros-datasets]]"
  - "[[metadata-per-ligne-dans-le]]"
  - "[[append-atomique-au-jsonl-sans]]"
---
CSV te force à encoder tout en string puis parser, gère mal les fields avec des virgules ou des newlines, pis supporte pas nativement les arrays ou les nested objects. JSONL t'en passe tout ça gratis. Par contre CSV c'est effectivement plus compact pour les datasets tabulaires clean avec un schema fixe et aucune variation. Pour des données NLP avec du texte libre ou des structures variables, JSONL no contest — CSV c'est plate tbh.
