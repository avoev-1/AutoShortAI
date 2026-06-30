# Installer Architecture

Installers are made from `InstallPlan` and `InstallStep` contracts.

## Install Modes

- developer mode
- local user mode
- Studio launcher mode
- minimal CLI mode
- headless worker mode
- device node mode

Each mode must be verifiable and reversible where possible.
