---
title: VS Code Debugger, éviter le console.log
summary: Le debugger intégré de VS Code est assez puissant pour que le console.log debugging devienne inutile, mais ça prend du temps à s'y habituer vraiment.
type: lesson
links:
  - "[[vs-code-reste-l-editeur]]"
  - "[[extensions-vs-code-qui-changent]]"
  - "[[typescript-par-defaut-pas-juste]]"
  - "[[keybindings-vs-code-les-customiser]]"
  - "[[node-js-partout-dans-le]]"
---
Les breakpoints conditionnels, le watch des variables, le step-into, c'est infiniment plus efficient que d'éparpiller des console.log partout pis les enlever après. Pour du TypeScript avec source maps, le debugger attache direct au code source, pas au JS compilé, c'est pretty nice. Le `.vscode/launch.json` est souvent le premier truc à configurer dans un nouveau projet.
