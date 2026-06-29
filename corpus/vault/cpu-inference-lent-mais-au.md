---
title: CPU inférence: lent mais au moins ça marche
summary: Runner des LLMs sur CPU c'est douloureux niveau perf, mais ça reste fonctionnel pour des petits models — utile comme fallback pendant le debug GPU.
type: journal
links:
  - "[[frametime-comme-preuve-que-le]]"
  - "[[ollama-fallback-cpu-silencieux-danger]]"
  - "[[ollama-0-30-11-fix]]"
  - "[[le-cout-reel-du-fallback]]"
---
Pendant que je figurais out le ROCm/gfx1201 mess, j'ai quand même pu tester des petits models sur CPU. Un 3B parameter model sur CPU c'est... utilisable, genre 2-4 t/s selon le hardware. Un 7B+ c'est de la torture. Mais au moins tu sais que le model est bon, que le prompt marche, pis que le seul problème c'est le backend GPU.
