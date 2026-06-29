---
title: Website: dashboard de config pour le créateur
summary: Le website dans l'archi sert d'interface de configuration — le créateur y setup quelles features de son avatar sont conditionnelles et selon quels critères.
type: reference
links:
  - "[[archi-feature-checker-api-osc]]"
  - "[[granularite-conditionnelle-feature-par-feature]]"
  - "[[unity-side-integration-point-clean]]"
  - "[[createur-liability-pourquoi-le-gate]]"
  - "[[avatar-expressions-vs-custom-params]]"
---
Le créateur va sur le site, il link son avatar, pis il configure par feature: autorisé en public ou pas. Ces settings sont stockés server-side pis l'OSC app les fetch via l'API. Ça évite d'avoir à tout configurer dans Unity à chaque update.
