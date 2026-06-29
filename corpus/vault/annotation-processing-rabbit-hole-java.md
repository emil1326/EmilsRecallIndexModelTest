---
title: Annotation processing rabbit hole Java
summary: J'ai essayé d'ajouter un annotation processor custom dans Arrow pour générer du boilerplate pis j'ai perdu deux jours dans les entrailles de `javax.annotation.processing`, c'était intense.
type: journal
links:
  - "[[gradle-multi-module-structure-de]]"
  - "[[api-fluent-builder-pattern-arrow]]"
  - "[[refactor-arrow-savoir-quand-arreter]]"
  - "[[arrow-roadmap-evolue-par-besoin]]"
---
Le `AbstractProcessor` API est correct mais le setup avec Gradle pour que ça compile dans le bon ordre c'est un cauchemar de classpath. J'ai fini par abandon ça au profit de Lombok pour les cas simples. Le custom processor est encore dans le code mais commenté, genre reminder que j'ai essayé xD.
