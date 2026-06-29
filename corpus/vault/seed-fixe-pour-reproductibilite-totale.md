---
title: Seed fixe pour reproductibilité totale
summary: Fixer la seed partout — Python random, NumPy, PyTorch, sklearn — c'est la base pour que les splits pis les résultats soient reproductibles entre runs.
type: reference
links:
  - "[[seeds-differents-par-librairie-attention]]"
  - "[[reproductibilite-end-to-end-du]]"
  - "[[logger-le-split-avec-seed]]"
  - "[[shuffle-avant-le-split-toujours]]"
---
Y'a plusieurs sources de random indépendantes dans un pipeline ML, pis oublier une seule ruine tout. Faut set `random.seed(42)`, `np.random.seed(42)`, `torch.manual_seed(42)` pis même `PYTHONHASHSEED=42` en env var. Si tu fais du multi-GPU, `torch.cuda.manual_seed_all(42)` aussi — oublie pas celle-là. 42 c'est la convention la plus répandue, mais franchement n'importe quoi de fixe fait le job du moment que c'est loggé.
