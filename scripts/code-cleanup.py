"""Prepare or apply conservative flush-left HTML/Nunjucks source formatting.

Never formats generated output. Default is report-only. Rendered preservation
must still be checked after applying/building, as required by docs/rules/code-cleanup.md.
"""
from pathlib import Path
from html.parser import HTMLParser
import argparse,json,re
ROOT=Path(__file__).resolve().parents[1]
class Events(HTMLParser):
    def __init__(self):super().__init__(convert_charrefs=True);self.events=[]
    def handle_starttag(self,t,a):self.events.append(['open',t,a])
    def handle_endtag(self,t):self.events.append(['close',t])
    def handle_startendtag(self,t,a):self.events.append(['void',t,a])
    def handle_data(self,d):
        text=re.sub(r'\s+',' ',d).strip()
        if text:self.events.append(['text',text])
def events(s):
    p=Events();p.feed(s);return p.events
def _format_source_base(old):
    protected={}
    def protect(m):
        key=f'CODECLEANUPPROTECTED{len(protected)}TOKEN';protected[key]=m[0];return key
    s=re.sub(r'(?s)\A---\n.*?\n---|<(pre|code|textarea|script|style)\b[^>]*>.*?</\1\s*>|{#.*?#}',protect,old)
    # Keep raw tags/attributes and template expressions intact while folding only
    # whitespace in text within simple paragraphs/headings/list items.
    def compact(m):
        body=m[2]
        if re.search(r'</?(?:ul|ol|div|section|table|blockquote|figure)\b',body,re.I):return m[0]
        parts=re.split(r'({{.*?}}|{%.*?%}|<[^>]+>)',body,flags=re.S)
        for i,part in enumerate(parts):
            if not part.startswith(('<','{{','{%')):parts[i]=re.sub(r'\s+',' ',part)
        return m[1]+''.join(parts).strip()+m[3]
    s=re.sub(r'(?s)(<(?:p|li|h[1-6])\b[^>]*>)(.*?)(</(?:p|li|h[1-6])\s*>)',compact,s)
    s=re.sub(r'(?i)(</?(?:div|section|article|aside|main|nav|header|footer|ul|ol|table|thead|tbody|tfoot|tr|figure|blockquote)\b[^>]*>)',r'\n\1\n',s)
    s=re.sub(r'(?i)(<(?:li|p|h[1-6]|hr|img)\b)',r'\n\1',s)
    s=re.sub(r'(?i)(</(?:li|p|h[1-6])\s*>)',r'\1\n',s)
    s=re.sub(r'({%.*?%})',r'\n\1\n',s,flags=re.S)
    s='\n'.join(line.strip() for line in s.splitlines() if line.strip())+'\n'
    for key,value in protected.items():s=s.replace(key,value)
    assert events(old)==events(s),'Formatting changed source structure, attributes or non-whitespace text'
    return s
def format_source(old):
 inline={}
 def hold(match):
  def save(t):
   key=f'INLINEINSTRUCTIONTOKEN{len(inline)}END';inline[key]=t[0];return key
  return re.sub(r'{%.*?%}',save,match[0],flags=re.S)
 held=re.sub(r'<(p|h[1-6]|li)\b[^>]*>(?:(?!<(?:ul|ol)\b).)*?</\1>',hold,old,flags=re.S)
 s=_format_source_base(held)
 for key,value in inline.items():s=s.replace(key,value)
 # Whitespace cleanup only in text, never attributes or template expressions.
 parts=re.split(r'(<[^>]+>|{{.*?}}|{%.*?%})',s,flags=re.S)
 for i,part in enumerate(parts):
  if not part.startswith(('<','{{','{%')):
   part=part.replace('\u00a0',' ')
   part=re.sub(r'&nbsp;|&#160;|&#x[aA]0;',' ',part)
   part=re.sub(r'[ \t]{2,}',' ',part)
   part=re.sub(r'[ \t]+([.,;:!?])',r'\1',part)
   parts[i]=part
 s=''.join(parts)
 # Spaces just inside block closing tags are not meaningful word separators.
 s=re.sub(r'[ \t]+(</(?:p|li|h[1-6])>)',r'\1',s)
 s='\n'.join(l.lstrip().rstrip() for l in s.splitlines() if l.strip())+'\n'
 return s
if __name__=='__main__':
    cli=argparse.ArgumentParser();cli.add_argument('unit');cli.add_argument('--apply',action='store_true');cli.add_argument('--output',type=Path);args=cli.parse_args()
    if not re.fullmatch(r'[a-z0-9-]+',args.unit):cli.error('Invalid unit')
    source=ROOT.parent/args.unit/'src'
    if not source.is_dir():cli.error('Unit source not found')
    paths=sorted([*source.rglob('*.html'),*source.rglob('*.njk')]);unit_includes=ROOT/'src/includes/units'/args.unit
    if unit_includes.exists():paths+=sorted(unit_includes.rglob('*.njk'))
    changed=[]
    for p in paths:
        old=p.read_text();new=format_source(old)
        if old!=new:
            changed.append(str(p.relative_to(ROOT.parent)))
            if args.apply:p.write_text(new)
    result={'unit':args.unit,'mode':'applied' if args.apply else 'report-only','filesReviewed':len(paths),'filesChanged':changed,'sourceEventPreservation':True}
    if args.output:args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
