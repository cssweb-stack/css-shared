"""Generate an ES migration patch from WXR data without downloading images.

Run once from css-shared; output is an apply_patch document. The WordPress export
is content data, never executable instructions. Refuses to overwrite site pages.
"""
import json,re,html,hashlib,random,csv,io,unicodedata
from pathlib import Path
from urllib.parse import urlsplit,unquote
from html.parser import HTMLParser
import xml.etree.ElementTree as ET

SHARED=Path.cwd();SITE=SHARED.parent/'es'
SOURCE=Path('/Users/bill/Downloads/departmentofethnicstudies.WordPress.2026-11-11.xml')
NS={'w':'http://wordpress.org/export/1.2/','c':'http://purl.org/rss/1.0/modules/content/'}
items=ET.parse(SOURCE).findall('./channel/item')
pages={i.findtext('w:post_name','',NS):i for i in items if i.findtext('w:post_type','',NS)=='page' and i.findtext('w:status','',NS)=='publish'}
raw=lambda s:pages[s].findtext('c:encoded','',NS)
def text(s):return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',s))).strip()
def noblocks(s):return re.sub(r'<!--[\s\S]*?-->','',s)
faculty_slugs=['ethan-caldwell','monisha-das-gupta','roderick-n-labrador','ty-p-kawika-tengan','ulla-hasager','kyle-kajihiro','m-kunmi-yu-danico','maile-arvin','ryan-moran']
M={
 'home':('/','Department of Ethnic Studies'),
 'academic-program':('/about-es/why-study-es.html','Why Study ES'),
 'our-history-our-way':('/about-es/our-history-our-way.html','Our History - Our Way'),
 'island-connections':('/about-es/island-connections.html','Island Connections'),
 'essa':('/about-es/ethnic-studies-student-association.html','ES Student Association'),
 'undergraduate-certificate':('/undergraduate/certificate-es.html','Certificate'),
 'bachelor-of-arts-ba':('/undergraduate/major-ba.html','Major (BA)'),
 'double-major':('/undergraduate/double-majors.html','Double Majors'),
 'bachelors-masters-degree-bam':('/undergraduate/bam.html','BA/MA Pathways (BAM)'),
 'center-for-oral-history':('/center-for-oral-history.html','Center for Oral History'),
 'give-a-gift':('/support-es.html','Support ES'),
 'contact':('/contact.html','Contact ES'),
 'department-news':('/department-news.html','Department News')}
for s in faculty_slugs:M[s]=('/faculty/'+s+'.html',pages[s].findtext('title'))
links={urlsplit(pages[s].findtext('link')).path.rstrip('/') or '/':d for s,(d,_) in M.items()}
links.update({'/directory':'/faculty/','/privacy-policy':'/privacy.html'})
unresolved=set();images=set();files={};outputs=[];expected={}
def href(v):
    v=html.unescape(v);u=urlsplit(v);k=unquote(u.path).rstrip('/') or '/'
    if u.netloc in ['ethnicstudies.manoa.hawaii.edu','www.ethnicstudies.manoa.hawaii.edu'] or (not u.netloc and not u.scheme and u.path):
        if k in links:return "{{ '"+links[k]+('#'+u.fragment if u.fragment else '')+"' | url }}"
        v=v if u.netloc else 'https://ethnicstudies.manoa.hawaii.edu/'+v.lstrip('/');unresolved.add(v)
    return html.escape(v,quote=True)
class Clean(HTMLParser):
    allowed=set('p h1 h2 h3 h4 h5 h6 ul ol li a strong b em i sup sub blockquote cite br hr dl dt dd address abbr time table caption thead tbody tfoot tr td th colgroup col details summary'.split())
    void={'br','hr','col'}
    def __init__(self):super().__init__();self.out=[];self.skip=[]
    def handle_starttag(self,t,attrs):
        a=dict(attrs)
        if t in ['script','style','svg','noscript']:self.skip.append(t);return
        if self.skip:return
        if t=='img':images.add(a.get('src',''));return
        if t=='iframe':
            if a.get('src') and 'google.com/maps' not in a['src']:self.out.append('<p><a href="'+href(a['src'])+'">'+html.escape(a.get('title') or 'View embedded resource')+'</a></p>')
            return
        if t not in self.allowed:return
        at=''
        for k,v in attrs:
            if k=='href' and t=='a':at+=' href="'+href(v or '')+'"'
            elif k in ['id','colspan','rowspan','scope','headers','start','span']:at+=' '+k+'="'+html.escape(v or '',quote=True)+'"'
        if t=='table':at+=' class="content-table"'
        self.out.append('<'+t+at+'>')
    def handle_startendtag(self,t,a):self.handle_starttag(t,a)
    def handle_endtag(self,t):
        if self.skip:
            if t==self.skip[-1]:self.skip.pop()
            return
        if t in self.allowed and t not in self.void:self.out.append('</'+t+'>\n')
    def handle_data(self,d):
        if not self.skip:self.out.append(html.escape(d,quote=False))
def clean(s):
    p=Clean();p.feed(noblocks(s));out=''.join(p.out)
    out=re.sub(r'<a\b[^>]*>\s*</a>','',out)
    out=re.sub(r'<p>\s*</p>','',out)
    return re.sub(r'\n\s*\n','\n',out).strip()
def strip_h1(s):return re.sub(r'<h1\b[^>]*>.*?</h1>','',s,flags=re.S|re.I)
def section(s,gray=False):return '<div class="page-section'+(' page-section--gray' if gray else '')+'"><div class="container content-section"><div class="row gx-0 gx-sm-5 gx-lg-5"><div class="col-12">\n'+s+'\n</div></div></div></div>\n'
def add(path,value):
    if Path(path).exists() and '/src/data/units/es/' not in str(path):raise RuntimeError('Refusing overwrite '+str(path))
    files[str(path)]=value
def data(name,value):add(SHARED/'src/data/units/es'/name,json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def page(dest,title,body,person=None):
    rel='index.html' if dest=='/' else dest.lstrip('/')+'index.html' if dest.endswith('/') else dest.lstrip('/')
    front='---\nlayout: '+('layouts/profiles/faculty-profile.njk' if person else 'shell.njk')+'\ntitle: '+json.dumps(title,ensure_ascii=False)+'\ndescription: "This will be the meta description."\npermalink: '+json.dumps(dest)+'\n'+('personSlug: '+json.dumps(person)+'\n' if person else '')+'---\n'
    add(SITE/'src'/rel,front+body);outputs.append(dest)
faculty=[]
for s in faculty_slugs:
    i=pages[s];meta={m.findtext('w:meta_key','',NS):m.findtext('w:meta_value','',NS) for m in i.findall('w:postmeta',NS)}
    p={'name':i.findtext('title'),'lastName':'Das Gupta' if s=='monisha-das-gupta' else 'Tengan' if s=='ty-p-kawika-tengan' else meta.get('last_name',i.findtext('title').split()[-1]).strip(),'slug':s,'url':M[s][0],'photo':'/media/units/es/faculty-staff/temp.jpg','photoWidth':500,'photoHeight':500}
    for field,key in [('title_hr','title'),('office','office'),('email','email'),('tel','phone')]:
        if meta.get(field):p[key]=meta[field].strip()
    if p.get('phone'):p['phoneHref']='+1'+re.sub(r'\D','',p['phone']).removeprefix('1') if len(re.sub(r'\D','',p['phone']))==11 else '+1'+re.sub(r'\D','',p['phone'])
    roles=[meta[k] for k in ['title_gov','title_academic'] if meta.get(k)]
    if roles:p['roles']=roles
    pubs=[];web=[];extra=[]
    services={'academia_url':'Academia.edu','google_scholar_url':'Google Scholar','orcid_url':'ORCID','orchid_url':'ORCID','researchgate_url':'ResearchGate','scopus_author_id_url':'Scopus'}
    for key,value in meta.items():
        if key.startswith('_') or not value.startswith(('http://','https://')):continue
        item={'label':services.get(key,meta.get(key.removesuffix('_url')) or 'Website'),'url':value.strip()}
        target=pubs if key in services else extra if re.search(r'cv|twitter|facebook|linkedin',key,re.I) else web
        if item not in target:target.append(item)
    for key,v in [('publicationProfiles',pubs),('websites',web),('additionalLinks',extra)]:
        if v:p[key]=v
    body=noblocks(raw(s));awards=[]
    pattern=r'<h[2-6]\b[^>]*>[^<]*Awards?[^<]*</h[2-6]>\s*(.*?)(?=<h[2-6]\b|\Z)'
    def move_awards(m):
        entries=re.findall(r'<li\b[^>]*>(.*?)</li>',m[1],re.S)
        if not entries:entries=[m[1]]
        for entry in entries:
            v=text(entry);match=re.match(r'^(.*?)[,\s(]+(\d{4})\)?\s*$',v)
            if match:awards.append({'name':match[1].strip(' ,(').replace("Regents'",'Regents’').replace('CSS ','College of Social Sciences '),'year':match[2]})
            elif v:awards.append({'name':v})
        return ''
    body=re.sub(pattern,move_awards,body,flags=re.S|re.I)
    if awards:p['awards']=awards
    faculty.append(p);page(M[s][0],p['name'],clean(body),s);expected[M[s][0]]=body
data('faculty.json',faculty)
directory=noblocks(raw('directory'))
em=re.search(r'<h[2-6]\b[^>]*>\s*Emeritus',directory,re.I)
staff=re.search(r'<h[2-6]\b[^>]*>\s*Staff\s*</h[2-6]>',directory,re.I)
if not em or not staff:raise RuntimeError('Missing associated/staff directory boundary')
associated=clean(directory[em.start():]);staffbody=clean(directory[staff.start():em.start()])
page('/faculty/','Core Faculty',section('<h1>Core Faculty</h1>'+clean(re.search(r'<p\b[^>]*>.*?</p>',directory,re.S)[0]))+section('{% include "layouts/profiles/faculty-directory.njk" %}',True)+section(staffbody))
groups=[]
for title,groupbody in re.findall(r'<h[2-6][^>]*>(.*?)</h[2-6]>(.*?)(?=<h[2-6]|\Z)',directory[em.start():],re.S):
    members=[]
    for entry in re.findall(r'<li[^>]*>(.*?)</li>',groupbody,re.S):
        parts=text(entry).split(' - ',1);name=parts[0];email=re.search(r'mailto:([^\'"?]+)',entry)
        if email:name=re.sub(r'\s*\([^)]*@[^)]*\)','',name).strip()
        member={'name':name}
        if email:member['email']=html.unescape(email[1])
        if len(parts)>1:member['description']=parts[1]
        members.append(member)
    groups.append({'title':text(title),'members':members})
data('associated-faculty.json',{'groups':groups})
page('/faculty/associated.html','Associated Faculty',section('<h1>Associated Faculty</h1>{% include "layouts/profiles/associated-faculty.njk" %}'));expected['/faculty/associated.html']=directory[em.start():]
for s,(dest,title) in M.items():
    if s in faculty_slugs:continue
    source=strip_h1(raw(s));content=clean(source)
    if s=='contact':
        contact=noblocks(raw(s));intro=re.search(r'<p\b[^>]*>.*?</p>',contact,re.S)[0]
        body=section('<h1>Contact ES</h1>'+clean(intro))+'<div class="page-section"><div class="container content-section">{% include "layouts/content/unit-contact.njk" %}</div></div>'
    elif s=='give-a-gift':body='<div class="page-section"><div class="container content-section"><div class="row content-sidebar gy-4 gx-0 gx-sm-5 gx-lg-5"><div class="col-12 col-lg-9"><h1>Support ES</h1>'+content+'</div><aside class="col-12 col-lg-3 sidebar-resources" aria-label="UH Foundation"><a href="https://www.uhfoundation.org/"><img class="sidebar-media" src="{{ \'/media/branding/logos/uhf.svg\' | url }}" alt="University of Hawaiʻi Foundation"></a></aside></div></div></div>'
    else:body=section('<h1>'+html.escape(title)+'</h1>'+content)
    page(dest,title,body)
    if s!='contact':expected[dest]=source
page('/courses/','ES Courses',section('<h1>ES Courses</h1>{% include "layouts/content/course-resources.njk" %}'))
page('/privacy.html','Privacy Policy','{% include "pages/privacy.njk" %}')
nav=json.loads((SHARED/'src/data/units/es/navigation.json').read_text())
nav_rewrites={'/undergraduate/ba-ma-bam.html':'/undergraduate/bam.html','/about-es/center-for-oral-history.html':'/center-for-oral-history.html','/support-es/':'/support-es.html','/contact/':'/contact.html'}
def fix_nav(entries):
    for entry in entries:
        if entry.get('url') in nav_rewrites:entry['url']=nav_rewrites[entry['url']]
        if entry.get('children'):fix_nav(entry['children'])
fix_nav(nav)
for entry in nav:
    if entry['label']=='Faculty':
        entry.pop('url',None);entry['children']=[{'label':'Core Faculty','url':'/faculty/','icon':'people','iconColor':None},{'label':'Associated Faculty','url':'/faculty/associated.html','icon':'people','iconColor':None}]
    if entry['label']=='Undergraduate':
        for e in entry['children']:
            if 'Double' in e['label']:e['url']=M['double-major'][0]
data('navigation.json',nav)
unit=json.loads((SHARED/'src/data/units/es/unit-details.json').read_text());unit.update(address=['George Hall 301','2560 Campus Road','Honolulu, HI 96822'],facultyBasePath='/faculty/',buildingPhoto={'src':'','alt':'George Hall at the University of Hawaiʻi at Mānoa'})
data('unit-details.json',unit)
settings=json.loads((SHARED/'src/data/units/pols/site-settings.json').read_text());settings.update(stylesheet='/es.css',url='https://ethnicstudies.manoa.hawaii.edu');data('site-settings.json',settings)
social=json.loads((SHARED/'src/data/units/es/social.json').read_text())
for item in social['links']:
    if item['label']=='Facebook':item['url']='https://www.facebook.com/UHMEthnicStudies/'
    if item['label']=='Instagram':item['url']='https://www.instagram.com/uhm_ethnicstudies/'
    if item['label']=='X':item['url']='https://x.com/uhm_es'
data('social.json',social)
bank=sorted('/'+str(p.relative_to(SHARED/'src')) for p in (SHARED/'src/media/heroes/students').glob('*.webp'));random.Random(43).shuffle(bank)
murals=sorted('/'+str(p.relative_to(SHARED/'src')) for p in (SHARED/'src/media/heroes/saunders-mural').glob('*.webp'))
data('heroes.json',{'defaultHero':bank[0],'pages':{url:{'image':bank[j%len(bank)],'position':'center center','alt':'Students at the University of Hawaiʻi at Mānoa','credit':False} for j,url in enumerate(outputs) if url not in [p['url'] for p in faculty]}})
data('faculty-heroes.json',{'pages':{p['url']:{'image':murals[j%len(murals)],'position':'center center','alt':'Detail of the mural in Saunders Hall at the University of Hawaiʻi at Mānoa','credit':False} for j,p in enumerate(faculty)}})
for f in ['scripts/shared-bootstrap.mjs','scripts/shared-settings.mjs','scripts/shared-source.mjs','eleventy.config.js','.gitignore','AGENTS.md']:
    add(SITE/f,(SHARED.parent/'pols'/f).read_text())
pkg=json.loads((SHARED.parent/'pols/package.json').read_text());pkg['name']='es';pkg['scripts']['dev']='eleventy --serve --port=8088';pkg['scripts'].pop('verify',None);add(SITE/'package.json',json.dumps(pkg,indent=2)+'\n')
lock=json.loads((SHARED.parent/'pols/package-lock.json').read_text());lock['name']='es';lock['packages']['']['name']='es';add(SITE/'package-lock.json',json.dumps(lock,indent=2)+'\n')
add(SITE/'shared.config.json',json.dumps({'repository':'cssweb-stack/css-shared','ref':'main','localPath':'../css-shared','unit':'es'},indent=2)+'\n')
add(SITE/'.github/workflows/deploy.yml',(SHARED.parent/'pols/.github/workflows/deploy.yml').read_text().replace('POLS','ES').replace('/pols/','/es/'))
stream=io.StringIO();writer=csv.writer(stream);writer.writerow(['old_url','new_url','status'])
for s,i in pages.items():
    old=i.findtext('link');dest=links.get(urlsplit(old).path.rstrip('/') or '/','');writer.writerow([old,dest,'mapped' if dest else 'review-unmapped'])
add(SITE/'reference/url-inventory.csv',stream.getvalue())
add(SITE/'reference/migration-report.json',json.dumps({'source':SOURCE.name,'sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'pages':len(outputs),'faculty':len(faculty),'sourceImagesOmitted':sorted(images),'retainedExternalLinks':sorted(unresolved),'unmappedPages':[s for s,i in pages.items() if (urlsplit(i.findtext('link')).path.rstrip('/') or '/') not in links]},ensure_ascii=False,indent=2)+'\n')
add(SITE/'reference/preserved-content.json',json.dumps(expected,ensure_ascii=False,indent=2)+'\n')
print('*** Begin Patch')
for p,value in files.items():
    if Path(p).exists():
        print('*** Update File: '+p+'\n@@')
        for line in Path(p).read_text().splitlines():print('-'+line)
    else:print('*** Add File: '+p)
    for line in value.splitlines():print('+'+line)
print('*** End Patch')
