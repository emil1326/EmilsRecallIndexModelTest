---
title: Pourquoi OSC plutôt que WebSocket pour Unity
summary: J'utilise OSC pour la communication Unity vers serveur parce que les libraries OSC dans Unity sont stables depuis longtemps et le protocol est simple et léger.
type: lesson
links:
  - "[[osc-bridge-tourne-en-parallele]]"
  - "[[le-backend-bridge-unity-vers]]"
  - "[[port-mapping-dev-3000-prod]]"
  - "[[garder-le-server-lean-sans]]"
---
WebSocket dans Unity c'est faisable mais c'est plus de setup pis les librairies sont moins matures. OSC c'est un protocol qui existe depuis les années 90 pour exactement ce genre de use case — des messages simples typés entre applications. Pour du one-way ou simple request-reply, OSC fit mieux que WebSocket tsu.
