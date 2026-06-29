---
title: Le repro minimal, first thing always
summary: Créer le plus petit cas possible qui reproduit le bug de façon consistante est la step la plus importante avant tout le reste.
type: lesson
links:
  - "[[un-repro-minimal-revele-souvent]]"
  - "[[isoler-systeme-vs-app-avant]]"
  - "[[les-assumptions-non-validees-causent]]"
  - "[[race-condition-impossible-a-repro]]"
---
Si tu peux pas repro le bug de façon consistante, tu debugs dans le vide, genre littéralement. Le repro minimal te force à isoler les variables, pis souvent en le faisant tu trouves le bug toi-même, comme par magie. C'est plate à faire mais ça save tellement de temps après.
