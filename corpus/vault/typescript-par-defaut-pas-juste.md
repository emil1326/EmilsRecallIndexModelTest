---
title: TypeScript par défaut pas juste par mode
summary: Emil part en TypeScript par défaut sur tout projet JavaScript, le type checking catch trop d'erreurs stupides pour ignorer ça, même sur des petits projets.
type: identity
links:
  - "[[node-js-partout-dans-le]]"
  - "[[npm-reste-le-package-manager]]"
  - "[[vs-code-reste-l-editeur]]"
  - "[[extensions-vs-code-qui-changent]]"
  - "[[npm-scripts-suffisent-pas-besoin]]"
---
Le setup initial de TypeScript est un peu chiant, tsconfig, les déclarations de types, mais le payoff est immédiat en termes de refactor safe. JavaScript pur c'est cool pour du quick scripting mais dès que le projet grossit, `undefined is not a function` commence à frapper. TypeScript c'est juste du JS avec une ceinture de sécurité, smh, faut l'utiliser.
