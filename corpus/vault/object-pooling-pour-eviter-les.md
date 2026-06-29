---
title: Object pooling pour éviter les GC spikes
summary: Plutôt que d'instantier et détruire des objets continuellement, on recycle un pool pré-alloué — zéro GC pressure dans le hot path.
type: reference
links:
  - "[[les-gc-allocs-causent-des]]"
  - "[[struct-layout-pis-cache-locality]]"
  - "[[string-concat-dans-un-hot]]"
  - "[[burst-compiler-pour-les-loops]]"
---
Le pattern de base: une queue d'objets disabled, on pop quand on en a besoin, on push quand c'est fini. Unity a un ObjectPool<T> built-in depuis 2021, plus besoin de whip up le sien from scratch. La vraie gain c'est pas la vitesse d'instantiation — c'est l'absence de GC collect qui stall le main thread de façon imprévisible.
