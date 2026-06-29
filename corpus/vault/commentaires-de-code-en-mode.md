---
title: Commentaires de code en mode oral pas documentation
summary: Emil écrit ses commentaires de code comme il parlerait à un collègue — casual, direct, avec le pourquoi — pas comme une doc technique formelle.
type: reference
links:
  - "[[le-franglais-c-est-pas]]"
  - "[[prose-en-paragraphes-jamais-en]]"
  - "[[ton-corporate-dans-les-reviews]]"
  - "[[code-review-honnete-ou-pas]]"
---
Un commentaire utile explique pourquoi une décision a été prise, pas juste ce que le code fait (ça se voit). Genre : "// cached ici parce que le rebuild était trop slow on-demand" > "// cache the value". Si ça prend un ton trop formel, Emil le réécrit instinctivement — c'est un réflexe.
