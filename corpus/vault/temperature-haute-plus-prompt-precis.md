---
title: Temperature Haute Plus Prompt Précis Paradoxe
summary: Augmenter la temperature nécessite des prompts plus précis pour éviter le chaos — temperature et prompt clarity doivent scaler ensemble, pas indépendamment.
type: lesson
links:
  - "[[system-prompt-loi-du-monde]]"
  - "[[persona-system-prompt-stay-in]]"
  - "[[few-shot-trois-a-cinq]]"
  - "[[json-force-avec-schema-inline]]"
  - "[[think-false-reasoning-models-reponse]]"
---
Le mythe: temperature haute = créativité libre, prompt vague = ça va quand même marcher. La réalité: plus la temperature est haute, plus le model a besoin d'un prompt constrainé pour rester dans les rails. Temperature 0 c'est déterministe et pardonne un prompt mediocre; temperature 1 avec un prompt vague c'est un slot machine. Pour de la créativité controlled, high temp plus contraintes précises dans le prompt. Pour de l'extraction ou classification, temperature 0 ou near-0 tout le temps.
