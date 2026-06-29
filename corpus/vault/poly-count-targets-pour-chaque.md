---
title: Poly count targets pour chaque performance rank
summary: VRChat rank Good c'est sous 70k triangles, Medium sous 150k — au-delà de 70k t'es déjà dans le territory où beaucoup de users vont se hider automatiquement.
type: reference
links:
  - "[[performance-rank-cible-pour-avatars]]"
  - "[[fallback-avatar-requis-pour-safety]]"
  - "[[dynamic-bones-dead-physbones-only]]"
  - "[[avatar-cloning-risk-avec-les]]"
  - "[[thumbnail-vrchat-pris-in-world]]"
  - "[[budget-parametres-vrchat-limite-256]]"
---
En pratique pour un avatar humanoid détaillé, 70k c'est tight mais faisable avec du LOD planning smart. Les accessories et les tails/wings c'est là que ça explose vite sans qu'on s'en aperçoive. Moi je vise genre 60-80k pour le main mesh pis j'assume que certains users verront le fallback — c'est acceptable.
