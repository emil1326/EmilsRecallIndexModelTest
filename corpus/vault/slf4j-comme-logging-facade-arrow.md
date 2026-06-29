---
title: SLF4J comme logging facade Arrow
summary: Arrow logue avec SLF4J comme facade et Logback comme implementation par défaut, ce qui laisse le consumer choisir son backend sans changer le code Arrow.
type: reference
links:
  - "[[config-yaml-avec-override-par]]"
  - "[[gradle-multi-module-structure-de]]"
  - "[[checked-exceptions-arrow-les-evite]]"
  - "[[junit5-testcontainers-pour-tests-integration]]"
---
C'est le pattern standard pour les libraries Java et Arrow se comporte en library embedded-friendly, pas en application standalone hardcodée. Le `logback.xml` dans les resources est un default raisonnable que le consumer peut overrider avec son propre classpath. No brainer vraiment.
