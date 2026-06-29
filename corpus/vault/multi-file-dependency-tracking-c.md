---
title: Multi-file dependency tracking c'est pas trivial
summary: Tracker les dépendances entre fichiers (imports, requires, includes) demande de parser ou d'utiliser la symbol table de chaque langage — c'est pas universellement simple à faire right.
type: journal
links:
  - "[[dependency-graph-colonne-vertebrale-du]]"
  - "[[transitive-deps-le-vrai-rabbit]]"
  - "[[propagation-dans-le-graph-ordre]]"
  - "[[expiration-anticipee-sur-imports-transitifs]]"
---
Pour Python, importer ast.parse et lire les Import nodes c'est gérable. Pour TypeScript avec tsconfig.json et path aliases, ça devient beaucoup plus fun genre xD. La plupart des projets viables utilisent soit le LSP du langage pour les deps, soit une approximation par regex sur les import statements. L'approximation est souvent 95% correcte pis suffisante.
