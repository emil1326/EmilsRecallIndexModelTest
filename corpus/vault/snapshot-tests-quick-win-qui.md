---
title: Snapshot tests: quick win qui devient un nightmare
summary: Les snapshot tests sont du quick win pour UI mais finissent par être updatés aveuglément avec --updateSnapshot sans vérifier si le changement était intentionnel.
type: lesson
links:
  - "[[quand-delete-un-test-moins]]"
  - "[[code-coverage-la-metrique-qui]]"
  - "[[regression-tests-ecrire-le-test]]"
  - "[[setup-teardown-garder-ca-minimal]]"
---
La tentation c'est de --updateSnapshot sans vraiment checker le diff parce que c'est trop gros pour reviewer sérieusement. Passé un certain point les snapshots deviennent du bruit dans ton repo — t'updates aveuglément, git log dit 'chore: update snapshots', pis personne sait si c'était intentionnel. Bon pour bootstrapper une UI, pas pour maintenir du code long terme. C'est plate tbh.
