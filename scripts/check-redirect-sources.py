#!/usr/bin/env python3
"""Local pre-publication check: redirect sources must be evidenced public URLs."""
import json
from pathlib import Path
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


def check(migration, evidence):
    public_paths = {unquote(item['path']).casefold() for item in evidence['paths']}
    errors = []
    for category in ('redirects', 'retired', 'unresolved'):
        for item in migration.get(category, []):
            if unquote(item['from']).casefold() not in public_paths:
                errors.append(f"{category}: {item['from']} has no original-public-URL evidence")
    for post_id in migration.get('queryRedirects', {}):
        if post_id not in evidence['postIds']:
            errors.append(f'queryRedirects: {post_id} has no original published-post evidence')
    return errors


def main():
    inventory = json.loads((ROOT / 'src/data/common/original-public-urls.json').read_text())
    units = sys.argv[1:] or list(inventory)
    errors = []
    count = 0
    for unit in units:
        if unit not in inventory:
            errors.append(f'{unit}: no original public source inventory')
            continue
        migration = json.loads((ROOT / f'src/data/units/{unit}/url-migration.json').read_text())
        errors.extend(f'{unit}: {error}' for error in check(migration, inventory[unit]))
        count += len(migration.get('redirects', []))
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'PASS: {count} redirects across {len(units)} sites use evidenced original public URLs; retired, unresolved and query sources checked too.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
