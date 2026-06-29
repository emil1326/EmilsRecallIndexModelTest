---
title: Port déjà occupé — erreur silencieuse qui tue
summary: Si le port 9001 est déjà utilisé par un autre process quand VRChat tente de binder, l'app reçoit juste rien, sans aucun message d'erreur. C'est plate tbh.
type: lesson
links:
  - "[[ports-9000-9001-le-handshake]]"
  - "[[udp-fire-and-forget-pas]]"
  - "[[enable-osc-dans-vrchat-settings]]"
  - "[[build-un-bridge-desktop-architecture]]"
---
C'est le bug le plus frustrant parce que y'a zéro feedback — ton app démarre, aucune exception, mais tu reçois strictement rien. La cause neuf fois sur dix: une ancienne instance de ton app ou un autre soft OSC a déjà bindé le port 9001. Un netstat rapide ou le Task Manager te montrent le coupable. Ça wrecke un bon 30 minutes quand tu t'y attends pas, smh.
