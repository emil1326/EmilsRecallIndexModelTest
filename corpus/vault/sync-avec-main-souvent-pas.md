---
title: Sync avec main souvent pas à la fin
summary: Rebaser ta feature branch sur main régulièrement (toutes les 1-2 jours) plutôt qu'une fois juste avant le merge évite les gros conflict nightmares de dernière minute.
type: lesson
links:
  - "[[rebase-ou-merge-selon-le]]"
  - "[[branches-courtes-vivent-mieux-mergent]]"
  - "[[hotfix-branch-part-toujours-de]]"
  - "[[git-log-oneline-graph-voir]]"
  - "[[force-push-interdit-sur-branches]]"
  - "[[npm-scripts-suffisent-pas-besoin]]"
---
Le pattern c'est: git fetch origin, git rebase origin/main sur ta branch — si y'a des conflicts, tu les règles en petites bouchées pendant que le contexte est encore frais. Attendre le dernier jour pour syncer c'est se condamner à passer sa matinée à démêler des conflicts dans du code que t'as à moitié oublié. Même sur des projets solo, si t'as plusieurs branches en parallèle, le sync régulier ça évite bien des maux de tête.
