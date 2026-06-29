---
title: Static batching vs dynamic batching: quand choisir
summary: Le static batching combine les meshes au build time (zéro CPU overhead runtime), le dynamic batching les combine chaque frame — ce qui a un cost CPU non négligeable.
type: reference
links:
  - "[[draw-calls-le-vrai-cost]]"
  - "[[texture-streaming-pis-vram-bandwidth]]"
  - "[[gpu-overdraw-pis-fill-rate]]"
  - "[[les-gc-allocs-causent-des]]"
---
Le dynamic batching a une réputation de fix magique mais c'est souvent pire que le problème, surtout si les meshes sont un peu gros. Le static batching, lui, gonfle la VRAM parce que les meshes combinés sont gardés en mémoire séparément. Faut choisir selon si tes objets bougent ou pas, tsu — et checker dans le Frame Debugger que le batch se fait vraiment.
