---
title: CustomEditor vs EditorWindow: quand choisir quoi
summary: CustomEditor c'est pour customiser l'Inspector d'un Component ciblé, EditorWindow c'est pour des tools standalone avec leur propre state — les mélanger inutilement c'est de l'over-engineering.
type: reference
links:
  - "[[editorwindow-lifecycle-onenable-pas-onawake]]"
  - "[[aac-applicator-le-probleme-que]]"
  - "[[textmesh-wrapper-pourquoi-wrapper-tmp]]"
  - "[[pourquoi-imgui-reste-le-choix]]"
---
La règle générale tsu: si t'édites les propriétés d'un objet sélectionné → CustomEditor. Si t'as besoin d'un outil indépendant avec son propre state → EditorWindow. Dans EmilsWork les deux coexistent selon le besoin — l'AAC Applicator c'est une EditorWindow mais les settings TextMesh c'est un CustomEditor.
