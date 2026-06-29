---
title: Very Poor Avatar peut Outperformer Good Avatar
summary: Un avatar ranked Very Poor par VRChat peut avoir un meilleur frametime réel qu'un Good si les métriques qui comptent vraiment sont bien gérées.
type: lesson
links:
  - "[[frametime-perf-rank-pour-les]]"
  - "[[renderer-count-dans-le-perf]]"
  - "[[polycount-seuil-70k-tris-avatar]]"
  - "[[material-slots-brisent-le-gpu]]"
---
Le rank Very Poor se trigger souvent sur un seul critère hors seuil (ex: trop de bones) même si tout le reste est propre. C'est frustrant pis ça donne une image fausse, genre. Le frametime dans le Profiler, lui, il ment pas: si ton avatar à Very Poor est à 2ms et le Good d'un autre est à 6ms, tu sais qui est vraiment optimisé.
