---
title: Tags sémantiques sur chaque release
summary: Tagger chaque release avec semantic versioning (v1.2.3) dans git donne un point de référence clair pour rollbacks, changelogs, pis la communication avec les users.
type: reference
links:
  - "[[conventional-commits-format-feat-fix]]"
  - "[[main-branch-doit-rester-deployable]]"
  - "[[hotfix-branch-part-toujours-de]]"
  - "[[pr-review-c-est-plus]]"
  - "[[branches-courtes-vivent-mieux-mergent]]"
---
git tag -a v1.2.3 -m 'Release 1.2.3' suivi de git push origin v1.2.3 — ou laisser GitHub le faire depuis une release. MAJOR.MINOR.PATCH: major pour breaking changes, minor pour nouvelles features backward-compatible, patch pour bug fixes. C'est pas obligatoire sur des projets perso mais dès que t'as des users ou des dépendants, le semver c'est la base pour pas les faire souffrir.
