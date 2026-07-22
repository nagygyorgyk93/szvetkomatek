#!/usr/bin/env python3
"""Szvetkó matek — keresőindex-építő.
Futtatás a repo gyökeréből:  python _tools/build_search_index.py
Minden tartalmi változás után újra kell futtatni (F5 integrációs lépés),
az eredmény: assets/search-index.json
"""
import json, re, sys
from pathlib import Path
from html.parser import HTMLParser

GYOKER = Path(__file__).resolve().parent.parent
KIHAGY = {"_sablonok", "_tools", "assets", "node_modules", ".git"}
KIHAGY_FAJL = {"search.html"}

class Kinyero(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cim = ""
        self.fejezetek = []
        self.szoveg = []
        self._gyujt = None      # 'title' | 'fej' | None
        self._testben = False
        self._kihagy_melyseg = 0

    def handle_starttag(self, tag, attrs):
        if tag == "title": self._gyujt = "title"
        elif tag in ("h1","h2","h3"):
            self._gyujt = "fej"; self.fejezetek.append("")
        elif tag == "body": self._testben = True
        elif tag in ("script","style","nav","header","footer") or \
             (tag == "div" and dict(attrs).get("id") == "progress"):
            self._kihagy_melyseg += 1

    def handle_endtag(self, tag):
        if tag == "title" or tag in ("h1","h2","h3"): self._gyujt = None
        elif tag in ("script","style","nav","header","footer"):
            self._kihagy_melyseg = max(0, self._kihagy_melyseg - 1)

    def handle_data(self, data):
        if self._gyujt == "title": self.cim += data
        elif self._gyujt == "fej":
            if self._kihagy_melyseg == 0: self.fejezetek[-1] += data
        elif self._testben and self._kihagy_melyseg == 0:
            self.szoveg.append(data)

def feldolgoz(ut: Path):
    p = Kinyero()
    p.feed(ut.read_text(encoding="utf-8"))
    rel = ut.relative_to(GYOKER).as_posix()
    reszek = rel.split("/")
    tagozat = reszek[0] if reszek[0] in {"1e","2e","3e","4e","4im"} else ""
    tema = reszek[1].split("-",1)[1].replace("-"," ") if len(reszek) > 2 else ""
    szoveg = re.sub(r"\s+", " ", " ".join(p.szoveg)).strip()
    cim = p.cim.split("|")[0].split("—")[0].strip() or rel
    return {
        "url": rel, "tagozat": tagozat, "tema": tema, "cim": cim,
        "fejezetek": [f.strip() for f in p.fejezetek if f.strip()],
        "szoveg": szoveg[:3000],
    }

def main():
    index = []
    for ut in sorted(GYOKER.rglob("*.html")):
        rel = ut.relative_to(GYOKER).parts
        if rel[0] in KIHAGY or ut.name in KIHAGY_FAJL: continue
        index.append(feldolgoz(ut))
    ki = GYOKER / "assets" / "search-index.json"
    ki.write_text(json.dumps(index, ensure_ascii=False), encoding="utf-8")
    print(f"OK: {len(index)} oldal indexelve -> {ki.relative_to(GYOKER)}")

if __name__ == "__main__":
    sys.exit(main())
