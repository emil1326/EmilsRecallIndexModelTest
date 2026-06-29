---
title: Persona System Prompt Stay In Character
summary: Définir une persona précise avec des traits de style concrets dans le system prompt force le model à stay in character bien plus consistamment qu'une description floue.
type: lesson
links:
  - "[[system-prompt-loi-du-monde]]"
  - "[[franglais-prompt-output-franglais-garanti]]"
  - "[[system-prompt-sweet-spot-cinq]]"
  - "[[negative-few-shot-pour-casser]]"
  - "[[chain-of-thought-sans-extended]]"
---
"Tu es un assistant utile" c'est zero information. "Tu es un dev senior grognon qui répond en 2 phrases max et utilise pas d'emojis" — là le model a quelque chose à grab. Plus le persona est specific et opinionated, moins il drift au fil de la conversation. Le model a besoin d'anchors concrets; les descriptions génériques ça fit pour rien.
