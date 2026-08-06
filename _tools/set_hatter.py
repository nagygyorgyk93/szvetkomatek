#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Szvetkó matek — helyszín-háttér hozzárendelése az oldaltípus szerint.

Minden HTML <body> tagjére ráírja a data-hatter attribútumot; a konkrét képeket
a theme.css `body[data-hatter="…"]` szabályai kötik hozzá. Idempotens: a meglévő
data-hatter értéket felülírja, minden mást változatlanul hagy (nyers szöveges
csere — bs4-újraszerializálás TILOS az inline SVG-k miatt).

Futtatás a repo gyökeréből:  python _tools/set_hatter.py [--dry]
"""
import re
import sys
from pathlib import Path

GYOKER = Path(__file__).resolve().parent.parent

# oldaltípus → helyszín-kulcs (a theme.css-ben definiált body[data-hatter] értékek)
TIPUS = {
    "landing":       "foepulet",    # gyökér index.html — a kampusz főépülete
    "kereso":        "diszterem",
    "tagozat-index": "diszterem",   # díszterem = holografikus eligazító
    "temakor-index": "foepulet",
    "tananyag":      "altalanos",   # Taktikai és Elemző Központ
    "feladatok":     "digitalis",   # Tech-Labor / Páncélműhely
    "osszefoglalo":  "digitalis",
    "hazi":          "tornaterem",  # Vészterem (Vészterem)
    "terepkuldetes": "rajzterem",   # Misztikus Művészetek Műterme
}


def tipus(rel: Path) -> str:
    """Az oldal típusa a repo-gyökérhez képesti útvonalból."""
    nev = rel.name
    reszek = rel.parts
    if len(reszek) == 1:
        return "landing" if nev == "index.html" else "kereso"
    if reszek[0] == "_sablonok":
        return {"tananyag.html": "tananyag", "feladatok.html": "feladatok",
                "osszefoglalo.html": "osszefoglalo",
                "temakor-index.html": "temakor-index"}.get(nev, "tananyag")
    if nev == "index.html":
        return "tagozat-index" if len(reszek) == 2 else "temakor-index"
    if nev.startswith("tananyag-"):
        return "tananyag"
    if nev == "feladatok-hazi.html":
        return "hazi"
    if nev.startswith("feladatok-"):
        return "feladatok"
    if nev == "osszefoglalo.html":
        return "osszefoglalo"
    if nev == "terepkuldetes.html":
        return "terepkuldetes"
    return "tananyag"


BODY_RE = re.compile(r"<body\b([^>]*)>", re.IGNORECASE)
ATTR_RE = re.compile(r'\s*data-hatter\s*=\s*"[^"]*"')


def feldolgoz(f: Path, dry: bool = False) -> bool:
    szoveg = f.read_text(encoding="utf-8")
    m = BODY_RE.search(szoveg)
    if not m:
        print(f"  ! nincs <body>: {f}")
        return False
    kulcs = TIPUS[tipus(f.relative_to(GYOKER))]
    attrs = ATTR_RE.sub("", m.group(1)).rstrip()
    uj = f'<body{attrs} data-hatter="{kulcs}">'
    if uj == m.group(0):
        return False
    if not dry:
        f.write_text(szoveg[:m.start()] + uj + szoveg[m.end():], encoding="utf-8")
    return True


def main() -> None:
    dry = "--dry" in sys.argv
    valtozott = 0
    osszes = 0
    for f in sorted(GYOKER.rglob("*.html")):
        if "assets" in f.parts or ".git" in f.parts:
            continue
        osszes += 1
        if feldolgoz(f, dry):
            valtozott += 1
    print(f"data-hatter: {valtozott} oldal frissítve / {osszes} összesen"
          + (" (próba)" if dry else ""))


if __name__ == "__main__":
    main()
