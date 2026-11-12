"""Text-only WordPress HTML sanitizer; preserve structure and explicit video embeds."""
import html, re
from html.parser import HTMLParser
from urllib.parse import urlsplit

class WordPressHTML(HTMLParser):
    allowed=set('p h1 h2 h3 h4 h5 h6 ul ol li a strong b em i sup sub blockquote cite br hr dl dt dd address abbr time table caption thead tbody tfoot tr td th colgroup col details summary'.split())
    void={'br','hr','col'}
    def __init__(self,link,image_inventory=None,videos=False):
        super().__init__(convert_charrefs=True)
        self.link=link;self.images=image_inventory if image_inventory is not None else set();self.videos=videos;self.out=[];self.skip=[]
    def handle_starttag(self,t,attrs):
        if t in ['script','style','noscript','svg']:self.skip.append(t);return
        if self.skip:return
        a=dict(attrs)
        if t=='img':self.images.add(a.get('src',''));return
        if t=='iframe':
            src=html.unescape(a.get('src',''))
            if self.videos and urlsplit(src).hostname in ['www.youtube.com','youtube.com','www.youtube-nocookie.com']:
                # Arguments are JSON strings, preserving quotes safely in Nunjucks.
                import json
                self.out.append('{% from "layouts/content/youtube.njk" import youtubeEmbed %}\n{{ youtubeEmbed('+json.dumps(src)+', '+json.dumps(a.get('title') or 'YouTube video',ensure_ascii=False)+', site.url) }}\n')
            elif src and 'google.com/maps' not in src:self.out.append('<p><a href="'+self.link(src)+'">'+html.escape(a.get('title') or 'View embedded resource')+'</a></p>')
            return
        if t=='button':t='h3'
        if t not in self.allowed:return
        at=''
        for key,value in attrs:
            if key=='href' and t=='a':at+=' href="'+self.link(value or '')+'"'
            elif key in ['id','colspan','rowspan','scope','start','span','headers']:at+=' '+key+'="'+html.escape(value or '',quote=True)+'"'
        if t=='table':at+=' class="content-table"'
        self.out.append('<'+t+at+'>')
    def handle_startendtag(self,t,a):self.handle_starttag(t,a)
    def handle_endtag(self,t):
        if self.skip:
            if t==self.skip[-1]:self.skip.pop()
            return
        if t=='button':t='h3'
        if t in self.allowed and t not in self.void:self.out.append('</'+t+'>\n')
    def handle_data(self,s):
        if not self.skip:self.out.append(html.escape(s,quote=False))

def clean_html(value,link,image_inventory=None,videos=False):
    p=WordPressHTML(link,image_inventory,videos);p.feed(value)
    s=''.join(p.out)
    for _ in range(2):s=re.sub(r'<(a|h[1-6])\b[^>]*>\s*</\1>','',s)
    return re.sub(r'\n\s*\n','\n',s).strip()

def no_h1(value):return re.sub(r'<h1\b[^>]*>.*?</h1>','',value,flags=re.S|re.I).strip()
def text(value):return re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',value))).strip()
