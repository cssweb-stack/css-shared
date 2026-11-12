"""Prepare a reviewable SCI people-only migration patch; never download images.

One-time import, not a synchronization command: refuse to overwrite site pages.
"""
from pathlib import Path
from urllib.parse import urlsplit, unquote
import xml.etree.ElementTree as E
import json, re, html, csv, io, random, hashlib
from wordpress_html import clean_html, no_h1, text

ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT.parent / 'sci'
UNIT = ROOT / 'src/data/units/sci'
SOURCE = ROOT / 'exports/sci/communicationandinformationsci.WordPress.2026-11-12.xml'
NS = {'w': 'http://wordpress.org/export/1.2/', 'c': 'http://purl.org/rss/1.0/modules/content/'}
items = E.parse(SOURCE).findall('./channel/item')
all_pages = [i for i in items if i.findtext('w:post_type', '', NS) == 'page']
def is_person(i):
    return any(c.get('nicename') in ['faculty', 'staff'] for c in i.findall('category'))
sources = [i for i in all_pages if is_person(i) and i.findtext('w:status', '', NS) == 'publish']
assert len(sources) == 30
def slug(i): return i.findtext('w:post_name', '', NS)
assert len({slug(i) for i in sources}) == len(sources)
programs = [
    {'id': 'communication', 'name': 'Communication'},
    {'id': 'communicology', 'name': 'Communicology'},
    {'id': 'journalism', 'name': 'Journalism'},
    {'id': 'library-and-information-science', 'name': 'Library and Information Science'},
    {'id': 'matsunaga-institute-for-peace', 'name': 'Matsunaga Institute for Peace'},
]
program_ids = {p['name']: p['id'] for p in programs}
destinations = {urlsplit(i.findtext('link')).path.rstrip('/'): '/faculty/' + slug(i) + '.html' for i in sources}
destinations.update({'/directory': '/directory/', '/privacy-policy': '/privacy.html'})
images = set(); unresolved = set(); files = {}; published = []; people = []; retention = {}
def link(value):
    value = html.unescape(value).strip(); u = urlsplit(value)
    key = '/' + unquote(u.path).strip('/')
    if u.netloc in ['sci.manoa.hawaii.edu', 'www.sci.manoa.hawaii.edu'] or (not u.scheme and not u.netloc and u.path):
        if key in destinations:
            return "{{ '" + destinations[key] + ('#' + u.fragment if u.fragment else '') + "' | url }}"
        value = value if u.netloc else 'https://sci.manoa.hawaii.edu/' + value.lstrip('/')
        unresolved.add(value)
    return html.escape(value, quote=True)
def add(path, value):
    path = Path(path)
    if path.exists() and str(path).startswith(str(SITE)):
        raise RuntimeError('Refusing to overwrite ' + str(path))
    files[str(path)] = value
def data(name, value): add(UNIT / name, json.dumps(value, ensure_ascii=False, indent=2) + '\n')
def page(url, title, body, person=None, description=None):
    name = 'index.html' if url == '/' else url.lstrip('/') + 'index.html' if url.endswith('/') else url.lstrip('/')
    front = {'layout': 'layouts/profiles/faculty-profile.njk' if person else 'shell.njk', 'title': title,
             'description': description or 'This will be the meta description.', 'permalink': url}
    if person: front['personSlug'] = person
    add(SITE / 'src' / name, '---\n' + ''.join(k + ': ' + json.dumps(v, ensure_ascii=False) + '\n' for k, v in front.items()) + '---\n' + body + '\n')
    published.append(url)
def section(body, gray=False):
    return '<div class="page-section' + (' page-section--gray' if gray else '') + '"><div class="container content-section"><div class="row gx-0 gx-sm-5 gx-lg-5"><div class="col-12">\n' + body + '\n</div></div></div></div>\n'
services = [('academia_url', 'Academia.edu'), ('google_scholar_url', 'Google Scholar'), ('orcid_url', 'ORCID'), ('researchgate_url', 'ResearchGate'), ('scopus_author_id_url', 'Scopus Author ID')]
for item in sources:
    fields = {m.findtext('w:meta_key', '', NS): m.findtext('w:meta_value', '', NS).strip() for m in item.findall('w:postmeta', NS)}
    kind = 'staff' if any(c.get('nicename') == 'staff' for c in item.findall('category')) else 'faculty'
    p = {'name': item.findtext('title'), 'lastName': fields['last_name'], 'slug': slug(item),
         'url': '/faculty/' + slug(item) + '.html', 'type': kind,
         'showInFacultyDirectory': kind == 'faculty', 'showInKeyContacts': False,
         'photo': '/media/shared/placeholders/temp.jpg', 'photoWidth': 500, 'photoHeight': 500,
         'title': fields['title_hr'], 'programs': []}
    roles = list(dict.fromkeys(fields[k] for k in ['title_gov', 'title_academic'] if fields.get(k)))
    if roles: p['roles'] = roles
    for k in ['office', 'email']:
        if fields.get(k): p[k] = fields[k]
    if fields.get('tel'):
        digits = re.sub(r'\D', '', fields['tel'])
        if len(digits) == 11 and digits.startswith('1'): digits = digits[1:]
        assert len(digits) == 10, (p['name'], digits)
        p.update(phone=f'({digits[:3]}) {digits[3:6]}-{digits[6:]}', phoneHref='+1' + digits)
    affiliations = []
    for key in ['program', 'program_2']:
        name = fields.get(key)
        if not name: continue
        if name in program_ids: p['programs'].append(program_ids[name])
        affiliations.append({'label': name, 'url': fields.get(key + '_url', '')})
    if affiliations: p['affiliations'] = affiliations
    if kind == 'faculty': assert p['programs'], p['name']
    for key, label in services:
        if fields.get(key): p.setdefault('publicationProfiles', []).append({'label': label, 'url': html.unescape(fields[key])})
    if fields.get('website_url'): p['websites'] = [{'label': 'Personal Website', 'url': html.unescape(fields['website_url'])}]
    if fields.get('scholars_url'): p.setdefault('additionalLinks', []).append({'label': 'Scholars', 'url': fields['scholars_url']})
    if fields.get('award'):
        award = fields['award']; match = re.search(r',\s*(\d{4})$', award)
        p['awards'] = [{'name': award[:match.start()] if match else award, **({'year': match[1]} if match else {})}]
    raw = item.findtext('c:encoded', '', NS)
    body = no_h1(clean_html(raw, link, images))
    # Record full normalized visible-text equality independently of wrappers/images.
    retention[slug(item)] = {'sourceCharacters': len(text(raw)), 'importedCharacters': len(text(body)), 'textPreserved': text(raw) == text(body)}
    if slug(item) == 'andrew-wertheimer':
        retention[slug(item)]['reviewNote'] = 'Only difference: removed the space before the comma following (minor). No words removed.'
    seo = re.search(r's:11:"description";s:\d+:"(.*?)";', fields.get('slim_seo', ''), re.S)
    page(p['url'], p['name'], body, p['slug'], html.unescape(seo[1]) if seo else None)
    people.append(p)
assert sum(p['type'] == 'faculty' for p in people) == 27
data('people.json', people); data('programs.json', programs)
jumps = '<nav aria-label="Directory groups"><ul>' + ''.join('<li><a href="#program-' + p['id'] + '">' + html.escape(p['name'].replace(' and ', ' & ')) + '</a></li>' for p in programs) + '<li><a href="#school-staff">School Staff</a></li></ul></nav>'
page('/directory/', 'School Directory', section('<h1>School Directory</h1>' + jumps) + section('{% include "layouts/profiles/program-directory.njk" %}', True))
page('/', 'School of Communication and Information', section('<h1>School of Communication and Information</h1><p><a href="{{ \'/directory/\' | url }}">Explore the school directory</a>.</p>'))
page('/privacy.html', 'Privacy Policy', '{% include "pages/privacy.njk" %}')
# Preserve the complete proposed navigation for the later full-site phase.
add(ROOT / 'exports/sci/navigation-before-people-phase.json', (UNIT / 'navigation.json').read_text())
data('navigation.json', [{'label': 'Home', 'url': '/'}, {'label': 'School Directory', 'url': '/directory/'}])
settings = json.loads((ROOT / 'src/data/units/wgss/site-settings.json').read_text())
settings.update(stylesheet='/sci.css', url='https://sci.manoa.hawaii.edu', openGraph=json.loads((UNIT / 'site-settings.json').read_text())['openGraph'])
data('site-settings.json', settings)
unit = json.loads((UNIT / 'unit-details.json').read_text()); unit['facultyBasePath'] = '/faculty/'; data('unit-details.json', unit)
students = sorted('/' + str(p.relative_to(ROOT / 'src')) for p in (ROOT / 'src/media/heroes/students').glob('*.webp'))
murals = sorted('/' + str(p.relative_to(ROOT / 'src')) for p in (ROOT / 'src/media/heroes/saunders-mural').glob('*.webp'))
rng = random.Random(1112); rng.shuffle(students); rng.shuffle(murals)
bio_urls = {p['url'] for p in people}
data('heroes.json', {'defaultHero': students[0], 'pages': {url: {'image': students[i % len(students)], 'position': 'center center', 'alt': 'Students at the University of Hawaiʻi at Mānoa', 'credit': False} for i, url in enumerate(published) if url not in bio_urls}})
data('faculty-heroes.json', {'pages': {p['url']: {'image': murals[i % len(murals)], 'position': 'center center', 'alt': 'Detail of the mural in Saunders Hall at the University of Hawaiʻi at Mānoa', 'credit': False} for i, p in enumerate(people)}})
for f in ['scripts/shared-bootstrap.mjs', 'scripts/shared-settings.mjs', 'scripts/shared-source.mjs', 'scripts/verify-site.py', 'eleventy.config.js', '.gitignore', 'AGENTS.md']:
    add(SITE / f, (ROOT.parent / 'wgss' / f).read_text())
pkg = json.loads((ROOT.parent / 'wgss/package.json').read_text()); pkg['name'] = 'sci'; pkg['scripts']['dev'] = 'eleventy --serve --port=8093'; add(SITE / 'package.json', json.dumps(pkg, indent=2) + '\n')
lock = json.loads((ROOT.parent / 'wgss/package-lock.json').read_text()); lock['name'] = 'sci'; lock['packages']['']['name'] = 'sci'; add(SITE / 'package-lock.json', json.dumps(lock, indent=2) + '\n')
add(SITE / 'shared.config.json', json.dumps({'repository': 'cssweb-stack/css-shared', 'ref': 'main', 'localPath': '../css-shared', 'unit': 'sci'}, indent=2) + '\n')
add(SITE / '.github/workflows/deploy.yml', (ROOT.parent / 'wgss/.github/workflows/deploy.yml').read_text().replace('WGSS', 'SCI').replace('/wgss/', '/sci/'))
inventory = io.StringIO(); writer = csv.writer(inventory); writer.writerow(['source_id', 'old_url', 'new_url', 'status'])
for item in all_pages:
    old = item.findtext('link'); destination = destinations.get(urlsplit(old).path.rstrip('/'), '')
    status = item.findtext('w:status', '', NS)
    writer.writerow([item.findtext('w:post_id', '', NS), old, destination if status == 'publish' else '', 'mapped' if destination and status == 'publish' else 'draft-excluded' if status != 'publish' else 'deferred'])
add(SITE / 'reference/url-inventory.csv', inventory.getvalue())
report = {'source': SOURCE.name, 'sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(), 'pages': len(published), 'coreFaculty': 27, 'staff': 3,
          'phase': 'People and grouped directory only; remaining school pages deferred.', 'youtubeEmbeds': {}, 'publishedUrls': published,
          'programCounts': {p['id']: sum(p['id'] in person['programs'] for person in people) for p in programs},
          'draftPeopleExcluded': [i.findtext('title') for i in all_pages if is_person(i) and i.findtext('w:status', '', NS) != 'publish'],
          'textRetention': retention, 'sourceImagesNotDownloaded': sorted(images), 'unmigratedSourceLinksKeptExternal': sorted(unresolved),
          'reviewNotes': ['Rich Gazan: export lists Professor and Program Chair, CIS; no third title supplied. Andrew Wertheimer is Program Director, LIS.', 'Ava Kikut-Stein: supplied Personal Website is a Google Sites edit URL; retained pending a public URL.', 'School staff have no program assignment in source metadata; kept in School Staff rather than inferring from office.']}
add(SITE / 'reference/migration-report.json', json.dumps(report, ensure_ascii=False, indent=2) + '\n')
add(SITE / 'README.md', '# SCI — people phase\n\nRun npm ci, then npm run dev. Preview http://localhost:8093/directory/.\nRun npm run build and npm run verify before publishing.\nShared people/program data, media and templates live in ../css-shared.\nOnly the directory, individual people pages and a minimal home/privacy page are built.\nOther school pages and final navigation are deferred. No remote, commit, push or deployment performed.\n')
print('*** Begin Patch')
for path, value in files.items():
    p = Path(path)
    if p.exists():
        print('*** Update File: ' + path + '\n@@')
        for line in p.read_text().splitlines(): print('-' + line)
    else: print('*** Add File: ' + path)
    for line in value.splitlines(): print('+' + line)
print('*** End Patch')
