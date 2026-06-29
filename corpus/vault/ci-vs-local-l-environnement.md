---
title: CI vs local: l'environnement tue les tests
summary: Un test qui passe local mais fail en CI c'est presque toujours un problème d'environnement — paths absolus, variables d'env, timezone, ordre de fichiers.
type: lesson
links:
  - "[[tests-flaky-ils-pourrissent-tout]]"
  - "[[datetime-et-random-sources-de]]"
  - "[[test-isolation-chaque-test-son]]"
  - "[[valider-le-test-loop-en]]"
---
Le classique: 'works on my machine' — tests verts local, rouge en CI. C'est presque toujours un path absolu hardcodé, une variable d'env qui existe juste dans ton shell, un fichier qui traîne dans ton workspace local, ou un timezone. Tes tests doivent être hermétiques par rapport à l'environnement — si ça peut varier d'une machine à l'autre, ça doit être injectable.
