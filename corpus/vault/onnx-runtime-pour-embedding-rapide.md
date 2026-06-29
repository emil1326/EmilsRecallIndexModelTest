---
title: ONNX runtime pour embedding rapide
summary: Exporter e5-small en ONNX permet d'utiliser onnxruntime pour l'inférence, beaucoup plus rapide que PyTorch en CPU-only — souvent 2-3x speedup sans GPU.
type: reference
links:
  - "[[e5-small-choisi-pour-le]]"
  - "[[batch-size-affecte-throughput-embedding]]"
  - "[[daemon-tourne-en-background-process]]"
  - "[[embedding-caching-pour-eviter-recalcul]]"
---
Pour un daemon background sans GPU, ONNX c'est le move. T'exportes le modèle une fois avec torch.onnx.export, pis après tu n'as plus besoin de PyTorch à runtime. Onnxruntime est plus léger, démarre plus vite, et profile mieux. C'est un peu de setup mais ça vaut vraiment.
