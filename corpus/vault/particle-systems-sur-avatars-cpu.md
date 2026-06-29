---
title: Particle Systems sur Avatars: CPU Danger
summary: Les particle systems actifs sur un avatar coûtent du CPU à chaque frame pour tout le monde dans l'instance, pas juste le owner de l'avatar.
type: lesson
links:
  - "[[audio-sources-sur-avatar-red]]"
  - "[[physbones-chains-complexes-saignent-le]]"
  - "[[vram-budget-en-instance-de]]"
  - "[[frametime-perf-rank-pour-les]]"
---
C'est le truc que les gens réalisent pas assez: en VRChat, tu render les avatars des autres toi-même côté client. Donc les particle systems de quelqu'un d'autre tournent sur ton GPU et CPU. Un avatar avec des particules constant-émission bling bling c'est un grief avatar déguisé en esthétique, smh. Limiter les particle systems à des effets triggered (pas always-on) c'est la décision correcte.
