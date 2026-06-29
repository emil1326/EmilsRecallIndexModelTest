---
title: Blueprint ID contrôle quel avatar se overwrite
summary: Le blueprint ID dans le pipeline descriptor détermine exactement quel slot VRChat tu vas overwrite — se tromper de ID c'est catastrophique si t'as un avatar public live.
type: lesson
links:
  - "[[sdk2-mort-sdk3-only-maintenant]]"
  - "[[private-build-avant-tout-upload]]"
  - "[[compte-vrchat-secondaire-pour-qa]]"
  - "[[semantic-versioning-dans-les-filenames]]"
  - "[[reducing-build-time-avec-asset]]"
  - "[[build-from-real-need-pas]]"
---
Genre t'as ben des chances d'écraser ton avatar public avec un WIP si tu swappes pas le blueprint ID avant de build. Bonne pratique: garder un fichier txt avec tous tes IDs catégorisés (public/private/test) quelque part dans le projet. J'ai appris ça à la dure, smh.
