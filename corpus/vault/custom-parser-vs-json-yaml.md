---
title: Custom parser vs JSON YAML, le vrai coût
summary: Écrire un custom parser c'est un rabbit hole quasi-systématique, JSON ou YAML couvrent 95% des cas sauf si ton format a vraiment des contraintes uniques.
type: lesson
links:
  - "[[file-based-vs-database-pour]]"
  - "[[savoir-quand-killer-un-rabbit]]"
  - "[[build-by-need-pas-by]]"
  - "[[forker-une-library-vs-la]]"
---
J'ai écrit deux custom parsers dans ma vie et je regretterais pas la première fois — c'était pour un format de données vraiment spécifique où JSON était verbeux et illisible. Mais la deuxième fois c'était clairement du NIH (Not Invented Here) syndrome. Le coût réel d'un custom parser c'est pas juste l'écriture, c'est les edge cases, les messages d'erreur utiles, la maintenance. YAML est souvent le compromise parfait pour du config human-editable.
