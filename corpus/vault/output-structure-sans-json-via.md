---
title: Output Structure Sans JSON Via Markdown
summary: Quand JSON est overkill, forcer une structure markdown avec des headers fixes est plus lisible pour les humains et quasi aussi facile à parser en code.
type: reference
links:
  - "[[json-force-avec-schema-inline]]"
  - "[[json-schema-system-exemple-user]]"
  - "[[max-tokens-strict-controler-output]]"
  - "[[few-shot-trois-a-cinq]]"
  - "[[separators-dans-prompt-eviter-confusion]]"
---
Pas tout les outputs ont besoin d'être du JSON pur — si c'est un output semi-structuré que des humains vont lire aussi, markdown avec des headers fixes (`## Summary`, `## Action Items`) c'est souvent mieux. C'est plus facile à prompt (juste montrer un exemple) pis les LLMs le suivent bien. Regex-parse les sections si t'as besoin d'en extraire en code. Pragmatique > puriste.
