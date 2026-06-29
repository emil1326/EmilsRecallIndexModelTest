---
title: ScriptableObject vs MonoBehaviour le vrai choix
summary: ScriptableObject pour les data containers et la config, MonoBehaviour pour le behaviour avec lifecycle Unity, mélanger les deux rôles c'est une dette garantie.
type: reference
links:
  - "[[singleton-vs-di-dans-unity]]"
  - "[[hard-coded-vs-data-driven]]"
  - "[[custom-editor-window-vs-inspector]]"
  - "[[quand-abstraire-vs-quand-hardcoder]]"
---
Le mistake classique c'est mettre du behaviour dans un ScriptableObject parce que "c'est pratique d'y accéder sans une instance dans la scene". Mais là tu perds l'encapsulation pis ça devient un God Object progressivement. La split rule que je suis: si ça a besoin de Update() ou de réagir à des Unity events, c'est un MonoBehaviour. Sinon, ScriptableObject. Ça semble basic mais c'est violé constamment dans les gros projets.
