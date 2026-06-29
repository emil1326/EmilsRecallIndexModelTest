---
title: System Prompt Versioning Comme Du Code
summary: Versionner les system prompts dans git est indispensable en prod — un changement de prompt peut casser une feature autant qu'un changement de code, pas de blague.
type: lesson
links:
  - "[[system-prompt-loi-du-monde]]"
  - "[[system-prompt-sweet-spot-cinq]]"
  - "[[prompt-injection-trust-jamais-l]]"
  - "[[system-prompt-pas-d-infos]]"
  - "[[few-shot-trois-a-cinq]]"
---
J'ai casé un feature en prod en "améliorant" un system prompt sans version control — les side effects d'un prompt sont juste plus durs à tracer que ceux du code, mais ils sont réels. Garde tes prompts dans des fichiers versionés, taggue les versions, écris pourquoi t'as changé quoi. Pis test avant de deploy, genre comme... du code. La discipline est la même, les conséquences aussi.
