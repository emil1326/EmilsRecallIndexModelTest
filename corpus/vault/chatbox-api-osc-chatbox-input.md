---
title: Chatbox API OSC — /chatbox/input path
summary: VRChat expose /chatbox/input en OSC pour typer du texte in-game depuis une app desktop, avec un bool param pour envoyer direct ou afficher dans la typing box.
type: reference
links:
  - "[[format-d-un-message-osc]]"
  - "[[osc-dans-vrchat-protocole-de]]"
  - "[[build-un-bridge-desktop-architecture]]"
  - "[[avatar-parameters-le-namespace-avatar]]"
---
L'endpoint /chatbox/input prend deux arguments: un string (le texte) et un bool (true = envoyer direct, false = remplir la typing box sans envoyer). Y'a aussi /chatbox/typing pour afficher l'indicateur de frappe. C'est super simple à implémenter et ça ouvre des possibilités intéressantes pour des apps TTS, traducteurs auto, ou même juste un clavier physique custom.
