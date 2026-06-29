---
title: Checked exceptions Arrow les évite
summary: Arrow wrap toutes les checked exceptions Java en unchecked `ArrowException` custom, parce que forcer les callers à catch des IOExceptions partout c'est une ergonomie de merde.
type: lesson
links:
  - "[[api-fluent-builder-pattern-arrow]]"
  - "[[slf4j-comme-logging-facade-arrow]]"
  - "[[serialization-jackson-vs-kryo-dans]]"
  - "[[in-memory-store-bati-sur]]"
---
Java checked exceptions c'est controversé mais pour une library ça force les gens à écrire des try-catch vides juste pour que ça compile, c'est du bruit. `ArrowException` extends `RuntimeException`, elle a un `ErrorCode` enum pour catégoriser. Si quelqu'un veut catch explicitly, il peut, mais c'est son choix.
