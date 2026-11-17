"""Import approved PUBA news from supplied XML/ZIP; never fetch remote media.

Usage: PYTHONPATH=/tmp/puba-import-tools python3 scripts/migrations/puba-news.py
Requires Pillow and BeautifulSoup; these are import tools, not site dependencies.
"""
from pathlib import Path
import sys,json,re,html,hashlib,unicodedata,zipfile,io,csv
from urllib.parse import urlsplit,unquote,parse_qs
from datetime import datetime
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup,Comment
from PIL import Image,ImageOps
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[2];PROJECT=ROOT.parent/'puba'
NS={'w':'http://wordpress.org/export/1.2/','c':'http://purl.org/rss/1.0/modules/content/','e':'http://wordpress.org/export/1.2/excerpt/'}
SOURCE=ROOT.parent / 'CSS-Exports' / 'puba/publicadministrationpuba.WordPress.2026-11-17.xml'
BACKUP=ROOT.parent / 'CSS-Exports' / 'puba/CSSPublicAdministrationProgram-111726-backup.zip'
SLUGS={546:'morgen-johansen-program-welcome',548:'aspa-conference-2022',554:'student-samuel-kippen',557:'student-mary-janell-murro',564:'alumni-radiant-cordero',566:'alumni-shannon-mark',579:'paso-officers-2021-2022',605:'faculty-highlights-spring-2022',607:'support-future-puba-students',612:'public-affairs-ranking-88',1317:'student-sharon-baillie',1324:'student-moises-ayala',1327:'alumni-rachele-lamosao',1330:'alumni-kenika-lorenzo-elarco',1339:'paso-year-review-2023',1405:'graduates-marshall-islands-publication',1413:'scholarship-committee-news',1557:'graduates-palau-climate-publication',1607:'alumni-brendan-kinoshita',1614:'student-jordyn-ryan',1636:'student-andrew-phomsouvanh',1641:'paso-maunalua-bay',1714:'helen-yu-naspaa-community',1717:'student-chetsada-changmai',1720:'faculty-policing-publication',2135:'helen-yu-interim-director',2198:'helen-yu-ewha-fellow',2137:'helen-yu-journal-editor',2224:'david-lee-refugee-resettlement',2236:'morgen-johansen-outgoing-director',2239:'faculty-highlights-winter-2024',2267:'paso-policy-climate-change',2280:'aspa-conference-2024',2283:'roy-takumi-education-chair',2343:'director-welcome-fall-2024',2351:'alumni-daniel-koge',2355:'kelly-leroux-voter-participation',2360:'hano-conference-2024',2366:'students-capitol-mock-testimony',2406:'director-welcome-spring-2025',2439:'kamakani-konia-arts-director',2451:'paso-nonprofit-disaster-responses',2458:'public-affairs-ranking-82',2461:'laurel-johnston-state-budget',2511:'director-welcome-fall-2025',2516:'hano-conference-2025',2520:'wendy-hensel-leadership-visit',2619:'paso-inclusive-policy-design',2634:'carmela-resuma-green-fees',2650:'director-welcome-spring-2026',2657:'helen-yu-researcher-ranking',2664:'cheryl-bellisario-housing-policy',2668:'paso-nonprofits-human-rights',2673:'naspaa-simulation-2026',2737:'director-welcome-fall-2026',2748:'student-spotlight-seungwoo-back'}
def wp(i,k):return i.findtext('w:'+k,default='',namespaces=NS)
def meta(i):return {m.findtext('w:meta_key',namespaces=NS):m.findtext('w:meta_value',default='',namespaces=NS) for m in i.findall('w:postmeta',NS)}
def plain(s):return ' '.join(BeautifulSoup(s or '', 'html.parser').get_text(' ',strip=True).split())
def slug(s):return re.sub(r'[^a-z0-9]+','-',unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()).strip('-')
def quoted(s):return json.dumps(s,ensure_ascii=False)
def local(s):return '{{ '+quoted(s)+' | url }}'
items=ET.parse(SOURCE).findall('./channel/item')
posts=[i for i in items if wp(i,'post_type')=='post' and wp(i,'status')=='publish']
assert len(posts)==54
assert len(set(SLUGS.values()))==len(SLUGS)
attachments={wp(i,'post_id'):i for i in items if wp(i,'post_type')=='attachment'}
attachment_paths={}
for aid,a in attachments.items():
 for u in [a.findtext('w:attachment_url',default='',namespaces=NS),a.findtext('guid',default=''),meta(a).get('_wp_attached_file','')]:
  path=unquote(urlsplit(u).path).split('/uploads/')[-1]
  if path:attachment_paths[path]=aid
migration_path=ROOT/'src/data/units/puba/url-migration.json'
migration=json.loads(migration_path.read_text())
path_map={unquote(urlsplit(r['from']).path).rstrip('/') or '/':r['to'] for r in migration['redirects']}
post_urls={wp(i,'post_id'):'/news/'+SLUGS[int(wp(i,'post_id'))]+'.html' for i in posts}
for i in posts:
 path_map['/'+wp(i,'post_name')]=post_urls[wp(i,'post_id')]
 path_map[unquote(urlsplit(i.findtext('link')).path).rstrip('/') or '/']=post_urls[wp(i,'post_id')] if not urlsplit(i.findtext('link')).query else path_map.get('/', '/')
path_map['/news']='/news/';path_map['/about/news.html']='/news/'
report={'posts':[],'media':[],'excludedDrafts':[{'id':wp(i,'post_id'),'title':i.findtext('title')} for i in items if wp(i,'post_type')=='post' and wp(i,'status')!='publish'],'missingMedia':[],'reviewItems':[]}
archive=zipfile.ZipFile(BACKUP);members=set(archive.namelist());image_cache={};source_cache={}
news_dir=PROJECT/'src/news';news_dir.mkdir(exist_ok=True)
# Keep the full source body in the XML; imported pages contain semantic HTML only.
allowed={'p','h2','h3','h4','h5','h6','ul','ol','li','a','strong','em','b','i','u','s','sup','sub','blockquote','cite','br','hr','table','thead','tbody','tfoot','tr','th','td','caption','dl','dt','dd','address','abbr','time','figure','figcaption','img','iframe'}
def image_source(url,aid=None):
 key=unquote(urlsplit(url).path).split('/uploads/')[-1]
 if aid and aid in attachments:
  a=attachments[aid];key=meta(a).get('_wp_attached_file') or unquote(urlsplit(a.findtext('w:attachment_url',default='',namespaces=NS)).path).split('/uploads/')[-1]
 member='files/wp-content/uploads/'+key
 if member not in members:
  # Original export occasionally changes extension after WordPress conversion.
  stem=re.sub(r'-\d+x\d+$','',str(Path(key).with_suffix('')))
  candidates=[m for m in members if m.startswith('files/wp-content/uploads/'+stem+'.')]
  if len(candidates)==1:member=candidates[0]
 if member not in members:raise FileNotFoundError(url)
 return member,archive.read(member)
def import_image(url,postslug,aid=None,alt='',caption='',primary=False):
 if not aid:
  key=unquote(urlsplit(url).path).split('/uploads/')[-1];aid=attachment_paths.get(key)
  if not aid:aid=attachment_paths.get(re.sub(r'-\d+x\d+(?=\.[^.]+$)','',key))
 a=attachments.get(aid);am=meta(a) if a is not None else {}
 alt=plain(alt or am.get('_wp_attachment_image_alt',''))
 caption_html=caption or (a.findtext('e:encoded',default='',namespaces=NS) if a is not None else '')
 caption=plain(caption_html)
 try:member,data=image_source(url,aid)
 except FileNotFoundError:
  report['missingMedia'].append({'post':postslug,'url':url});raise
 digest=hashlib.sha256(data).hexdigest()
 if digest in image_cache:return {**image_cache[digest],'alt':alt,'caption':caption,'sourceAttachment':aid}
 im=Image.open(io.BytesIO(data));im=ImageOps.exif_transpose(im);before=im.size
 original_name=Path(member).stem;name=slug(original_name)
 name=re.sub(r'-(?:scaled|\d+x\d+)$','',name)
 if not name or re.fullmatch(r'(?:img|image|dsc|photo|screenshot)[-\d]*',name):name=postslug
 name='-'.join(name.split('-')[:7])
 if primary:name=postslug
 elif name in ['img-8819a','climate-jpg','sch-jpg']:name={'img-8819a':'wendy-hensel-core-class','climate-jpg':'marshall-islands-climate-publication','sch-jpg':'scholarship-committee'}[name]
 elif name.startswith('ryse-'):name=name.replace('ryse-','ryse-service-event-',1)
 elif name.endswith('-jpg'):name=name[:-4]
 folder=ROOT/'src/media/units/puba/news'/postslug;folder.mkdir(parents=True,exist_ok=True)
 if getattr(im,'is_animated',False):
  dest=folder/(name+Path(member).suffix.lower());dest.write_bytes(data)
  report['reviewItems'].append({'post':postslug,'issue':'Animated image retained in original format','image':str(dest.relative_to(ROOT))})
 else:
  im.thumbnail((1280,1280),Image.Resampling.LANCZOS)
  if im.mode not in ['RGB','RGBA']:im=im.convert('RGBA' if 'transparency' in im.info else 'RGB')
  dest=folder/(name+'.webp');im.save(dest,'WEBP',quality=82,method=6)
  if member.lower().endswith('.webp') and before==im.size and len(data)<dest.stat().st_size:dest.write_bytes(data)
 output={'src':'/'+str(dest.relative_to(ROOT/'src')),'width':im.width,'height':im.height}
 image_cache[digest]=output
 report['media'].append({**output,'source':member,'sourceAttachment':aid,'sourceBytes':len(data),'bytes':dest.stat().st_size,'sourceWidth':before[0],'sourceHeight':before[1],'resized':before!=im.size,'sha256':digest})
 if dest.stat().st_size>300000:report['reviewItems'].append({'post':postslug,'issue':'Optimized image larger than 300 KB','image':output['src']})
 return {**output,'alt':alt,'caption':caption,'sourceAttachment':aid}
def rewrite_link(value):
 u=urlsplit(html.unescape(value));host=u.hostname
 if u.scheme in ['mailto','tel']:return value
 internal=host in ['puba.manoa.hawaii.edu','www.puba.manoa.hawaii.edu','csspubadev.flywheelsites.com'] or not u.scheme and not u.netloc
 if not internal:return value
 query=parse_qs(u.query);pid=(query.get('p') or query.get('page_id') or [None])[0]
 if pid in post_urls:return post_urls[pid]+('#'+u.fragment if u.fragment else '')
 key=unquote(u.path).rstrip('/') or '/'
 dest=path_map.get(key) or path_map.get('/'+key.rsplit('/',1)[-1])
 if not dest and ((PROJECT/'src'/key.lstrip('/')).with_suffix('.html').exists() or (PROJECT/'src'/key.lstrip('/')/'index.html').exists()):dest=key+'/' if not key.endswith('.html') else key
 if dest:return dest+('#'+u.fragment if u.fragment else '')
 return value if host else 'https://puba.manoa.hawaii.edu'+value

def clean_body(raw,postslug,featured):
 soup=BeautifulSoup(raw,'html.parser');anomalies=[];inline=[]
 for c in soup.find_all(string=lambda v:isinstance(v,Comment)):c.extract()
 for tag in soup.find_all(['script','style','svg','noscript']):tag.decompose()
 for tag in soup.find_all('iframe'):
  anomalies.append('Embedded video/frame');tag.attrs={k:v for k,v in tag.attrs.items() if k in ['src','title','allow','allowfullscreen']}
  if 'youtube' in tag.get('src',''):
   src=tag['src'];src+=('&' if '?' in src else '?')+'enablejsapi=1&origin=https://puba.manoa.hawaii.edu';tag['src']=src
  tag['title']=tag.get('title') or 'Embedded media';tag['loading']='lazy'
 for tag in list(soup.find_all('img')):
  orig=tag.get('src','');fig=tag.find_parent('figure');cap=fig.find('figcaption') if fig else None
  image=import_image(orig,postslug,alt=tag.get('alt',''),caption=str(cap) if cap else '')
  if image['src']==featured['src']:
   # Use featured image once; preserve any unique body caption text.
   if fig:
    if cap and plain(str(cap)) and plain(str(cap))!=featured['caption']:
     p=soup.new_tag('p');p.string=plain(str(cap));fig.replace_with(p)
    else:fig.decompose()
   else:tag.decompose()
   continue
  inline.append(image)
  tag.attrs={'src':image['src'],'alt':image['alt'],'width':str(image['width']),'height':str(image['height']),'loading':'lazy','decoding':'async','class':'photo-style'}
  if fig:
   fig.attrs={'class':'news-inline-figure'}
   if not cap and image['caption']:
    cap=soup.new_tag('figcaption');cap.string=image['caption'];fig.append(cap)
  else:
   fig=soup.new_tag('figure');fig['class']='news-inline-figure';tag.wrap(fig)
   if image['caption']:
    cap=soup.new_tag('figcaption');cap.string=image['caption'];fig.append(cap)
 for tag in list(soup.find_all(True)):
  if tag.parent is None:continue
  if tag.name not in allowed:tag.unwrap();continue
  if tag.name in ['img','iframe']:continue
  attrs={}
  for k,v in tag.attrs.items():
   if k=='id' or tag.name in ['th','td'] and k in ['scope','colspan','rowspan'] or tag.name=='ol' and k=='start' or tag.name=='abbr' and k=='title':attrs[k]=v
   if k=='href' and tag.name=='a':attrs[k]=rewrite_link(v)
   if tag.name=='figure' and k=='class':attrs[k]=v
  tag.attrs=attrs
 for p in list(soup.find_all('p')):
  if not p.get_text(strip=True) and not p.find(['img','iframe']):p.decompose()
 for tag in soup.find_all(['video','audio','table']):anomalies.append('Special content: '+tag.name)
 body=str(soup)
 # Local paths go through the common deployment-prefix filter.
 body=re.sub(r'(href|src)="(/[^\"]*)"',lambda m:m[1]+'="'+local(html.unescape(m[2]))+'"',body)
 body=body.replace('{{{{','{{')
 return body,inline,anomalies

import importlib.util
spec=importlib.util.spec_from_file_location('formatting',ROOT/'scripts/code-cleanup.py');formatting=importlib.util.module_from_spec(spec);spec.loader.exec_module(formatting)
for i in sorted(posts,key=lambda i:wp(i,'post_date')):
 pid=wp(i,'post_id');ps=SLUGS[int(pid)];pm=meta(i);aid=pm['_thumbnail_id'];a=attachments[aid]
 image=import_image(a.findtext('w:attachment_url',default='',namespaces=NS),ps,aid,primary=True)
 raw=i.findtext('c:encoded',default='',namespaces=NS)
 body,extras,anomalies=clean_body(raw,ps,image)
 original_text=plain(re.sub(r'<svg\b.*?</svg>','',raw,flags=re.S))
 body_text=plain(body)
 # Caption text can move to featured figure; otherwise preserve substantive source words.
 title=plain(i.findtext('title',default=''));date=wp(i,'post_date')[:10]
 first=BeautifulSoup(body,'html.parser').find('p');description=plain(str(first)) if first else body_text
 if len(description)>175:description=description[:172].rsplit(' ',1)[0]+'…'
 fields={'layout':'layouts/news/article.njk','title':title,'description':description,'permalink':post_urls[pid],'tags':['unit-news'],'published':date,'date':wp(i,'post_date').replace(' ','T')+'-10:00','wordpressId':int(pid),'newsImage':image}
 front='---\n'+'\n'.join(k+': '+quoted(v) for k,v in fields.items())+'\n---\n'
 page=news_dir/(ps+'.html');assert not page.exists() or 'wordpressId: '+pid in page.read_text(),str(page)
 page.write_text(formatting.format_template_source(front+body+'\n'))
 missing_alt=[x['src'] for x in [image]+extras if not x['alt']]
 entry={'id':pid,'title':title,'published':date,'url':post_urls[pid],'oldUrl':i.findtext('link'),'oldSlug':'/'+wp(i,'post_name')+'/','featuredImage':image,'additionalImages':extras,'anomalies':anomalies,'missingAlt':missing_alt,'missingCaption':not bool(image['caption']),'sourceText':original_text,'importedText':body_text}
 report['posts'].append(entry)
 if extras:report['reviewItems'].append({'post':ps,'url':entry['url'],'issue':f'{len(extras)} additional inline images; review original-position/gallery presentation'})
 for anomaly in anomalies:report['reviewItems'].append({'post':ps,'url':entry['url'],'issue':anomaly})
 if missing_alt:report['reviewItems'].append({'post':ps,'url':entry['url'],'issue':'Missing supplied alt text; requires image-purpose review','images':missing_alt})
 if not image['caption']:report['reviewItems'].append({'post':ps,'url':entry['url'],'issue':'No featured caption supplied; none invented'})
 if any('wp-content' in v for v in re.findall(r'href="([^\"]+)"',body)):report['reviewItems'].append({'post':ps,'issue':'Remaining WordPress asset link'})
# Preserve category-based legacy aliases found in article links as direct redirects.
for item in posts:
 for value in re.findall(r'href=[\"\']([^\"\']+)',item.findtext('c:encoded',default='',namespaces=NS)):
  parsed=urlsplit(html.unescape(value));old=unquote(parsed.path)
  target=rewrite_link(value)
  if parsed.hostname=='puba.manoa.hawaii.edu' and target.startswith('/news/') and not old.startswith('/news/') and not any(r['from']==old for r in migration['redirects']):migration['redirects'].append({'from':old,'to':target,'label':'PUBA news archive'})
# Redirect every old pretty slug, including the two XML links serialized as ?p=ID.
for post in report['posts']:
 source=post['oldSlug']
 if not any(r['from']==source for r in migration['redirects']):migration['redirects'].append({'from':source,'to':post['url'],'label':post['title']})
 for r in migration['redirects']:
  if r['to']=='/about/news.html':r['to']='/news/'
if not any(r['from']=='/about/news.html' for r in migration['redirects']):migration['redirects'].append({'from':'/about/news.html','to':'/news/','label':'PUBA News'})
migration['redirects']=[r for r in migration['redirects'] if r['from']!='/news/']
restored={p['oldSlug'] for p in report['posts']} | {'/news/'}
for category in ['unresolved','retired']:
 migration[category]=[r for r in migration.get(category,[]) if r['from'] not in restored]
migration['queryRedirects']={post['id']:post['url'] for post in report['posts']}
migration_path.write_text(json.dumps(migration,ensure_ascii=False,indent=2)+'\n')
report['summary']={'published':len(posts),'draftsExcluded':len(report['excludedDrafts']),'distinctImages':len(report['media']),'postsWithAdditionalImages':sum(bool(p['additionalImages']) for p in report['posts']),'postsWithEmbeds':sum(bool(p['anomalies']) for p in report['posts']),'missingFeaturedCaptions':sum(p['missingCaption'] for p in report['posts']),'missingAltUsages':sum(len(p['missingAlt']) for p in report['posts']),'sourceImageBytes':sum(m['sourceBytes'] for m in report['media']),'optimizedImageBytes':sum(m['bytes'] for m in report['media'])}
# The inventory is migration data; editorial excerpts are deliberately not stored.
ref=PROJECT/'reference/news-import.json';ref.parent.mkdir(parents=True,exist_ok=True);ref.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
with (PROJECT/'reference/news-url-inventory.csv').open('w',newline='') as f:
 writer=csv.writer(f);writer.writerow(['wordpress_id','old_url','old_pretty_path','new_url']);writer.writerows([p['id'],p['oldUrl'],p['oldSlug'],p['url']] for p in report['posts'])
print(json.dumps(report['summary'],indent=2))
