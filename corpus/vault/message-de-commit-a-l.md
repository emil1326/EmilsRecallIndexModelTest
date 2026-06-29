---
title: Message de commit à l'impératif présent
summary: Les messages de commit s'écrivent à l'impératif présent ('Add feature', pas 'Added feature') parce que ça décrit ce que le commit fait quand on l'applique.
type: reference
links:
  - "[[conventional-commits-format-feat-fix]]"
  - "[[un-commit-une-seule-idee]]"
  - "[[wip-commits-a-squasher-avant]]"
  - "[[pr-review-c-est-plus]]"
  - "[[interactive-rebase-cleanup-avant-pr]]"
---
La convention vient de git lui-même — les commits auto-générés par git merge ou git revert utilisent l'impératif. 'Fix null pointer in shader loader' plutôt que 'Fixed null pointer' ou 'Fixes null pointer'. Ça peut sembler un détail de merde mais dans un historique dense ça crée une cohérence qui aide vraiment à scanner. Pis ça force à décrire l'action précise pas juste 'update stuff'.
