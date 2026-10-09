"""Közös betöltési jelzések: kritikus betűkészletek és halasztható szkriptek.

A tanulói tartalmat nem alakítja át. A saját jelölt blokkot generálja újra,
a felismert helyi kezelőszkriptekhez defer attribútumot ad. A KaTeX és az
inline képletrajzolás sorrendjét megtartja. A set_hatter.py is meghívja.
Alapértelmezésben csak jelent; írás: python _tools/betoltes.py --apply.
"""
import argparse
import posixpath
import re
from html.parser import HTMLParser
from pathlib import Path

GYOKER = Path(__file__).resolve().parent.parent
KIHAGY = {'_tools', '_docs', '_sablonok', '_layout', 'assets', 'node_modules', '.git', '.github', '.claude'}
# A magyar fejléc és a bevezető szöveg mindkét karakterkészletet használja.
# A többi vastagságot továbbra is a stíluslap tölti be igény szerint.
FONTS = [
    'fonts/inter-latin-400-normal.woff2', 'fonts/inter-latin-ext-400-normal.woff2',
    'fonts/inter-latin-700-normal.woff2', 'fonts/inter-latin-ext-700-normal.woff2',
    'fonts/space-grotesk-latin-700-normal.woff2', 'fonts/space-grotesk-latin-ext-700-normal.woff2',
]
MATEK_FONTS = ['katex/fonts/KaTeX_Main-Regular.woff2', 'katex/fonts/KaTeX_Math-Italic.woff2']
HALASZTHATO = {'ui.js', 'quiz.js', 'search.js', 'naplo-oldal.js', 'interaktiv.js'}
KEZDET = '<!-- Szvetkó: betöltési jelzések -->'
VEGE = '<!-- /Szvetkó: betöltési jelzések -->'
BLOKK = re.compile(re.escape(KEZDET) + r'\r?\n.*?' + re.escape(VEGE) + r'\r?\n', re.S)


def web_lap(rel):
    return rel.suffix == '.html' and not KIHAGY.intersection(rel.parts)


class Fejlec(HTMLParser):
    def __init__(self, s):
        super().__init__(convert_charrefs=False)
        self.s = s
        self.sorok = [0]
        for m in re.finditer('\n', s):
            self.sorok.append(m.end())
        self.root = None
        self.styles = []
        self.scripts = []
        self.preloads = set()
        self.matek = False
        self.head = False
        self.head_vege = None

    def hely(self):
        sor, oszlop = self.getpos()
        return self.sorok[sor - 1] + oszlop

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html':
            self.root = a.get('data-root')
        if tag == 'head':
            self.head = True
        if tag == 'link' and self.head:
            if a.get('rel') == 'stylesheet':
                self.styles.append(self.hely())
                if a.get('href', '').endswith('/katex/katex.min.css'):
                    self.matek = True
            if a.get('rel') == 'preload':
                self.preloads.add(a.get('href'))
        if tag == 'script' and a.get('src'):
            self.scripts.append((self.hely(), self.get_starttag_text(), a))

    def handle_endtag(self, tag):
        if tag == 'head':
            self.head_vege = self.hely()
            self.head = False


def kimenet(s, rel):
    """Csak a saját betöltési blokk és az ismert script-starttagek változhatnak."""
    eredeti = s
    s = BLOKK.sub('', s)
    h = Fejlec(s)
    h.feed(s)
    if not h.root or not h.styles or h.head_vege is None:
        return eredeti
    # Csak a jelenlegi gyökérmélységek; hibás attribútumot nem találgatunk.
    if h.root not in {'.', '..', '../..'}:
        raise ValueError(f'Ismeretlen data-root: {rel}')
    prefix = '' if h.root == '.' else h.root + '/'
    # A rövid listázó és keresőoldalon a korai fontkérés lassította az első megjelenést.
    # Itt a meglévő font-display:swap dolgozik; a tanulási lapokon és a főoldalon előtöltünk.
    fonts = list(FONTS) if h.matek or rel.as_posix() == 'index.html' else []
    fonts += MATEK_FONTS if h.matek else []
    fonts = [prefix + 'assets/' + f for f in fonts if prefix + 'assets/' + f not in h.preloads]
    javitasok = []
    for hely, tag, a in h.scripts:
        src = a['src']
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', src):
            continue
        cel = posixpath.normpath(posixpath.join(rel.parent.as_posix(), src))
        nev = posixpath.basename(cel)
        if cel != 'assets/js/' + nev or nev not in HALASZTHATO:
            continue
        if 'defer' in a or 'async' in a or a.get('type') == 'module':
            continue
        uj = tag[:-1] + ' defer>'
        javitasok.append((hely, hely + len(tag), uj))
    if fonts:
        nl = '\r\n' if '\r\n' in s else '\n'
        blokk = nl.join([KEZDET] + [f'<link rel="preload" href="{f}" as="font" type="font/woff2" crossorigin>' for f in fonts] + [VEGE, ''])
        # A stíluslapok kérése induljon előbb; a fontok ne fogják vissza az első rajzolást.
        javitasok.append((h.head_vege, h.head_vege, blokk))
    for a, b, uj in sorted(javitasok, reverse=True):
        s = s[:a] + uj + s[b:]
    return s


def feldolgoz(f, dry=False):
    adat = f.read_bytes()
    s = adat.decode('utf-8')
    uj = kimenet(s, f.relative_to(GYOKER))
    if uj == s:
        return False
    if not dry:
        f.write_bytes(uj.encode('utf-8'))
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    lapok = [f for f in sorted(GYOKER.rglob('*.html')) if web_lap(f.relative_to(GYOKER))]
    n = sum(feldolgoz(f, dry=not args.apply) for f in lapok)
    print(f'Betöltési jelzések: {n} / {len(lapok)} oldal' + ('' if args.apply else ' (csak jelentés)'))


if __name__ == '__main__':
    main()
