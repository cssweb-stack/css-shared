"""One-time PUBA text migration. Usage: python3 scripts/migrations/puba-wordpress.py export.xml staged-site

Run against a fresh create-unit scaffold. Does not download inline media or execute
WordPress blocks. Source XML is data; only semantic HTML is emitted.
"""
import sys, re, json, html, hashlib
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, urlunsplit, unquote
import xml.etree.ElementTree as ET

SHARED = Path(__file__).resolve().parents[2]
source, target = Path(sys.argv[1]), Path(sys.argv[2])
NS = {'wp':'http://wordpress.org/export/1.2/', 'content':'http://purl.org/rss/1.0/modules/content/'}
items = ET.parse(source).findall('./channel/item')
def wp(item, name): return item.findtext('wp:'+name, default='', namespaces=NS)
pages = {('home' if urlsplit(i.findtext('link')).path == '/' else urlsplit(i.findtext('link')).path.strip('/')):i for i in items if wp(i,'post_type')=='page'}
attachments = {wp(i,'post_id'):i for i in items if wp(i,'post_type')=='attachment'}
mapping = {
'home':('/', 'Home'),
'program-overview':('/about/why-study-puba.html','Why Study PUBA'),
'advisory-board':('/about/advisory-board.html','Advisory Board'),
'alumni-network':('/about/alumni-network.html','Alumni Network'),
'pi-alpha-alpha':('/about/pi-alpha-alpha.html','Pi Alpha Alpha'),
'news':('/about/puba-news.html','PUBA News'),
'naspaa-accreditation':('/naspaa/accreditation.html','Accreditation'),
'naspaa-requirements':('/naspaa/requirements.html','Requirements'),
'apply-for-admission':('/applications-admissions.html','Applications & Admissions'),
'funding-opportunities':('/funding-opportunities.html','Funding Opportunities'),
 'testimonials':('/testimonials.html','Testimonials'),
'mpa':('/masters-mpa/','Master’s (MPA)'),
'practicum-placements':('/masters-mpa/practicum-placements.html','Practicum Placements'),
'mpa-timelines':('/masters-mpa/timelines.html','Timelines'),
'mpa-learning-outcomes':('/masters-mpa/learning-outcomes.html','Learning Outcomes'),
'gcert-nonprofit-management':('/graduate-certificate/nonprofit-management.html','Nonprofit Management'),
'gcert-public-policy':('/graduate-certificate/public-policy.html','Public Policy'),
'give-a-gift':('/support-puba.html','Support PUBA'),
'contact':('/contact.html','Contact'),
}
# Names and order come from the PUBA worksheet, not WordPress profile metadata.
faculty = [('Maile Arvin','maile-arvin'),('Soyun Jeong','soyun-jeong'),('Janet Jock','janet-jock'),('Steven W. Mumford','steven-w-mumford'),('Gowun Park','gowun-park'),('Helen H. Yu','helen-h-yu')]
for name,slug in faculty: mapping[slug]=('/faculty/'+slug+'.html',name)
links={urlsplit(i.findtext('link')).path.rstrip('/') or '/':mapping[slug][0] for slug,i in pages.items() if slug in mapping}
links.update({'/directory':'/faculty/','/privacy-policy':'/privacy.html','/academic-program/mpa':'/masters-mpa/','/academic-program':'/masters-mpa/'})
ids={wp(i,'post_id'):links.get(urlsplit(i.findtext('link')).path.rstrip('/') or '/') for i in pages.values()}
# Excluded legacy destinations remain live links. Preserve policy access pending centralization.
retained=[]
def link(value):
 u=urlsplit(value)
 if u.scheme in ('mailto','tel'): return html.escape(value,quote=True)
 internal=u.hostname in ('puba.manoa.hawaii.edu','www.puba.manoa.hawaii.edu') or (not u.netloc and not u.scheme)
 if internal and (u.path or u.query):
  key=unquote(u.path).rstrip('/') or '/'
  dest=links.get(key)
  if not dest and u.query.startswith('page_id='): dest=ids.get(u.query.split('=',1)[1])
  if dest:
   suffix=('?'+u.query if u.query and not u.query.startswith('page_id=') else '')+('#'+u.fragment if u.fragment else '')
   return '{{ '+repr(dest+suffix)+' | url }}'
  if u.path.startswith('/wp-content/') or '/wp-content/' in u.path:
   return html.escape('https://puba.manoa.hawaii.edu'+u.path+('?' + u.query if u.query else '')+('#'+u.fragment if u.fragment else ''),quote=True)
  if key not in ('/',''):
   full=value if u.netloc else 'https://puba.manoa.hawaii.edu/'+value.lstrip('/')
   retained.append(full)
   return html.escape(full,quote=True)
 return html.escape(value,quote=True)

class Node:
 def __init__(self,tag='',attrs=()): self.tag=tag; self.attrs=dict(attrs); self.children=[]
 def text(self): return ''.join(c if isinstance(c,str) else c.text() for c in self.children)
class Parser(HTMLParser):
 def __init__(self): super().__init__(convert_charrefs=True); self.root=Node(); self.stack=[self.root]
 def handle_starttag(self,t,a):
  n=Node(t,a); self.stack[-1].children.append(n)
  if t not in {'img','br','hr','input','meta','link','source','wbr','embed','area','col','param'}:self.stack.append(n)
 def handle_startendtag(self,t,a): self.handle_starttag(t,a); self.handle_endtag(t)
 def handle_endtag(self,t):
  for x in range(len(self.stack)-1,0,-1):
   if self.stack[x].tag==t: self.stack=self.stack[:x]; break
 def handle_data(self,d):self.stack[-1].children.append(d)

allowed={'p','h1','h2','h3','h4','h5','h6','ul','ol','li','a','strong','em','b','i','u','s','sup','sub','blockquote','cite','br','hr','table','thead','tbody','tfoot','tr','th','td','caption','dl','dt','dd','address','abbr','time'}
block={'p','h1','h2','h3','h4','h5','h6','ul','ol','li','blockquote','table','thead','tbody','tfoot','tr','dl','dt','dd','address','hr'}
drop={'script','style','svg','img','iframe','video','audio','picture','source','noscript','form','input','button'}
def render(n):
 if isinstance(n,str): return html.escape(n,quote=False)
 if n.tag in drop:return ''
 inner=''.join(render(c) for c in n.children)
 if n.tag not in allowed:
  return ('<p>'+inner.strip()+'</p>\n') if n.tag=='figcaption' and inner.strip() else inner
 if not inner.strip() and n.tag not in {'br','hr'}:return ''
 attrs=''
 for k,v in n.attrs.items():
  if k=='href' and n.tag=='a': attrs+=' href="'+link(v)+'"'
  elif k=='id' or (n.tag in {'th','td'} and k in {'colspan','rowspan','scope'}) or (n.tag=='ol' and k=='start') or (n.tag=='abbr' and k=='title'):
   attrs+=' '+k+'="'+html.escape(v or '',quote=True)+'"'
 if n.tag=='a' and not attrs: return inner
 if n.tag in {'br','hr'}:return '<'+n.tag+attrs+'>'
 return '<'+n.tag+attrs+'>'+(inner.strip() if n.tag in block else inner)+'</'+n.tag+'>'+ ('\n' if n.tag in block else '')
def clean(item):
 p=Parser();p.feed(item.findtext('content:encoded',default='',namespaces=NS))
 t=render(p.root)
 t=re.sub(r'\n\s*\n','\n',t)
 # WordPress button blocks are standalone anchors; give these paragraph structure.
 t=re.sub(r'(?m)^\s*(<a\b[^\n]*</a>)\s*$',r'<p>\1</p>',t)
 return t.strip()
def plain(t):
 p=Parser();p.feed(t);return re.sub(r'\s+',' ',p.root.text()).strip()
def write(url,title,body):
 rel='index.html' if url=='/' else url.lstrip('/')+('index.html' if url.endswith('/') else '')
 # Scaffolder puts directory permalinks in a root file; use real folder index files instead.
 old=target/'src'/(url.strip('/')+'.html')
 if url.endswith('/') and url!='/' and old.exists():old.unlink()
 p=target/'src'/rel;p.parent.mkdir(parents=True,exist_ok=True)
 if url!='/contact.html': body='<div class="page-section">\n<div class="container content-section">\n<div class="row gx-0 gx-sm-5 gx-lg-5">\n<div class="col-12">\n'+body.strip()+'\n</div>\n</div>\n</div>\n</div>'
 p.write_text('---\nlayout: shell.njk\ntitle: '+json.dumps(title,ensure_ascii=False)+'\npermalink: '+json.dumps(url)+'\n---\n'+body.strip()+'\n')
 return rel

report=[];heropages={};heroassets={}
for slug,(url,title) in mapping.items():
 item=pages[slug];body=clean(item)
 if slug in {s for _,s in faculty}:
  # Bio exports already contain only the write-up, beginning at Background.
  start=re.search(r'<h[1-6](?:\s[^>]*)?>Background</h[1-6]>',body)
  if not start:raise RuntimeError('Missing bio boundary: '+slug)
  body=body[start.start():]
 elif slug=='contact':
  # Keep the exact heading and office-hours text; shared include owns office details/map.
  prefix=body.split('<p><strong>Main Office</strong>')[0]
  body='<div class="page-section">\n<div class="container content-section">\n<div class="row gx-0 gx-sm-5 gx-lg-5">\n<div class="col-12">\n'+prefix+'\n</div>\n</div>\n</div>\n</div>\n\n<div class="page-section">\n<div class="container content-section">\n{% include "layouts/content/unit-contact.njk" %}\n</div>\n</div>\n'
 elif slug in {'apply-for-admission','program-overview','give-a-gift'}:
  body=re.sub(r'<h1>.*?</h1>','<h1>'+html.escape(title)+'</h1>',body,count=1,flags=re.S)
 if slug=='news': body=body[:body.index('<hr>')].rstrip()
 if '<h1' not in body and slug not in {s for _,s in faculty}:body='<h1>'+html.escape(title)+'</h1>\n'+body
 rel=write(url,title,body)
 meta={m.findtext('wp:meta_key',namespaces=NS):m.findtext('wp:meta_value',namespaces=NS) for m in item.findall('wp:postmeta',NS)}
 aid=meta.get('_thumbnail_id');a=attachments.get(aid)
 if a is not None and slug not in {s for _,s in faculty}:
  imageurl=wp(a,'attachment_url')
  if not imageurl.lower().endswith('.webp'): raise RuntimeError('Hero is not WebP: '+imageurl)
  if imageurl not in heroassets:
   heroassets[imageurl]='/media/heroes/puba/'+str(len(heroassets)+1).zfill(2)+'.webp'
  alt=next((m.findtext('wp:meta_value',default='',namespaces=NS) for m in a.findall('wp:postmeta',NS) if m.findtext('wp:meta_key',namespaces=NS)=='_wp_attachment_image_alt'),'')
  heropages[url]={'image':heroassets[imageurl],'position':'center center','alt':alt,'credit':False}
 report.append({'source':item.findtext('link'),'destination':url,'file':rel,'sourceTitle':item.findtext('title'),'title':title})

# All non-core faculty lists are plain text; preserve the graduate assistant information too.
directory=clean(pages['directory'])
associated=directory[directory.index('<h2>Cooperating Faculty</h2>'):]
kyla=directory[directory.index('<h3>Kyla Ranker</h3>'):directory.index('<h2>Cooperating Faculty</h2>')]
write('/faculty/associated.html','Associated Faculty','<h1>Associated Faculty</h1>\n'+associated+'\n<h2>Staff</h2>\n'+kyla)
write('/faculty/','Core Faculty','<h1>Core Faculty</h1>\n<ul>\n'+'\n'.join('<li><a href="{{ '+repr('/faculty/'+s+'.html')+' | url }}">'+html.escape(name)+'</a></li>' for name,s in faculty)+'\n</ul>')
write('/courses/','Courses','<h1>Courses</h1>\n<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>')
heropages['/faculty/']=heropages['/testimonials.html'].copy();heropages['/faculty/associated.html']=heropages['/faculty/'].copy()
data=SHARED/'src/data/units/puba'
(data/'heroes.json').write_text(json.dumps({'defaultHero':heropages['/']['image'],'pages':heropages},ensure_ascii=False,indent=2)+'\n')
manifest={'source':source.name,'sourceSha256':hashlib.sha256(source.read_bytes()).hexdigest(),'pages':report,'heroes':[{'source':u,'destination':p} for u,p in heroassets.items()], 'legacyLinks':sorted(set(retained)),'excluded':['academic-program','gcert-public-service-leadership'],'deferred':['policies-and-procedures','faculty profile components','inline images'],'directorySplit':{'core':'/faculty/','associated':'/faculty/associated.html','contactProfilesDeferred':['Helen H. Yu','Sarah Amend']}}
(SHARED/'exports/puba-migration-2026-11-09.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
# Keep original source and deferred text outside published src.
archive=SHARED/'exports/puba';archive.mkdir(exist_ok=True)
(archive/'directory.html').write_text(directory+'\n')
(archive/'policies-and-procedures.html').write_text(clean(pages['policies-and-procedures'])+'\n')
print(json.dumps({'migrated':len(report),'heroes':len(heroassets),'legacyLinks':sorted(set(retained))},ensure_ascii=False,indent=2))
