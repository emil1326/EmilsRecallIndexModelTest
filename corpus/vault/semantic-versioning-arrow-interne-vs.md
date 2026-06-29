---
title: Semantic versioning Arrow interne vs externe
summary: Arrow utilise le semantic versioning pour les releases publiques mais un build number interne incrémental pour tracker les builds de dev, les deux coexistent sans conflict.
type: lesson
links:
  - "[[gradle-multi-module-structure-de]]"
  - "[[gradle-dependency-locking-evite-surprises]]"
  - "[[arrow-roadmap-evolue-par-besoin]]"
  - "[[gradle-build-cache-game-changer]]"
---
La version Gradle dans `build.gradle` c'est le semver public genre `1.2.0-SNAPSHOT`. Le build number interne est généré à compile time depuis un counter dans `gradle.properties` pis embedé dans le JAR manifest. Ça permet de distinguer deux builds du même semver quand je debug une regression.
