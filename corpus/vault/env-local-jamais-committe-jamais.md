---
title: .env local jamais committé jamais
summary: Les variables d'environnement comme API keys, ports et secrets vivent dans un .env dans le .gitignore — aucune exception, même pour un projet solo.
type: reference
links:
  - "[[api-key-dans-le-header]]"
  - "[[port-mapping-dev-3000-prod]]"
  - "[[ssl-avec-let-s-encrypt]]"
  - "[[heberger-chez-moi-plutot-que]]"
---
J'ai eu un moment de fatigue où j'ai failli committer le .env juste pour tester. Je l'ai pas fait, good. Un .env.example avec les clés à remplir mais pas les valeurs, c'est tout ce qui va dans le repo. Les bonnes habitudes ça se cultive même quand c'est juste toi le seul dev.
