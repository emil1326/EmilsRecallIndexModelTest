---
title: Micro-benchmark: le piège du JIT warmup
summary: Benchmarker du C# sans warm-up rounds va mesurer le JIT compile time plutôt que les performances réelles de ton code — les premiers runs sont toujours plus lents.
type: lesson
links:
  - "[[profiler-beginsample-pour-isoler-les]]"
  - "[[les-gc-allocs-causent-des]]"
  - "[[burst-compiler-pour-les-loops]]"
  - "[[ma-heuristique-d-optim-le]]"
---
En pratique, la première exécution d'une méthode en .NET peut être genre 10-100x plus lente que les suivantes à cause du JIT. Pour benchmarker correctement, faut des warm-up iterations before de collecter les samples. BenchmarkDotNet handle ça automatiquement si tu veux être rigoureux — sinon tes chiffres sont juste wrong et tu prends des mauvaises décisions d'optim.
