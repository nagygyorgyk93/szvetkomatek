#!/usr/bin/env python3
"""Szvetkó matek — belső link- és horgony-ellenőrző.
Futtatás a repo gyökeréből:  python _tools/check_links.py
Minden belső hivatkozást (href/src) és #horgonyt ellenőriz. Kilépési kód: hibaszám.
"""
import re, sys
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote

GYOKER = Path(__file__).resolve().parent.parent
KIHAGY = {"node_modules", ".git", "_sablonok"}  # a sablonok útvonalai a VÉGLEGES helyükre szólnak

class Gyujto(HTMLParser):
    def __init__(self):
        super().__init__()
        self.linkek = []   # (href|src)
        self.idk = set()
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a: self.idk.add(a["id"])
        if tag == "a" and a.get("name"): self.idk.add(a["name"])
        for kulcs in ("href","src"):
            if kulcs in a: self.linkek.append(a[kulcs])

def main():
    oldalak = {}
    for ut in GYOKER.rglob("*.html"):
        if any(r in KIHAGY for r in ut.relative_to(GYOKER).parts): continue
        g = Gyujto(); g.feed(ut.read_text(encoding="utf-8"))
        oldalak[ut] = g
    hibak = 0
    for ut, g in sorted(oldalak.items()):
        rel = ut.relative_to(GYOKER).as_posix()
        sablon = rel.startswith("_sablonok/")
        for link in g.linkek:
            if re.match(r"^(https?:|mailto:|data:|javascript:)", link): continue
            if sablon and "{{" in link: continue   # sablon-helyőrző
            u = urlparse(link)
            cel_ut, horgony = unquote(u.path), u.fragment
            if not cel_ut:                      # sajátoldali #horgony
                if horgony and horgony not in g.idk:
                    print(f"HIBA {rel}: hiányzó saját horgony #{horgony}"); hibak += 1
                continue
            cel = (ut.parent / cel_ut).resolve()
            if not cel.exists():
                print(f"HIBA {rel}: törött link -> {link}"); hibak += 1
                continue
            if horgony and cel.suffix == ".html" and cel in oldalak \
               and horgony not in oldalak[cel].idk:
                print(f"HIBA {rel}: {cel_ut} létezik, de nincs #{horgony} horgony"); hibak += 1
    print(f"{'HIBÁS' if hibak else 'RENDBEN'}: {len(oldalak)} oldal, {hibak} hiba")
    return hibak

if __name__ == "__main__":
    sys.exit(main())
