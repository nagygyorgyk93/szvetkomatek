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

# Témakör-jelvények: küldetés-cím + mentor + jel (a `_WEBOLDAL_tortenet_[osztály].md`
# fejezet-térképe szerint). Új témakörnél ide is fel kell venni egy sort — ha kimarad,
# a jelvény a semleges 🛡️ jelet és a témakör címét kapja.
JELVENY = {
    "1e/01-logika-halmazok-fuggvenyek":        ("🃏", "Az Igazság Csarnoka", "Ikol · Dr. Bizarr · Petar Pauk"),
    "1e/02-trigonometria":                     ("🏹", "A Célzó", "Barton Kálmán"),
    "1e/03-egesz-es-valos-szamok":             ("🔢", "A Kódtörő · A Kalibrálás", "Iruhs · Banner Brúnó"),
    "1e/04-aranyossag":                        ("🐜", "A Zsugor-protokoll", "Hangya Henrik & Darázs Dorka"),
    "1e/05-geometria":                         ("🔮", "A Csatatér-térkép · A Tükör-világ", "Dr. Bizarr · Vanda & Fürge Pjotr"),
    "1e/06-racionalis-algebrai-kifejezesek":   ("⚙️", "A Hatalom Nyelve", "Iruhs & Krats Ynot"),
    "1e/07-linearis-egyenletek-es-rendszerek": ("🛡️", "A Végső Egyenlet", "a teljes csapat"),
    "1e/08-hasonlosag":                        ("📐", "A Skála Törvénye", "Hangya Henrik"),
    "2e/01-hatvanyozas-gyokvonas-komplex-szamok": ("🧬", "A Képzelet Határa", "Vihar Vera · X. Károly professzor"),
    "2e/02-masodfoku-egyenletek-es-fuggvenyek":   ("⚔️", "Az M-Faktor", "Nagol · Küklopsz"),
    "2e/03-exponencialis-es-logaritmus-fuggveny": ("🧬", "Az Evolúciós Ugrás", "Dr. Bestia"),
    "2e/04-trigonometrikus-fuggvenyek":           ("🌀", "A Fázisugrás", "Éjjáró · Szürke Janka"),
    "3e/01-poliederek":                           ("🔷", "A Kristálypára Kristályok", "Prizma"),
    "3e/02-forgastestek":                         ("🔷", "Az Átalakulás Kamrája", "Medúza"),
}

H1 = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S)
KVIZ = re.compile(r'class="kviz\b')
FELADAT = re.compile(r'<article class="(feladat[^"]*)"')
TAGEK = re.compile(r"<[^>]+>")

# A feladatok pontja a nehézséggel nő (a naplo.js FPONT-jával azonos!);
# a gyakorló blokkok kártyáin nincs szint-osztály → alapszintnek számítanak.
FPONT = {"alap": 2, "kozep": 3, "nehez": 5, "joker": 5, "": 2}


def feladat_xp(osztaly: str) -> int:
    for szint in ("nehez", "kozep", "joker", "alap"):
        if szint in osztaly.split():
            return FPONT[szint]
    return FPONT[""]


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
            kviz_db = feladat_db = feladat_xp_ossz = 0
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
                    osztalyok = FELADAT.findall(sz)
                    db = len(osztalyok)
                    xp_db = sum(feladat_xp(o) for o in osztalyok)
                    feladat_db += db
                    feladat_xp_ossz += xp_db
                    fgy.append({"u": url, "c": cim(f), "db": db, "xp": xp_db,
                                "hazi": f.name == "feladatok-hazi.html"})
            if not oldalak and not fgy:
                continue
            jel, kuldetes, mentor = JELVENY.get(f"{tag}/{tema.name}", ("🛡️", "", ""))
            temak.append({
                "mappa": tema.name,
                "url": f"{tag}/{tema.name}/index.html",
                "cim": cim(tema / "index.html") if (tema / "index.html").exists() else tema.name,
                "jel": jel, "kuldetes": kuldetes, "mentor": mentor,
                "oldalak": oldalak,
                "fgy": fgy,
                "db": {"oldal": sum(1 for o in oldalak if o["t"] != "projekt"),
                       "projekt": sum(1 for o in oldalak if o["t"] == "projekt"),
                       "kviz": kviz_db, "feladat": feladat_db,
                       "feladat_xp": feladat_xp_ossz},
            })
        ki["tagozatok"][tag] = {"cim": cim(tdir / "index.html"), "url": f"{tag}/index.html",
                                "temakorok": temak}
    KI.write_text(json.dumps(ki, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    ossz = {"oldal": 0, "projekt": 0, "kviz": 0, "feladat": 0, "feladat_xp": 0}
    for t in ki["tagozatok"].values():
        for tk in t["temakorok"]:
            for k in ossz:
                ossz[k] += tk["db"][k]
    xp = ossz["oldal"] * 10 + ossz["projekt"] * 30 + ossz["kviz"] * 5 + ossz["feladat_xp"]
    print(f"OK: {KI.relative_to(GYOKER)} — {ossz}, elérhető XP: {xp}")


if __name__ == "__main__":
    main()
