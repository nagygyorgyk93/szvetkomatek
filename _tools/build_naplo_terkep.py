#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Szvetkó matek — küldetésnapló-térkép építése.

Végigolvassa a tagozat-/témakör-mappákat, és összeírja, MIBŐL mennyi van:
hány tananyag-egység, összefoglaló, terepküldetés, kvíz és feladatkártya.
Ebből tudja a `naplo.js` és a `kuldetesnaplo.html` a haladás nevezőit.

Futtatás a repo gyökeréből:  python _tools/build_naplo_terkep.py
Kimenet: assets/naplo-terkep.json
"""
import json
import re
from pathlib import Path

GYOKER = Path(__file__).resolve().parent.parent
KI = GYOKER / "assets" / "naplo-terkep.json"
TAGOZATOK = ["1e", "2e", "3e", "4e", "4im"]

H1 = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S)
KVIZ = re.compile(r'class="kviz\b')
FELADAT = re.compile(r'<article class="feladat\b')
TAGEK = re.compile(r"<[^>]+>")


def cim(f: Path) -> str:
    m = H1.search(f.read_text(encoding="utf-8"))
    if not m:
        return f.stem
    return re.sub(r"\s+", " ", TAGEK.sub("", m.group(1))).strip()


def main() -> None:
    ki = {"xp": {"oldal": 10, "kviz": 5, "feladat": 2, "projekt": 30}, "tagozatok": {}}
    for tag in TAGOZATOK:
        tdir = GYOKER / tag
        if not (tdir / "index.html").exists():
            continue
        temak = []
        for tema in sorted(p for p in tdir.iterdir() if p.is_dir() and re.match(r"\d\d-", p.name)):
            oldalak, fgy = [], []
            kviz_db = feladat_db = 0
            for f in sorted(tema.glob("*.html")):
                sz = f.read_text(encoding="utf-8")
                url = f"{tag}/{tema.name}/{f.name}"
                k = len(KVIZ.findall(sz))
                kviz_db += k
                if f.name.startswith("tananyag-"):
                    oldalak.append({"u": url, "c": cim(f), "t": "tananyag", "k": k})
                elif f.name == "osszefoglalo.html":
                    oldalak.append({"u": url, "c": cim(f), "t": "osszefoglalo", "k": k})
                elif f.name == "terepkuldetes.html":
                    oldalak.append({"u": url, "c": cim(f), "t": "projekt", "k": k})
                elif f.name.startswith("feladatok-"):
                    db = len(FELADAT.findall(sz))
                    feladat_db += db
                    fgy.append({"u": url, "c": cim(f), "db": db,
                                "hazi": f.name == "feladatok-hazi.html"})
            if not oldalak and not fgy:
                continue
            temak.append({
                "mappa": tema.name,
                "url": f"{tag}/{tema.name}/index.html",
                "cim": cim(tema / "index.html") if (tema / "index.html").exists() else tema.name,
                "oldalak": oldalak,
                "fgy": fgy,
                "db": {"oldal": sum(1 for o in oldalak if o["t"] != "projekt"),
                       "projekt": sum(1 for o in oldalak if o["t"] == "projekt"),
                       "kviz": kviz_db, "feladat": feladat_db},
            })
        ki["tagozatok"][tag] = {"cim": cim(tdir / "index.html"), "url": f"{tag}/index.html",
                                "temakorok": temak}
    KI.write_text(json.dumps(ki, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    ossz = {"oldal": 0, "projekt": 0, "kviz": 0, "feladat": 0}
    for t in ki["tagozatok"].values():
        for tk in t["temakorok"]:
            for k in ossz:
                ossz[k] += tk["db"][k]
    xp = (ossz["oldal"] * 10 + ossz["projekt"] * 30 + ossz["kviz"] * 5 + ossz["feladat"] * 2)
    print(f"OK: {KI.relative_to(GYOKER)} — {ossz}, elérhető XP: {xp}")


if __name__ == "__main__":
    main()
