---
title: Gradle build cache game changer Arrow
summary: Activer le Gradle build cache dans Arrow a coupé les rebuild times de moitié en réutilisant les outputs de tâches déjà compilées qui n'ont pas changé.
type: lesson
links:
  - "[[gradle-multi-module-structure-de]]"
  - "[[gradle-dependency-locking-evite-surprises]]"
  - "[[lazy-rebuild-arrow-se-declenche]]"
  - "[[semantic-versioning-arrow-interne-vs]]"
---
`org.gradle.caching=true` dans `gradle.properties`, pis le build cache local s'active. Les tâches `compileJava` et `test` sont cachables si les inputs changent pas. En pratique quand je switch de branches pour tester quelque chose pis je reviens, tout recompile pas, c'est un gain de qualité de vie non négligeable.
