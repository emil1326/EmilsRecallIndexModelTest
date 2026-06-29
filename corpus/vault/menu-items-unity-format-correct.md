---
title: Menu items Unity format correct
summary: Les menu items Unity utilisent le path 'Emil's Tools/Feature/Action' avec apostrophe — c'est user-facing donc la forme complète Emil's avec ponctuation c'est correct.
type: reference
links:
  - "[[emil-s-apostrophe-seulement-en]]"
  - "[[window-titles-affichent-emil-s]]"
  - "[[emilswork-namespace-complet-dans-unity]]"
  - "[[display-string-vs-code-identifier]]"
---
MenuItem("Emil's Tools/AAC/Applicator") c'est le bon pattern pour les custom editor menus. L'user voit 'Emil's Tools' dans la barre de menu pis c'est clair pis branded. La string du MenuItem c'est user-facing donc on suit la convention avec apostrophe, pas la convention identifier.
