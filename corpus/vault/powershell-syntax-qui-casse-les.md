---
title: PowerShell syntax qui casse les pieds
summary: PowerShell a une syntaxe qui brise les outils Unix standards, les pipes, les variables d'environnement, les wildcards fonctionnent différemment et ça catch Emil off-guard.
type: lesson
links:
  - "[[git-bash-plutot-que-powershell]]"
  - "[[windows-terminal-comme-host-principal]]"
  - "[[windows-pour-dev-pas-parfait]]"
  - "[[git-en-cli-pas-en]]"
---
Les `$env:VAR` au lieu de `$VAR`, les `&&` qui marchent pas en PS5, faut toujours switcher le brain en mode Windows quand on est dans PowerShell. Le pire c'est quand un script shell qui marche parfait dans Bash fail silencieusement dans PowerShell pour des raisons cryptiques. C'est pour ça qu'Emil reste dans Git Bash le plus possible, smh.
