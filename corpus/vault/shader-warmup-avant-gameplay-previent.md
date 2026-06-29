---
title: Shader warmup avant gameplay prévient les hitches
summary: Appeler ShaderVariantCollection.WarmUp() pendant un loading screen force la compilation synchrone des variants critiques pis ça élimine les stalls de shader compile en plein gameplay.
type: lesson
links:
  - "[[shader-compile-stall-rdna4-c]]"
  - "[[shader-variant-explosion-ca-compile]]"
  - "[[async-shader-compilation-evite-les]]"
  - "[[shader-feature-vs-multi-compile]]"
  - "[[frametime-en-ms-plus-utile]]"
---
L'idée c'est de lister toutes les shader variants que ton jeu va utiliser dans une ShaderVariantCollection, pis de warmup pendant que le joueur voit un loading screen — là un hitch de 2 secondes, personne s'en fout. Sans ça, les variants compilent la première fois qu'ils sont rendus en gameplay, pis t'as un hitch visible. Faut maintenir la collection à jour quand tu rajoutes des keywords ou des materials.
