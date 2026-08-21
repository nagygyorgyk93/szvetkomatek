# -*- coding: utf-8 -*-
"""A 🎯 Gyors kérdés válaszsorrendjének megkeverése a KÉZI (builder nélküli) oldalakon.

Miért kell: a kvízek túlnyomó részében a helyes válasz az ELSŐ gomb volt, így két
oldal után a diák nem gondolkodik, hanem az elsőt nyomja — a kvíz nem mér semmit.

A buildereknél ezt a `tananyag_common.kviz()` intézi (`_kever`), és `data-kevert="1"`
jelet tesz a `.kviz` divre. Ez a szkript ugyanazt a **determinisztikus** forgatást
végzi el a HTML-ben azoknál a kvízeknél, amelyeken NINCS ilyen jel — így idempotens,
és nem keveri kétszer ugyanazt.

Használat a repo gyökeréből:  python _tools/kviz_kever.py [--apply]
"""
import os, re, sys, collections

ZARO = ("egyik sem", "egyikben sem", "egyik se", "mindegyik", "mindhárom",
        "mindkettő", "egyik állítás sem")

KVIZ = re.compile(
    r'<div class="kviz" data-answer="(?P<jo>\d+)"(?P<attr>[^>]*)>'
    r'(?P<kozep>.*?)'
    r'<div class="opciok">(?P<gombok>.*?)</div>',
    re.S)
GOMB = re.compile(r'<button>(.*?)</button>', re.S)
TAG = re.compile(r'<[^>]+>')


def kever(kerdes: str, opciok: list, jo_idx: int):
    n = len(opciok)
    if n < 2:
        return opciok, jo_idx, False
    for o in opciok:
        tiszta = TAG.sub('', o).strip().lower().lstrip('$„”"\'')
        if tiszta.startswith(ZARO):
            return opciok, jo_idx, False
    el = sum(ord(c) for c in kerdes) % n
    if el == 0:
        el = 1 if n > 1 else 0          # a 0 eltolás nem keverne semmit
    return opciok[el:] + opciok[:el], (jo_idx - el) % n, True


def main():
    gyoker = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 and
                             not sys.argv[1].startswith('--') else '.')
    ir = '--apply' in sys.argv
    stat = collections.Counter()
    fajlok = 0
    for r, ds, fs in os.walk(gyoker):
        ds[:] = [d for d in ds if d not in ('.git', '_tools', 'assets')]
        for f in fs:
            if not f.endswith('.html'):
                continue
            p = os.path.join(r, f)
            t = open(p, encoding='utf-8', newline='').read()

            def csere(m):
                if 'data-kevert' in m.group('attr'):
                    stat['kihagyva (builder)'] += 1
                    return m.group(0)
                opciok = GOMB.findall(m.group('gombok'))
                # a kérdés szövege a .kviz-cím utáni <p> — az eltolás ebből számolódik
                kerdes_m = re.search(r'<p>(?!<)(.*?)</p>\s*$', m.group('kozep'), re.S)
                kerdes = TAG.sub('', kerdes_m.group(1)) if kerdes_m else m.group('kozep')
                uj, jo, valt = kever(kerdes, opciok, int(m.group('jo')))
                if not valt:
                    stat['kihagyva (záró opció)'] += 1
                    return m.group(0)
                stat['megkeverve'] += 1
                gombok = "".join(f'<button>{o}</button>' for o in uj)
                return (f'<div class="kviz" data-answer="{jo}" data-kevert="1"'
                        f'{m.group("attr")}>{m.group("kozep")}'
                        f'<div class="opciok">{gombok}</div>')

            uj = KVIZ.sub(csere, t)
            if uj != t:
                fajlok += 1
                if ir:
                    open(p, 'w', encoding='utf-8', newline='').write(uj)
    print(f"{'ÍRVA' if ir else 'SZÁRAZ'}: {fajlok} fájl · " +
          " · ".join(f"{k}: {v}" for k, v in sorted(stat.items())))


if __name__ == '__main__':
    main()
