---
title: Seuil Critique: 150 Bones Actifs VRChat
summary: VRChat commence à souffrir en performance passé environ 150 bones actifs sur un avatar; les finger bones inutilisés sont les premiers candidats à supprimer.
type: reference
links:
  - "[[physbones-chains-complexes-saignent-le]]"
  - "[[armature-merging-moins-de-bones]]"
  - "[[skinned-mesh-vs-mesh-renderer]]"
  - "[[vrc-constraints-plus-performantes-que]]"
---
150 c'est pas un chiffre officiel VRChat, c'est un seuil empirique que la communauté a identifié par tests de frametime. Les avatars anime ont souvent des bones de robe, cape, cheveux, doigts complets, en plus de l'armature de base, pis ça monte vite à 200-300. Désactiver les finger bones si ton avatar use pas le finger tracking, c'est une win facile avec presque zéro downside.
