---
title: UdonSharp pour les worlds avec logique C# custom
summary: UdonSharp permet d'écrire la logique de world en C# type-safe plutôt qu'en Udon graph visuel — c'est way plus maintenable pour tout ce qui est complexe.
type: reference
links:
  - "[[vcc-remplace-le-sdk-unity]]"
  - "[[reducing-build-time-avec-asset]]"
  - "[[compte-vrchat-secondaire-pour-qa]]"
  - "[[blueprint-id-controle-quel-avatar]]"
  - "[[private-build-avant-tout-upload]]"
---
Le graph visuel Udon c'est bien pour des trucs simples mais ça scale vraiment pas — personne veut maintenir ça longterm. UdonSharp compile vers Udon bytecode, alors y'a zéro overhead au runtime. Le seul gotcha c'est les limitations du Udon sandbox qui te permettent pas de faire certains appels Unity normaux.
