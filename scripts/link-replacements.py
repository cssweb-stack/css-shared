"""Find known obsolete external URLs in one unit; optionally update that unit."""
from pathlib import Path
from urllib.parse import urlsplit
import argparse
import json
import re

ROOT = Path(__file__).resolve().parents[1]
cli = argparse.ArgumentParser(description=__doc__)
cli.add_argument('unit', help='Unit repository abbreviation, for example soc')
cli.add_argument('--apply', action='store_true', help='Replace matches in the selected unit only')
args = cli.parse_args()
if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', args.unit):
    cli.error('Invalid unit abbreviation')
site = ROOT.parent / args.unit / 'src'
data = ROOT / 'src/data/units' / args.unit
if not site.is_dir() or not data.is_dir():
    cli.error('Unit source/data directory not found')
rules = json.loads((ROOT / 'src/data/common/url-replacements.json').read_text())['replacements']
files = sorted(site.rglob('*.html')) + sorted(data.glob('*.json'))
total = changed = 0
for path in files:
    before = text = path.read_text()
    for rule in rules:
        old = urlsplit(rule['from'])
        if rule.get('matchHttpHttpsAndWwwVariants'):
            host = re.escape(old.hostname.removeprefix('www.'))
            prefix = r'https?://(?:www\.)?' + host
        else:
            prefix = re.escape(old.scheme + '://' + old.netloc)
        # Match the whole old path; retain any query string or fragment.
        pattern = prefix + re.escape(old.path.rstrip('/')) + r'/?(?=[?#\s\"\'<>]|$)'
        text, count = re.subn(pattern, lambda _: rule['to'], text)
        if count:
            total += count
            print(f'{path.relative_to(ROOT.parent)}: {count} {rule["label"]}')
    if text != before:
        changed += 1
        if args.apply:
            path.write_text(text)
print(f'{"Updated" if args.apply else "Found"} {total} obsolete links in {changed} files for {args.unit}.')
raise SystemExit(0 if args.apply or not total else 1)
