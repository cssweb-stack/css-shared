"""Verify a built unit site against its centralized records and migration inventory."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,parse_qs,unquote
import json,sys,os

project=Path(sys.argv[1]).resolve()
prefix=sys.argv[2].rstrip('/') if len(sys.argv)>2 else ''
settings=json.loads((project/'shared.config.json').read_text())
shared=Path(os.environ['SHARED_SOURCE']).resolve() if os.environ.get('SHARED_SOURCE') else (project/settings['localPath']).resolve()
unit=shared/'src/data/units'/settings['unit'];out=project/'_site'
report=json.loads((project/'reference/migration-report.json').read_text())
people=json.loads((unit/'people.json').read_text())
heroes=json.loads((unit/'heroes.json').read_text())['pages']
heroes.update(json.loads((unit/'faculty-heroes.json').read_text())['pages'])
class Scan(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.urls=[];self.h1=0;self.description=False;self.images=[];self.videos=[]
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if t=='h1':self.h1+=1
  if a.get('id'):self.ids.append(a['id'])
  if t=='meta' and a.get('name')=='description' and a.get('content'):self.description=True
  if t=='img':self.images.append(a)
  if t=='iframe' and 'youtube' in a.get('src',''):self.videos.append(a)
  if t in ['a','img','script','link','iframe']:
   v=a.get('href') if t in ['a','link'] else a.get('src')
   if v:self.urls.append(v)
scans={};errors=[]
for p in out.rglob('*.html'):
 scan=Scan();scan.feed(p.read_text());scans[p]=scan
if len(scans)!=report['pages']:errors.append('Unexpected generated page count')
for p,scan in scans.items():
 rel=p.relative_to(out);raw=p.read_text()
 url='/' if str(rel)=='index.html' else '/'+str(rel).removesuffix('index.html') if rel.name=='index.html' else '/'+str(rel)
 if scan.h1!=1:errors.append(str(rel)+': expected one H1')
 if not scan.description:errors.append(str(rel)+': missing description')
 if len(scan.ids)!=len(set(scan.ids)):errors.append(str(rel)+': duplicate IDs')
 if url not in heroes or heroes[url]['image'] not in raw:errors.append(str(rel)+': missing assigned hero')
 if any(x in raw for x in ['{{','{%','logo-research-gate','logo-google-scholar']):errors.append(str(rel)+': leftover imported/template markup')
 for v in scan.urls:
  u=urlsplit(v)
  if u.scheme or u.netloc:continue
  path=unquote(u.path)
  if prefix and path.startswith('/'):
   if not path.startswith(prefix+'/'):errors.append(str(rel)+': missing prefix '+v);continue
   path=path[len(prefix):]
  target=out/path.lstrip('/') if path.startswith('/') else p.parent/path if path else p
  if target.is_dir():target=target/'index.html'
  if not target.exists():errors.append(str(rel)+': missing '+v)
  elif u.fragment and target in scans and unquote(u.fragment) not in scans[target].ids:errors.append(str(rel)+': missing anchor '+v)
 for img in scan.images:
  if 'alt' not in img:errors.append(str(rel)+': image missing alt attribute')
 for video in scan.videos:
  q=parse_qs(urlsplit(video['src']).query)
  if q.get('enablejsapi')!=['1'] or not q.get('origin'):errors.append(str(rel)+': YouTube API/origin missing')
  if not video.get('title'):errors.append(str(rel)+': YouTube title missing')
core=[p for p in people if p.get('showInFacultyDirectory')]
if len(core)!=report['coreFaculty']:errors.append('Unexpected core roster count')
for person in people:
 if person.get('photo') and not (shared/'src'/person['photo'].lstrip('/')).exists():errors.append(person['name']+': missing source portrait')
 if person.get('url'):
  file=out/person['url'].lstrip('/')
  if not file.exists():errors.append(person['name']+': missing bio');continue
  raw=file.read_text()
  if 'profile-sidebar' not in raw or 'profile-biography' not in raw:errors.append(person['name']+': missing shared bio layout')
  portraits=[img for img in scans[file].images if img.get('src','').endswith(person['photo'])]
  if not portraits or not any(img.get('alt')==person['name'] for img in portraits):errors.append(person['name']+': missing portrait/name alt')
expected_videos=sum(report.get('youtubeEmbeds',{}).values())
actual_videos=sum(len(s.videos) for s in scans.values())
if actual_videos!=expected_videos:errors.append('Unexpected YouTube embed count')
if errors:print('\n'.join(errors));sys.exit(1)
print(f'Checked {len(scans)} pages, {len(core)} core faculty, {actual_videos} YouTube embeds, local links/assets/anchors, metadata, image alt, and heroes. Prefix: {prefix or "/"}.')
