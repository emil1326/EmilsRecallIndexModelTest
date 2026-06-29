---
title: npm scripts suffisent, pas besoin de Gulp
summary: Emil n'utilise pas Gulp, Grunt ou des task runners complexes, les npm scripts dans le package.json font le job pour 95% des besoins de build.
type: identity
links:
  - "[[npm-reste-le-package-manager]]"
  - "[[node-js-partout-dans-le]]"
  - "[[typescript-par-defaut-pas-juste]]"
  - "[[hot-reload-dans-le-dev]]"
  - "[[vs-code-reste-l-editeur]]"
---
`"build": "tsc && node dist/index.js"` c'est souvent tout ce qu'il faut, pas besoin de Gulpfile de 200 lignes pour ça. Gulp c'était la mode il y a 10 ans, là les npm scripts + Vite couvrent presque tout ce qu'on peut vouloir faire. Rajouter une dépendance de task runner juste pour paraître pro, c'est du overhead inutile.
