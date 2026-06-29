---
title: max_tokens Strict Contrôler Output Length
summary: Setter un max_tokens raisonnable force le model à être concis et évite les outputs verbeux qui coûtent cher en tokens et diluent complètement l'info utile dedans.
type: reference
links:
  - "[[context-window-compter-tokens-avant]]"
  - "[[think-false-reasoning-models-reponse]]"
  - "[[reasoning-budget-cout-eleve-gain]]"
  - "[[json-force-avec-schema-inline]]"
  - "[[output-structure-sans-json-via]]"
---
Par défaut, les models vont souvent générer plus que nécessaire parce que leur training les pousse à couvrir thoroughly. Mettre max_tokens à 200-300 pour des responses courtes attendues force le model à prioriser l'essentiel. Attention: pas trop bas sinon il va truncate en plein milieu d'une phrase — trouver le sweet spot selon la task. Combiner avec "réponds en 3 phrases max" dans le prompt double l'effet.
