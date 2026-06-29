# AutoShortAI ZIP10 — Auto-Learning Adaptation Engine

ZIP10 defines the architecture contracts for controlled learning and adaptive improvement inside AutoShortAI.

This release does **not** implement a heavy machine-learning system and does **not** allow uncontrolled automatic mutation of the project. It introduces the interfaces, data models, policies, hooks, templates and structure tests required for future implementation by Claude.

## Purpose

ZIP10 connects ZIP09 analytics with ZIP07 creative strategy.

It allows AutoShortAI to:

- interpret cross-platform analytics feedback,
- generate learning insights,
- suggest creative profile adjustments,
- compare experiment variants,
- store learning memory locally,
- apply safety and confidence policies,
- prepare future semi-automatic adaptation.

## Non-negotiable project rule

AutoShortAI is platform-agnostic.

YouTube Shorts is the first priority, but the architecture must support TikTok, Instagram Reels, Facebook Reels, Snapchat Spotlight, X/Twitter video and future platforms through adapters, providers and capability contracts.

No ZIP10 class may hard-code a single platform as the only supported target.

## Main modules

- `autoshortai.learning.models`
- `autoshortai.learning.contracts`
- `autoshortai.learning.engine`
- `autoshortai.learning.adaptation`
- `autoshortai.learning.memory`
- `autoshortai.learning.experiments`
- `autoshortai.learning.policies`
- `autoshortai.learning.confidence`
- `autoshortai.learning.bridge`
- `autoshortai.learning.hooks`

## Installation

Run from the AutoShortAI repository root:

```bash
bash ~/Bureau/Projects/Archives/AutoShortAI_ZIP10_Auto_Learning_Adaptation_Engine/INSTALL.sh
bash ~/Bureau/Projects/Archives/AutoShortAI_ZIP10_Auto_Learning_Adaptation_Engine/VERIFY.sh
```

## Git commit convention

```bash
git commit -m "feat(zip10): auto learning adaptation engine"
```
