"""Az 1e három kézzel migrált oldalának meglévő ábráit frissíti.

Csak a megnevezett ábrakártyát cseréli; az oldal többi részét megőrzi.
A régi leíráshorgonyok az állítható változatban is megmaradnak.
"""
from html.parser import HTMLParser
from pathlib import Path
import re
from tananyag_common import mat, svg_nyildiagram_interaktiv, svg_eltolas_interaktiv, svg_felegyenes_interaktiv

ROOT = Path(__file__).resolve().parents[2]
CÉLOK = [
    ('1e/01-logika-halmazok-fuggvenyek/tananyag-fuggveny-fogalma.html', 'abra-fuggveny-leiras', svg_nyildiagram_interaktiv),
    ('1e/05-geometria/tananyag-transzformaciok.html', 'abra-transzformaciok-1', svg_eltolas_interaktiv),
    ('1e/07-linearis-egyenletek-es-rendszerek/tananyag-egyenlotlensegek.html', 'abra-egyenlotlensegek-1', svg_felegyenes_interaktiv),
]
ÜRES = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}

class Kártya(HTMLParser):
    """Forrásbeli határokat gyűjt, a HTML újraszerializálása nélkül."""
    def __init__(self, text, anchor):
        super().__init__(convert_charrefs=False)
        self.text, self.anchor, self.stack, self.target = text, anchor, [], None
        self.lines = [0]
        self.lines.extend(m.end() for m in re.finditer('\n',text))
    def pos(self):
        line,col=self.getpos()
        return self.lines[line-1]+col
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        node={'tag':tag,'start':self.pos(),'end':None,'classes':attrs.get('class','').split()}
        if attrs.get('id')==self.anchor:
            cards=[p for p in self.stack if 'svgcard' in p['classes']]
            if not cards: raise ValueError('A leíráshoz nem tartozik ábrakártya: '+self.anchor)
            self.target=cards[-1]
            if self.anchor=='abra-fuggveny-leiras' and 'interaktiv' not in self.target['classes']:
                self.target=next(p for p in reversed(self.stack) if 'svgrow' in p['classes'])
        if tag not in ÜRES:self.stack.append(node)
    def handle_startendtag(self,tag,attrs):
        # A célok hagyományos, nem önlezáró leíráselemek.
        pass
    def handle_endtag(self,tag):
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i]['tag']==tag:
                for node in self.stack[i:]:node['end']=self.text.find('>',self.pos())+1
                del self.stack[i:]
                return

def frissít(path,anchor,helper):
    text=path.read_bytes().decode('utf-8')
    parser=Kártya(text,anchor);parser.feed(text)
    card=parser.target
    if not card or card['end'] is None:raise ValueError('Nem található teljes ábrakártya: '+anchor)
    start,end=card['start'],card['end']
    # A segéd saját szkriptjét ismételt futtatáskor is csak egyszer hagyjuk meg.
    oldscript=re.match(r'(?:\s*<script src="../../assets/js/interaktiv\.js"(?:\s+defer)?\s*></script>)+',text[end:])
    if oldscript:end+=oldscript.end()
    replacement=mat(helper())
    if '\r\n' in text:replacement=replacement.replace('\n','\r\n')
    updated=text[:start]+replacement+text[end:]
    old_ids=set(re.findall(r'\bid="([^"]+)"',text[start:end]))
    protected={s for s in old_ids if s.startswith('abra-')}
    if not protected.issubset(set(re.findall(r'\bid="([^"]+)"',replacement))):
        raise ValueError('Elveszett leíráshorgony: '+str(protected))
    if updated!=text:
        path.write_bytes(updated.encode('utf-8'))
        print('Frissítve: '+str(path.relative_to(ROOT)))
    else:print('Változatlan: '+str(path.relative_to(ROOT)))

if __name__=='__main__':
    for rel,anchor,helper in CÉLOK:frissít(ROOT/rel,anchor,helper)
