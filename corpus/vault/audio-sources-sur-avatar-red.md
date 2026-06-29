---
title: Audio Sources sur Avatar: Red Flag CPU
summary: Les audio sources actives sur les avatars consomment du CPU processing à chaque frame pour tout le monde dans l'instance, pis ça s'accumule vite en monde peuplé.
type: lesson
links:
  - "[[particle-systems-sur-avatars-cpu]]"
  - "[[vram-budget-en-instance-de]]"
  - "[[physbones-chains-complexes-saignent-le]]"
  - "[[frametime-perf-rank-pour-les]]"
---
Un avatar qui loop une musique ambient 24/7 c'est un grief en communauté, mais même au-delà du social aspect, c'est du CPU pour tout le monde dans l'instance. VRChat a des protections contre les audio sources trop fortes, mais le processing overhead existe quand même. Si t'as besoin d'un effet sonore sur ton avatar, utilise-le triggered et local only si possible.
