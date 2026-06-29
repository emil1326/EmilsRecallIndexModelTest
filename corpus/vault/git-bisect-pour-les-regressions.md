---
title: Git bisect pour les régressions mystérieuses
summary: Git bisect automatise la bisection binaire sur l'historique des commits pour identifier exactement quel commit a introduit une régression, c'est magique.
type: reference
links:
  - "[[la-bisection-coupe-le-debug]]"
  - "[[changer-une-seule-variable-par]]"
  - "[[garder-un-journal-des-hypotheses]]"
  - "[[symptome-vs-cause-racine-pas]]"
---
Tu lui dis juste 'ce commit-ci est bon, ce commit-là est cassé' pis git bisect fait le checkout automatique des commits intermédiaires pour toi. En O(log n) commits testés, t'as ton coupable. C'est underused comme outil, genre vraiment — la plupart des devs savent que ça existe pis le font pas.
