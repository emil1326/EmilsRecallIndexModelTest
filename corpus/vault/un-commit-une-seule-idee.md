---
title: Un commit = une seule idée
summary: Un commit atomique ça veut dire une et une seule chose changée — si ton message de commit a un 'et', t'as probablement deux commits à faire.
type: lesson
links:
  - "[[message-de-commit-a-l]]"
  - "[[wip-commits-a-squasher-avant]]"
  - "[[git-bisect-pour-trouver-le]]"
  - "[[interactive-rebase-cleanup-avant-pr]]"
  - "[[squash-commits-avant-merge-dans]]"
---
Le truc c'est que quand tu reviewes ou que tu fais un git bisect plus tard, les commits atomiques sont infiniment plus utiles que des gros blobs de changements. J'ai eu des fois où j'ai commité genre 'refactor + fix bug + update styles' dans le même commit pis je me suis maudit moi-même trois semaines après. Discipline de base mais c'est facile à oublier quand t'es dans le flow.
