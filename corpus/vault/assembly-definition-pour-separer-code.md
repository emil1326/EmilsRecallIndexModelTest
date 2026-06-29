---
title: Assembly definition pour séparer code Editor du runtime
summary: Tout code editor doit être dans un .asmdef séparé avec la platform Editor — sinon les types UnityEditor leakent dans le build runtime pis ça explose.
type: reference
links:
  - "[[missing-editor-namespace-casse-le]]"
  - "[[module-first-design-versus-monolith]]"
  - "[[customeditor-vs-editorwindow-quand-choisir]]"
  - "[[emilswork-suite-de-tools-modulaires]]"
---
C'est une des premières choses à configurer sérieusement quand on fait des editor tools — le dossier "Editor" sans .asmdef ça marche en projet mais dès qu'on build le runtime ça explose. Pour EmilsWork chaque module a son .asmdef editor versus runtime, ça garde les dépendances clean pis le build time est meilleur aussi. Faut juste pas oublier de référencer les assemblies dont t'as besoin.
