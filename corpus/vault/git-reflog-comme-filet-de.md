---
title: git reflog comme filet de sécurité
summary: git reflog garde un historique de tous les mouvements de HEAD localement, ce qui permet de récupérer des commits 'perdus' après un reset ou un rebase raté.
type: reference
links:
  - "[[rebase-ou-merge-selon-le]]"
  - "[[force-push-interdit-sur-branches]]"
  - "[[interactive-rebase-cleanup-avant-pr]]"
  - "[[git-bisect-pour-trouver-le]]"
  - "[[wip-commits-a-squasher-avant]]"
---
Si t'as fait un git reset --hard un peu trop vite ou un rebase qui s'est mal passé, git reflog montre toutes les positions que HEAD a eues récemment avec les SHA. Tu fais git checkout SHA et boom, t'as retrouvé ton travail. C'est le filet sous le trapèze — ça te donne la liberté de faire des trucs risqués localement sachant que t'as toujours un out. Ça expire après 90 jours par défaut, mais bon.
