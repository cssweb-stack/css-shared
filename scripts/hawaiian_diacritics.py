"""Report-only diacritic candidates; a finite watchlist, not a spellchecker."""
from html.parser import HTMLParser
from pathlib import Path
import json, re

SPELLINGS = {'hawaii': 'Hawaiʻi', 'manoa': 'Mānoa', 'oahu': 'Oʻahu',
             'kauai': 'Kauaʻi', 'molokai': 'Molokaʻi',
             'lanai': 'Lānaʻi (island; verify context)', 'aina': 'ʻāina',
             'ohana': 'ʻohana', 'kupuna': 'kūpuna (plural; singular kupuna can be correct)'}
PATTERN = re.compile(r'\b(?:' + '|'.join(SPELLINGS) + r')\b|[‘’`\'](?:āina|Āina)\b', re.I)
TEXT_KEYS = {'name','title','label','description','research','studyArea','office',
             'alt','roles','address','support','text','content'}

def review_unit(site_source, unit_data):
    findings = []
    def scan(value, file, location, line):
        value = re.sub(r'{{[\s\S]*?}}|{%[\s\S]*?%}|https?://\S+|mailto:\S+', ' ', value)
        value = re.sub(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', ' ', value, flags=re.I)
        for match in PATTERN.finditer(value):
            original = match[0]
            findings.append({'file': str(file), 'location': location, 'line': line,
                'original': original, 'suggested': SPELLINGS.get(original.lower(), 'ʻāina'),
                'kind': 'wrong_character' if original[0] in '‘’`\'' else 'possible_missing_diacritic',
                'context': re.sub(r'\s+', ' ', value[max(0,match.start()-45):match.end()+80]).strip()})
    class Scan(HTMLParser):
        def __init__(self, file, location='text'):
            super().__init__(convert_charrefs=True)
            self.file=file;self.location=location;self.ignore=[]
        def handle_starttag(self, tag, attrs):
            if tag in ['script','style','pre','code','textarea','kbd','samp']:self.ignore.append(tag)
            if not self.ignore:
                for key,value in attrs:
                    if key in ['alt','title','aria-label'] and value:
                        scan(value,self.file,self.location+' attribute:'+key,self.getpos()[0])
        def handle_startendtag(self, tag, attrs):self.handle_starttag(tag,attrs)
        def handle_endtag(self, tag):
            if self.ignore and self.ignore[-1]==tag:self.ignore.pop()
        def handle_data(self, value):
            if not self.ignore:scan(value,self.file,self.location,self.getpos()[0])
    for file in sorted(Path(site_source).rglob('*.html')):Scan(file).feed(file.read_text())
    for file in sorted(Path(unit_data).glob('*.json')):
        def walk(value,key='',location='$'):
            if isinstance(value,dict):
                for k,v in value.items():walk(v,k,location+'.'+k)
            elif isinstance(value,list):
                for i,v in enumerate(value):walk(v,key,location+'['+str(i)+']')
            elif isinstance(value,str) and key in TEXT_KEYS and not re.match(r'^(?:https?://|/|mailto:|tel:)',value):
                Scan(file,location).feed(value)
        walk(json.loads(file.read_text()))
    return findings
