---
title: Fixtures: setup partagé, attention au coupling
summary: Les fixtures c'est du setup réutilisable entre tests — pratique pour la data complexe, mais une fixture trop grosse couple des tests qui devraient être indépendants.
type: reference
links:
  - "[[test-data-hardcode-ca-scale]]"
  - "[[test-isolation-chaque-test-son]]"
  - "[[setup-teardown-garder-ca-minimal]]"
  - "[[mocks-qui-masquent-le-vrai]]"
---
Une fixture bien faite c'est une dépendance explicite visible dans la signature du test — t'as pas à fouiller dans un setUp distant pour comprendre le state de départ. Quand tes fixtures sont trop grosses ou génériques, tes tests deviennent couplés à des détails qui les concernent pas pantoute. Genre avoir une fixture 'user complet avec abonnement actif' quand ton test check juste le format d'email, c'est du bruit inutile.
