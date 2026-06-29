---
title: Singleton vs DI dans Unity, ownership
summary: Le Singleton en Unity c'est simple mais le ownership de qui crée et détruit l'instance devient flou fast, DI force à être explicite sur la lifetime.
type: lesson
links:
  - "[[scriptableobject-vs-monobehaviour-le-vrai]]"
  - "[[build-by-need-pas-by]]"
  - "[[quand-abstraire-vs-quand-hardcoder]]"
  - "[[ecs-vs-oop-pour-les]]"
---
J'ai eu des crashes subtils parce qu'un Singleton se faisait accéder dans OnDestroy après que la scène était unloadée — le classic null ref tardif. L'avantage du DI c'est que la lifetime est déclarée explicitement, mais le setup overhead dans Unity est réel tsu. Pour les petits projets, un Singleton bien gardé avec un instance check propre c'est fine. Pour du code partagé entre scènes, pense à DI ou au moins un Service Locator explicite.
