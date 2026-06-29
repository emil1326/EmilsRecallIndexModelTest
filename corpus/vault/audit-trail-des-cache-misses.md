---
title: Audit trail des cache misses pour diagnostiquer
summary: Logger chaque cache miss avec le fichier, la raison (expired, invalid, missing) et le temps de rebuild permet de diagnostiquer les patterns d'invalidation qui font trop de misses.
type: reference
links:
  - "[[cache-hit-rate-la-vraie]]"
  - "[[debug-mode-devrait-bypass-le]]"
  - "[[cascade-invalidation-quand-un-leaf]]"
  - "[[reapply-des-security-rules-apres]]"
---
Sans ce logging, impossible de savoir si les misses viennent d'une strategy d'invalidation trop agressive, d'un bug dans le dependency tracking, ou juste de fichiers légitimement souvent modifiés. Un petit dashboard — même juste des stats CLI — qui montre les top-10 fichiers qui causent des cache misses c'est un game changer pour le debug. Ça prend une heure à implémenter et ça sauve des journées.
