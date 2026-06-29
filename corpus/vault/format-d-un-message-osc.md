---
title: Format d'un message OSC — address pis args
summary: Un message OSC c'est une address path genre /avatar/parameters/NomParam suivie d'args typés (float, bool, int) — super simple à parser si tu sais quoi chercher.
type: reference
links:
  - "[[avatar-parameters-le-namespace-avatar]]"
  - "[[types-de-params-osc-vrchat]]"
  - "[[chatbox-api-osc-chatbox-input]]"
  - "[[lib-osc-existante-vs-implementation]]"
---
L'address OSC c'est juste un string genre /avatar/parameters/MyParam, suivi d'un ou plusieurs arguments selon le type. Le format binaire c'est: header, address string null-padded à un multiple de 4 bytes, puis les args — documenté mais vraiment léger. T'as besoin de vraiment pas grand chose pour parser ça manuellement, c'est pour ça que je comprends pas pourquoi les gens instalent des libs énormes pour ça.
