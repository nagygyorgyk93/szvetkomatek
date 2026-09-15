#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Szvetkó matek — egy oldalon belül ismétlődő id-k megszüntetése.

Két forrása van a duplikált id-nek:
  1. az SVG-generátorok (svg_fuggvenyek, _fej, trigonometrikus kör …) minden ábrába
     ugyanazt a `<marker id="nyil">`-t teszik — két ábra egy oldalon már ütközik, és a
     nyílhegy a böngészőtől függően az első ábra markerét kapja;
  2. a feladatgyűjteményekben a `<h2 id="joker">` és a joker-kártya `<article id="joker">`
     ugyanazt az id-t viseli.

Az SVG-n belüli id-t a blokk tartalmából számolt, DETERMINISZTIKUS (crc32) utótaggal
nevezzük át, a hivatkozásokkal (`url(#…)`, `href="#…"`) együtt, csak ha az id az oldalon
több ábrában is előfordul. A h2 id-je `joker-szint` lesz (a kártya id-jére a kulcs-modulok
hivatkoznak, az marad). Idempotens; nyers szöveges csere (bs4 TILOS az inline SVG-k miatt).

A builderek (`tananyag_common.lap`, `fgy_common.oldal`) írás előtt meghívják az
`egyedi_idk()`-t. A régi, builder nélküli oldalakra:
    python _tools/egyedi_id.py [--dry]          (a repo gyökeréből)
"""
import collections
import re
import sys
import zlib
from pathlib import Path

GYOKER = Path(__file__).resolve().parent.parent
SVG = re.compile(r'<svg\b.*?</svg>', re.S)
SVG_ID = re.compile(r'\sid="([^"]+)"')


def egyedi_idk(html: str) -> str:
    blokkok = list(SVG.finditer(html))
    hol = collections.Counter()
    for b in blokkok:
        for i in set(SVG_ID.findall(b.group(0))):
            hol[i] += 1
    utk = {i for i, n in hol.items() if n > 1}
    if utk:
        ki, poz, latott = [], 0, set()
        for b in blokkok:
            s = b.group(0)
            ids = set(SVG_ID.findall(s)) & utk
            if ids:
                h = format(zlib.crc32(s.encode()) & 0xFFFFF, "05x")
                while h in latott:
                    h = format((int(h, 16) + 1) & 0xFFFFF, "05x")
                latott.add(h)
                for i in sorted(ids, key=len, reverse=True):
                    uj = f"{i}-{h}"
                    s = (s.replace(f'id="{i}"', f'id="{uj}"')
                          .replace(f'url(#{i})', f'url(#{uj})')
                          .replace(f'href="#{i}"', f'href="#{uj}"'))
            ki.append(html[poz:b.start()])
            ki.append(s)
            poz = b.end()
        ki.append(html[poz:])
        html = "".join(ki)
    if html.count('id="joker"') > 1:
        html = html.replace('<h2 id="joker">', '<h2 id="joker-szint">')
    return html


def main(argv):
    dry = "--dry" in argv
    valtozott = 0
    for ut in sorted(GYOKER.rglob("*.html")):
        if any(r.startswith(("_", ".")) or r == "node_modules" for r in ut.relative_to(GYOKER).parts):
            continue
        s = ut.read_text(encoding="utf-8")
        uj = egyedi_idk(s)
        if uj != s:
            valtozott += 1
            print("  ", ut.relative_to(GYOKER))
            if not dry:
                ut.write_text(uj, encoding="utf-8")
    print(f"egyedi id: {valtozott} oldal {'módosulna' if dry else 'frissítve'}")


if __name__ == "__main__":
    main(sys.argv[1:])
