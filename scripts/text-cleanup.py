"""Prepare a standard text-cleanup patch and measured findings for one unit.

Review proposed edits against docs/text-cleanup.md before applying. Original exports,
URLs/attributes, template expressions and preformatted text are not modified.
"""
from pathlib import Path
from html.parser import HTMLParser
import re,json,collections,argparse,tempfile
from hawaiian_diacritics import review_unit
from heading_formatting import review_headings

ROOT=Path(__file__).resolve().parents[1]
cli=argparse.ArgumentParser(description='Prepare reviewable prose-cleanup patches; never edit source files directly.')
cli.add_argument('unit', help='Unit abbreviation, for example wgss')
args=cli.parse_args()
if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', args.unit):cli.error('Invalid unit abbreviation')
site_source=ROOT.parent/args.unit/'src'
unit_data=ROOT/'src/data/units'/args.unit
if not site_source.is_dir() or not unit_data.is_dir():cli.error('Unit source/data directory not found')
output_dir=Path(tempfile.mkdtemp(prefix=args.unit+'-text-cleanup-'))
counts=collections.Counter();changes={};report=[]
def normalize(s):
 def sub(pattern,repl,key,flags=0):
  nonlocal s
  def replace(m):
   value=m.expand(repl)
   if value!=m[0]:counts[key]+=1
   return value
  s=re.sub(pattern,replace,s,flags=flags)
 sub(r'\u00a0|&nbsp;|&#0*160;|&#x0*a0;',' ','nonbreaking_spaces',re.I)
 sub(r'[\u200b\ufeff\u00ad]','','invisible_characters')
 sub(r"Hawai[`‘’']i",'Hawaiʻi','okina')
 sub(r'University of Hawaii at Manoa','University of Hawaiʻi at Mānoa','university_name')
 sub(r'(?<=Hawaiʻi at )Manoa\b','Mānoa','kahako')
 sub(r'[ \t]*—[ \t]*',' — ','em_dash_spacing')
 # Count only dash changes, not already correctly spaced dashes.
 sub(r'(?<=\S) {2,}(?=\S)',' ','double_spaces')
 sub(r'(?<=\w)[ \t]+([,.;:!?])',r'\1','space_before_punctuation')
 return s
class Scan(HTMLParser):
 def __init__(self,s):
  super().__init__(convert_charrefs=False);self.source=s;self.starts=[0]+[m.end() for m in re.finditer('\n',s)];self.edits=[];self.ignore=[];self.attrs=[]
 def position(self):
  line,col=self.getpos();return self.starts[line-1]+col
 def handle_starttag(self,t,a):
  self.attrs.append((t,a))
  if t in ['pre','code','kbd','samp','script','style','textarea']:self.ignore.append(t)
 def handle_startendtag(self,t,a):self.attrs.append((t,a))
 def handle_endtag(self,t):
  if self.ignore and self.ignore[-1]==t:self.ignore.pop()
 def handle_data(self,s):
  if self.ignore:return
  # Template code is never prose.
  out=''.join(part if part.startswith(('{%','{{')) else normalize(part) for part in re.split(r'({%[\s\S]*?%}|{{[\s\S]*?}})',s))
  if out!=s:self.edits.append((self.position(),len(s),out))
 def handle_entityref(self,name):
  if not self.ignore and name.lower()=='nbsp':self.edits.append((self.position(),len(name)+2,' '));counts['nonbreaking_spaces']+=1
 def handle_charref(self,name):
  try:val=int(name[1:],16) if name.lower().startswith('x') else int(name)
  except ValueError:return
  if not self.ignore and val==160:self.edits.append((self.position(),len(name)+3,' '));counts['nonbreaking_spaces']+=1
for p in site_source.rglob('*.html'):
 old=p.read_text();parser=Scan(old);parser.feed(old);new=old
 for start,length,value in reversed(parser.edits):new=new[:start]+value+new[start+length:]
 new,n=re.subn(r'<p>\s*(?:(?:<(?:strong|em|b|i)>\s*)|(?:</(?:strong|em|b|i)>\s*)|<br\s*/?>\s*)*</p>','',new)
 counts['empty_paragraphs']+=n
 if new!=old:
  snapshot=counts.copy();after=Scan(new);after.feed(new);counts.clear();counts.update(snapshot)
  assert parser.attrs==after.attrs or [x for x in parser.attrs if x[0]!='p']==[x for x in after.attrs if x[0]!='p'],('Attribute changed',p)
  changes[p]=new
keys={'name','title','label','description','research','studyArea','office','alt','roles','address'}
for p in unit_data.glob('*.json'):
 old=p.read_text();d=json.loads(old)
 def walk(x,parent=''):
  if isinstance(x,dict):return {k:walk(v,k) for k,v in x.items()}
  if isinstance(x,list):return [walk(v,parent) for v in x]
  if isinstance(x,str) and parent in keys:return normalize(x)
  return x
 new=walk(d)
 if new!=d:changes[p]=json.dumps(new,ensure_ascii=False,indent=2)+'\n'
for index,(p,s) in enumerate(changes.items()):
 old=p.read_text();patch='*** Begin Patch\n*** Update File: '+str(p.resolve())+'\n@@\n'+'\n'.join('-'+x for x in old.splitlines())+'\n'+'\n'.join('+'+x for x in s.splitlines())+'\n*** End Patch\n';(output_dir/('change-'+str(index)+'.patch')).write_text(patch)
 report.append(str(p))
diacritics = review_unit(site_source, unit_data)
headings = review_headings(site_source, unit_data)
(output_dir/'findings.json').write_text(json.dumps({'files':report,'counts':dict(counts),'diacritic_review':diacritics,'heading_formatting':headings},ensure_ascii=False,indent=2))
print('Prepared',len(changes),'file patches');print(dict(counts))
print('Report-only Hawaiian diacritic candidates:', len(diacritics))
print('Headings with embedded bold/italic tags:', len(headings))

print('Reviewable patches/findings:', output_dir)
