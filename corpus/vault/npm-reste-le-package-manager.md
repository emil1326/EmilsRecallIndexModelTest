---
title: npm reste le package manager principal
summary: Emil utilise npm par défaut même si pnpm ou yarn existent, pas de raison de switcher quand npm fait le job sans complication sur Windows.
type: reference
links:
  - "[[node-js-partout-dans-le]]"
  - "[[typescript-par-defaut-pas-juste]]"
  - "[[npm-scripts-suffisent-pas-besoin]]"
  - "[[git-bash-plutot-que-powershell]]"
  - "[[hot-reload-dans-le-dev]]"
---
pnpm c'est objectivement plus rapide et plus économe en disk space, mais chaque projet a ses cas de compatibilité qui rendent le switch pas si simple. npm a l'avantage d'être là partout par défaut avec Node, pas besoin d'installer quoi que ce soit extra. Pour des gros monorepos peut-être que ça vaudrait le coup de réévaluer, mais là, npm ça fit.
