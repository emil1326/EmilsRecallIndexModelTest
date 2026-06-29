---
title: Hotfix branch part toujours de main
summary: Un hotfix branch depuis le dernier tag/release sur main, pas depuis une feature branch en cours — sinon tu risques de shipper des changements pas encore reviewés avec ton fix.
type: reference
links:
  - "[[branch-naming-feature-hotfix-chore]]"
  - "[[main-branch-doit-rester-deployable]]"
  - "[[tags-semantiques-sur-chaque-release]]"
  - "[[stash-buffer-temporaire-pas-un]]"
  - "[[sync-avec-main-souvent-pas]]"
  - "[[ollama-tourne-local-sur-la]]"
---
La flow c'est: git checkout main, git pull, git checkout -b hotfix/description-du-bug, fix, PR vers main, tag la release. Ensuite tu merges main dans ta feature branch en cours si elle était outdated. C'est tentant de brancher de là où t'es pour sauver du temps mais ça crée des situations sketch où ton hotfix embarque du code expérimental. Fait pas ça.
