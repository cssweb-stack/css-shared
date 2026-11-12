"""Report heading emphasis so shared CSS, not embedded tags, controls headings."""
from html.parser import HTMLParser
from pathlib import Path
import json, re

def review_headings(site_source, unit_data):
    findings=[]
    class Scan(HTMLParser):
        def __init__(self,file,location='HTML'):
            super().__init__();self.file=file;self.location=location;self.heading=None;self.ignore=[]
        def handle_starttag(self,tag,attrs):
            if tag in ['pre','code','script','style','textarea']:self.ignore.append(tag)
            if self.ignore:return
            if re.fullmatch(r'h[1-6]',tag):self.heading=tag
            elif self.heading and tag in ['strong','b','em','i']:
                findings.append({'file':str(self.file),'location':self.location,
                    'line':self.getpos()[0],'heading':self.heading,'tag':tag})
        def handle_endtag(self,tag):
            if self.ignore and self.ignore[-1]==tag:self.ignore.pop()
            if tag==self.heading:self.heading=None
    for file in sorted(Path(site_source).rglob('*.html')):Scan(file).feed(file.read_text())
    for file in sorted(Path(unit_data).glob('*.json')):
        def walk(value,location='$'):
            if isinstance(value,dict):
                for k,v in value.items():walk(v,location+'.'+k)
            elif isinstance(value,list):
                for i,v in enumerate(value):walk(v,location+'['+str(i)+']')
            elif isinstance(value,str) and re.search(r'<h[1-6]\b',value,re.I):Scan(file,location).feed(value)
        walk(json.loads(file.read_text()))
    return findings
