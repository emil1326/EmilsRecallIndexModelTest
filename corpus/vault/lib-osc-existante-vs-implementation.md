---
title: Lib OSC existante vs implementation custom — le trade-off
summary: Implémenter OSC from scratch over UDP est souvent plus simple qu'ajouter une lib externe (OscCore, python-osc) pour un petit projet — le protocol est vraiment pas compliqué.
type: journal
links:
  - "[[format-d-un-message-osc]]"
  - "[[udp-fire-and-forget-pas]]"
  - "[[build-un-bridge-desktop-architecture]]"
  - "[[osc-dans-vrchat-protocole-de]]"
---
OscCore c'est la lib standard en C# pour Unity, python-osc pour Python, mais pour une app desktop standalone le protocol est tellement simple que je préfère parser les bytes manuellement. Un message OSC c'est une address string padded à 4 bytes + une type tag string + les arguments — genre 50-80 lignes de code, pas besoin d'une dependency entière pour ça. Ça dépend du scope du projet évidemment, mais pour du prototypage rapide le scratch gagne.
