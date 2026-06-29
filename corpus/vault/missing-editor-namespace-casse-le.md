---
title: Missing Editor namespace casse le build runtime
summary: Un using UnityEditor dans du code non protégé par #if UNITY_EDITOR ou un assembly Editor-only casse le build standalone — message d'erreur pas toujours clair.
type: lesson
links:
  - "[[assembly-definition-pour-separer-code]]"
  - "[[module-first-design-versus-monolith]]"
  - "[[editorwindow-lifecycle-onenable-pas-onawake]]"
  - "[[emilswork-suite-de-tools-modulaires]]"
---
J'ai eu ce bug tellement de fois tsu — t'oublies un seul using UnityEditor quelque part dans du runtime code pis le build explose. La solution propre c'est les assembly definitions séparées, mais dans le pire cas un #if UNITY_EDITOR wrap ça. C'est la première chose à checker quand un build qui marchait hier plante aujourd'hui.
