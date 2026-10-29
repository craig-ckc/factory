#!/usr/bin/env python3
"""Check Factory's maintained packaging contracts without provider dependencies."""
import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote


def check(root):
    root = Path(root).resolve()
    plugin = root / 'plugins/factory'
    errors = []
    versions = set()
    for relative in ('plugin.json', '.claude-plugin/plugin.json', '.cursor-plugin/plugin.json'):
        path = plugin / relative
        try:
            value = json.loads(path.read_text())
            if value.get('name') != 'factory' or not re.fullmatch(r'\d+\.\d+\.\d+', value.get('version', '')):
                errors.append(f'{path.relative_to(root)}: invalid name/version')
            versions.add(value.get('version'))
        except (ValueError, OSError) as exc:
            errors.append(f'{path}: {exc}')
    if len(versions) != 1:
        errors.append('Plugin versions differ across agent manifests')
    for relative in ('.agents/plugins/marketplace.json', '.claude-plugin/marketplace.json', '.cursor-plugin/marketplace.json'):
        try:
            value = json.loads((root / relative).read_text())
            if value.get('name') != 'factory-local' or len(value.get('plugins', [])) != 1:
                errors.append(f'{relative}: unexpected marketplace identity or entries')
            for entry in value.get('plugins', []):
                source = entry.get('source')
                location = source.get('path') if isinstance(source, dict) else source
                if entry.get('name') != 'factory' or not isinstance(location, str) or (root / location).resolve() != plugin:
                    errors.append(f'{relative}: plugin source does not resolve to shared Factory tree')
        except (ValueError, OSError) as exc:
            errors.append(f'{relative}: {exc}')
    skills = sorted(plugin.glob('skills/*/SKILL.md'))
    if len(skills) != 17:
        errors.append(f'Expected 17 skills; found {len(skills)}')
    for path in skills:
        text = path.read_text()
        match = re.match(r'\A---\nname: ([a-z0-9-]+)\ndescription: (.+)\n---\n', text)
        if not match or match.group(1) != path.parent.name:
            errors.append(f'{path.relative_to(root)}: invalid flat skill metadata')
    for path in list(plugin.rglob('*.md')) + [root / 'README.md']:
        if not path.is_file():
            errors.append(f'Missing {path}')
            continue
        # Maintained Markdown links only; fenced example code is not a link contract.
        text = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if '://' in target or target.startswith(('#', 'mailto:')):
                continue
            target = unquote(target.split('#', 1)[0].strip('<>'))
            if target and not (path.parent / target).exists():
                errors.append(f'{path.relative_to(root)}: broken link {target}')
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    errors = check(args.root)
    print(json.dumps({'verdict': 'FAIL' if errors else 'PASS', 'errors': errors}, indent=2))
    return bool(errors)


if __name__ == '__main__':
    sys.exit(main())
