---
title: Shader variant baking upfront ou runtime
summary: Bake les shader variants upfront pour éviter les hitches runtime, mais ça coûte du build time pis nécessite de savoir tes variants à l'avance.
type: reference
links:
  - "[[frametime-beats-fps-pour-decider]]"
  - "[[savoir-quand-killer-un-rabbit]]"
  - "[[hard-coded-vs-data-driven]]"
  - "[[build-by-need-pas-by]]"
---
Les hitches à la première utilisation d'un shader c'est une des pires expériences pour le joueur — ça feel comme un freeze random. Bake upfront règle ça mais ton build pipeline devient way plus long pis tu dois maintenir une liste de variants. Si ton jeu est experimental et que les variants changent souvent, le runtime compile avec un pre-warm au load peut être plus pragmatique. J'ai galéré avec ça pas mal avant de settle on un hybrid approach.
