---
title: VRChat instance types: la taxonomy complète
summary: VRChat a plusieurs types d'instances (Public, Friends+, Invite, Group, etc.) que le feature checker doit traiter différemment selon leur niveau d'ouverture au public.
type: reference
links:
  - "[[vrchat-api-instance-type-source]]"
  - "[[trust-hierarchy-instance-type-prime]]"
  - "[[private-world-toggle-libre-peu]]"
  - "[[la-logique-de-gate-fallback]]"
---
Public = gate immédiat. Friends+ et Friends Only = zone grise (des inconnus peuvent potentiellement être là via friends). Invite et Group = généralement safe. Le feature checker simplifie: Public = gate, tout le reste = check underage flag seulement. C'est une simplification mais workable.
