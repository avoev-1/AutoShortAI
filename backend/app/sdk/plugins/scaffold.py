from pathlib import Path


def scaffold_plugin(root: Path, plugin_type: str, plugin_name: str) -> Path:
    safe_name = plugin_name.lower().replace(" ", "_").replace("-", "_")
    plugin_dir = root / plugin_type / safe_name
    plugin_dir.mkdir(parents=True, exist_ok=True)

    manifest_path = plugin_dir / "manifest.json"
    readme_path = plugin_dir / "README.md"

    if not manifest_path.exists():
        manifest_path.write_text(
            '{\n'
            f'  "plugin_id": "{plugin_type}.{safe_name}",\n'
            f'  "name": "{plugin_name}",\n'
            f'  "plugin_type": "{plugin_type}",\n'
            '  "version": "0.1.0",\n'
            '  "entrypoint": "replace.me:Plugin",\n'
            '  "description": "Generated plugin scaffold.",\n'
            '  "permissions": [],\n'
            '  "capabilities": [],\n'
            '  "dependencies": [],\n'
            '  "enabled": false\n'
            '}\n',
            encoding="utf-8",
        )

    if not readme_path.exists():
        readme_path.write_text(f"# {plugin_name}\n\nGenerated plugin scaffold.\n", encoding="utf-8")

    return plugin_dir
