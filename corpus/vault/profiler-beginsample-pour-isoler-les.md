---
title: Profiler.BeginSample pour isoler les hotspots
summary: Wrapper tes sections de code avec Profiler.BeginSample/EndSample permet de voir exactement quel bout prend combien de ms dans le Unity Profiler.
type: reference
links:
  - "[[les-gc-allocs-causent-des]]"
  - "[[cpu-bottleneck-pis-gpu-bottleneck]]"
  - "[[ma-heuristique-d-optim-le]]"
  - "[[micro-benchmark-le-piege-du]]"
---
Sans ça, le profiler te montre des gros blobs vagues genre "Update" à 8ms pis tu sais pas où chercher. Avec les samples customs, tu peux drill down jusqu'au call précis qui coûte cher. Faut juste penser à les strip en build release sinon tu pénalises ton propre perf — le conditional compile avec UNITY_EDITOR ou un define custom, c'est la voie.
