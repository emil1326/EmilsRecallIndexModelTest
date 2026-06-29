---
title: Le coût réel du fallback silencieux en prod
summary: Un fallback CPU non-détecté en prod veut dire des inférences 10x-20x plus lentes, des timeouts, une UX brisée — et toi qui cherches un bug applicatif qui existe pas.
type: lesson
links:
  - "[[le-silent-failure-pattern-des]]"
  - "[[ollama-fallback-cpu-silencieux-danger]]"
  - "[[rocm-smi-verifier-l-usage]]"
  - "[[cpu-inference-lent-mais-au]]"
---
Le vrai coût c'est pas juste la lenteur — c'est le temps perdu à chercher le problème au mauvais endroit. Tu vas tune ton prompt, tu vas check tes connections réseau, tu vas reboot ton service... alors que le problème c'est juste que le GPU est pas utilisé. Monitorer le GPU actif comme step 1 du debug save énormément de temps à long terme.
