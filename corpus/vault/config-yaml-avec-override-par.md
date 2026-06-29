---
title: Config YAML avec override par env var
summary: Arrow lit sa config depuis un fichier YAML de base et laisse les env vars override n'importe quel setting, ce qui rend le deployment flexible sans recompiler.
type: reference
links:
  - "[[feature-flags-comme-roadmap-tracker]]"
  - "[[picocli-pour-le-cli-arrow]]"
  - "[[slf4j-comme-logging-facade-arrow]]"
  - "[[gradle-multi-module-structure-de]]"
---
Le format c'est `ARROW_STORE_TTL=60000` qui mappe sur `arrow.store.ttl` dans le YAML. J'utilise SnakeYAML pour parser le fichier pis une petite fonction qui merge les env vars par-dessus. Simple, no magic, pis ça marche dans Docker sans changer une ligne de code.
