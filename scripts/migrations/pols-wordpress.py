"""Generate a reviewable POLS migration patch; never download media.

Run from css-shared. Output is an apply_patch document, not an executable export.
"""
import json, re, html, unicodedata, hashlib, random, csv, io
from pathlib import Path
from urllib.parse import urlsplit, unquote
from html.parser import HTMLParser
import xml.etree.ElementTree as ET

SHARED = Path.cwd()
SITE = SHARED.parent / 'pols'
SOURCE = Path('/Users/bill/Downloads/politicalsciencepols.WordPress.2026-11-11.xml')
NS = {'w':'http://wordpress.org/export/1.2/', 'c':'http://purl.org/rss/1.0/modules/content/'}
items = ET.parse(SOURCE).findall('./channel/item')
pages = {i.findtext('w:post_name','',NS):i for i in items if i.findtext('w:post_type','',NS)=='page' and i.findtext('w:status','',NS)=='publish'}
raw = lambda slug: pages[slug].findtext('c:encoded','',NS)
def slugify(value):
    return re.sub(r'[^a-z0-9]+','-',unicodedata.normalize('NFKD',value).encode('ascii','ignore').decode().lower()).strip('-')
def text(value):
    return re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',value))).strip()
def lines(value):
    value=re.sub(r'<(?:br\b[^>]*|/p|/h[1-6]|/li)>','\n',value,flags=re.I)
    return [text(x) for x in value.splitlines() if text(x)]

faculty_slugs = ['noenoe-silva','carolyn-stephenson','dean-saranillio','debbie-samaniego','felix-mantz','kathy-ferguson','nicole-sunday-grove','nevzat-soguk','lawrence-nitz','jamaica-osorio','noelani-goodyear-kaopua','debora-halbert','sankaran-krishna','kate-zhou','ehito-kimura','katharina-heyer','jonathan-goldberg-hiller','jairus-grove']
specials=['alternative-futures','comparative-politics','indigenous-politics','international-relations','law-and-policy','political-theory']
M={
 'home':('/', 'Political Science at the University of Hawaiʻi'),
 'specializations':('/about-pols/specializations/','Specializations'),
 'certificate-in-law-and-society':('/undergraduate/certificate-law-society.html','Certificate (Law and Society)'),
 'minor':('/undergraduate/minor.html','Minor'), 'major':('/undergraduate/major-ba.html','Major (BA)'),
 'bam':('/undergraduate/bam.html','BA/MA Pathway (BAM)'), 'honors-track':('/undergraduate/honors-track.html','Honors Track'),
 'internships-and-scholarships':('/undergraduate/internships-scholarships/','Internships and Scholarships'),
 'community-internships':('/undergraduate/internships-scholarships/community-internships.html','Community Internships'),
 'undergraduate-advising':('/undergraduate/advising-support.html','Advising & Support'),
 'undergraduate-slos':('/undergraduate/student-learning-outcomes.html','Undergraduate Student Learning Outcomes'),
 'ma-program':('/graduate/master-ma.html','Master’s (MA)'), 'phd-program':('/graduate/doctorate-phd.html','Doctorate (PhD)'),
 'graduate-students':('/graduate/current-cohort.html','Current POLS MA and PhD Students'),
 'funding-opportunities':('/graduate/funding-sources.html','Funding Sources'),
 'teaching-opportunities':('/graduate/teaching-opportunities.html','Teaching Opportunities'),
 'graduate-slos':('/graduate/student-learning-outcomes.html','Graduate Student Learning Outcomes'),
 'applications-admissions':('/graduate/applications-admissions.html','Applications and Admissions'),
 'give-a-gift':('/support-pols.html','Support POLS'), 'contact':('/contact.html','Contact POLS'),
 'pi-sigma-alpha':('/pi-sigma-alpha.html','Pi Sigma Alpha'),
 'news':('/news.html','News'), 'colloquia':('/colloquia.html','Colloquia')}
for s in specials:M[s]=('/about-pols/specializations/'+s+'.html',pages[s].findtext('title'))
for s in faculty_slugs:M[s]=('/faculty/'+s+'.html',pages[s].findtext('title'))
links={urlsplit(pages[s].findtext('link')).path.rstrip('/') or '/':dest for s,(dest,_) in M.items()}
why='/about-pols/why-study-pols.html'
for s in ['about','undergraduate-program','graduate-program']:links[urlsplit(pages[s].findtext('link')).path.rstrip('/')]=why
links.update({'/faculty':'/faculty/','/privacy-policy':'/privacy.html'})
unresolved=set(); image_inventory=[]
def link(v):
    u=urlsplit(html.unescape(v)); key=unquote(u.path).rstrip('/') or '/'
    if u.netloc in ('politicalscience.manoa.hawaii.edu','www.politicalscience.manoa.hawaii.edu') or (not u.netloc and not u.scheme and u.path):
        if key in links:return "{{ '"+links[key]+('#'+u.fragment if u.fragment else '')+"' | url }}"
        absolute=v if u.netloc else 'https://politicalscience.manoa.hawaii.edu/'+v.lstrip('/')
        unresolved.add(absolute);return html.escape(absolute,quote=True)
    return html.escape(v,quote=True)
class Clean(HTMLParser):
    allowed=set('p h1 h2 h3 h4 h5 h6 ul ol li a strong b em i sup sub blockquote cite br hr dl dt dd address abbr time table caption thead tbody tfoot tr td th colgroup col details summary'.split())
    void={'br','hr','col'}
    def __init__(self):super().__init__(convert_charrefs=True);self.out=[];self.skip=0;self.stack=[]
    def handle_starttag(self,t,attrs):
        a=dict(attrs)
        if t in ('script','style','noscript'):self.skip+=1;return
        if self.skip:return
        if t=='img':image_inventory.append(a.get('src',''));return
        if t=='iframe':
            if a.get('src') and 'google.com/maps' not in a['src']:self.out.append('<p><a href="'+link(a['src'])+'">'+html.escape(a.get('title') or 'View embedded resource')+'</a></p>')
            return
        if t not in self.allowed:return
        at=''
        for k,v in attrs:
            if k=='href' and t=='a':at+=' href="'+link(v or '')+'"'
            elif k in ('id','colspan','rowspan','scope','start','span','headers'):at+=' '+k+'="'+html.escape(v or '',quote=True)+'"'
        if t=='table':at+=' class="content-table"'
        self.out.append('<'+t+at+'>')
    def handle_startendtag(self,t,a):self.handle_starttag(t,a)
    def handle_endtag(self,t):
        if t in ('script','style','noscript'):self.skip=max(0,self.skip-1);return
        if not self.skip and t in self.allowed and t not in self.void:self.out.append('</'+t+'>\n')
    def handle_data(self,d):
        if not self.skip:self.out.append(html.escape(d,quote=False))
def clean(value):
    p=Clean();p.feed(value);s=''.join(p.out)
    s=re.sub(r'\[/?(?:fl_builder|embed|gallery)[^\]]*\]','',s)
    return re.sub(r'\n\s*\n','\n',s).strip()
def strip_h1(value):return re.sub(r'<h1\b[^>]*>.*?</h1>','',value,flags=re.S|re.I)
def section(body,gray=False):
    return '<div class="page-section'+(' page-section--gray' if gray else '')+'">\n<div class="container content-section">\n<div class="row gx-0 gx-sm-5 gx-lg-5"><div class="col-12">\n'+body+'\n</div></div>\n</div>\n</div>\n'
files={}; published=[]
def add(path,value):
    if Path(path).exists() and '/src/data/units/pols/' not in str(path):raise RuntimeError('Refusing to overwrite '+str(path))
    files[str(path)]=value
def data(name,value):add(SHARED/'src/data/units/pols'/name,json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def page(dest,title,body,profile=None):
    file='index.html' if dest=='/' else dest.lstrip('/')+'index.html' if dest.endswith('/') else dest.lstrip('/')
    front='---\nlayout: '+('layouts/profiles/faculty-profile.njk' if profile else 'shell.njk')+'\ntitle: '+json.dumps(title,ensure_ascii=False)+'\ndescription: "This will be the meta description."\npermalink: '+json.dumps(dest)+'\n'+('personSlug: '+json.dumps(profile)+'\n' if profile else '')+'---\n'
    add(SITE/'src'/file,front+body);published.append(dest)
faculty=[]
services=[('scholar.google','Google Scholar'),('researchgate.net','ResearchGate'),('academia.edu','Academia.edu'),('orcid.org','ORCID'),('pubmed','PubMed')]
for s in faculty_slugs:
    r=raw(s);boundary=re.search(r'<h[2-6][^>]*>\s*Background\s*</h[2-6]>',r,re.I)
    if not boundary:raise ValueError('No biography boundary '+s)
    side=r[:boundary.start()];name=text(re.search(r'<h1[^>]*>(.*?)</h1>',side,re.S).group(1))
    em=re.search(r'<em[^>]*>(.*?)</em>',side,re.S);titles=text(em.group(1)).split(', ',1) if em else []
    person={'name':name,'lastName':name.split()[-1],'slug':s,'url':M[s][0],'photo':'/media/units/pols/faculty-staff/temp.jpg','photoWidth':400,'photoHeight':400}
    if titles:person['title']=titles[0]
    if len(titles)>1:person['roles']=[titles[1]]
    for line in lines(side):
        if line.startswith('Office:'):person['office']=line.split(':',1)[1].strip()
        if line.startswith(('Telephone:','Phone:')):
            person['phone']=line.split(':',1)[1].strip();person['phoneHref']='+'+re.sub(r'\D','',person['phone']) if person['phone'].startswith('1') else '+1'+re.sub(r'\D','',person['phone'])
    email=re.search(r'href=[\'"]mailto:([^\'"?]+)',side,re.I)
    if email:person['email']=html.unescape(email.group(1))
    websites=[];publications=[];extras=[]
    for href,inside in re.findall(r'<a\b[^>]*href=[\'"]([^\'"]+)[\'"][^>]*>(.*?)</a>',side,re.S|re.I):
        href=html.unescape(href).strip();label=text(inside)
        if href.startswith(('mailto:','tel:')):continue
        service=next((label for domain,label in services if domain in href),None)
        if service:publications.append({'label':service,'url':href})
        elif re.search(r'award|medal|teaching|clopton',label,re.I):continue
        else:
            item={'label':label or 'Website','url':href}
            (extras if any(x in href for x in ['twitter.com','facebook.com','wikipedia.org','bsky.app']) or 'CV' in label else websites).append(item)
    for key,value in [('websites',websites),('publicationProfiles',publications),('additionalLinks',extras)]:
        if value:person[key]=value
    award_lines=[x for x in lines(side) if re.search(r'\b(?:Award|Medal|Citation|Excellence)\b',x) and re.search(r'\(\d{4}\)',x) and 'Browse' not in x]
    if award_lines:
        person['awards']=[]
        for a in award_lines:
            match=re.search(r'^(.*?)\s*\((\d{4})\)',a)
            if match:
                an=match[1].replace('CSS Excellence in Teaching Award','College of Social Sciences Award for Excellence in Teaching').replace('BOR Excellence in Teaching','Regents’ Medal for Excellence in Teaching').replace("Regents'",'Regents’')
                person['awards'].append({'name':an,'year':match[2]})
    faculty.append(person);page(M[s][0],name,clean(r[boundary.start():]),s)
students=[]
for heading,body in re.findall(r'<h2[^>]*>(.*?)</h2>(.*?)(?=<h2|\Z)',raw('graduate-students'),re.S|re.I):
    name=text(heading);fields={}
    for line in lines(body):
        for label,key in [('Program:','program'),('Research Interests:','research')]:
            if line.startswith(label):fields[key]=line[len(label):].strip()
    program=fields.get('program','');match=re.match(r'([^()]+?)(?:\s*\((.*?)\))?$',program)
    student={'name':name,'lastName':name.split()[-1],'slug':slugify(name),'program':match[1].strip() if match else program,'studyArea':match[2] or '' if match else '', 'research':fields.get('research',''),'photo':'/media/units/pols/graduate-students/temp.jpg','advisors':[]}
    email=re.search(r'mailto:([^\'"?]+)',body)
    if email:student['email']=html.unescape(email[1])
    advisor=re.search(r'<p[^>]*>\s*<em[^>]*>Advisors?:?</em>\s*:?(.*?)</p>',body,re.S|re.I)
    if advisor:
        for href,label in re.findall(r'<a[^>]*href=[\'"]([^\'"]+)[\'"][^>]*>(.*?)</a>',advisor[1],re.S):
            a={'name':text(label)};dest=links.get(urlsplit(href).path.rstrip('/'))
            if dest:a['url']=dest
            student['advisors'].append(a)
        if not student['advisors'] and text(advisor[1]):student['advisors']=[{'name':text(advisor[1])}]
    students.append(student)
data('faculty.json',faculty);data('graduate-students.json',students)
for s,(dest,title) in M.items():
    if s in faculty_slugs:continue
    content=strip_h1(clean(raw(s)))
    if s=='graduate-students':
        body=section('<h1>'+title+'</h1><p class="intro">Explore the research interests of graduate students in the Department of Political Science at the University of Hawaiʻi at Mānoa. Their work spans Indigenous politics, political theory, alternative futures, comparative politics, international relations, law, and policy.</p>')+section('{% include "layouts/profiles/student-directory.njk" %}',True)
    elif s=='contact':
        intro=re.search(r'<p[^>]*>.*?</p>',raw(s),re.S)[0]
        tail=re.split(r'</iframe>',raw(s),maxsplit=1)[-1]
        hours=re.search(r'<p><a[^>]+>Faculty/Lecturer/GA Office Hours</a></p>',raw(s),re.S)
        body=section('<h1>'+title+'</h1>'+clean(intro))+'<div class="page-section"><div class="container content-section">{% include "layouts/content/unit-contact.njk" %}</div></div>'+section((clean(hours[0]) if hours else '')+clean(tail))
    elif s=='specializations':body=section('<h1>'+title+'</h1>'+content+'<ul>'+''.join('<li><a href="'+link('https://politicalscience.manoa.hawaii.edu/'+x+'/')+'">'+M[x][1]+'</a></li>' for x in specials)+'</ul>')
    elif s=='give-a-gift':body='<div class="page-section"><div class="container content-section"><div class="row content-sidebar gy-4 gx-0 gx-sm-5 gx-lg-5"><div class="col-12 col-lg-9"><h1>'+title+'</h1>'+content+'</div><aside class="col-12 col-lg-3 sidebar-resources" aria-label="UH Foundation"><a href="https://www.uhfoundation.org/"><img class="sidebar-media" src="{{ \'/media/branding/logos/uhf.svg\' | url }}" alt="University of Hawaiʻi Foundation"></a></aside></div></div></div>'
    else:body=section('<h1>'+html.escape(title)+'</h1>'+content)
    if s=='internships-and-scholarships':body+=section('<p><a href="{{ \'/undergraduate/internships-scholarships/community-internships.html\' | url }}">Community Internships</a></p>')
    page(dest,title,body)
page(why,'Why Study POLS',section('<h1>Why Study POLS</h1>'+''.join('<h2>'+label+'</h2>'+strip_h1(clean(raw(s))) for s,label in [('about','About Political Science'),('undergraduate-program','Undergraduate Study'),('graduate-program','Graduate Study')])))
page('/faculty/','Faculty',section('<h1>Faculty</h1><p class="intro">Meet the faculty of the Department of Political Science at the University of Hawaiʻi at Mānoa.</p>')+section('{% include "layouts/profiles/faculty-directory.njk" %}',True))
page('/about-pols/pols-courses.html','POLS Courses',section('<h1>POLS Courses</h1>{% include "layouts/content/course-resources.njk" %}'))
page('/privacy.html','Privacy Policy','{% include "pages/privacy.njk" %}')
def nav(label,url,icon=None):return {'label':label,'url':url,**({'icon':icon,'iconColor':None} if icon else {})}
ug=[('Certificate (Law and Society)','certificate-in-law-and-society','award'),('Minor','minor','book'),('Major (BA)','major','mortarboard'),('BA/MA Pathway (BAM)','bam','signpost-2'),('Honors Track','honors-track','star'),('Internships & Scholarships','internships-and-scholarships','door-open'),('Advising & Support','undergraduate-advising','compass'),('Student Learning Outcomes','undergraduate-slos','list-check')]
grad=[('Master’s (MA)','ma-program','mortarboard'),('Doctorate (PhD)','phd-program','mortarboard'),('Current Cohort','graduate-students','people'),('Funding Sources','funding-opportunities','cash-coin'),('Teaching Opportunities','teaching-opportunities','briefcase'),('Student Learning Outcomes','graduate-slos','list-check')]
data('navigation.json',[nav('Home','/'),{'label':'About','children':[nav('Why Study POLS',why,'question-circle'),nav('Specializations',M['specializations'][0],'layers')]},nav('Courses','/about-pols/pols-courses.html'),{'label':'Undergraduate','children':[nav(a,M[b][0],c) for a,b,c in ug]},{'label':'Graduate','children':[nav(a,M[b][0],c) for a,b,c in grad]},nav('Faculty','/faculty/'),nav('Support POLS','/support-pols.html'),nav('Contact','/contact.html')])
unit=json.loads((SHARED/'src/data/units/psy/unit-details.json').read_text())
unit.update(name='Department of Political Science',shortName='POLS',building='saunders-hall',address=['Saunders 640','2424 Maile Way','Honolulu, HI 96822'],phone={'label':'(808) 956-8357','href':'tel:+18089568357'},email={'label':'polisci@hawaii.edu','href':'mailto:polisci@hawaii.edu'},footerIdentity={'prefix':'Department of','name':'Political Science'},facultyBasePath='/faculty/')
unit['logo']['alt']='Department of Political Science, University of Hawaiʻi at Mānoa'
unit['buildingPhoto']={'src':'/media/shared/other/saunders-hall.webp','alt':'Saunders Hall at the University of Hawaiʻi at Mānoa','width':300,'height':162}
for v in unit['logo']['variants'].values():v['src']=v['src'].replace('psy-','pols-')
data('unit-details.json',unit)
settings=json.loads((SHARED/'src/data/units/psy/site-settings.json').read_text());settings.update(stylesheet='/pols.css',url='https://politicalscience.manoa.hawaii.edu');data('site-settings.json',settings)
data('social.json',{'links':[{'label':'X','url':'https://x.com/uhmpolisci','icon':'social/twitter-x'}]})
data('search.json',{'provider':'google-site-restricted','domain':'politicalscience.manoa.hawaii.edu','label':'POLS'})
data('catalog-courses.json',{'prefix':'POLS','catalog':{'label':'UH Mānoa Catalog (POLS)','url':'https://manoa.hawaii.edu/catalog/category/social-sciences/pols/'}})
student_bank=sorted('/'+str(p.relative_to(SHARED/'src')) for p in (SHARED/'src/media/heroes/students').glob('*.webp'));mural_bank=sorted('/'+str(p.relative_to(SHARED/'src')) for p in (SHARED/'src/media/heroes/saunders-mural').glob('*.webp'));random.Random(42).shuffle(student_bank)
data('heroes.json',{'defaultHero':student_bank[0],'pages':{url:{'image':student_bank[i%len(student_bank)],'position':'center center','alt':'Students at the University of Hawaiʻi at Mānoa','credit':False} for i,url in enumerate(published) if not url.startswith('/faculty/') or url=='/faculty/'}})
data('faculty-heroes.json',{'pages':{p['url']:{'image':mural_bank[i%len(mural_bank)],'position':'center center','alt':'Detail of the mural in Saunders Hall at the University of Hawaiʻi at Mānoa','credit':False} for i,p in enumerate(faculty)}})
for f in ['scripts/shared-bootstrap.mjs','scripts/shared-settings.mjs','scripts/shared-source.mjs','eleventy.config.js','.gitignore','AGENTS.md']:
    add(SITE/f,(SHARED.parent/'psy'/f).read_text())
pkg=json.loads((SHARED.parent/'psy/package.json').read_text());pkg['name']='pols';pkg['scripts']['dev']='eleventy --serve --port=8087';pkg['scripts'].pop('verify',None);data_pkg=json.dumps(pkg,indent=2)+'\n';add(SITE/'package.json',data_pkg)
lock=json.loads((SHARED.parent/'psy/package-lock.json').read_text());lock['name']='pols';lock['packages']['']['name']='pols';add(SITE/'package-lock.json',json.dumps(lock,indent=2)+'\n')
add(SITE/'shared.config.json',json.dumps({'repository':'cssweb-stack/css-shared','ref':'main','localPath':'../css-shared','unit':'pols'},indent=2)+'\n')
add(SITE/'.github/workflows/deploy.yml',(SHARED.parent/'psy/.github/workflows/deploy.yml').read_text().replace('PSY','POLS').replace('/psy/','/pols/'))
csvout=io.StringIO();writer=csv.writer(csvout);writer.writerow(['old_url','new_url','status'])
for s,i in pages.items():
    old=i.findtext('link');dest=links.get(urlsplit(old).path.rstrip('/') or '/','');writer.writerow([old,dest,'mapped' if dest else 'review-unlisted'])
add(SITE/'reference/url-inventory.csv',csvout.getvalue())
add(SITE/'reference/migration-report.json',json.dumps({'source':SOURCE.name,'sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'pages':len(published),'faculty':len(faculty),'students':len(students),'unlistedSourcePages':[s for s in pages if (urlsplit(pages[s].findtext('link')).path.rstrip('/') or '/') not in links],'originalImageUrls':sorted(set(image_inventory)),'retainedExternalLinks':sorted(unresolved)},ensure_ascii=False,indent=2)+'\n')
add(SHARED/'docs/pols-migration.md','# Political Science migration\n\nNavigation Review POLS column and Sheet2, refined by the user walkthrough, define\nthe draft. Shared JSON/media/templates live in css-shared; page sources in pols.\nNo source images were downloaded. Faculty and students use supplied temp JPEGs.\nWhy Study combines all About and Undergraduate/Graduate Program HTML without images.\nTables keep their imported rows, cells, captions, and spans.\n\nPi Sigma Alpha is root-level. Specializations and Internships/Scholarships use\nfolder indexes and sibling subpages. Applications/Admissions, News, and Colloquia\nare preserved as non-navigation pages. Three unlisted faculty pages remain in the\noriginal export for later review; consult reference/migration-report.json.\nCurrent cohort data requires user roster review before launch.\n\nEvery page has local metadata; hero assignments are stable JSON selections.\nSearch indexing is disabled. The deployment workflow is prepared, not deployed.\n')
print('*** Begin Patch')
for p,value in files.items():
    if Path(p).exists():
        print('*** Update File: '+p+'\n@@')
        for line in Path(p).read_text().splitlines():print('-'+line)
    else:print('*** Add File: '+p)
    for line in value.splitlines():print('+'+line)
print('*** End Patch')
