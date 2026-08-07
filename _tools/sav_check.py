# -*- coding: utf-8 -*-
"""Gyakorló-sáv lefedettség — a tananyag-egységek .gyakorolj sávjai hézag és
nem létező kártyára mutatás nélkül fedik-e le a témakör feladatgyűjteményét.

Külön szkript, mert témakör-szintű (a verify_web.py laponként dolgozik).
"""
import collections
import glob
import os
import re
import sys

SAV = re.compile(r'<a class="sav [a-z]+" href="([^"#]*)#(alap|kozep|nehez)-(\d+)"[^>]*>'
                 r'.*?<span class="cimke">([^<]*)</span>', re.S)
TART = re.compile(r'([AKN])\s*([\d,\s–-]+)')
BETU = {'A': 'alap', 'K': 'kozep', 'N': 'nehez'}
GYOKER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def szamok(sp):
    ki = set()
    for r in re.split(r'[,\s]+', sp.strip()):
        m = re.match(r'^(\d+)[–-](\d+)$', r or '')
        if m:
            ki |= set(range(int(m.group(1)), int(m.group(2)) + 1))
        elif r.isdigit():
            ki.add(int(r))
    return ki


def main():
    hibak = 0
    for tag in ('1e', '2e', '3e', '4e', '4im'):
        gy = os.path.join(GYOKER, tag)
        if not os.path.isdir(gy):
            continue
        for tema in sorted(os.listdir(gy)):
            d = os.path.join(gy, tema)
            if not os.path.isdir(d):
                continue
            h = collections.defaultdict(lambda: collections.defaultdict(set))
            for f in sorted(glob.glob(d + '/tananyag-*.html')):
                sz = open(f, encoding='utf-8', errors='ignore').read()
                for cel, _, _, cimke in SAV.findall(sz):
                    for b, sp in TART.findall(cimke):
                        h[cel][BETU[b]] |= szamok(sp)
            for cel, szintek in sorted(h.items()):
                p = os.path.join(d, cel)
                if not os.path.exists(p):
                    print(f"✗ {tag}/{tema}: a sáv nem létező fájlra mutat ({cel})")
                    hibak += 1
                    continue
                s = open(p, encoding='utf-8', errors='ignore').read()
                for szint, fedve in sorted(szintek.items()):
                    db = len(re.findall(r'id="%s-\d+"' % szint, s))
                    tul = sorted(x for x in fedve if x > db)
                    hi = sorted(set(range(1, db + 1)) - fedve)
                    if tul:
                        print(f"✗ {tag}/{tema} · {cel} · {szint}: a sáv nem létező "
                              f"kártyára mutat: {tul} (összesen {db} van)")
                        hibak += 1
                    if hi:
                        print(f"⚠ {tag}/{tema} · {cel} · {szint}: ezeket a kártyákat egyetlen "
                              f"tananyag-egység sem adja fel: {hi}")
    print("RENDBEN: minden feladatkártyát felad valamelyik egység"
          if not hibak else f"HIBÁS: {hibak} sávhiba")
    return 1 if hibak else 0


if __name__ == '__main__':
    sys.exit(main())
