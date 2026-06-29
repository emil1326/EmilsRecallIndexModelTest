---
title: Instruction Fin De Prompt Meilleur Recall
summary: Les instructions critiques en fin de user message sont mieux suivies que celles au début — le recency effect joue clairement en ta faveur sur la plupart des models.
type: lesson
links:
  - "[[few-shot-ordering-exemples-recents]]"
  - "[[system-prompt-loi-du-monde]]"
  - "[[xml-tags-pour-delimiter-sections]]"
  - "[[system-prompt-sweet-spot-cinq]]"
  - "[[separators-dans-prompt-eviter-confusion]]"
---
C'est le même principe que le few-shot ordering — ce qui est vu en dernier a plus de pull. Si t'as une instruction importante genre "réponds en moins de 100 mots" ou "termine par une question", mets-la en fin de message, pas en header. J'ai testé ça empiriquement et le delta est assez consistent pour que ça change mes habitudes de prompt writing. Le "lost in the middle" problem c'est réel, faut pas l'ignorer.
