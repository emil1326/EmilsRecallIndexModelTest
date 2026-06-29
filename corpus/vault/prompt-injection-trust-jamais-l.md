---
title: Prompt Injection Trust Jamais L'Input Raw
summary: Ne jamais passer du contenu user non-sanitizé directement dans un prompt avec des instructions critiques — le prompt injection peut override ton system prompt facilement.
type: lesson
links:
  - "[[system-prompt-pas-d-infos]]"
  - "[[xml-tags-pour-delimiter-sections]]"
  - "[[system-prompt-loi-du-monde]]"
  - "[[separators-dans-prompt-eviter-confusion]]"
  - "[[context-window-compter-tokens-avant]]"
---
Si ton app prend un input user pis le stuff directement dans le prompt sans sanitization, un user malicieux peut écrire "ignore previous instructions and..." pis potentiellement bypasser tes guardrails. C'est le XSS des LLMs en gros. Délimite toujours l'input user avec des XML tags ou des quotes claires, pis entraîne le model à ignorer les instructions dans le contenu user. C'est pas optional en prod.
