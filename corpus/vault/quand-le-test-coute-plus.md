---
title: Quand le test coûte plus que le bug
summary: Y'a des cas où écrire le test prend plus de temps que le bug aurait pris à fixer — faut savoir quand skip pis move on.
type: lesson
links:
  - "[[quand-delete-un-test-moins]]"
  - "[[regression-tests-ecrire-le-test]]"
  - "[[code-coverage-la-metrique-qui]]"
  - "[[valider-le-test-loop-en]]"
---
Le testing ça a un coût réel en temps pis en maintenance, pis des fois ce coût dépasse la valeur du test. Pour un prototype throwaway ou un script one-off qui va mourir dans une semaine, forcer le TDD c'est du overkill. La question c'est: est-ce que ce code va vivre assez longtemps pour que ce test paye back son coût d'écriture pis de maintenance?
