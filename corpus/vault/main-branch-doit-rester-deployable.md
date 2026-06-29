---
title: Main branch doit rester deployable toujours
summary: Main/master doit être deployable à tout moment — si quelqu'un pull main pis ça compile pas ou les tests passent pas, c'est une urgence, pas un 'je fixerai ça demain'.
type: lesson
links:
  - "[[branch-naming-feature-hotfix-chore]]"
  - "[[no-verify-c-est-toujours]]"
  - "[[hotfix-branch-part-toujours-de]]"
  - "[[draft-pr-pour-early-feedback]]"
  - "[[tags-semantiques-sur-chaque-release]]"
---
Ça implique: branch protection rules sur GitHub (require PR + status checks avant merge), jamais de commit direct sur main, pis CI obligatoire. Le truc c'est que si main est toujours stable, t'as une baseline de confiance — n'importe qui peut brancher de là pis savoir que ça part de quelque chose de sain. J'ai travaillé sur des projets où main était constamment cassé pis c'est épuisant, genre tout le monde passe son temps à debug l'environnement.
