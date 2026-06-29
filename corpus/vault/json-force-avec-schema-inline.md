---
title: JSON Forcé Avec Schema Inline Explicit
summary: Inclure le JSON schema exact inline dans le prompt avec les types pis les noms de fields réduit drastiquement les hallucinations de structure en output.
type: reference
links:
  - "[[json-schema-system-exemple-user]]"
  - "[[output-structure-sans-json-via]]"
  - "[[system-prompt-loi-du-monde]]"
  - "[[max-tokens-strict-controler-output]]"
  - "[[separators-dans-prompt-eviter-confusion]]"
---
Juste dire "réponds en JSON" c'est insuffisant — le model va inventer les field names à sa guise pis ça va être un mess en prod. Colle le schema complet dans le prompt: `{"name": string, "score": number}`. Encore mieux si t'utilises les structured outputs d'Anthropic/OpenAI qui forcent le format au niveau du sampling. Le lazy "output JSON please" ça marche pas pantoute de façon fiable.
