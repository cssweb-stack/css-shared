"""Build reviewed SOC pages from WXR data. Export markup is never executable code.
Usage: python3 soc-wordpress.py export.xml shared-repository site-directory
"""
import sys,json,re,html,hashlib,shutil,csv
from pathlib import Path
from urllib.parse import urlsplit,unquote
from html.parser import HTMLParser
import xml.etree.ElementTree as ET
SOURCE=Path(sys.argv[1]).resolve(); SHARED=Path(sys.argv[2]).resolve(); ROOT=Path(sys.argv[3]).resolve()
NS={'wp':'http://wordpress.org/export/1.2/','content':'http://purl.org/rss/1.0/modules/content/'}
def wp(i,k):return i.findtext('wp:'+k,'',NS)
items=ET.parse(SOURCE).findall('./channel/item')
pages={wp(i,'post_name'):i for i in items if wp(i,'post_type')=='page' and wp(i,'status')=='publish'}
M={
'home':('/','Sociology at the University of Hawaiʻi'),
'history':('/about-soc/history.html','History'),
'minor-requirements':('/undergraduate/minor/','Minor'),
'minor-concentrations':('/undergraduate/minor/concentrations.html','Minor Concentrations'),
'ba-requirements':('/undergraduate/major/','Major (BA)'),
'major-concentrations':('/undergraduate/major/concentrations.html','Major Concentrations'),
'student-learning-outcomes':('/undergraduate/major/student-learning-outcomes.html','Student Learning Outcomes'),
'bam':('/undergraduate/bam.html','BA/MA Pathway (BAM)'),
'honors-track':('/undergraduate/honors-track.html','Honors Track'),
'scholarships-and-funding':('/undergraduate/funding-sources.html','Funding Sources'),
'undergraduate-advising':('/undergraduate/advising-support/','Advising & Support'),
'academic-planning':('/undergraduate/advising-support/academic-planning.html','Academic Planning'),
'ma-program':('/graduate/master-ma.html','Master’s (MA)'),
'phd-program':('/graduate/doctorate-phd.html','Doctorate (PhD)'),
'graduate-students':('/graduate/current-cohort.html','Current Cohort'),
'graduate-funding':('/graduate/funding-sources/','Funding Sources'),
'sakihara-scholarship':('/graduate/funding-sources/sakihara-scholarship.html','Sakihara Scholarship'),
'applications-admissions':('/graduate/applications-admissions.html','Applications & Admissions'),
'gssa':('/graduate/gssa.html','GSSA'),
'annual-review':('/graduate/annual-review.html','Annual Review'),
'course-identification':('/graduate/course-identification.html','Course Identification'),
'hormann-prize':('/hormann-prize.html','Hörmann Prize'),
'alpha-kappa-delta':('/alpha-kappa-delta.html','Alpha Kappa Delta'),
'give-a-gift':('/support-soc.html','Support SOC'),
'contact':('/contact.html','Contact SOC'),
}
AREAS=[
('asia-pacific-hawaii','asia-pacific-hawaii-regional-global-contexts','Asia, Pacific, and Hawaiʻi in Regional and Global Contexts'),
('nationalism-globalization-sustainability','nationalism-globalization-sustainability','Nationalism, Globalization, and Sustainability'),
('health-aging-medical-sociology','health-aging-medical-sociology','Health, Aging, and Medical Sociology'),
('race-ethnicity-gender-class','race-ethnicity-gender-class','Race, Ethnicity, Gender, and Class'),
('crime-law-social-control','crime-law-social-control','Crime, Law, and Social Control')]
FACULTY=[('Manfred B. Steger','manfred-b-steger'),('Nandita Sharma','nandita-sharma'),('Le Lin','le-lin'),('Jennifer Darrah','jennifer-darrah'),('Sun-Ki Chai','sun-ki-chai'),('Wei Zhang','wei-zhang'),('David Johnson','david-johnson'),('Katherine Irwin','katherine-irwin'),('Krysia Mossakowski','krysia-mossakowski'),('Ashley Rubin','ashley-rubin'),('Aya Kimura','aya-kimura'),('Myungji Yang','myungji-yang'),('Eunjeong Paek','eunjeong-paek'),('Yue Sun','yue-sun')]
for slug,name,title in AREAS:M[slug]=('/about-soc/research-areas/'+name+'.html',title)
for name,slug in FACULTY:M[slug]=('/faculty/'+slug+'.html',name)
assert all(s in pages for s in M),set(M)-set(pages)
links={urlsplit(pages[s].findtext('link')).path.rstrip('/') or '/':dest for s,(dest,title) in M.items()}
merges={'about':('/about-soc/why-study-soc.html','about-sociology'),'undergraduate':('/about-soc/why-study-soc.html','undergraduate-study'),'graduate':('/about-soc/why-study-soc.html','graduate-study'),'news':('/about-soc/news-events.html',''),'events':('/about-soc/news-events.html',''),'undergraduate-funding':('/undergraduate/funding-sources.html','additional-undergraduate-funding'),'department-travel-funds':('/graduate/funding-sources/','department-travel-funds')}
for slug,(dest,anchor) in merges.items():links[urlsplit(pages[slug].findtext('link')).path.rstrip('/')]=dest+('#'+anchor if anchor else '')
links.update({'/faculty':'/faculty/','/privacy-policy':'/privacy.html'})
ids={wp(i,'post_id'):links.get(urlsplit(i.findtext('link')).path.rstrip('/') or '/') for i in pages.values()}
assets={};retained=set();iframes=[]
def local_link(value):return '{{ '+repr(value)+' | url }}'
def rewrite(value):
 value=html.unescape(value.strip());u=urlsplit(value)
 if u.scheme in ('mailto','tel'):return html.escape(value,quote=True)
 if u.scheme and u.scheme not in ('https','http'):return '#'
 internal=u.hostname in ('sociology.manoa.hawaii.edu','www.sociology.manoa.hawaii.edu') or (not u.scheme and not u.netloc)
 if internal:
  if not u.path and u.fragment:return html.escape(value,quote=True)
  key=unquote(u.path).rstrip('/') or '/';dest=links.get(key)
  if key.startswith('/wp-content/uploads/') and Path(key).suffix.lower() in ('.png','.jpg','.jpeg','.webp','.svg'):
   absolute='https://sociology.manoa.hawaii.edu'+u.path
   name=hashlib.sha256(absolute.encode()).hexdigest()[:8]+'-'+re.sub(r'[^a-zA-Z0-9_.-]','-',unquote(Path(u.path).name))
   assets[absolute]='/media/content/'+name
   return local_link(assets[absolute]+('#'+u.fragment if u.fragment else ''))
  if not dest and 'page_id=' in u.query:dest=ids.get(u.query.split('page_id=')[-1].split('&')[0])
  if dest:return local_link(dest.split('#')[0]+('?' +u.query if u.query and 'page_id=' not in u.query else '')+('#'+u.fragment if u.fragment else ('#'+dest.split('#',1)[1] if '#' in dest else '')))
  absolute=value if u.netloc else 'https://sociology.manoa.hawaii.edu/'+value.lstrip('/')
  retained.add(absolute);return html.escape(absolute,quote=True)
 return html.escape(value,quote=True)

class Node:
 def __init__(self,tag='',attrs=()):self.tag=tag;self.attrs=dict(attrs);self.children=[]
 def text(self):return ''.join(c if isinstance(c,str) else c.text() for c in self.children)
class Parser(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.root=Node();self.stack=[self.root]
 def handle_starttag(self,t,a):
  if t in ('p','li','tr','td','th') and self.stack[-1].tag==t:self.stack.pop()
  n=Node(t,a);self.stack[-1].children.append(n)
  if t not in {'img','br','hr','input','meta','link','source','wbr','embed','area','col','param'}:self.stack.append(n)
 def handle_startendtag(self,t,a):
  self.handle_starttag(t,a)
  if self.stack[-1].tag==t:self.stack.pop()
 def handle_endtag(self,t):
  for j in range(len(self.stack)-1,0,-1):
   if self.stack[j].tag==t:self.stack=self.stack[:j];break
 def handle_data(self,d):self.stack[-1].children.append(d)

def descendants(n,tag):
 result=[]
 for c in n.children:
  if isinstance(c,Node):
   if c.tag==tag:result.append(c)
   else:result.extend(descendants(c,tag))
 return result

def media(n):
 src=n.attrs.get('src','');alt=n.attrs.get('alt','')
 if not src:return ''
 if 'uhf_left' in src:return '<img class="img-fluid" src="'+local_link('/media/branding/logos/uhf.svg')+'" alt="University of Hawaiʻi Foundation" width="230" height="59">'
 u=urlsplit(src)
 if u.scheme not in ('https','http'):return ''
 name=unquote(Path(u.path).name);name=re.sub(r'[^a-zA-Z0-9_.-]','-',name)
 name=hashlib.sha256(src.encode()).hexdigest()[:8]+'-'+name
 dest='/media/content/'+name;assets[src]=dest
 attrs=''
 for key in ('width','height'):
  if n.attrs.get(key,'').isdigit():attrs+=' '+key+'="'+n.attrs[key]+'"'
 return '<img class="img-fluid" src="'+local_link(dest)+'" alt="'+html.escape(alt,quote=True)+'"'+attrs+' loading="lazy" decoding="async">'

allowed={'p','h1','h2','h3','h4','h5','h6','ul','ol','li','a','strong','em','sup','sub','blockquote','cite','br','hr','dl','dt','dd','address','abbr','time','figure','figcaption'}
blocks={'p','h1','h2','h3','h4','h5','h6','ul','ol','li','blockquote','dl','dt','dd','address','hr','figure','figcaption'}
drop={'script','style','svg','video','audio','source','noscript','form','input','button','meta','link'}

def table(n):
 rows=descendants(n,'tr');out='<table class="content-table">'
 for row in rows:
  out+='<tr>'
  for c in row.children:
   if not isinstance(c,Node) or c.tag not in ('td','th'):continue
   attrs=''
   for key in ['colspan','rowspan']:
    if c.attrs.get(key,'').isdigit():attrs+=' '+key+'="'+c.attrs[key]+'"'
   if c.tag=='th':attrs+=' scope="col"'
   out+='<'+c.tag+attrs+'>'+''.join(render(x) for x in c.children)+'</'+c.tag+'>'
  out+='</tr>'
 return out+'</table>\n'

def render(n):
 if isinstance(n,str):return html.escape(n,quote=False)
 if n.tag in drop:return ''
 if n.tag=='img':return media(n)
 if n.tag=='iframe':
  src=n.attrs.get('src','');iframes.append(src)
  if src and urlsplit(src).scheme in ('https','http') and 'google.com/maps' not in src:return '<p><a href="'+html.escape(src,quote=True)+'">'+html.escape(n.attrs.get('title') or 'View embedded resource')+'</a></p>\n'
  return ''
 if n.tag=='table':return table(n)
 if n.tag in ('b','i'):n.tag={'b':'strong','i':'em'}[n.tag]
 inner=''.join(render(c) for c in n.children)
 if n.tag not in allowed:return inner
 if not inner.strip() and n.tag not in ('br','hr'):return ''
 attrs=''
 for k,v in n.attrs.items():
  if k=='href' and n.tag=='a':attrs+=' href="'+rewrite(v or '')+'"'
  elif k=='id' or (n.tag=='ol' and k=='start') or (n.tag=='abbr' and k=='title'):attrs+=' '+k+'="'+html.escape(v or '',quote=True)+'"'
 if n.tag=='a' and 'href=' not in attrs:return inner
 if n.tag in ('br','hr'):return '<'+n.tag+attrs+'>'
 return '<'+n.tag+attrs+'>'+inner.strip()+'</'+n.tag+'>'+('\n' if n.tag in blocks else '')

def normalize(text):
 # Give former standalone sidebar buttons ordinary paragraph structure.
 p=Parser();p.feed(text)
 out=[];inline=[]
 def flush():
  v=''.join(inline).strip();inline.clear()
  if v:out.append('<p>'+v+'</p>')
 for c in p.root.children:
  if isinstance(c,Node) and c.tag=='a':
   flush();out.append('<p>'+render_normal(c)+'</p>')
  elif isinstance(c,Node) and c.tag in blocks|{'table'}:
   flush();out.append(render_normal(c))
  else:inline.append(render_normal(c))
 flush()
 return '\n'.join(out)

def render_normal(n):
 if isinstance(n,str):return html.escape(n,quote=False)
 # Already-sanitized HTML only: do not run link/media rewriting a second time.
 attrs=''.join(' '+k+'="'+html.escape(v or '',quote=False).replace(chr(34),'&quot;')+'"' for k,v in n.attrs.items())
 if n.tag in ('br','hr','img'):return '<'+n.tag+attrs+'>'
 return '<'+n.tag+attrs+'>'+''.join(render_normal(c) for c in n.children)+'</'+n.tag+'>'


def clean(slug):
 raw=pages[slug].findtext('content:encoded','',NS)
 # Former accordion labels become visible headings with stable fragment IDs.
 def accordion_heading(match):
  index=int(match[1])+1
  prefix='phd' if slug=='phd-program' else 'section'
  return '<h2 id="'+prefix+'-'+str(index)+'">'+html.escape(match[2].strip())+'</h2>\n'
 raw=re.sub(r'<button\b[^>]*id="fl-accordion--icon-(\d+)"[^>]*>.*?</button>\s*([^<]+)(?=<)',accordion_heading,raw,flags=re.S)
 # WordPress plugin shortcodes are data artifacts, not content for the new site.
 raw=re.sub(r'\[(?:/?(?:custom-twitter-feeds|fl_builder|embed|gallery))\b[^\]]*\]','',raw)
 p=Parser();p.feed(raw)
 return normalize(render(p.root))
def without_h1(body):return re.sub(r'<h1\b[^>]*>(.*?)</h1>',r'<h2>\1</h2>',body,flags=re.S)
def replace_h1(body,title):
 body=re.sub(r'<h1\b[^>]*>.*?</h1>','',body,flags=re.S)
 return '<h1>'+html.escape(title)+'</h1>\n'+body

def linked_list(entries):
 return '<ul>\n'+''.join('<li><a href="'+local_link(url)+'">'+html.escape(label)+'</a></li>\n' for label,url in entries)+'</ul>\n'
def append_links(body,title,entries):
 return body+'\n<h2>'+html.escape(title)+'</h2>\n'+linked_list(entries)
def section(body):
 return '<div class="page-section">\n<div class="container content-section">\n<div class="row gx-0 gx-sm-5 gx-lg-5">\n<div class="col-12">\n'+body.strip()+'\n</div>\n</div>\n</div>\n</div>\n'
report=[];all_urls=[]
def write(url,title,body,sources=()):
 rel='index.html' if url=='/' else url.lstrip('/')+('index.html' if url.endswith('/') else '')
 p=ROOT/'src'/rel;p.parent.mkdir(parents=True,exist_ok=True)
 body=replace_h1(body,title)
 body=re.sub(r'(<h1\b[^>]*>.*?</h1>\s*)<p>',r'\1<p class="intro">',body,count=1,flags=re.S)
 front='---\nlayout: shell.njk\ntitle: '+json.dumps(title,ensure_ascii=False)+'\ndescription: "This will be the meta description."\npermalink: '+json.dumps(url)+'\n---\n'
 p.write_text(front+section(body))
 all_urls.append(url)
 report.append({'sources':[pages[s].findtext('link') for s in sources],'destination':url,'file':rel,'title':title})

bodies={s:clean(s) for s in M}
why='<h1>Why Study SOC</h1>\n'
for slug,heading,anchor in [('about','About Sociology','about-sociology'),('undergraduate','Undergraduate Study','undergraduate-study'),('graduate','Graduate Study','graduate-study')]:
 body=clean(slug);body=re.sub(r'<h1\b[^>]*>.*?</h1>','',body,flags=re.S)
 why+='<h2 id="'+anchor+'">'+heading+'</h2>\n'+body+'\n'
write('/about-soc/why-study-soc.html','Why Study SOC',why,['about','undergraduate','graduate'])
areas='<h1>Research Areas</h1>\n<p>Explore the Department of Sociology’s five research areas.</p>\n'+linked_list([(title,M[slug][0]) for slug,name,title in AREAS])
write('/about-soc/research-areas/','Research Areas',areas)
news='<h1>News and Events</h1>\n<p>Department news and event announcements are shared on our Twitter/X account.</p>\n<p><a href="https://x.com/UHM_Sociology">Follow @UHM_Sociology on X</a></p>\n<p>The department’s news and events feed will appear here. Feed integration is pending.</p>\n<p>Email <a href="mailto:socdept@hawaii.edu">socdept@hawaii.edu</a> to join the events email list.</p>'
write('/about-soc/news-events.html','News and Events',news,['news','events'])
# Preserve supplemental source material as sections rather than additional navigation pages.
bodies['scholarships-and-funding']+='\n<h2 id="additional-undergraduate-funding">Additional Undergraduate Funding</h2>\n'+without_h1(clean('undergraduate-funding'))
bodies['graduate-funding']+='\n<h2 id="department-travel-funds">Department Travel Funds</h2>\n'+without_h1(clean('department-travel-funds'))
children={
'minor-requirements':[('Concentrations',M['minor-concentrations'][0])],
'ba-requirements':[('Concentrations',M['major-concentrations'][0]),('Student Learning Outcomes',M['student-learning-outcomes'][0])],
'undergraduate-advising':[('Academic Planning',M['academic-planning'][0]),('Hörmann Prize',M['hormann-prize'][0]),('Alpha Kappa Delta',M['alpha-kappa-delta'][0])],
'graduate-funding':[('Sakihara Scholarship',M['sakihara-scholarship'][0]),('Hörmann Prize',M['hormann-prize'][0])],
'ma-program':[(M[s][1],M[s][0]) for s in ['gssa','annual-review','course-identification','alpha-kappa-delta']],
'phd-program':[(M[s][1],M[s][0]) for s in ['gssa','annual-review','course-identification','alpha-kappa-delta']]}
for slug,entries in children.items():bodies[slug]=append_links(bodies[slug],'Related Resources',entries)
for slug,(url,title) in M.items():
 sources=[slug]
 if slug=='scholarships-and-funding':sources+=['undergraduate-funding']
 if slug=='graduate-funding':sources+=['department-travel-funds']
 write(url,title,bodies[slug],sources)
faculty='<h1>Faculty</h1>\n<p>From both local and global vantage points, our faculty provide students with a broad foundation in theory and methods of sociological research.</p>\n'+linked_list([(name,M[slug][0]) for name,slug in FACULTY])
write('/faculty/','Faculty',faculty,['faculty'])
write('/about-soc/soc-courses.html','Courses','<h1>Courses</h1>\n<p>Find Sociology class availability, course descriptions, and catalog information.</p>\n{% include "layouts/content/course-resources.njk" %}')
privacy='---\nlayout: shell.njk\ntitle: "Privacy Policy"\ndescription: "How College of Social Sciences websites use Google Analytics and visitor information, and how to manage your privacy choices."\npermalink: "/privacy.html"\n---\n{% include "pages/privacy.njk" %}\n'
(ROOT/'src/privacy.html').write_text(privacy);all_urls.append('/privacy.html')
# Remove only scaffold pages that are not in the approved output set.
expected={('index.html' if u=='/' else u.lstrip('/')+('index.html' if u.endswith('/') else '')) for u in all_urls}
for p in (ROOT/'src').rglob('*.html'):
 if str(p.relative_to(ROOT/'src')) not in expected:p.unlink()
placeholder='/media/heroes/saunders-mural/01.webp'
hero={'image':placeholder,'position':'center center','alt':'Temporary hero: detail of the Saunders Hall mural','credit':False}
(SHARED/'src/data/units/soc/heroes.json').write_text(json.dumps({'defaultHero':placeholder,'pages':{u:hero.copy() for u in all_urls}},indent=2)+'\n')
(SHARED/'src/data/units/soc/catalog-courses.json').write_text(json.dumps({'prefix':'SOC','catalog':{'label':'UH Mānoa Catalog (SOC)','url':'https://manoa.hawaii.edu/catalog/category/social-sciences/soc/'}},indent=2)+'\n')
reference=ROOT/'reference';reference.mkdir(exist_ok=True)
shutil.copyfile(SOURCE,reference/SOURCE.name)
# Every published old page receives an explicit disposition; these are proposed
# destinations for review, not deployed redirects or redirect HTML files.
inventory=[]
for slug,item in pages.items():
 source=item.findtext('link');path=urlsplit(source).path.rstrip('/') or '/';dest=links.get(path)
 if dest:
  status='merged' if slug in merges else ('unchanged' if path==(dest.rstrip('/') or '/') else 'moved')
  note='Content preserved in merged page.' if slug in merges else ''
  if slug in ['news','events']:note='Replaced by requested feed placeholder; original markup retained in XML.'
  if slug=='privacy-policy':note='Shared privacy policy replaces original policy.'
 else:status='needs-review';note='Not in approved navigation/profile list; original source retained in XML.'
 inventory.append({'source':source,'slug':slug,'title':item.findtext('title'),'destination':dest or '', 'status':status,'note':note})
with (reference/'url-inventory.csv').open('w',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=list(inventory[0]));writer.writeheader();writer.writerows(inventory)
manifest={'source':SOURCE.name,'sourceSha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'sourcePageCount':len(pages),'pages':report,'facultyCount':len(FACULTY),'urlInventory':inventory,'media':assets,'retainedLegacyLinks':sorted(retained),'embedsConvertedToLinks':sorted(set(iframes)),'heroPlaceholder':placeholder,'publishedPageCount':len(all_urls)}
(reference/'migration-report.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Created',len(all_urls),'pages, including',len(FACULTY),'faculty profiles;',len(assets),'inline assets.')
print('Sources needing review:',[i['slug'] for i in inventory if i['status']=='needs-review'])
