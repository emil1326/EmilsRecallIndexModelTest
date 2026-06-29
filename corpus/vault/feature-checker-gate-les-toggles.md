---
title: Feature checker: gate les toggles lewd
summary: Mon dernier projet, un feature checker: une API qui check si un user est dans un public world ou underage, pis bloque l'acces au toggle lewd sur un avatar public.
type: reference
links:
  - "[[le-vrai-probleme-tout-ou]]"
  - "[[archi-feature-checker-api-osc]]"
  - "[[vrchat-api-instance-type-source]]"
  - "[[ssl-avec-let-s-encrypt]]"
  - "[[fallback-avatar-requis-pour-safety]]"
---
Le but c'est de rendre les choses plus safe pour les createurs de contenu. Si le user est dans un public world ou flagged underage, le toggle lewd devient inaccessible automatiquement, sans que le createur ait a gerer ca a la main.
