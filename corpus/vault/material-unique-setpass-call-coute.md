---
title: Material unique SetPass call coûte côté CPU
summary: Chaque material unique dans une frame implique potentiellement un SetPass call côté CPU — c'est là que réside le vrai coût des materials nombreux, indépendamment du GPU.
type: lesson
links:
  - "[[material-count-pis-draw-calls]]"
  - "[[srp-batcher-batch-automatique-si]]"
  - "[[gpu-bound-vs-cpu-bound]]"
  - "[[draw-call-budget-selon-la]]"
  - "[[materialpropertyblock-evite-de-casser-le]]"
---
Un SetPass call c'est le CPU qui configure le render state pour le GPU: bind les textures, set les shader constants, configure le blending, etc. Si t'as 500 materials différents dans ta scène, tu paies 500 SetPass calls minimum. C'est pour ça que le SRP Batcher aide même sans réduire les draw calls — il réduit le SetPass overhead. Profiler ça avec Unity Frame Debugger qui breakdown les SetPass calls explicitement.
