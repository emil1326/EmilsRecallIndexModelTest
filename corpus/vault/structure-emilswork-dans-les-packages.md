---
title: Structure EmilsWork dans les packages distribués
summary: Organiser les fichiers sous Assets/EmilsWork/NomDuPackage dans un .unitypackage c'est essentiel pour éviter les conflicts avec les projets existants des buyers.
type: reference
links:
  - "[[gumroad-comme-storefront-pour-packages]]"
  - "[[credits-dans-le-readme-d]]"
  - "[[semantic-versioning-dans-les-filenames]]"
  - "[[vcc-remplace-le-sdk-unity]]"
  - "[[content-warning-tag-obligatoire-pour]]"
---
Si tu balance tout à la racine d'Assets, tu risques de fuck up les projets des gens qui ont déjà d'autres packages installés. Un folder propre genre Assets/EmilsWork/MonAvatar/... c'est clean et ça évite le drama. C'est aussi ben plus facile à delete proprement si quelqu'un veut désinstaller.
