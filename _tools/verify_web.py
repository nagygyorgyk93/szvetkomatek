#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Szvetkó matek — oldal-verifikátor (kánon + render).

Futtatás a repo gyökeréből:

    python _tools/verify_web.py                     # minden oldal
    python _tools/verify_web.py 2e/04-*/           # egy témakör
    python _tools/verify_web.py 2e/04-*/tananyag-*.html
    python _tools/verify_web.py --csak-kanon        # jsdom-réteg nélkül (gyors)
    python _tools/verify_web.py --json              # gépi kimenet

Két réteg:

1. **Kánon-réteg** (pure Python, mindig fut) — azt ellenőrzi, amit a
   `_WEBOLDAL_workflow.md` 4b/4c kánonja és a világ-biblia 5a. FIX szerkezete előír:
   s0 cím, „🎯 Gyors kérdés”, a doboz-ikonok típushoz kötése, `data-tagozat`/`data-hatter`,
   szakasz-id-k sorrendje, kézi számozás tilalma, **nyers `$` a címekben** (a `mat()`
   kimaradása), feladatkártyák id/szint/végeredmény hármasa, `data-answer` érvényessége,
   `.sav.hangya`/`.sav.hulk`, és hogy a naplo.js felismeri-e az oldaltípust.

2. **Render-réteg** (`verify_jsdom.mjs`, ha van node + jsdom) — lefuttatja az oldal saját
   JS-ét: KaTeX renderel-e hibátlanul, marad-e nyers `$` a **renderelt** szövegben,
   reagálnak-e a kvízgombok, van-e konzolhiba.

Amit egyik réteg SEM lát: layout — mobil-túlcsordulás, nyomtatási nézet, kontraszt.
Azt böngészőből kell nézni (lásd a `web-verifikacio` skill 3. rétegét).

A `check_links.py` a belső linkeket és horgonyokat ellenőrzi — ez a szkript azt NEM
duplikálja, futtasd mellette.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

GYOKER = Path(__file__).resolve().parent.parent
KIHAGY = {".git", "_sablonok", "node_modules", "_tools"}

# A KÁNON fix leképezései — ezek köntösből NEM módosíthatók (világ-biblia 5a).
IKON = {"definicio": "📗", "tetel": "📘", "pelda": "✏️", "csapda": "⚠️", "erdekesseg": "💡"}
S0_CIM = "📡 Küldetés-eligazítás"
KVIZ_CIM = "🎯 Gyors kérdés"
SZINTEK = ("alap", "kozep", "nehez", "joker")
# A naplo.js a fájlnév-minta alapján számol XP-t; ami nem illik rá, az nem számít bele.
NAPLO_MINTAK = (r"^tananyag-.*\.html$", r"^feladatok-.*\.html$",
                r"^osszefoglalo\.html$", r"^terepkuldetes\.html$", r"^index\.html$")

_TAG = re.compile(r"<[^>]+>")
_URES = {"br", "hr", "img", "meta", "link", "input", "source", "path", "circle",
         "line", "rect", "polyline", "polygon", "use", "stop", "ellipse", "text"}


def _szoveg(html: str) -> str:
    """Tagek nélküli szöveg, összenyomott whitespace-szel."""
    return " ".join(_TAG.sub(" ", html).split())


class TagMerleg(HTMLParser):
    """Nyitott/zárt tagek egyensúlya — a builderek néha nyitva hagynak egy `div`-et."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.verem: list[str] = []
        self.hibak: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag not in _URES and not tag.startswith("!"):
            self.verem.append(tag)

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if tag in _URES:
            return
        if tag in self.verem:
            while self.verem and self.verem.pop() != tag:
                pass
        else:
            self.hibak.append(f"záró </{tag}> nyitó nélkül")


def kanon_ellenorzes(ut: Path) -> tuple[list[str], list[str]]:
    """Egy oldal kánon-ellenőrzése. Visszaad: (hibák, figyelmeztetések)."""
    s = ut.read_text(encoding="utf-8")
    nev = ut.name
    hibak: list[str] = []
    figy: list[str] = []
    tananyag = nev.startswith("tananyag-")
    terepkuldetes = nev == "terepkuldetes.html"
    try:
        reszek = ut.relative_to(GYOKER).parts   # resolve() nélkül: a mounton lassú
    except ValueError:
        reszek = ut.parts
    # A gyökér-oldalak (index, search, kuldetesnaplo) nem tagozathoz tartoznak,
    # és a témakör-mappán belüli oldalakra vonatkoznak a naplo-minták.
    tagozati = bool(reszek) and reszek[0] in {"1e", "2e", "3e", "4e", "4im", "3im"}
    temakorben = tagozati and len(reszek) >= 3

    # --- body attribútumok ---
    body = re.search(r"<body([^>]*)>", s)
    battr = body.group(1) if body else ""
    if tagozati and "data-tagozat=" not in battr:
        hibak.append("a <body>-n nincs data-tagozat (accent-szín nem fog működni)")
    if "data-hatter=" not in battr:
        hibak.append("a <body>-n nincs data-hatter — futtasd: python _tools/set_hatter.py")

    # --- naplo.js felismerés ---
    if temakorben and not any(re.match(m, nev) for m in NAPLO_MINTAK):
        figy.append(f"a naplo.js fájlnév-mintái nem ismerik fel a(z) „{nev}”-t "
                    f"→ nem ad XP-t; vagy nevezd át, vagy vedd fel a naplo.js mintái közé")

    # --- h2 szakaszok ---
    h2k = re.findall(r'<h2([^>]*)>(.*?)</h2>', s, re.S)
    idk = [re.search(r'id="([^"]+)"', a).group(1) if re.search(r'id="([^"]+)"', a) else None
           for a, _ in h2k]
    if tananyag:
        if not h2k:
            hibak.append("tananyag-oldal h2 szakaszok nélkül")
        else:
            if idk[0] != "s0":
                hibak.append(f"az első h2 id-je „{idk[0]}”, nem „s0”")
            elif _szoveg(h2k[0][1]) != S0_CIM:
                hibak.append(f"az s0 címe „{_szoveg(h2k[0][1])}”, "
                             f"a KÁNON szerint „{S0_CIM}”")
        varhato = [f"s{i}" for i in range(len(h2k))]
        if idk != varhato:
            hibak.append(f"a h2 id-k nem folytonosak: {idk} (várt: {varhato})")

    # --- kézi számozás, emoji és nyers $ a címekben ---
    for tag in ("h1", "h2", "h3"):
        for attr, torzs in re.findall(rf'<{tag}([^>]*)>(.*?)</{tag}>', s, re.S):
            szov = _szoveg(torzs)
            azon = re.search(r'id="([^"]+)"', attr)
            azon = azon.group(1) if azon else ""
            if tananyag and re.match(r"^\d+[.)]\s", szov):
                hibak.append(f"<{tag}> kézi számozással: „{szov[:50]}” "
                             f"(tananyag-oldalon a számozást a TOC adja)")
            if "$" in szov:
                hibak.append(f"nyers $ a(z) <{tag}> címben: „{szov[:60]}” "
                             f"— a mat() nem futott le rajta, a diák dollárjeleket lát")
            if tananyag and tag == "h2" and re.search(r"[\U0001F300-\U0001FAFF☀-➿]", szov):
                if azon != "s0" and "Gyorsismétlő" not in szov:
                    figy.append(f"emoji a(z) <h2>-ben: „{szov[:40]}” "
                                f"(a KÁNON szerint csak s0-ban és a Gyorsismétlőben)")

    # nyers $ egyéb szövegblokkokban is
    for cimke, minta in (("summary", r"<summary[^>]*>(.*?)</summary>"),
                         ("doboz-cím", r'<p class="cim">(.*?)</p>'),
                         ("figcaption", r"<figcaption[^>]*>(.*?)</figcaption>"),
                         ("kép-alá", r'<p class="cap">(.*?)</p>')):
        for torzs in re.findall(minta, s, re.S):
            szov = _szoveg(torzs)
            if "$" in szov:
                hibak.append(f"nyers $ a(z) {cimke}-ben: „{szov[:60]}”")

    # --- nyers `<` a matek-határolókon belül ---
    # A böngésző a `<b+c`-t NYITÓ TAGNAK olvassa, és lenyeli a tartalmat: a képlet
    # eltűnik az oldalról (a diák csak „\\[a"-t lát). 2026-08-06-ig 10 helyen volt
    # így, mind az 1e migrált oldalain. Escape-elve (`&lt;`) a KaTeX ugyanazt kapja.
    for m in re.finditer(r"(?:\\\[(.*?)\\\]|\\\((.*?)\\\))", s, re.S):
        torzs = m.group(1) if m.group(1) is not None else m.group(2)
        if torzs and re.search(r"<[A-Za-z]", torzs):
            hibak.append(f"nyers `<` a matekban: „{' '.join(torzs.split())[:50]}” — a böngésző "
                         f"tagnak olvassa és a képlet ELTŰNIK; írd `&lt;`-ként")

    # --- doboz-ikonok a típushoz kötve ---
    for tipus, torzs in re.findall(
            r'<div class="doboz ([a-z]+)"[^>]*>\s*<p class="cim"><span class="ikon">([^<]*)</span>',
            s):
        if tipus not in IKON:
            figy.append(f"ismeretlen doboz-típus: „{tipus}”")
        elif torzs.strip() != IKON[tipus]:
            hibak.append(f"a „{tipus}” doboz ikonja „{torzs.strip()}”, "
                         f"a KÁNON szerint „{IKON[tipus]}”")

    # --- kvízek ---
    for kviz in re.findall(r'<div class="kviz"(.*?)</div>\s*</div>', s, re.S):
        cim = re.search(r'<p class="kviz-cim">(.*?)</p>', kviz)
        if not cim:
            hibak.append("kvíz .kviz-cim nélkül")
        elif _szoveg(cim.group(1)) != KVIZ_CIM:
            hibak.append(f"a kvíz címe „{_szoveg(cim.group(1))}”, "
                         f"a KÁNON szerint „{KVIZ_CIM}”")
    # data-answer INDEX-érvényesség (a quiz.js 0-alapú indexet vár)
    for blokk in re.findall(r'<div class="(?:kviz|valtozat)"[^>]*data-answer="([^"]*)"(.*?)(?=<div class="(?:kviz|valtozat)"|\Z)',
                            s, re.S):
        val, torzs = blokk
        gombok = len(re.findall(r"<button", torzs))
        if not val.strip().lstrip("-").isdigit():
            hibak.append(f'data-answer="{val}" nem szám — a quiz.js 0-alapú INDEXET vár')
        elif gombok and not (0 <= int(val) < gombok):
            hibak.append(f'data-answer="{val}" kívül van a {gombok} gomb tartományán')

    # --- differenciált sávok ---
    if 'class="savok"' in s:
        if "sav hangya" not in s or "sav hulk" not in s:
            hibak.append("a .savok blokkban nincs .sav.hangya és/vagy .sav.hulk "
                         "(az osztálynevek fixek, csak a felirat évadfüggő)")

    # --- feladatkártyák ---
    kartyak = re.findall(r'<article class="feladat([^"]*)"([^>]*)>(.*?)</article>', s, re.S)
    azonok = []
    for osztaly, attr, torzs in kartyak:
        azon = re.search(r'id="([^"]+)"', attr)
        szintek = [x for x in SZINTEK if x in osztaly.split()]
        if azon:
            aid = azon.group(1)
            azonok.append(aid)
            # A gyakorló blokkok kártyái szándékosan szint nélküliek (2 XP) — nem jelzés.
            gyakorlo = aid.startswith("gy")
            if not szintek and not gyakorlo and not terepkuldetes:
                figy.append(f"a(z) #{aid} kártyán nincs szint-osztály — "
                            f"a naplo nem tudja, mennyi XP-t adjon")
            # A terepküldetés megoldása SZÁNDÉKOSAN nem a publikus oldalon van,
            # hanem privát tanári megoldókulcs-DOCX-ban.
            if "vegeredmeny" not in torzs and not terepkuldetes:
                hibak.append(f"a(z) #{aid} kártyán nincs .vegeredmeny lenyíló")
        if len(szintek) > 1:
            hibak.append(f"egy kártyán több szint-osztály: {szintek}")
    ismetlodo = [a for a, db in Counter(azonok).items() if db > 1]
    if ismetlodo:
        hibak.append(f"ismétlődő feladat-id: {ismetlodo} — a naplo XP-je és a linkek elromlanak")

    # --- tag-egyensúly ---
    m = TagMerleg()
    m.feed(s)
    if m.hibak:
        hibak.extend(m.hibak[:3])
    if m.verem:
        hibak.append(f"nyitva maradt tag(ek): {m.verem[-3:]}")

    return hibak, figy


def oldalak_gyujtese(mintak: list[str]) -> list[Path]:
    if not mintak:
        jeloltek = GYOKER.rglob("*.html")
    else:
        jeloltek = []
        for mt in mintak:
            p = Path(mt)
            if p.is_absolute():
                jeloltek.append(p) if p.suffix == ".html" else jeloltek.extend(p.rglob("*.html"))
            else:
                for t in GYOKER.glob(mt):
                    jeloltek.append(t) if t.suffix == ".html" else jeloltek.extend(t.rglob("*.html"))
    ki = []
    for p in sorted(set(jeloltek)):
        try:
            rel = p.relative_to(GYOKER).parts
        except ValueError:
            rel = p.parts
        if any(r in KIHAGY for r in rel):
            continue
        if p.suffix == ".html" and p.is_file():
            ki.append(p)
    return ki


def render_reteg(oldalak: list[Path]) -> dict[str, dict]:
    """A jsdom-réteg lefuttatása. Hiba esetén üres dictet ad, nem áll meg."""
    mjs = Path(__file__).resolve().parent / "verify_jsdom.mjs"
    if not mjs.exists():
        return {"__hiba__": {"ok": "nincs verify_jsdom.mjs"}}
    try:
        pr = subprocess.run(
            ["node", str(mjs)] + [str(p) for p in oldalak],
            capture_output=True, text=True, timeout=60 + 12 * len(oldalak),
            cwd=str(GYOKER),
        )
    except FileNotFoundError:
        return {"__hiba__": {"ok": "nincs `node` — a render-réteg kimaradt"}}
    except subprocess.TimeoutExpired:
        return {"__hiba__": {"ok": "a jsdom-réteg túllépte az időkorlátot"}}
    ki: dict[str, dict] = {}
    for sor in pr.stdout.splitlines():
        sor = sor.strip()
        if sor.startswith("{"):
            try:
                d = json.loads(sor)
                ki[Path(d["fajl"]).name] = d
            except Exception:
                pass
    if not ki and pr.stderr:
        ok = pr.stderr.strip().splitlines()[-1][:160]
        return {"__hiba__": {"ok": f"a jsdom-réteg nem futott: {ok}"}}
    return ki


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Szvetkó matek oldal-verifikátor")
    ap.add_argument("mintak", nargs="*", help="fájl- vagy mappaminták (üres = minden oldal)")
    ap.add_argument("--csak-kanon", action="store_true", help="a jsdom-réteg kihagyása")
    ap.add_argument("--json", action="store_true", help="gépi kimenet")
    ap.add_argument("--szoveg", action="store_true",
                    help="a renderelt szöveg kiírása (friss szemű teszthez), nem ellenőrzés")
    ap.add_argument("--kulcs-nelkul", action="store_true",
                    help="--szoveg mellett: a .vegeredmeny lenyílók kihagyva, a kulcsok a végén")
    args = ap.parse_args(argv)

    oldalak = oldalak_gyujtese(args.mintak)
    if not oldalak:
        print("Nincs ellenőrizendő oldal.", file=sys.stderr)
        return 2

    if args.szoveg:
        mjs = Path(__file__).resolve().parent / "verify_jsdom.mjs"
        hivas = ["node", str(mjs), "--szoveg"]
        if args.kulcs_nelkul:
            hivas.append("--kulcs-nelkul")
        return subprocess.call(hivas + [str(p) for p in oldalak], cwd=str(GYOKER))

    render = {} if args.csak_kanon else render_reteg(oldalak)
    render_hiba = render.pop("__hiba__", None)

    ossz_hiba = 0
    eredmeny = []
    for p in oldalak:
        hibak, figy = kanon_ellenorzes(p)
        r = render.get(p.name, {})
        if r:
            if r.get("betoltes_hiba"):
                hibak.append(f"render: az oldal nem töltődött be — {r['betoltes_hiba'][:90]}")
            if r.get("katex_hiba"):
                hibak.append(f"render: KaTeX-hiba ({len(r['katex_hiba'])} db): "
                             f"{r['katex_hiba'][:2]}")
            if r.get("nyers_dollar"):
                hibak.append(f"render: {r['nyers_dollar']} nyers $ a renderelt szövegben "
                             f"— „{r.get('nyers_minta','')[:60]}”")
            if r.get("kviz_rossz"):
                hibak.append(f"render: kvíz nem reagált a helyes gombra: {r['kviz_rossz'][:2]}")
            for h in r.get("hibak", []):
                figy.append(f"render-konzol: {h[:110]}")
        ossz_hiba += len(hibak)
        eredmeny.append({
            "fajl": p.relative_to(GYOKER).as_posix() if GYOKER in p.parents else str(p),
            "hibak": hibak, "figyelmeztetesek": figy,
            "katex": r.get("katex_db"), "kviz": f"{r.get('kviz_ok','?')}/{r.get('kviz_db','?')}" if r else None,
        })

    if args.json:
        print(json.dumps({"oldalak": eredmeny, "hibaszam": ossz_hiba,
                          "render_hiba": render_hiba}, ensure_ascii=False, indent=1))
        return 1 if ossz_hiba else 0

    if render_hiba:
        print(f"⚠ {render_hiba['ok']}")
        print("  (a kánon-réteg lefutott; jsdom telepítése: "
              "npm install jsdom --prefix /tmp/vw)\n")

    for e in eredmeny:
        if not e["hibak"] and not e["figyelmeztetesek"]:
            continue
        fej = e["fajl"]
        if e["katex"] is not None:
            fej += f"   [katex {e['katex']} · kvíz {e['kviz']}]"
        print(f"── {fej}")
        for h in e["hibak"]:
            print(f"   ✗ {h}")
        for f in e["figyelmeztetesek"]:
            print(f"   ⚠ {f}")
        print()

    tiszta = sum(1 for e in eredmeny if not e["hibak"])
    print(f"{'HIBÁS' if ossz_hiba else 'RENDBEN'}: {len(eredmeny)} oldal, "
          f"{ossz_hiba} hiba, {tiszta} oldal hibátlan")
    if not args.csak_kanon and not render_hiba:
        print("A layout (mobil-túlcsordulás, nyomtatás, kontraszt) NEM ellenőrizve — "
              "azt böngészőből nézd.")
    return 1 if ossz_hiba else 0


if __name__ == "__main__":
    sys.exit(main())
