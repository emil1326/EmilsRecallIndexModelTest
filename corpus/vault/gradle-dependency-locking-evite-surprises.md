---
title: Gradle dependency locking évite surprises
summary: Arrow utilise le dependency locking Gradle pour pin les versions exactes des dépendances transitives, ce qui évite les surprises de build quand une dépendance change en background.
type: reference
links:
  - "[[gradle-multi-module-structure-de]]"
  - "[[serialization-jackson-vs-kryo-dans]]"
  - "[[gradle-build-cache-game-changer]]"
  - "[[semantic-versioning-arrow-interne-vs]]"
---
Sans locking, `implementation 'com.fasterxml.jackson.core:jackson-databind:2.+'` peut résoudre à une version différente sur une autre machine. Le `gradle dependencies --write-locks` génère un `gradle.lockfile` par module que je commit. On update délibérément avec `--update-locks`, pas par surprise.
