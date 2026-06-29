---
title: Asset filenames branding présent toujours
summary: Les noms de fichiers d'assets Unity (ScriptableObjects, prefabs, shaders) incluent le branding Emils pour éviter les collisions pis rendre l'origine du fichier claire dans n'importe quel projet.
type: reference
links:
  - "[[identifiers-code-sans-espaces-ni]]"
  - "[[quiet-branding-trouvable-dans-chaque]]"
  - "[[emilswork-namespace-complet-dans-unity]]"
  - "[[emilswork-toujours-au-long-jamais]]"
  - "[[abreviations-dans-les-identifiers-non]]"
---
Un fichier EmilsAACData.asset ou EmilsFeatureConfig.asset c'est immédiatement identifiable dans un folder plein d'autres assets. C'est pas juste du vanity branding, ça sert à éviter des conflits de noms dans des projets qui importent plusieurs packages. Naming collision c'est chiant, pis c'est évitable.
