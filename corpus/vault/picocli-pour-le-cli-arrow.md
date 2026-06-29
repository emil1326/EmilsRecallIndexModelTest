---
title: Picocli pour le CLI Arrow
summary: Arrow CLI est construit avec picocli qui génère le help text pis le tab completion automatiquement depuis les annotations sur les command classes, c'est propre.
type: reference
links:
  - "[[gradle-multi-module-structure-de]]"
  - "[[config-yaml-avec-override-par]]"
  - "[[emilswork-branding-dans-les-modules]]"
  - "[[arrow-outil-java-ne-d]]"
---
`@Command`, `@Option`, `@Parameters` sur les classes pis picocli s'occupe du parsing, de la validation des types pis du error messaging. Le GraalVM native image support de picocli est un bonus si je veux ever ship un binary standalone. Aucun regret sur ce choix.
