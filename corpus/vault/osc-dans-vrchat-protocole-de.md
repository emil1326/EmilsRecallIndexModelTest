---
title: OSC dans VRChat — protocole de base
summary: OSC c'est le bridge officiel de VRChat pour connecter des apps externes aux params d'avatar et au chatbox, tout ça en UDP local sur loopback.
type: reference
links:
  - "[[ports-9000-9001-le-handshake]]"
  - "[[enable-osc-dans-vrchat-settings]]"
  - "[[udp-fire-and-forget-pas]]"
  - "[[build-un-bridge-desktop-architecture]]"
  - "[[format-d-un-message-osc]]"
---
VRChat a ouvert ça officiellement en 2022 pis depuis ce moment-là tout le monde a commencé à builder des overlays pis des apps tierces. Le protocol OSC c'était à la base du contrôle de mixers audio, repurposed pour du game data — plutôt clever tsu. UDP local, donc pas de connexion à maintenir, juste du fire-and-forget vers localhost.
