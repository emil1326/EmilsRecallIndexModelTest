---
title: VRChat API: instance type = source of truth
summary: L'instance type retourné par l'API VRChat, c'est ce qui détermine si le feature checker gate ou non, pas le nombre de joueurs ni autre chose.
type: reference
links:
  - "[[feature-checker-gate-les-toggles]]"
  - "[[la-logique-de-gate-fallback]]"
  - "[[trust-hierarchy-instance-type-prime]]"
  - "[[private-world-toggle-libre-peu]]"
  - "[[archi-feature-checker-api-osc]]"
---
VRChat expose l'instance type via son API, pis c'est littéralement le seul check fiable pour savoir si on est dans un public world. Friends+ ou Invite = on s'en fout moins, Public = le gate kick in. C'est pas grandiose comme système mais ça fit pour les besoins réels.
