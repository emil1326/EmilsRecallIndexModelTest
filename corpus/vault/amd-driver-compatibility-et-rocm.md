---
title: AMD driver compatibility et ROCm stack
summary: Le driver AMD userspace (amdgpu-pro ou open-source) et la version ROCm doivent être compatible — un mismatch peut empêcher ROCm de voir ton GPU correctement.
type: reference
links:
  - "[[pimax-driver-lock-bloque-les]]"
  - "[[rocm-version-pinning-blessing-ou]]"
  - "[[rocm-smi-verifier-l-usage]]"
  - "[[driver-pimax-40h-de-debug]]"
  - "[[physics-fixedupdate-le-cost-cache]]"
---
ROCm dépend du KFD (Kernel Fusion Driver) et du userspace HIP runtime — si ton driver kernel-side est trop vieux par rapport à ta version ROCm, ou vice-versa, t'as des surprises. L'install ROCm officielle d'AMD gère ça, mais si t'as un driver pinné pour une autre raison (genre Pimax...) tu peux avoir un mismatch silencieux. Vérifier avec rocm-smi --showversion.
