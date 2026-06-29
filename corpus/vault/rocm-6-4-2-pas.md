---
title: ROCm 6.4.2 pas encore sur gfx1201
summary: ROCm 6.4.2 reconnaît pas encore officiellement le chip RDNA4 gfx1201, ce qui fait qu'Ollama fall back sur CPU sans aucun avertissement visible.
type: lesson
links:
  - "[[ollama-fallback-cpu-silencieux-danger]]"
  - "[[ollama-0-30-11-fix]]"
  - "[[rdna4-gfx1201-encore-trop-neuf]]"
  - "[[detecter-si-ollama-run-sur]]"
---
gfx1201, c'est la nouvelle archi RDNA4 — encore trop fraîche pour que le ROCm stack l'ait intégrée dans la 6.4.2. Résultat: mon GPU flambant neuf se tournait les pouces pendant qu'Ollama transpirait sur le CPU. Aucun message d'erreur, juste des inférences au ralenti pis une question genre 'mais pourquoi c'est si lent?'
