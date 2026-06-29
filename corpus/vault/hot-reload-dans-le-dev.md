---
title: Hot reload dans le dev server
summary: Emil dépend du hot reload dans ses dev servers, Vite ou Node watch mode, pour voir les changements instantanément sans refresh manuel.
type: reference
links:
  - "[[node-js-partout-dans-le]]"
  - "[[npm-reste-le-package-manager]]"
  - "[[npm-scripts-suffisent-pas-besoin]]"
  - "[[vs-code-debugger-eviter-le]]"
  - "[[windows-terminal-comme-host-principal]]"
---
Vite c'est genre le gold standard pour ça, HMR ultra-rapide, le state de l'app est préservé pendant les edits, c'est un autre level. Pour du Node.js pur, `node --watch` ou `nodemon` font le job pour relancer le serveur automatiquement. Travailler sans hot reload en 2025 c'est du masochisme, tbh.
