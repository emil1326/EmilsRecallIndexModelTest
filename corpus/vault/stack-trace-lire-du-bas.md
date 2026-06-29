---
title: Stack trace: lire du bas vers le haut
summary: Le stack trace se lit de bas en haut — le haut donne le symptôme, mais la cause racine est presque toujours plus bas.
type: reference
links:
  - "[[symptome-vs-cause-racine-pas]]"
  - "[[lire-le-message-d-erreur]]"
  - "[[les-assumptions-non-validees-causent]]"
  - "[[le-bug-est-parfois-dans]]"
---
La plupart des devs lisent le premier message pis partent chercher là. La root cause est presque toujours plus bas dans le stack. Cherche le premier frame dans TON code (pas dans une lib externe), c'est là que tu devrais commencer à investiguer, pas dans les entrailles de React ou whatever.
