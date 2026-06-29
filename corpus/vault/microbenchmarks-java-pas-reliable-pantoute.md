---
title: Microbenchmarks Java pas reliable pantoute
summary: Les microbenchmarks JMH sur Arrow donnent des chiffres satisfaisants mais ils reflètent rarement la réalité en production à cause du JIT warmup pis du GC imprévisible.
type: lesson
links:
  - "[[off-heap-memory-pas-worth]]"
  - "[[in-memory-store-bati-sur]]"
  - "[[lazy-rebuild-arrow-se-declenche]]"
  - "[[refactor-arrow-savoir-quand-arreter]]"
---
J'ai passé du temps à optimiser des hot paths basé sur des benchmarks JMH pis en vrai application le gain était dans le noise. Le JIT va compiler pis recompiler ce qu'il veut, pis la GC pause peut tripler ta latence sans prévenir. Je me fie plus aux end-to-end timings avec des vraies données.
