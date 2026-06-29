---
title: Config JSON OSC par avatar — auto-généré
summary: VRChat génère un fichier JSON de config OSC par avatar dans AppData qui liste tous ses params avec leurs types — pratique pour auto-découvrir les params sans les hardcoder.
type: reference
links:
  - "[[avatar-parameters-le-namespace-avatar]]"
  - "[[avatar-swap-reset-tous-les]]"
  - "[[avatar-expressions-vs-custom-params]]"
  - "[[build-un-bridge-desktop-architecture]]"
---
VRChat génère ce fichier dans AppData/LocalLow/VRChat/VRChat/OSC/{userID}/Avatars/{avatarID}.json et il liste tous les params de l'avatar courant avec leurs types et addresses complètes. Way plus pratique que de décompiler un avatar pour trouver les noms des params. Ton app peut le lire au startup pour construire son dictionnaire de params dynamiquement — zero hardcoding.
