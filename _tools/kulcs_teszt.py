# -*- coding: utf-8 -*-
"""Megoldókulcs-önteszt a builder nélküli feladatgyűjteményekhez.

A 2e gyűjteményeknek van builderük, és abban sympy-önteszt fut minden
végeredményre. A hat örökölt 1e-gyűjteménynek nincs — a négy talált
kulcshiba mind onnan jött. Ez a szkript pótolja a hálót anélkül, hogy a
239 kártyát át kellene írni Pythonba: kiolvassa a HTML-ből a
„Végeredmény" szövegét, és összeveti egy FÜGGETLENÜL kiszámolt értékkel.

A várt értékeket a `_tools/kulcsok/*.py` modulok írják le:

    FAJL = '1e/01-logika-halmazok-fuggvenyek/feladatok-halmazok.html'
    TESZT = {
        'alap-3': [('a', {1,2,3,4,5,6,8}), ('b', {2,4}), …],
        'kozep-1': [('', 12)],          # egyetlen, betűjel nélküli válasz
    }

Támogatott várt típusok: `set` (halmaz), `int`/`float`/`Fraction` (szám),
`str` (szó szerinti részlet, kisbetűsítve, ékezet- és szóköztűrően).
"""
from __future__ import annotations

import glob
import importlib.util
import os
import re
import sys
import unicodedata
from fractions import Fraction

GYOKER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAG = re.compile(r'<[^>]+>')


def _szoveg(h: str) -> str:
    h = re.sub(r'\\(?:varnothing|emptyset)\b', ' \u2205 ', h)
    h = re.sub(r'\\[a-zA-Z]+\s*', ' ', h)          # KaTeX-parancsok
    h = TAG.sub(' ', h)
    for a, b in (('&lt;', '<'), ('&gt;', '>'), ('&amp;', '&'), ('&nbsp;', ' '),
                 ('\u2212', '-'), ('\u2013', '-'), ('\u2014', '-')):
        h = h.replace(a, b)
    return re.sub(r'\s+', ' ', h).strip()


def vegeredmenyek(ut: str) -> dict[str, str]:
    """id → a Végeredmény-lenyíló szövege."""
    s = open(ut, encoding='utf-8', errors='ignore').read()
    ki = {}
    for m in re.finditer(r'<article class="feladat[^"]*"[^>]*id="([^"]+)"(.*?)</article>',
                         s, re.S):
        azon, torzs = m.group(1), m.group(2)
        v = re.search(r'<details[^>]*>.*?</summary>(.*?)</details>', torzs, re.S)
        if v:
            ki[azon] = _szoveg(v.group(1))
    return ki


def _reszek(szoveg: str) -> dict[str, str]:
    """„a) … ; b) … ; c) …" → {'a': …, 'b': …}. Betűjel nélkül: {'': egész}."""
    darabok = re.split(r'(?:^|[;\s])([a-h])\)\s*', ' ' + szoveg)
    if len(darabok) < 3:
        return {'': szoveg}
    ki = {}
    for i in range(1, len(darabok) - 1, 2):
        ki[darabok[i]] = darabok[i + 1].strip(' ;.')
    return ki


def _halmaz(t: str) -> set | None:
    t = t.replace('\\', '')
    if '\u2205' in t and '{' not in t:
        return set()
    jeloltek = re.findall(r'\{([^{}]*)\}', t)
    # a jó jelölt elemekre bontható és nem tartalmaz operátor-maradványt
    tartalom = next((j for j in jeloltek
                     if j.strip() and all(re.fullmatch(r'[\w\u2205 -]+', e.strip())
                                          for e in re.split(r'[,;]', j) if e.strip())
                     and not re.search(r'[A-Z]\s+[A-Z]', j)), None)
    if tartalom is None:
        return None
    elemek = [e.strip() for e in re.split(r'[,;]', tartalom) if e.strip()]
    ki = set()
    for e in elemek:
        try:
            ki.add(int(e))
        except ValueError:
            ki.add(unicodedata.normalize('NFKD', e).encode('ascii', 'ignore').decode().lower())
    return ki


def _szamok(t: str) -> list[Fraction]:
    t = t.replace('{,}', ',').replace('\\', '')
    return [Fraction(x.replace(',', '.')) for x in re.findall(r'-?\d+(?:[.,]\d+)?', t)]


def _norm(t: str) -> str:
    t = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '', t)


def ellenoriz(modul) -> list[str]:
    ut = os.path.join(GYOKER, modul.FAJL)
    if not os.path.exists(ut):
        return [f'✗ nincs ilyen fájl: {modul.FAJL}']
    kulcsok = vegeredmenyek(ut)
    hibak = []
    for azon, vartak in modul.TESZT.items():
        if azon not in kulcsok:
            hibak.append(f'✗ {azon}: nincs Végeredmény-lenyíló (vagy nincs ilyen kártya)')
            continue
        reszek = _reszek(kulcsok[azon])
        for betu, vart in vartak:
            kapott = reszek.get(betu)
            if kapott is None:
                hibak.append(f'✗ {azon} {betu}): nincs ilyen részfeladat a kulcsban')
                continue
            if isinstance(vart, bool):
                # tautológia-döntés: a „nem tautológia” tartalmazza a „tautológia” szót,
                # ezért a tagadást külön kell néznünk
                n = _norm(kapott)
                allit = 'tautologia' in n and not n.startswith('nem')
                tenyleges = allit
                jo = allit == vart
            elif isinstance(vart, set):
                tenyleges = _halmaz(kapott)
                jo = tenyleges == vart
            elif isinstance(vart, (int, float, Fraction)):
                szamok = _szamok(kapott)
                tenyleges = szamok[-1] if szamok else None
                jo = any(abs(x - Fraction(vart)) < Fraction(1, 10**6) for x in szamok)
            else:
                tenyleges = kapott
                jo = _norm(str(vart)) in _norm(kapott)
            if not jo:
                hibak.append(f'✗ {azon} {betu}): a kulcs „{kapott[:70]}", '
                             f'a független számolás {vart}')
    return hibak


def main() -> int:
    modulok = sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                            'kulcsok', '*.py')))
    ossz_hiba, ossz_teszt = 0, 0
    for m in modulok:
        nev = os.path.basename(m)[:-3]
        spec = importlib.util.spec_from_file_location(nev, m)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        db = sum(len(v) for v in mod.TESZT.values())
        hibak = ellenoriz(mod)
        ossz_hiba += len(hibak)
        ossz_teszt += db
        print(f'── {mod.FAJL.split("/")[-1]:44s} {db:3d} ellenőrzés, {len(hibak)} hiba')
        for h in hibak:
            print('   ' + h)
    print(f'\n{"RENDBEN" if not ossz_hiba else "HIBÁS"}: {ossz_teszt} kulcsellenőrzés, '
          f'{ossz_hiba} eltérés')
    return 1 if ossz_hiba else 0


if __name__ == '__main__':
    sys.exit(main())
