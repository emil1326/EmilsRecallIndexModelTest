---
title: API fluent builder pattern Arrow
summary: L'API publique d'Arrow utilise un fluent builder pattern pour la config du store, genre `Arrow.builder().withTTL(60000).withReplication(3).build()`, c'est lisible pis chainable.
type: reference
links:
  - "[[checked-exceptions-arrow-les-evite]]"
  - "[[config-yaml-avec-override-par]]"
  - "[[replication-factor-3-comme-defaut]]"
  - "[[emilswork-branding-dans-les-modules]]"
---
C'est plus verbose qu'un constructeur simple mais l'autocomplete IDE aide beaucoup pis c'est auto-documenté. Le builder valide les paramètres avant le `build()` pis throw un `ArrowConfigException` si quelque chose est incompatible. Plus agréable à utiliser que passer 8 paramètres dans un constructeur smh.
