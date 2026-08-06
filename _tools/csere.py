# -*- coding: utf-8 -*-
"""Marvel → Szvetkó-kampusz csere. Használat:
     python csere.py <gyoker> --dry     (csak riport)
     python csere.py <gyoker> --apply   (ír)
A base64 data-URI blokkokat kimaszkolja, hogy a képadatba ne nyúljon bele.
"""
import os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from szotar import SZOTAR, NEVELO_AZ, NEVELO_A

_NEV = []
for _n in NEVELO_AZ:
    _NEV.append((re.compile(r'(?<![\wáéíóöőúüű])a(\s+)(?=' + _n + r')'), r'az\1'))
    _NEV.append((re.compile(r'(?<![\wáéíóöőúüű])A(\s+)(?=' + _n + r')'), r'Az\1'))
for _n in NEVELO_A:
    _NEV.append((re.compile(r'(?<![\wáéíóöőúüű])az(\s+)(?=' + _n + r'\b)'), r'a\1'))
    _NEV.append((re.compile(r'(?<![\wáéíóöőúüű])Az(\s+)(?=' + _n + r'\b)'), r'A\1'))

KITERJESZTES = {'.html', '.css', '.js', '.py', '.json', '.md', '.mjs'}
KIHAGY_DIR = {'.git', 'katex', 'fonts', 'img', '__pycache__', 'node_modules', '_ellenorzes'}
B64 = re.compile(r'data:[a-zA-Z0-9/+.-]+;base64,[A-Za-z0-9+/=\s]+')

SZABALYOK = [(re.compile(p), c) for p, c in SZOTAR]


def maszkol(t):
    tarolo = []
    def _le(m):
        tarolo.append(m.group(0))
        return f'\x00B64#{len(tarolo)-1}\x00'
    return B64.sub(_le, t), tarolo


def visszamaszkol(t, tarolo):
    for i, v in enumerate(tarolo):
        t = t.replace(f'\x00B64#{i}\x00', v)
    return t


def fajlok(gyoker):
    for r, ds, fs in os.walk(gyoker):
        ds[:] = [d for d in ds if d not in KIHAGY_DIR]
        for f in fs:
            if os.path.splitext(f)[1].lower() in KITERJESZTES:
                yield os.path.join(r, f)


def main():
    gyoker = sys.argv[1]
    ir = '--apply' in sys.argv
    statisztika = collections.Counter()
    valtozott = []
    for p in fajlok(gyoker):
        try:
            eredeti = open(p, encoding='utf-8', newline='').read()
        except UnicodeDecodeError:
            continue
        t, tarolo = maszkol(eredeti)
        for rx, csere in SZABALYOK:
            t, n = rx.subn(csere, t)
            if n:
                statisztika[rx.pattern] += n
        for rx, csere in _NEV:
            t, n = rx.subn(csere, t)
            if n:
                statisztika['[névelő]'] += n
        t = visszamaszkol(t, tarolo)
        if t != eredeti:
            valtozott.append(p)
            if ir:
                with open(p, 'w', encoding='utf-8', newline='') as fh:
                    fh.write(t)
    print(f"{'ÍRVA' if ir else 'SZÁRAZ FUTÁS'} — {len(valtozott)} fájl, "
          f"{sum(statisztika.values())} csere")
    for pat, n in statisztika.most_common():
        print(f"{n:6d}  {pat}")
    print("\n--- nem talált szabályok ---")
    for rx, _ in SZABALYOK:
        if rx.pattern not in statisztika:
            print("  ", rx.pattern)


if __name__ == '__main__':
    main()
