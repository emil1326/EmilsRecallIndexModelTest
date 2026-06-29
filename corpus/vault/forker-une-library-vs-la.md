---
title: Forker une library vs la wrapper
summary: Wrapper une library préserve la capacité de recevoir les updates upstream, forker donne un contrôle total mais crée une dette de maintenance permanente.
type: reference
links:
  - "[[custom-parser-vs-json-yaml]]"
  - "[[monorepo-vs-multi-repo-pour]]"
  - "[[rebuild-from-scratch-vs-refactor]]"
  - "[[build-by-need-pas-by]]"
---
La règle: si le changement que tu veux faire est un bug fix ou un edge case, essaie de contribuer upstream ou wrapper. Si c'est un changement fondamental de behavior incompatible avec le design intent de la library, fork. J'ai forké une library une fois pensant que je maintiendrais le sync avec upstream — spoiler: j'ai jamais merge un seul upstream commit après. Un fork c'est une promesse à toi-même que tu tiendras rarement.
