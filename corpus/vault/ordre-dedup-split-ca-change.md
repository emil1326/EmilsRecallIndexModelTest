---
title: Ordre dedup/split: ça change tout
summary: Dedupliquer avant de splitter c'est la seule façon correcte — faire le dedup après peut créer des splits débalancés pis surtout des near-dupes qui restent entre train et test.
type: lesson
links:
  - "[[dedup-exact-sur-hash-md5]]"
  - "[[minhash-lsh-pour-dedup-fuzzy]]"
  - "[[shuffle-avant-le-split-toujours]]"
  - "[[augmentation-et-leakage-combo-subtil]]"
  - "[[leakage-train-test-le-vrai]]"
---
Si tu splittes d'abord pis dédup après, tu pourrais te retrouver avec des splits de tailles très différentes de ce que t'avais prévu. Pire, si un groupe de near-duplicates est split entre train et test, tu vas en garder un dans chaque — c'est exactement le leakage que tu voulais éviter. Le pipeline correct c'est: `collect → clean → dedup → shuffle → split → augment (train seulement)`. Cet ordre-là c'est pas négociable, tsé.
