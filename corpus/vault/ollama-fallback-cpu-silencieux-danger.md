---
title: Ollama fallback CPU silencieux, danger réel
summary: Ollama te dit rien quand il switch sur CPU — tu peux runner des inférences pendant des heures sans savoir que ton GPU sert à rien.
type: journal
links:
  - "[[rocm-6-4-2-pas]]"
  - "[[detecter-si-ollama-run-sur]]"
  - "[[le-silent-failure-pattern-des]]"
  - "[[rocm-smi-verifier-l-usage]]"
  - "[[vs-code-debugger-eviter-le]]"
---
C'est le pire type de bug: pas d'erreur, juste... de la lenteur. J'ai genre tourné plusieurs models pendant un moment avant de tilter que quelque chose clochait. Le silent failure, c'est vicieux parce que tu cherches des problèmes dans ton prompt ou ton model, pas dans ton backend. Check ton GPU utilization first, always.
