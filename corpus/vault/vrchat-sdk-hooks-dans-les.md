---
title: VRChat SDK hooks dans les tools EmilsWork
summary: Le VRChat SDK expose des callbacks de build comme IVRCSDKBuildRequestedCallback que les tools EmilsWork peuvent hooker pour valider ou auto-fixer des configs avant upload.
type: reference
links:
  - "[[feature-locker-ne-d-un]]"
  - "[[aac-applicator-le-probleme-que]]"
  - "[[far-plan-emilswork-gros-tool]]"
  - "[[assembly-definition-pour-separer-code]]"
---
C'est pas documenté des masses mais VRChat SDK a des interfaces qu'on peut implémenter pour s'injecter dans le pipeline build/upload. Genre un hook qui vérifie que tous les Feature Locked components sont unlocked avant d'uploader, ou qui applique les themes avant le build. Pour les tools EmilsWork intégrés à VRChat c'est le bon endroit pour la validation — pas un bouton manuel que les users vont oublier.
