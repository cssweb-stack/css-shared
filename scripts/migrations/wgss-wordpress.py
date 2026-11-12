"""Generate a one-time WGSS migration patch from the user-supplied Pages export.

Central data/media/templates; local HTML prose. No image downloads.
"""
from pathlib import Path
from urllib.parse import urlsplit, unquote
from zipfile import ZipFile
import xml.etree.ElementTree as E
import json,re,html,csv,io,hashlib,random
from wordpress_html import clean_html,no_h1,text

ROOT=Path.cwd();SITE=ROOT.parent/'wgss';UNIT=ROOT/'src/data/units/wgss'
SOURCE=ROOT/'exports/wgss/womengenderandsexualitystudieswgss.WordPress.2026-11-11.xml'
NS={'w':'http://wordpress.org/export/1.2/','c':'http://purl.org/rss/1.0/modules/content/'}
items=E.parse(SOURCE).findall('./channel/item')
pages={i.findtext('w:post_name','',NS):i for i in items if i.findtext('w:post_type','',NS)=='page' and i.findtext('w:status','',NS)=='publish'}
def raw(s):return pages[s].findtext('c:encoded','',NS)
core=['monisha-das-gupta','kathy-ferguson','l-ayu-saraswati','mire-koikari','lani-teves','s-heijin-lee','lisa-m-vallin']
M={'home':('/','Women, Gender and Sexuality Studies at the University of Hawaiʻi'),
 'alumni':('/about-wgss/alumni.html','Alumni'),'colloquia':('/about-wgss/colloquia.html','Colloquia'),
 'certificate-requirements':('/undergraduate/certificate.html','WGSS Certificate'),
 'queer-studies-certificate':('/undergraduate/queer-studies.html','Queer Studies Certificate'),
 'ba-requirements':('/undergraduate/major-ba/','Major (BA)'),
 'design-courses':('/undergraduate/major-ba/transnational-courses.html','Transnational Courses'),
 'online-ba-requirements':('/undergraduate/major-ba-online.html','Major (BA) Online'),
 'double-major':('/undergraduate/double-majors.html','Double Majors'),
 'honors-track':('/undergraduate/honors-track.html','Honors Track'),
 'wgss-graduate-certificate':('/graduate/graduate-certificate.html','WGSS Graduate Certificate'),
 'faculty':('/faculty/','Faculty'), 'give-a-gift':('/support-wgss.html','Support WGSS'),
 'contact':('/contact.html','Contact WGSS'), 'scholarships':('/funding-sources.html','Funding Sources')}
why='/about-wgss/why-study-wgss.html';outcomes='/undergraduate/student-learning-outcomes.html';applications='/graduate/applications-admissions.html'
links={urlsplit(pages[s].findtext('link')).path.rstrip('/') or '/':dest for s,(dest,_) in M.items()}
for s in ['about','undergraduate','graduate','jobs-prospects']:links[urlsplit(pages[s].findtext('link')).path.rstrip('/')]=why
for s in core+['meda-chesney-lind']:links['/'+s]='/faculty/'+s+'.html'
links.update({'/privacy-policy':'/privacy.html','/adws-certificate-requirements':'/graduate/graduate-certificate.html','/focus-courses':'/undergraduate/major-ba/transnational-courses.html'})
images=set();unresolved=set()
def link(v):
 v=html.unescape(v).strip();u=urlsplit(v);key='/'+unquote(u.path).strip('/') if u.path.strip('/') else '/'
 if u.netloc in ['wgss.manoa.hawaii.edu','www.wgss.manoa.hawaii.edu'] or (not u.netloc and not u.scheme and u.path):
  if key in links:return "{{ '"+links[key]+('#'+u.fragment if u.fragment else '')+"' | url }}"
  absolute=v if u.netloc else 'https://wgss.manoa.hawaii.edu/'+v.lstrip('/');unresolved.add(absolute);return html.escape(absolute,quote=True)
 return html.escape(v,quote=True)
def clean(s):return clean_html(s,link,images,videos=True)
def section(body,gray=False):return '<div class="page-section'+(' page-section--gray' if gray else '')+'"><div class="container content-section"><div class="row gx-0 gx-sm-5 gx-lg-5"><div class="col-12">\n'+body+'\n</div></div></div></div>\n'
files={};published=[]
def add(p,v):
 p=Path(p)
 if p.exists() and not str(p).startswith(str(UNIT)):raise RuntimeError('Refusing to overwrite '+str(p))
 files[str(p)]=v
def data(name,v):add(UNIT/name,json.dumps(v,ensure_ascii=False,indent=2)+'\n')
def page(dest,title,body,person=None):
 filename='index.html' if dest=='/' else dest.lstrip('/')+'index.html' if dest.endswith('/') else dest.lstrip('/')
 front='---\nlayout: '+('layouts/profiles/faculty-profile.njk' if person else 'shell.njk')+'\ntitle: '+json.dumps(title,ensure_ascii=False)+'\ndescription: "This will be the meta description."\npermalink: '+json.dumps(dest)+'\n'+('personSlug: '+json.dumps(person)+'\n' if person else '')+'---\n'
 add(SITE/'src'/filename,front+body);published.append(dest)
def fields(s):
 result={}
 for line in re.split(r'<br\s*/?>|</(?:p|h[1-6])>',s,flags=re.I):
  t=text(line)
  for prefix,key in [('Office:','office'),('Telephone:','phone'),('Phone:','phone')]:
   if t.startswith(prefix):result[key]=t[len(prefix):].strip()
 email=re.search(r'mailto:([^\'"?]+)',s)
 if email:result['email']=html.unescape(email[1])
 em=re.search(r'<em[^>]*>(.*?)</em>',s,re.S)
 if em:
  titles=text(em[1]).split(', ',1);result['title']=titles[0]
  if len(titles)>1:result['roles']=[titles[1]]
 return result
names={'monisha-das-gupta':('Monisha Das Gupta','Das Gupta'),'kathy-ferguson':('Kathy Ferguson','Ferguson'),'l-ayu-saraswati':('L. Ayu Saraswati','Saraswati'),'mire-koikari':('Mire Koikari','Koikari'),'lani-teves':('Lani Teves','Teves'),'s-heijin-lee':('S. Heijin Lee','Lee'),'lisa-m-vallin':('Lisa M. Vallin','Vallin'),'meda-chesney-lind':('Meda Chesney Lind','Chesney Lind')}
directory_blocks={text(name):body for name,body in re.findall(r'<h2[^>]*>(.*?)</h2>(.*?)(?=<h2\b|\Z)',raw('faculty'),re.S|re.I)}
contact_blocks={text(name):body for name,body in re.findall(r'<h2[^>]*>(.*?)</h2>(.*?)(?=<h2\b|\Z)',raw('contact'),re.S|re.I)}
people=[];missing=[]
services=[('scholar.google','Google Scholar'),('researchgate.net','ResearchGate'),('academia.edu','Academia.edu'),('orcid.org','ORCID'),('pubmed','PubMed')]
for slug in core+['meda-chesney-lind']:
 name,last=names[slug];is_core=slug in core;source=raw(slug) if slug in pages else '';boundary=re.search(r'<h2[^>]*>\s*Background\s*</h2>',source,re.I);side=source[:boundary.start()] if boundary else ''
 p={'name':name,'lastName':last,'slug':slug,'url':'/faculty/'+slug+'.html','type':'faculty','showInFacultyDirectory':is_core,'showInKeyContacts':name in contact_blocks,'photo':'/media/shared/placeholders/temp.jpg','photoWidth':500,'photoHeight':500}
 p.update(fields(directory_blocks.get(name,'')));p.update(fields(side))
 # Contact records supplement fields without replacing established academic titles/roles.
 for k,v in fields(contact_blocks.get(name,'')).items():
  if k not in ['title','roles'] and not p.get(k):p[k]=v
 if p.get('phone'):
  digits=re.sub(r'\D','',p['phone']);digits=digits[1:] if len(digits)==11 and digits.startswith('1') else digits
  assert len(digits)==10,(name,p['phone']);p['phone']=f'({digits[:3]}) {digits[3:6]}-{digits[6:]}';p['phoneHref']='+1'+digits
 for href,label in re.findall(r'<a\b[^>]*href=[\'"]([^\'"]+)[\'"][^>]*>(.*?)</a>',side,re.S):
  if href.startswith(('mailto:','tel:')):continue
  service=next((label for domain,label in services if domain in href),None)
  p.setdefault('publicationProfiles' if service else 'websites',[]).append({'label':service or text(label) or name,'url':html.unescape(href)})
 if not source:missing.append(name)
 bio=clean(source[boundary.start():]) if boundary else '<!-- Biography text was not included in the supplied export. -->'
 people.append(p);page(p['url'],name,bio,slug)
staff=fields(contact_blocks['Brooke Tanaka']);digits=re.sub(r'\D','',staff.pop('phone'));digits=digits[-10:]
people.append({'name':'Brooke Tanaka','lastName':'Tanaka','slug':'brooke-tanaka','type':'staff','showInFacultyDirectory':False,'showInKeyContacts':True,'photo':'/media/shared/placeholders/temp.jpg','photoWidth':500,'photoHeight':500,**staff,'phone':f'({digits[:3]}) {digits[3:6]}-{digits[6:]}','phoneHref':'+1'+digits})
data('people.json',people)
emeriti=[]
for name in ['Meda Chesney Lind','Ruth Dawson']:
 f=fields(directory_blocks[name]);m={'name':name,'description':f.get('title','')}
 if f.get('email'):m['email']=f['email']
 if name=='Meda Chesney Lind':m['links']=[{'label':'Biography','url':'/faculty/meda-chesney-lind.html'}]
 emeriti.append(m)
data('emeriti-faculty.json',{'groups':[{'title':'Emeriti Faculty','members':emeriti}]})

ug=no_h1(clean(raw('undergraduate')))
outcome_match=re.search(r'<h2[^>]*>Undergraduate Student Learning Objectives</h2>\s*(<ol>.*?</ol>)',ug,re.S)
assert outcome_match
outcome_body=outcome_match[0]
ug=ug[:outcome_match.start()]+'<p><a href="{{ \''+outcomes+'\' | url }}">Student Learning Outcomes</a></p>'+ug[outcome_match.end():]
graduate=no_h1(clean(raw('graduate')))
start=graduate.index('<h2>Applying for Graduate Study</h2>');end=graduate.find('<hr',start)
admissions=graduate[start:end if end>=0 else len(graduate)]
for slug,(dest,title) in M.items():
 content=no_h1(clean(raw(slug)))
 if slug=='faculty':
  intro=re.search(r'<p>.*?</p>',content,re.S)[0]
  extra=re.findall(r'<li>.*?Affiliate Faculty.*?</li>',content,re.S)
  body=section('<h1>Faculty</h1>'+intro)+section('{% include "layouts/profiles/faculty-directory.njk" %}<div class="mt-5">{% set facultyGroups = emeriti_faculty.groups %}{% include "layouts/profiles/associated-faculty.njk" %}</div>'+('<ul>'+''.join(extra)+'</ul>' if extra else ''),True)
 elif slug=='contact':
  intro=re.search(r'<p>.*?</p>',content,re.S)[0]
  body=section('<h1>Contact WGSS</h1>'+intro)+'<div class="page-section"><div class="container content-section">{% include "layouts/content/unit-contact.njk" %}</div></div>\n'+section('<h2>Key Contacts</h2>{% set directoryPeople = key_contacts %}{% include "layouts/profiles/people-grid.njk" %}',True)
 elif slug=='give-a-gift':
  body='{% from "layouts/content/image-text-row.njk" import imageTextRow %}\n<div class="page-section"><div class="container content-section">{% call imageTextRow(\'/media/branding/logos/uhf.svg\', 230, 59.33, \'University of Hawaiʻi Foundation\', true, \'https://www.uhfoundation.org/\', \'sidebar-media\') %}\n<h1>Support WGSS</h1>\n'+content+'\n{% endcall %}</div></div>'
 else:body=section('<h1>'+html.escape(title)+'</h1>'+content)
 if slug in ['ba-requirements','online-ba-requirements']:body+=section('<p><a href="{{ \''+outcomes+'\' | url }}">Student Learning Outcomes</a></p>')
 page(dest,title,body)
page(why,'Why Study WGSS',section('<h1>Why Study WGSS</h1>'+''.join('<h2>'+label+'</h2>'+body for label,body in [('About WGSS',no_h1(clean(raw('about')))),('Undergraduate Study',ug),('Graduate Study',graduate),('Job Prospects',no_h1(clean(raw('jobs-prospects'))))])))
page(outcomes,'Student Learning Outcomes',section('<h1>Student Learning Outcomes</h1>'+outcome_body))
page(applications,'Applications & Admissions',section('<h1>Applications &amp; Admissions</h1>'+admissions))
page('/wgss-courses.html','WGSS Courses',section('<h1>WGSS Courses</h1><p>Course information will be added here.</p>')+section('{% include "layouts/content/course-resources.njk" %}'))
page('/privacy.html','Privacy Policy','{% include "pages/privacy.njk" %}')
nav=json.loads((UNIT/'navigation.json').read_text());about=next(x for x in nav if x['label']=='About');about['children']=[x for x in about['children'] if x['label']!='Job Prospects']
next(x for x in nav if x['label']=='Courses')['url']='/wgss-courses.html'
next(x for x in nav if x['label']=='Undergraduate')['children'][2]['url']='/undergraduate/major-ba/'
next(x for x in nav if x['label']=='Graduate')['children'].append({'label':'Applications & Admissions','url':applications,'icon':'door-open','iconColor':None})
next(x for x in nav if x['label']=='Support WGSS')['url']='/support-wgss.html';next(x for x in nav if x['label']=='Contact')['url']='/contact.html';data('navigation.json',nav)
data('funding-link.json',{'label':'Funding Sources','url':'/funding-sources.html','icon':'cash-coin'})
unit=json.loads((UNIT/'unit-details.json').read_text());unit['facultyBasePath']='/faculty/';data('unit-details.json',unit)
settings=json.loads((ROOT/'src/data/units/anth/site-settings.json').read_text());settings.update(stylesheet='/wgss.css',url='https://wgss.manoa.hawaii.edu',openGraph=json.loads((UNIT/'site-settings.json').read_text())['openGraph']);data('site-settings.json',settings)
data('catalog-courses.json',{'prefix':'WGSS','catalogKey':'womenGenderAndSexualityStudies'})
data('social.json',{'links':[{'label':'X','url':'https://twitter.com/uhm_wgss?lang=en','icon':'social/twitter-x'}]})
student_bank=sorted('/'+str(p.relative_to(ROOT/'src')) for p in (ROOT/'src/media/heroes/students').glob('*.webp'));murals=sorted('/'+str(p.relative_to(ROOT/'src')) for p in (ROOT/'src/media/heroes/saunders-mural').glob('*.webp'));rng=random.Random(1111);rng.shuffle(student_bank);rng.shuffle(murals)
bio_urls={p['url'] for p in people if p.get('url')}
data('heroes.json',{'defaultHero':student_bank[0],'pages':{url:{'image':student_bank[i%len(student_bank)],'position':'center center','alt':'Students at the University of Hawaiʻi at Mānoa','credit':False} for i,url in enumerate(published) if url not in bio_urls}})
data('faculty-heroes.json',{'pages':{p['url']:{'image':murals[i%len(murals)],'position':'center center','alt':'Detail of the mural in Saunders Hall at the University of Hawaiʻi at Mānoa','credit':False} for i,p in enumerate(people) if p.get('url')}})
for f in ['scripts/shared-bootstrap.mjs','scripts/shared-settings.mjs','scripts/shared-source.mjs','eleventy.config.js','.gitignore','AGENTS.md']:add(SITE/f,(ROOT.parent/'anth'/f).read_text())
pkg=json.loads((ROOT.parent/'anth/package.json').read_text());pkg['name']='wgss';pkg['scripts']['dev']='eleventy --serve --port=8090';add(SITE/'package.json',json.dumps(pkg,indent=2)+'\n')
lock=json.loads((ROOT.parent/'anth/package-lock.json').read_text());lock['name']='wgss';lock['packages']['']['name']='wgss';add(SITE/'package-lock.json',json.dumps(lock,indent=2)+'\n')
add(SITE/'shared.config.json',json.dumps({'repository':'cssweb-stack/css-shared','ref':'main','localPath':'../css-shared','unit':'wgss'},indent=2)+'\n')
add(SITE/'.github/workflows/deploy.yml',(ROOT.parent/'anth/.github/workflows/deploy.yml').read_text().replace('ANTH','WGSS').replace('/anth/','/wgss/'))
inventory=io.StringIO();w=csv.writer(inventory);w.writerow(['old_url','new_url','status'])
for slug,item in pages.items():
 old=item.findtext('link');dest=links.get(urlsplit(old).path.rstrip('/') or '/','');w.writerow([old,dest,'mapped' if dest else 'review'])
add(SITE/'reference/url-inventory.csv',inventory.getvalue())
report={'source':SOURCE.name,'sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'pages':len(published),'coreFaculty':7,'otherBiographyPages':1,'staff':1,'missingBiographies':missing,'missingCoreContactFields':{p['name']:[k for k in ['email','office'] if not p.get(k)] for p in people if p['showInFacultyDirectory'] and any(not p.get(k) for k in ['email','office'])},'youtubeEmbeds':{'alumni':len(re.findall('<iframe',raw('alumni'))),'home':len(re.findall('<iframe',raw('home')))},'trackingStatus':'YouTube API enabled; live GA4/GTM event collection not verified.','learningOutcomeScope':'Source calls them Undergraduate Student Learning Objectives; BA-only scope not explicitly stated.','sourceImagesNotDownloaded':sorted(images),'unresolvedSourceLinks':sorted(unresolved),'publishedUrls':published}
add(SITE/'reference/migration-report.json',json.dumps(report,ensure_ascii=False,indent=2)+'\n')
add(SITE/'README.md','# WGSS website\n\nShared templates, data and media are in ../css-shared.\nRun npm ci, then npm run dev for http://localhost:8090/.\nRun npm run build and npm run verify before publishing.\nNo remote, commits, push or deployment performed. Review reference/migration-report.json.\n')
print('*** Begin Patch')
for path,value in files.items():
 p=Path(path)
 if p.exists():
  print('*** Update File: '+path+'\n@@')
  for line in p.read_text().splitlines():print('-'+line)
 else:print('*** Add File: '+path)
 for line in value.splitlines():print('+'+line)
print('*** End Patch')
