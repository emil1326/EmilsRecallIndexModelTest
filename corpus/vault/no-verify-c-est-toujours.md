---
title: --no-verify c'est toujours une mauvaise idée
summary: Skip les hooks avec --no-verify parce que les tests passent pas, c'est juste se tirer dans le pied plus tard — les hooks existent pour une raison.
type: lesson
links:
  - "[[main-branch-doit-rester-deployable]]"
  - "[[un-commit-une-seule-idee]]"
  - "[[draft-pr-pour-early-feedback]]"
  - "[[conventional-commits-format-feat-fix]]"
  - "[[pr-review-c-est-plus]]"
---
Genre t'as un pre-commit hook qui run le linter pis les tests, pis là t'as hâte de push, fait que tu fais --no-verify. Classic. Sauf que maintenant le CI va catch exactement le même problème pis t'auras perdu du temps pour rien. Fix le problème, commit proprement — c'est pas long pis tu dormiras mieux. J'ai été tata une ou deux fois avec ça, plus jamais.
