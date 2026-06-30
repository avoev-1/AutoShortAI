# ZIP19 Architecture — Cross-Platform Packaging & Installer

Core principles preserved from previous ZIP releases:

- AutoShortAI is not a SaaS.
- AutoShortAI remains local-first and personal-software-first.
- The complete software must stay platform-agnostic: YouTube Shorts is the first target, not the only target.
- The core must never become tied to one platform, one provider, one OS, one cloud, one database, one UI, one renderer, one app store, or one device class.
- Every ZIP must stay backward compatible with previous ZIPs.
- Architecture comes from ZIP releases; implementation must follow the ZIP-defined contracts.
- Claude implements code later, but must not invent incompatible architecture.
- Guardian Engine rules from ZIP15 must be used as an implementation checklist before and after future work.
- Secrets and credentials are protected by ZIP18 and must never be packaged or written into installers.
- Adult / X creator workflows are dedicated opt-in restricted workflows, isolated from the core and governed by age, consent, policy, review, storage, and credential rules.
- Heavy dependencies must be optional and module-scoped, never forced globally.

## Architectural Position

ZIP19 is the installation, packaging, dependency, migration, and launcher layer.

It packages modules without becoming the runtime core and without deciding product behavior.

```text
Architecture Modules
        ↓
Packaging Profiles
        ↓
Installer Profiles
        ↓
Dependency Checks
        ↓
Security / Guardian Verification
        ↓
Local Installable App
```

## 1. Packaging Core

Core contracts:

- `PackageManifest`
- `PackageTarget`
- `PackageProfile`
- `PackageBuild`
- `PackageArtifact`
- `PackageValidationResult`
- `InstallerProfile`

Supported targets prepared by architecture:

- `windows_desktop`
- `linux_desktop`
- `macos_desktop`
- `portable_cli`
- `developer_mode`
- `headless_worker`
- `device_node_package`

The core must not hard-code one OS, app store, installer technology, or desktop UI framework.

## 2. Installer Architecture

Installer modes:

- developer installation
- local user installation
- remote worker installation
- device node installation
- local dashboard / Studio installation
- minimal CLI installation

Contracts:

- `InstallerRuntime`
- `InstallPlan`
- `InstallStep`
- `InstallResult`
- `InstallRequirement`
- `InstallVerification`

Installers should be plan-driven and verifiable. Claude should implement small safe installers first, not a large opaque installer.

## 3. Dependency Manager

Dependencies must be optional unless required by the selected module profile.

Examples:

- Python base runtime
- FFmpeg optional for rendering pack
- Git optional for developer mode
- Node optional for future UI pack
- OS keyring optional for vault providers
- GPU tools optional for rendering / AI acceleration
- device tools optional for device farm pack

Contracts:

- `DependencySpec`
- `OptionalDependency`
- `DependencyCheck`
- `DependencyResolutionPlan`
- `SystemCapability`

Rule:

```text
Nothing heavy becomes mandatory because one optional feature needs it.
```

## 4. Platform Profiles

OS profiles:

- `WindowsPackageProfile`
- `LinuxPackageProfile`
- `MacOSPackageProfile`
- `PortablePackageProfile`
- `HeadlessWorkerProfile`

Each profile defines:

- local config path
- workspace path
- cache path
- logs path
- secrets provider preference
- file permissions
- launcher commands
- desktop integration readiness

## 5. Local App Launcher

Launcher modes:

- `studio`
- `cli`
- `worker`
- `headless`
- `guardian`
- `safe_mode`

Contracts:

- `AppLauncher`
- `LaunchProfile`
- `LaunchCommand`
- `RuntimeMode`
- `StartupCheck`

The launcher starts modules through contracts. It does not own business logic.

## 6. Module Installation Profiles

Module packs:

- `core_only`
- `creator_studio`
- `rendering_pack`
- `ai_worker_pack`
- `publishing_pack`
- `device_farm_pack`
- `restricted_creator_pack`
- `developer_pack`

Each pack declares dependencies, permissions, optional tools, workspace needs, and security requirements.

## 7. Restricted / Adult Creator Pack Packaging

Adult / X creator workflows are a real dedicated future category, but remain opt-in and isolated.

ZIP19 prepares:

- `restricted_creator_pack`
- opt-in installation
- disabled by default
- isolated workspace profile
- isolated credential scope through ZIP18
- isolated log profile
- policy checks before pack enablement
- manual review by default

Rules:

- no adult functionality enabled by default
- no adult credentials included
- no illegal explicit examples
- no mixing with general content
- consent metadata required
- all participants 18+ required

## 8. Update & Migration Readiness

Update contracts:

- `MigrationPlan`
- `MigrationStep`
- `RollbackPlan`
- `VersionCompatibilityCheck`
- `UpgradeReport`

Migrations must preserve ZIP01-ZIP18 compatibility and use Guardian checks before destructive actions.

## 9. Build Profiles

Build profiles:

- dev build
- local beta build
- portable build
- worker build
- studio build
- minimal CLI build

Contracts:

- `BuildProfile`
- `BuildTarget`
- `BuildArtifact`
- `BuildReport`
- `BuildValidation`

## 10. Packaging Verification

Packaging verification must check:

- required files exist
- imports are valid
- optional dependencies are not forced
- no secret files are packaged
- no credentials are embedded
- OS profiles are declared
- restricted creator pack disabled by default
- Guardian compatibility is preserved

## 11. Hooks

ZIP19 defines plugin-first hooks:

- `before_package_build`
- `after_package_build`
- `before_installer_created`
- `after_installer_created`
- `before_dependency_checked`
- `after_dependency_checked`
- `before_migration_run`
- `after_migration_run`
- `before_package_verified`
- `after_package_verified`

## Integration with Previous ZIPs

```text
ZIP11 = dashboard / Studio vision
ZIP12 = rendering pipeline
ZIP13 = AI worker runtime
ZIP14 = device farm deployment
ZIP15 = Guardian Engine
ZIP16 = multi-platform publishing runtime
ZIP17 = local workspace / media library
ZIP18 = security / secrets / credentials vault
ZIP19 = cross-platform packaging and installer architecture
```
