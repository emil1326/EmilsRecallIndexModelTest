---
title: Feature flags comme roadmap tracker Arrow
summary: Arrow utilise des feature flags in-code pour tracker les features en développement, ce qui remplace un roadmap doc externe que j'aurais jamais maintenu.
type: reference
links:
  - "[[config-yaml-avec-override-par]]"
  - "[[arrow-roadmap-evolue-par-besoin]]"
  - "[[emilswork-branding-dans-les-modules]]"
  - "[[api-fluent-builder-pattern-arrow]]"
---
Chaque feature non-finale est wrappée dans un `ArrowFeatures.isEnabled(FEATURE_NAME)` check, pis les flags sont configurables via le YAML de config. C'est une façon cheap de garder track de ce qui est stable vs expérimental. La "roadmap" c'est basically la liste des flags disabled en prod.
