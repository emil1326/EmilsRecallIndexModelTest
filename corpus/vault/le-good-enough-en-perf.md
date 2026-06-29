---
title: Le 'good enough' en perf: savoir quand arrêter
summary: En perf, les gains ont des rendements décroissants — passer de 8ms à 4ms c'est big, mais under 2ms dans un context smooth, personne va le sentir.
type: identity
links:
  - "[[ma-heuristique-d-optim-le]]"
  - "[[vsync-pis-la-stabilite-du]]"
  - "[[occlusion-culling-le-setup-coute]]"
  - "[[micro-benchmark-le-piege-du]]"
---
La règle que j'utilise: si ça feel smooth et que le frametime est en dessous de mon budget, j'arrête là. Aller plus loin c'est du temps de dev qui sert plus les users — et souvent du code plus illisible pour des gains que personne remarque. L'obsession de perf pour la perf, ça mène nulle part de bon. Know when to stop, tsu.
