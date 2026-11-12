"""Generate the ANTH first-pass migration patch from the three approved exports.

No media downloads. Run once from css-shared; review/apply the emitted patch.
"""
import csv, hashlib, html, io, json, random, re, unicodedata
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
from zipfile import ZipFile
import xml.etree.ElementTree as E

ROOT = Path.cwd()
SITE = ROOT.parent / 'anth'
UNIT = ROOT / 'src/data/units/anth'
NS = {'w': 'http://wordpress.org/export/1.2/', 'c': 'http://purl.org/rss/1.0/modules/content/'}
sources = [ROOT / 'exports/anth' / ('departmentofanthropology.WordPress.2026-11-11' + suffix + '.xml') for suffix in ['', ' (1)', ' (2)']]
items = [i for source in sources for i in E.parse(source).findall('./channel/item')]
def records(kind):
    return {i.findtext('w:post_name', '', NS): i for i in items if i.findtext('w:post_type', '', NS) == kind and i.findtext('w:status', '', NS) == 'publish'}
pages, people_source, grads_source = records('page'), records('people'), records('grad')
def raw(slug): return pages[slug].findtext('c:encoded', '', NS)
def meta(item): return {m.findtext('w:meta_key', '', NS): m.findtext('w:meta_value', '', NS) for m in item.findall('w:postmeta', NS)}
def text(s): return re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', ' ', s))).strip()
def slugify(s): return re.sub('[^a-z0-9]+', '-', unicodedata.normalize('NFKD', s.replace('ʻ','').replace('’','')).encode('ascii','ignore').decode().lower()).strip('-')

# Read both workbook passes; ANTH second-pass core roster is authoritative.
with ZipFile(ROOT / 'exports/unit-navigation-review.xlsx') as z:
    n = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    strings = [''.join(t.text or '' for t in si.iter('{' + n['m'] + '}t')) for si in E.fromstring(z.read('xl/sharedStrings.xml'))]
    rels = {r.attrib['Id']: r.attrib['Target'] for r in E.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
    workbook = {}
    for sheet in E.fromstring(z.read('xl/workbook.xml')).find('m:sheets', n):
        if sheet.attrib['name'] not in ['ANTH', 'Navigation Review']: continue
        target = rels[sheet.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id']]
        target = target.lstrip('/') if target.startswith('/') else 'xl/' + target
        cells = {}
        for c in E.fromstring(z.read(target)).findall('.//m:sheetData/m:row/m:c', n):
            v = c.find('m:v', n)
            value = v.text if v is not None else ''.join(t.text or '' for t in c.findall('.//m:t', n))
            if c.attrib.get('t') == 's' and value is not None: value = strings[int(value)]
            if value: cells[c.attrib['r']] = value
        workbook[sheet.attrib['name']] = cells
    roster = [v for k,v in workbook['ANTH'].items() if k.endswith('28') and not k.startswith('A')]
core_slugs = [s for name in roster for s,i in people_source.items() if i.findtext('title') == name]
assert len(roster) == len(core_slugs) == 13, (roster, core_slugs)

specials = ['archaeology','biological-anthropology','cultural-anthropology','applied-archaeology','applied-cultural-anthropology','environmental-anthropology','medical-anthropology']
associated = [('adjunct-faculty','Adjunct Faculty'),('affiliate-graduate-faculty','Affiliate Graduate Faculty'),('cooperating-graduate-faculty','Cooperating Graduate Faculty'),('emeritus-retired-faculty','Emeritus and Retired Faculty'),('emeriti-faculty-in-memoriam','Emeriti (In Memoriam)')]
M = {
    'home': ('/', 'Anthropology at the University of Hawaiʻi'),
    'overview': ('/about-anth/subfields-specializations/', 'Subfields and Specializations'),
    'colloquia': ('/about-anth/colloquia.html','Colloquia'),
    'department-news': ('/about-anth/department-news.html','Department News'),
    'minor': ('/undergraduate/minor-anth.html','Minor'),
    'minor-medical-anthropology': ('/undergraduate/medical-anthropology-minor.html','Medical Anthropology, Minor'),
    'ba': ('/undergraduate/major-ba.html','Major (BA)'),
    'bam': ('/undergraduate/anth-bam.html','BA/MA Pathway (BAM)'),
    'honors-track': ('/undergraduate/honors-track.html','Honors Track'),
    'undergraduate-advising': ('/undergraduate/advising-support.html','Advising & Support'),
    'undergraduate-funding': ('/undergraduate/funding-sources.html','Funding Sources'),
    'undergraduate-mentoring-program': ('/undergraduate/ump.html','Undergraduate Mentoring Program (UMP)'),
    'ausa': ('/undergraduate/ausa.html','Anthropology Undergraduate Student Association (AUSA)'),
    'ma': ('/graduate/master-ma.html','Master’s (MA)'),
    'phd': ('/graduate/doctorate-phd.html','Doctorate (PhD)'),
    'graduate-students': ('/graduate/current-cohort.html','Current ANTH MA and PhD Students'),
    'graduate-funding': ('/graduate/funding-sources.html','Funding Sources'),
    'applications-admissions': ('/graduate/applications-admissions.html','Applications and Admissions'),
    'agsa': ('/graduate/agsa.html','Anthropology Graduate Student Association (AGSA)'),
    'directory': ('/faculty/core-faculty.html','Core Faculty'),
    'give-a-gift': ('/support-anth.html','Support ANTH'),
    'contact': ('/contact.html','Contact ANTH'),
    'lambda-alpha': ('/lambda-alpha.html','Lambda Alpha'),
    'policies-procedures': ('/policies-procedures.html','Policies and Procedures'),
}
for s in specials: M[s] = ('/about-anth/subfields-specializations/' + s + '.html', pages[s].findtext('title'))
why, experiential = '/about-anth/why-study-anth.html', '/undergraduate/experiential-learning.html'
links = {urlsplit(pages[s].findtext('link')).path.rstrip('/') or '/': dest for s,(dest,_) in M.items()}
for s in ['undergraduate','graduate']: links[urlsplit(pages[s].findtext('link')).path.rstrip('/')] = why
for s in ['practical-experience-internships','networking','field-schools']: links[urlsplit(pages[s].findtext('link')).path.rstrip('/')] = experiential
for s,_ in associated: links[urlsplit(pages[s].findtext('link')).path.rstrip('/')] = '/faculty/associated-faculty.html'
for s,item in people_source.items():
    links[urlsplit(item.findtext('link')).path.rstrip('/')] = '/faculty/' + s + '.html' if s in core_slugs else '/contact.html' if any(c.attrib.get('nicename') == 'staff' for c in item.findall('category')) else '/faculty/associated-faculty.html'
links.update({'/privacy-policy':'/privacy.html','/faculty':'/faculty/core-faculty.html'})
unresolved, image_inventory = set(), set()
def link(value):
    v = html.unescape(value).strip(); u = urlsplit(v)
    if u.netloc in ['anthropology.manoa.hawaii.edu','www.anthropology.manoa.hawaii.edu'] or (not u.netloc and not u.scheme and u.path):
        key = unquote(u.path).rstrip('/') or '/'
        if key in links: return "{{ '" + links[key] + ('#' + u.fragment if u.fragment else '') + "' | url }}"
        absolute = v if u.netloc else 'https://anthropology.manoa.hawaii.edu/' + v.lstrip('/')
        unresolved.add(absolute); return html.escape(absolute,quote=True)
    return html.escape(v,quote=True)

class Clean(HTMLParser):
    allowed = set('p h1 h2 h3 h4 h5 h6 ul ol li a strong b em i sup sub blockquote cite br hr dl dt dd address abbr time table caption thead tbody tfoot tr td th colgroup col details summary'.split())
    void = {'br','hr','col'}
    def __init__(self): super().__init__(convert_charrefs=True); self.out=[]; self.skip=[]
    def handle_starttag(self,t,attrs):
        if t in ['script','style','noscript','svg']: self.skip.append(t); return
        if self.skip: return
        a=dict(attrs)
        if t=='img': image_inventory.add(a.get('src','')); return
        if t=='iframe':
            if a.get('src') and 'google.com/maps' not in a['src']: self.out.append('<p><a href="'+link(a['src'])+'">'+html.escape(a.get('title') or 'View embedded resource')+'</a></p>')
            return
        if t=='button': t='h3'
        if t not in self.allowed: return
        at=''
        for k,v in attrs:
            if k=='href' and t=='a': at+=' href="'+link(v or '')+'"'
            elif k in ['id','colspan','rowspan','scope','start','span','headers']: at+=' '+k+'="'+html.escape(v or '',quote=True)+'"'
        if t=='table': at+=' class="content-table"'
        self.out.append('<'+t+at+'>')
    def handle_startendtag(self,t,attrs): self.handle_starttag(t,attrs)
    def handle_endtag(self,t):
        if self.skip:
            if t==self.skip[-1]: self.skip.pop()
            return
        if t=='button':t='h3'
        if t in self.allowed and t not in self.void:self.out.append('</'+t+'>\n')
    def handle_data(self,d):
        if not self.skip:self.out.append(html.escape(d,quote=False))
def clean(value):
    value = re.sub(r'<!-- wp:generateblocks/query-loop\b.*?<!-- /wp:generateblocks/query-loop -->','',value,flags=re.S)
    # Resource controls are rebuilt below; retain spreadsheet links within prose.
    def resource_button(m):
        return '' if re.search(r'Class Availability|Course Descriptions|UH Mānoa Catalog|UH Manoa Catalog|Area/Method/Theory Courses|5-Year Course Schedule',text(m[0]),re.I) else m[0]
    value = re.sub(r'<!-- wp:generateblocks/button\b.*?<!-- /wp:generateblocks/button -->',resource_button,value,flags=re.S)
    p=Clean();p.feed(value);s=''.join(p.out)
    s=re.sub(r'\[/?(?:fl_builder|embed|gallery)[^\]]*\]','',s)
    for _ in range(2):s=re.sub(r'<(a|p|h[1-6])\b[^>]*>\s*</\1>','',s)
    return re.sub(r'\n\s*\n','\n',s).strip()
def no_h1(s): return re.sub(r'<h1\b[^>]*>.*?</h1>','',s,flags=re.S|re.I).strip()
def section(body,gray=False):
    return '<div class="page-section'+(' page-section--gray' if gray else '')+'"><div class="container content-section"><div class="row gx-0 gx-sm-5 gx-lg-5"><div class="col-12">\n'+body+'\n</div></div></div></div>\n'
files, published = {}, []
def add(path,value):
    p=Path(path)
    if p.exists() and not str(p).startswith(str(UNIT)):raise RuntimeError('Refusing to overwrite '+str(p))
    files[str(p)]=value
def data(name,value):add(UNIT/name,json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def page(dest,title,body,person=None):
    name='index.html' if dest=='/' else dest.lstrip('/')+'index.html' if dest.endswith('/') else dest.lstrip('/')
    front='---\nlayout: '+('layouts/profiles/faculty-profile.njk' if person else 'shell.njk')+'\ntitle: '+json.dumps(title,ensure_ascii=False)+'\ndescription: "This will be the meta description."\npermalink: '+json.dumps(dest)+'\n'+('personSlug: '+json.dumps(person)+'\n' if person else '')+'---\n'
    add(SITE/'src'/name,front+body);published.append(dest)
placeholder='/media/shared/placeholders/temp.jpg'
def person_record(s,item):
    m=meta(item);name=item.findtext('title')
    p={'name':name,'lastName':m.get('ln-order') or name.split()[-1],'slug':s,'type':'faculty' if s in core_slugs else 'staff','showInFacultyDirectory':s in core_slugs,'showInKeyContacts':bool(m.get('role')) or s not in core_slugs,'title':m.get('title',''),'roles':[m['role']] if m.get('role') else [],'office':m.get('office',''),'email':m.get('email',''),'photo':placeholder,'photoWidth':500,'photoHeight':500}
    digits=re.sub(r'\D','',m.get('tel',''))
    if len(digits)==11 and digits.startswith('1'):digits=digits[1:]
    if len(digits)==10:p.update(phone=f'({digits[:3]}) {digits[3:6]}-{digits[6:]}',phoneHref='+1'+digits)
    if s in core_slugs:p['url']='/faculty/'+s+'.html'
    for key,fields in [('publicationProfiles',[('gs-url','Google Scholar'),('aca-url','Academia.edu'),('or-url','ORCID'),('rg-url','ResearchGate')]),('websites',[('web_url',name)]),('additionalLinks',[('insta_url','Instagram')])]:
        entries=[{'label':label,'url':html.unescape(m[field]).strip()} for field,label in fields if m.get(field,'').strip()]
        if entries:p[key]=entries
    return p
people=[]
for s in core_slugs:
    item=people_source[s];p=person_record(s,item);bio=clean(item.findtext('c:encoded','',NS));awards=[]
    def award_section(m):
        body=m.group(1)
        for li in re.findall(r'<li\b[^>]*>(.*?)</li>',body,re.S):
            t=text(li);year=re.search(r'(?:,?\s*|\()(\d{4})\)?$',t)
            name=t[:year.start()].rstrip(' ,(') if year else t
            name=name.replace('CSS Excellence in Teaching Award','College of Social Sciences Award for Excellence in Teaching')
            if name:awards.append({'name':name,**({'year':year[1]} if year else {})})
        return ''
    bio=re.sub(r'<h2\b[^>]*>(?:University|College|Teaching|Research) Awards?</h2>\s*(.*?)(?=<h2\b|\Z)',award_section,bio,flags=re.S|re.I)
    if awards:p['awards']=awards
    people.append(p);page(p['url'],p['name'],no_h1(bio),s)
for s,item in people_source.items():
    if any(c.attrib.get('nicename')=='staff' for c in item.findall('category')):people.append(person_record(s,item))
data('people.json',people)
aliases={}
for p in people:
    if p['type']=='faculty':
        aliases[p['name']]=p
        aliases[p['name'].split()[0]+' '+p['lastName']]=p
aliases['Ty Tengan']=next(p for p in people if p['slug']=='ty-p-kawika-tengan')
students=[];unmatched_advisors=[]
for s,item in grads_source.items():
    m=meta(item);area=m.get('subfield','')
    if area.startswith('a:'):area=', '.join(re.findall(r's:\d+:"([^"]*)";',area))
    student={'name':item.findtext('title'),'lastName':m.get('ln-order') or item.findtext('title').split()[-1],'slug':s,'program':m.get('program',''),'studyArea':area,'research':m.get('research',''),'email':m.get('email_gr',''),'photo':placeholder,'photoWidth':500,'photoHeight':500,'advisors':[]}
    advisor=m.get('advisor','').strip()
    if advisor:
        a={'name':advisor};p=aliases.get(advisor)
        if p:a.update(name=p['name'],url=p['url'])
        elif m.get('advisorurl'):a['url']=links.get(urlsplit(m['advisorurl']).path.rstrip('/'),m['advisorurl'])
        else:unmatched_advisors.append(advisor)
        student['advisors'].append(a)
    students.append(student)
students.sort(key=lambda s:s['lastName'].casefold());data('graduate-students.json',students)

# Existing text-based groups plus former people stored as custom posts.
groups=[]
for slug,title in associated:
    members=[];body=no_h1(clean(raw(slug)))
    for li in re.findall(r'<li\b[^>]*>(.*?)</li>',body,re.S):
        member_links=[{'url':html.unescape(href),'label':text(label)} for href,label in re.findall(r'<a\b[^>]*href="([^"]+)"[^>]*>(.*?)</a>',li,re.S)]
        t=text(re.sub(r'<a\b[^>]*>.*?</a>','',li,flags=re.S)).rstrip(' -–—|');parts=re.split(r'\s+[–—-]\s+',t,maxsplit=1)
        member={'name':parts[0]}
        if len(parts)>1:member['description']=parts[1]
        if member_links:member['links']=member_links
        members.append(member)
    if slug=='emeritus-retired-faculty':
        for s,item in people_source.items():
            if any(c.attrib.get('nicename')=='former' for c in item.findall('category')):
                m=meta(item);members.append({'name':item.findtext('title'),**({'email':m['email']} if m.get('email') else {}),'description':m.get('title','')})
    groups.append({'title':title,'members':members})
    add(ROOT/'exports/anth'/('associated-'+slug+'.html'),body+'\n')
data('associated-faculty.json',{'groups':groups})

resource_include='{% include "units/anth/course-planning.njk" %}\n{% include "layouts/content/course-resources.njk" %}'
degree_slugs={'minor','minor-medical-anthropology','ba','bam','honors-track','ma','phd','applied-archaeology','applied-cultural-anthropology'}
for s,(dest,title) in M.items():
    content=no_h1(clean(raw(s)))
    if s=='department-news':body=section('<h1>Department News</h1><p>Department news will be added here.</p>')
    elif s=='graduate-students':
        intro=re.search(r'<p\b[^>]*>.*?</p>',content,re.S)
        body=section('<h1>'+title+'</h1>'+(intro[0] if intro else ''))+section('{% include "layouts/profiles/student-directory.njk" %}',True)
    elif s=='directory':
        intro=re.search(r'<p\b[^>]*>.*?</p>',content,re.S)
        body=section('<h1>Core Faculty</h1>'+(intro[0] if intro else ''))+section('{% include "layouts/profiles/faculty-directory.njk" %}',True)
    elif s=='contact':
        intro=re.search(r'<p\b[^>]*>.*?</p>',content,re.S)
        body=section('<h1>Contact ANTH</h1>'+(intro[0] if intro else ''))+'<div class="page-section"><div class="container content-section">{% include "layouts/content/unit-contact.njk" %}</div></div>\n'+section('<h2>Key Contacts</h2>{% set directoryPeople = key_contacts %}{% include "layouts/profiles/people-grid.njk" %}',True)
    elif s=='give-a-gift':
        body='{% from "layouts/content/image-text-row.njk" import imageTextRow %}\n<div class="page-section"><div class="container content-section">{% call imageTextRow(\'/media/branding/logos/uhf.svg\', 230, 59.33, \'University of Hawaiʻi Foundation\', true, \'https://www.uhfoundation.org/\', \'sidebar-media\') %}\n<h1>Support ANTH</h1>\n'+content+'\n{% endcall %}</div></div>'
    elif s=='policies-procedures':body='{% include "pages/policies-procedures.njk" %}'
    else:body=section('<h1>'+html.escape(title)+'</h1>'+content)
    if s in degree_slugs:body+=section(resource_include)
    page(dest,title,body)
page(why,'Why Study ANTH',section('<h1>Why Study ANTH</h1>'+''.join('<h2>'+label+'</h2>'+no_h1(clean(raw(s))) for s,label in [('undergraduate','Undergraduate Study'),('graduate','Graduate Study')])))
page(experiential,'Experiential Learning',section('<h1>Experiential Learning</h1>'+''.join('<h2>'+label+'</h2>'+no_h1(clean(raw(s))) for s,label in [('practical-experience-internships','Practical Experience and Internships'),('networking','Networking'),('field-schools','Field Schools')])))
page('/faculty/associated-faculty.html','Associated Faculty',section('<h1>Associated Faculty</h1><p>Meet the adjunct, affiliate, cooperating, emeritus, and retired faculty associated with the Department of Anthropology.</p>')+section('{% include "layouts/profiles/associated-faculty.njk" %}',True))
page('/graduate/degrees-awarded.html','Degrees Awarded',section('<h1>Degrees Awarded</h1><p>Information about Anthropology degrees awarded will be added here.</p>'))
page('/anth-courses.html','ANTH Courses',section('<h1>ANTH Courses</h1><p>Course information will be added here.</p>')+section(resource_include))
page('/privacy.html','Privacy Policy','{% include "pages/privacy.njk" %}')

navigation=json.loads((UNIT/'navigation.json').read_text())
about=next(x for x in navigation if x['label']=='About')['children']
about[1].update(label='Subfields and Specializations',url=M['overview'][0])
next(x for x in navigation if x['label']=='Courses')['url']='/anth-courses.html'
ug=next(x for x in navigation if x['label']=='Undergraduate')['children']
ug[1].update(label='Medical Anthropology, Minor',url=M['minor-medical-anthropology'][0])
ug.insert(5,{'label':'Experiential Learning','url':experiential,'icon':'door-open','iconColor':None})
grad=next(x for x in navigation if x['label']=='Graduate')['children']
grad.append({'label':'Applications & Admissions','url':M['applications-admissions'][0],'icon':'door-open','iconColor':None})
next(x for x in navigation if x['label']=='Support ANTH')['url']=M['give-a-gift'][0]
next(x for x in navigation if x['label']=='Contact')['url']=M['contact'][0]
data('navigation.json',navigation)
unit=json.loads((UNIT/'unit-details.json').read_text());unit['address'][0]='Saunders Hall 346';unit['facultyBasePath']='/faculty/';data('unit-details.json',unit)
settings=json.loads((ROOT/'src/data/units/psy/site-settings.json').read_text());settings.update(stylesheet='/anth.css',url='https://anthropology.manoa.hawaii.edu',openGraph=json.loads((UNIT/'site-settings.json').read_text())['openGraph']);data('site-settings.json',settings)
data('catalog-courses.json',{'prefix':'ANTH','catalogKey':'anthropology'})
resources=[{'label':'Area/Method/Theory Courses','url':'https://docs.google.com/spreadsheets/d/1K7Ghioku0HaPfx5GbFlOsq5tQ9e9Tjtu6unMt9RyEps/edit?usp=sharing','icon':'list-check'}, {'label':'5-Year Course Schedule','url':'https://docs.google.com/spreadsheets/d/1jD5tHjS5xiP_f4zjyLF5puK61AtKAwZA8Ot2_DZF8yc/edit?usp=sharing','icon':'calendar3'}]
data('course-planning.json',{'links':resources})
add(ROOT/'src/includes/units/anth/course-planning.njk','''{% from "layouts/content/button.njk" import button %}
<nav class="course-resources course-resources--two mb-3" aria-label="Anthropology course planning">
<div class="row g-3 course-resource-grid">
{% for resource in course_planning.links %}<div class="col-12">{{ button(resource.label, resource.url, "teal" if loop.first else "blue", resource.icon) }}</div>{% endfor %}
</div>
</nav>
''')

# Policy sources remain attributed; do not imply differing unit wording is identical.
puba=(ROOT/'exports/puba/policies-and-procedures.html').read_text()
anth_policy=no_h1(clean(raw('policies-procedures')))
add(ROOT/'exports/anth/policies-and-procedures.html','<h1>Policies and Procedures</h1>\n'+anth_policy+'\n')
policy=section('<h1>Policies and Procedures</h1><p>University policies and procedures collected from Public Administration and Anthropology. Unit-specific wording is retained below.</p>')+section('<h2>Public Administration</h2>'+re.sub(r'<h2\b','<h3',re.sub(r'</h2>','</h3>',no_h1(puba))))+section('<h2>Anthropology</h2>'+re.sub(r'<h([2-5])\b',lambda m:'<h'+str(int(m[1])+1),re.sub(r'</h([2-5])>',lambda m:'</h'+str(int(m[1])+1)+'>',anth_policy)))
add(ROOT/'src/includes/pages/policies-procedures.njk',policy)

student_bank=sorted('/'+str(p.relative_to(ROOT/'src')) for p in (ROOT/'src/media/heroes/students').glob('*.webp'))
mural_bank=sorted('/'+str(p.relative_to(ROOT/'src')) for p in (ROOT/'src/media/heroes/saunders-mural').glob('*.webp'))
rng=random.Random(11011);rng.shuffle(student_bank);rng.shuffle(mural_bank)
data('heroes.json',{'defaultHero':student_bank[0],'pages':{url:{'image':student_bank[i%len(student_bank)],'position':'center center','alt':'Students at the University of Hawaiʻi at Mānoa','credit':False} for i,url in enumerate(published) if url not in {p['url'] for p in people if p.get('url')}}})
data('faculty-heroes.json',{'pages':{p['url']:{'image':mural_bank[i%len(mural_bank)],'position':'center center','alt':'Detail of the mural in Saunders Hall at the University of Hawaiʻi at Mānoa','credit':False} for i,p in enumerate(people) if p.get('url')}})
for f in ['scripts/shared-bootstrap.mjs','scripts/shared-settings.mjs','scripts/shared-source.mjs','eleventy.config.js','.gitignore','AGENTS.md']:add(SITE/f,(ROOT.parent/'pols'/f).read_text())
pkg=json.loads((ROOT.parent/'pols/package.json').read_text());pkg['name']='anth';pkg['scripts']['dev']='eleventy --serve --port=8089';add(SITE/'package.json',json.dumps(pkg,indent=2)+'\n')
lock=json.loads((ROOT.parent/'pols/package-lock.json').read_text());lock['name']='anth';lock['packages']['']['name']='anth';add(SITE/'package-lock.json',json.dumps(lock,indent=2)+'\n')
add(SITE/'shared.config.json',json.dumps({'repository':'cssweb-stack/css-shared','ref':'main','localPath':'../css-shared','unit':'anth'},indent=2)+'\n')
add(SITE/'.github/workflows/deploy.yml',(ROOT.parent/'pols/.github/workflows/deploy.yml').read_text().replace('POLS','ANTH').replace('/pols/','/anth/'))
verify=(ROOT.parent/'pols/scripts/verify-site.py').read_text().replace('POLS','ANTH').replace("units/pols","units/anth").replace('len(pages)!=51 or len(faculty)!=18 or len(students)!=27',f'len(pages)!={len(published)} or len(faculty)!=13 or len(students)!=25')
add(SITE/'scripts/verify-site.py',verify)
inventory=io.StringIO();writer=csv.writer(inventory);writer.writerow(['old_url','new_url','status'])
for kind in ['page','people','grad']:
    for i in [i for i in items if i.findtext('w:post_type','',NS)==kind]:
        old=i.findtext('link');status=i.findtext('w:status','',NS);key=urlsplit(old).path.rstrip('/') or '/'
        dest=links.get(key,'') if status=='publish' else ''
        if kind=='grad' and status=='publish':dest='/graduate/current-cohort.html';links[key]=dest
        writer.writerow([old,dest,'draft-excluded' if status!='publish' else 'mapped' if dest else 'review'])
add(SITE/'reference/url-inventory.csv',inventory.getvalue())
report={'sources':[{'file':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sources],'pages':len(published),'coreFaculty':len(core_slugs),'staff':len(people)-len(core_slugs),'graduateStudents':len(students),'draftStudentsExcluded':[i.findtext('title') for i in items if i.findtext('w:post_type','',NS)=='grad' and i.findtext('w:status','',NS)!='publish'],'unmatchedAdvisors':sorted(set(unmatched_advisors)),'associatedGroups':[{ 'title':g['title'],'count':len(g['members'])} for g in groups],'retainedSourceLinks':sorted(unresolved),'sourceImagesNotDownloaded':sorted(image_inventory),'deferred':['Blog posts/news migration','Degrees awarded content and spreadsheet links','Course page write-up','Policies source reconciliation and wider rollout','Real portraits'],'publishedUrls':published,'workbookPasses':workbook}
add(SITE/'reference/migration-report.json',json.dumps(report,ensure_ascii=False,indent=2)+'\n')
add(SITE/'README.md','# Anthropology website\n\nShared templates, data and media are in ../css-shared.\nRun npm ci, then npm run dev for http://localhost:8089/.\nRun npm run build and npm run verify before publishing.\nNo remote or deployment has been configured by this migration.\nReview reference/migration-report.json and url-inventory.csv before launch.\n')
print('*** Begin Patch')
for path,value in files.items():
    p=Path(path)
    if p.exists():
        print('*** Update File: '+path+'\n@@')
        for line in p.read_text().splitlines():print('-'+line)
    else:print('*** Add File: '+path)
    for line in value.splitlines():print('+'+line)
print('*** End Patch')
