---
title: Struct layout pis cache locality
summary: Accéder à des données éparpillées en mémoire cause des cache misses — regrouper les données hot ensemble dans des structs améliore drastiquement la perf CPU.
type: reference
links:
  - "[[les-gc-allocs-causent-des]]"
  - "[[object-pooling-pour-eviter-les]]"
  - "[[burst-compiler-pour-les-loops]]"
  - "[[micro-benchmark-le-piege-du]]"
---
Un cache miss sur x64 coûte genre 100-300 cycles d'attente — pour des tight loops, ça change complètement le ballpark. Le pattern Data-Oriented Design (DOT/ECS) est entièrement basé sur ce principe. En Unity classique, avoir des classes avec plein de fields dont tu uses juste 2 dans le hot path, c'est du gaspillage de cache pur.
