---
title: API auth qui a le droit de call le feature checker
summary: L'API du feature checker a besoin d'un système d'auth pour que seuls les apps légitimes puissent la call — sinon n'importe qui peut spoof les checks.
type: reference
links:
  - "[[archi-feature-checker-api-osc]]"
  - "[[website-dashboard-de-config-pour]]"
  - "[[osc-app-le-middleware-local]]"
  - "[[createur-liability-pourquoi-le-gate]]"
---
La question c'est: comment tu fais confiance à l'OSC app qui call l'API? Il faut un token ou une key que le créateur reçoit quand il configure son avatar sur le website. L'OSC app l'utilise pour s'authentifier. Simple mais nécessaire pour éviter le spoofing.
