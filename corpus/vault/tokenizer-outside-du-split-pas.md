---
title: Tokenizer outside du split, pas dedans
summary: Fitter un tokenizer — BPE, WordPiece, vocab — sur le full corpus avant de splitter c'est du leakage soft: le modèle bénéficie de stats du test set dans son vocabulaire.
type: lesson
links:
  - "[[leakage-train-test-le-vrai]]"
  - "[[sources-cachees-de-leakage-insidieux]]"
  - "[[augmentation-et-leakage-combo-subtil]]"
  - "[[reproductibilite-end-to-end-du]]"
---
Dans la pratique, fitter le vocab sur le full corpus versus seulement le train change peu les résultats sur les benchmarks classiques, mais c'est conceptuellement pas propre. Pour des expériences rigoureuses ou des papiers académiques, le tokenizer doit être fitté sur le train set only — la règle c'est la règle. En prod, c'est moins critique parce que le tokenizer est souvent pretrained sur un corpus externe de toute façon. Mais faut être conscient de la distinction pour savoir quand ça compte.
