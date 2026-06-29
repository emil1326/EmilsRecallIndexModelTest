---
title: Pimax driver lock bloque les updates AMD
summary: Le driver Pimax est locké sur une version AMD spécifique — updater le stack AMD pour ROCm brise le VR, un tradeoff vraiment frustrant à gérer.
type: journal
links:
  - "[[driver-pimax-40h-de-debug]]"
  - "[[rocm-6-4-2-pas]]"
  - "[[amd-driver-compatibility-et-rocm]]"
  - "[[ollama-0-30-11-fix]]"
  - "[[vs-code-settings-sync-pour]]"
---
Le Pimax a besoin de drivers AMD bien précis pour son runtime — et dès que tu touches à ça pour upgrader vers une version qui supporte mieux ROCm, ton headset plante. Pas de dual-boot propre, pas de workaround facile, juste un choix: VR ou AI local. J'ai décidé de pas toucher au driver AMD pour l'instant, voir la note sur le debug Pimax.
