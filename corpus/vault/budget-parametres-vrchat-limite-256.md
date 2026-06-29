---
title: Budget paramètres VRChat limite 256 bits
summary: VRChat impose un budget total de 256 bits pour les synced parameters; dépasser ça pis le SDK refuse d'upload carrément.
type: reference
links:
  - "[[bool-int-float-choisir-bon]]"
  - "[[synced-vs-unsynced-parametres-difference]]"
  - "[[pack-bool-en-int-economiser]]"
  - "[[avatar-parameter-driver-changer-params]]"
---
Chaque Bool prend 1 bit, Int et Float prennent 8 bits chacun dans le budget synced. Y'a aussi un hard cap de 128 paramètres au total, peu importe le coût en bits. C'est la vraie contrainte pour les avatars full-featured avec des tonnes de toggles — planifie tôt ou tu vas regretter.
