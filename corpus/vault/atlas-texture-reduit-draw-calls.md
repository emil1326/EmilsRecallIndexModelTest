---
title: Atlas Texture Réduit Draw Calls Drastiquement
summary: Merger plusieurs textures en un seul atlas avec une seule material peut réduire les draw calls d'un avatar de 10x, c'est honnêtement le move le plus impactant.
type: lesson
links:
  - "[[material-slots-brisent-le-gpu]]"
  - "[[budget-realiste-moins-de-24]]"
  - "[[textures-4k-et-vram-budget]]"
  - "[[dxt-vs-astc-compression-texture]]"
---
Le principe: si tout ton avatar partage la même texture atlas, Unity peut potentiellement batcher les draw calls ensemble. En pratique avec VRChat, tu vas souvent avoir une material pour le body, une pour les cheveux, une pour les accessoires au max. C'est moins parfait que 1 seule material totale, mais ça reste un step up énorme vs 12 materials séparées.
