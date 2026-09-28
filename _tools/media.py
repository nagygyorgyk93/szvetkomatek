# -*- coding: utf-8 -*-
"""Külső média (YouTube-videó, GeoGebra-szimuláció) beillesztése a lapokba.

Katalógus: _tools/media/<osztaly>.json (1e.json, 2e.json, …) — mindegyik egy JSON-lista.
A mezőket a MEZOK szótár írja le; a teljes szabályzat: .claude/skills/media-beagyazas.

A blokkok a  <!-- media:begin AZON --> … <!-- media:end AZON -->  jelölők közé kerülnek.
Minden futás kiveszi a régieket, és a katalógusból újraírja őket → idempotens.
A builderek újragenerálják a lapot (és ezzel a blokkokat is törlik), ezért a builder-lánc
része, a kepek.py után:   kepek.py . --apply → media.py . --apply → set_hatter.py → …

Használat (a web-gyökérből):
  python _tools/media.py [gyoker]              száraz futás: ellenőrzés + mi változna
  python _tools/media.py [gyoker] --apply      írás
  python _tools/media.py [gyoker] --online     elérhetőség: YouTube oEmbed (+ csatorna), GeoGebra API
  python _tools/media.py [gyoker] --jelentes   Markdown-táblázat (PR-leíráshoz)
"""
import argparse, datetime, glob, html, json, os, re, sys
import urllib.error, urllib.request

MEZOK = {
    "azon": "egyedi, [a-z0-9-], pl. 4e05-binom-video",
    "oldal": "a lap útja a web-gyökértől, pl. 4e/05-kombinatorika/tananyag-binomialis-tetel.html",
    "hely": "'sN' = az sN szakasz VÉGÉRE; '#elem-id' = az adott id-jű elem UTÁN",
    "tipus": "youtube | geogebra",
    "forras_azon": "YouTube-videóazonosító (11 kar.) vagy GeoGebra-anyagazonosító (/m/XXXX)",
    "cim": "a videó / szimuláció címe (ahogy a forrásnál szerepel, vagy magyarított)",
    "leiras": "1–2 mondat: mit nézzen/csináljon a kadét (HTML, KaTeX \\( \\) mehet) — opcionális",
    "szerzo": "a készítő neve (GeoGebra-licenc: kötelező a szerző feltüntetése)",
    "forras": "a forrás megnevezése a képaláírásban, pl. 'MNT Távoktatás magyar nyelven', 'GeoGebra'",
    "forras_url": "a forrás-oldal (MNT óra-oldala / geogebra.org/m/…)",
    "nyelv": "hu | en | sr | de | fr | … | - (nyelvfüggetlen)",
    "licenc": "rövid licenc-jelzés, pl. 'YouTube-beágyazás' / 'CC BY-NC-SA 4.0'",
    "ellenorizve": "ÉÉÉÉ-HH-NN — mikor nézte meg valaki, hogy él és illik a helyére",
    "hossz": "(youtube, opcionális) pp:mm",
    "kezdes": "(youtube, opcionális) indulás másodpercben",
    "arany": "(opcionális) 16/9 (alap) | 4/3 | 3/2 | 1/1",
    "allapot": "(opcionális) aktiv (alap) | kikapcsolva — a kikapcsolt elem nem kerül a lapra",
    "megjegyzes": "(opcionális) belső megjegyzés, a lapra nem kerül ki",
}
KOTELEZO = ("azon", "oldal", "hely", "tipus", "forras_azon", "cim", "szerzo", "forras",
            "forras_url", "nyelv", "licenc", "ellenorizve")
AZON_MINTA = {"youtube": re.compile(r"^[A-Za-z0-9_-]{11}$"),
              "geogebra": re.compile(r"^[A-Za-z0-9]{6,12}$")}
ARANYOK = {"16/9", "4/3", "3/2", "1/1"}
NYELV = {"en": "angol", "sr": "szerb", "de": "német", "fr": "francia", "es": "spanyol",
         "it": "olasz", "hr": "horvát", "sk": "szlovák", "ro": "román"}
BLOKK = re.compile(r"[ \t]*<!-- media:begin (\S+) -->.*?<!-- media:end \1 -->[ \t]*\n?", re.S)
BLOKK_ELEJEN = re.compile(r"\s*<!-- media:begin (\S+) -->.*?<!-- media:end \1 -->", re.S)
SZAKASZ_VEG = re.compile(r'<h2\b|<div class="gyakorolj|<div class="brief" data-outro|'
                         r'<div class="lapozo|<nav class="lapozo|</main>')
URES = {"br", "hr", "img", "input", "meta", "link", "source", "wbr"}


def esc(x):
    return html.escape(str(x), quote=True)


def katalogus(gyoker):
    elemek, hibak = [], []
    for f in sorted(glob.glob(os.path.join(gyoker, "_tools", "media", "*.json"))):
        try:
            lista = json.load(open(f, encoding="utf-8"))
        except Exception as ex:  # noqa: BLE001
            hibak.append(f"{os.path.basename(f)}: nem olvasható JSON ({ex})")
            continue
        if not isinstance(lista, list):
            hibak.append(f"{os.path.basename(f)}: a gyökérnek listának kell lennie")
            continue
        for e in lista:
            e["_fajl"] = os.path.basename(f)
            elemek.append(e)
    return elemek, hibak


def ellenoriz(gyoker, elemek):
    hibak, figy, lathato, videok = [], [], {}, {}
    ma = datetime.date.today()
    for e in elemek:
        hol = f"{e.get('_fajl')} / {e.get('azon', '?')}"
        hiany = [k for k in KOTELEZO if not str(e.get(k, "")).strip()]
        if hiany:
            hibak.append(f"{hol}: hiányzó mező(k): {', '.join(hiany)}")
            continue
        ismeretlen = [k for k in e if k not in MEZOK and not k.startswith("_")]
        if ismeretlen:
            figy.append(f"{hol}: ismeretlen mező(k): {', '.join(ismeretlen)}")
        if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", e["azon"]):
            hibak.append(f"{hol}: az azon csak kisbetű, számjegy, kötőjel lehet")
        if e["azon"] in lathato:
            hibak.append(f"{hol}: ismétlődő azon")
        lathato[e["azon"]] = e
        if e["tipus"] not in AZON_MINTA:
            hibak.append(f"{hol}: ismeretlen tipus {e['tipus']!r}")
            continue
        if not AZON_MINTA[e["tipus"]].match(e["forras_azon"]):
            hibak.append(f"{hol}: gyanús forras_azon {e['forras_azon']!r} ({e['tipus']})")
        # Egy videó csak egy helyre kerül (tanári döntés, 2026-09-28) — akkor is, ha az óra több lap
        # témáját lefedi, vagy ha két MNT-óra oldala ugyanazt a videót ágyazza be.
        if e["tipus"] == "youtube" and e.get("allapot", "aktiv") == "aktiv":
            elso = videok.setdefault(e["forras_azon"], e)
            if elso is not e:
                hibak.append(f"{hol}: ez a videó már szerepel ({elso['azon']}, {elso['oldal']}) — "
                             "egy videó csak egy helyre kerülhet; a többit kapcsold ki")
        if e.get("arany", "16/9") not in ARANYOK:
            hibak.append(f"{hol}: arany csak {sorted(ARANYOK)} lehet")
        if e.get("allapot", "aktiv") not in ("aktiv", "kikapcsolva"):
            hibak.append(f"{hol}: allapot csak aktiv | kikapcsolva lehet")
        if not str(e["forras_url"]).startswith("https://"):
            hibak.append(f"{hol}: a forras_url https:// legyen")
        try:
            d = datetime.date.fromisoformat(e["ellenorizve"])
            if (ma - d).days > 365:
                figy.append(f"{hol}: több mint egy éve ellenőrizve ({d}) — futtasd: --online")
        except ValueError:
            hibak.append(f"{hol}: az ellenorizve ÉÉÉÉ-HH-NN legyen")
        ut = os.path.join(gyoker, e["oldal"])
        if not os.path.isfile(ut):
            hibak.append(f"{hol}: nincs ilyen lap: {e['oldal']}")
        if e["tipus"] == "youtube" and e.get("nyelv") not in ("hu", "-"):
            figy.append(f"{hol}: nem magyar nyelvű videó — csak ha nincs jó magyar")
    return hibak, figy


def blokk(e, behuz):
    t, azon = e["tipus"], e["forras_azon"]
    nyelv = NYELV.get(e.get("nyelv"), e.get("nyelv"))
    info = []
    if t == "youtube":
        k = int(e.get("kezdes") or 0)
        nezo = f"https://www.youtube.com/watch?v={azon}" + (f"&t={k}s" if k else "")
        rovid = f"youtu.be/{azon}" + (f"?t={k}" if k else "")
        cimke, ikon = "Videó", "▶"
        if e.get("hossz"):
            info.append(esc(e["hossz"]))
        if k:
            info.append(f"a {k // 60}:{k % 60:02d}-tól")
        info.append("kattints a lejátszáshoz")
        alair = (f'<span class="media-forras">Forrás: <a href="{esc(e["forras_url"])}" '
                 f'target="_blank" rel="noopener">{esc(e["forras"])}</a> — {esc(e["szerzo"])}.</span>')
    else:
        nezo = f"https://www.geogebra.org/m/{azon}"
        rovid = f"geogebra.org/m/{azon}"
        cimke, ikon = "GeoGebra-szimuláció", "⟲"
        info.append("interaktív — kattints a betöltéshez")
        alair = (f'<span class="media-forras">Készült a <a href="{esc(e["forras_url"])}" '
                 f'target="_blank" rel="noopener">GeoGebra®</a> segítségével, '
                 f'szerző: {esc(e["szerzo"])} ({esc(e["licenc"])}).</span>')
    if nyelv and nyelv not in ("hu", "-"):
        info.insert(0, f"{nyelv} nyelvű")
    attr = [f'class="media"', f'id="media-{esc(e["azon"])}"', f'data-tipus="{t}"',
            f'data-azon="{esc(azon)}"', f'data-cim="{esc(e["cim"])}"']
    if e.get("arany") and e["arany"] != "16/9":
        attr.append(f'data-arany="{esc(e["arany"])}"')
    if t == "youtube" and int(e.get("kezdes") or 0):
        attr.append(f'data-kezdes="{int(e["kezdes"])}"')
    leiras = (e.get("leiras") or "").strip()
    b = behuz
    return "\n".join([
        f"{b}<!-- media:begin {e['azon']} -->",
        f"{b}<figure {' '.join(attr)}>",
        f'{b}  <div class="media-keret"><a class="media-indito" href="{esc(nezo)}" target="_blank" rel="noopener">'
        f'<span class="media-ikon" aria-hidden="true">{ikon}</span><span class="media-szoveg">'
        f'<span class="media-cimke">{cimke}</span><span class="media-cim">{esc(e["cim"])}</span>'
        f'<span class="media-info">{" · ".join(info)}</span></span></a></div>',
        f"{b}  <figcaption>{leiras + ' ' if leiras else ''}{alair} "
        f'<span class="media-url">({cimke}: {esc(e["cim"])} — {esc(rovid)})</span></figcaption>',
        f"{b}</figure>",
        f"{b}<!-- media:end {e['azon']} -->",
    ]) + "\n"


def pont(s, hely):
    """(pozíció, behúzás) — ide kerül a blokk; None, ha a hely nem található."""
    if hely.startswith("#"):
        m = re.search(r'<([a-zA-Z][\w-]*)\b[^>]*\bid="%s"[^>]*>' % re.escape(hely[1:]), s)
        if not m:
            return None
        tag = m.group(1).lower()
        vege = None
        if tag in URES or m.group(0).endswith("/>"):
            vege = m.end()
        else:
            melyseg = 1
            for t in re.finditer(r"<(/?)%s\b[^>]*?(/?)>" % re.escape(tag), s[m.end():], re.I):
                if t.group(1):
                    melyseg -= 1
                elif not t.group(2):
                    melyseg += 1
                if melyseg == 0:
                    vege = m.end() + t.end()
                    break
        if vege is None:
            return None
        while True:  # a már ott álló médiablokkok után (a katalógus-sorrend marad)
            mb = BLOKK_ELEJEN.match(s, vege)
            if not mb:
                break
            vege = mb.end()
        sor_eleje = s.rfind("\n", 0, m.start()) + 1
        behuz = re.match(r"[ \t]*", s[sor_eleje:]).group(0)
        nl = s.find("\n", vege)
        poz = nl + 1 if nl >= 0 and not s[vege:nl].strip() else vege
        return poz, behuz
    m = re.search(r'<h2\b[^>]*\bid="%s"' % re.escape(hely), s)
    if not m:
        return None
    t = SZAKASZ_VEG.search(s, m.end())
    if not t:
        return None
    sor_eleje = s.rfind("\n", 0, t.start()) + 1
    elotte = s[sor_eleje:t.start()]
    if elotte.strip():
        return t.start(), ""
    return sor_eleje, elotte


def lapok_markerrel(gyoker):
    for d, dirs, files in os.walk(gyoker):
        dirs[:] = [x for x in dirs if not x.startswith(".") and x not in ("node_modules", "_tools", "assets")]
        for f in files:
            if f.endswith(".html"):
                ut = os.path.join(d, f)
                if "<!-- media:begin" in open(ut, encoding="utf-8").read():
                    yield os.path.relpath(ut, gyoker).replace(os.sep, "/")


def online(elemek):
    rossz = 0
    for e in elemek:
        if e["tipus"] == "youtube":
            url = ("https://www.youtube.com/oembed?format=json&url="
                   f"https://www.youtube.com/watch?v={e['forras_azon']}")
        else:
            url = f"https://api.geogebra.org/v1.0/materials/{e['forras_azon']}?scope=basic"
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "szvetko-media/1.0"}), timeout=20) as r:
                adat = json.loads(r.read().decode("utf-8", "replace") or "{}")
            cim = adat.get("title") or adat.get("name") or ""
            csatorna = adat.get("author_name") or ""  # YouTube oEmbed: a feltöltő csatorna
            print(f"  OK   {e['azon']:<32} {cim[:60]}" + (f"  [{csatorna}]" if csatorna else ""))
        except urllib.error.HTTPError as ex:
            rossz += 1
            ok = {401: "beágyazás letiltva", 403: "tiltott / privát", 404: "nem létezik (törölt?)"}
            print(f"  HIBA {e['azon']:<32} HTTP {ex.code} — {ok.get(ex.code, 'ismeretlen')}")
        except Exception as ex:  # noqa: BLE001
            rossz += 1
            print(f"  ???  {e['azon']:<32} {type(ex).__name__}: {ex} (hálózat engedélyezve?)")
    return rossz


def jelentes(elemek):
    print("| azon | lap · hely | típus | cím | szerző / forrás | nyelv |")
    print("|---|---|---|---|---|---|")
    for e in elemek:
        link = (f"https://www.youtube.com/watch?v={e['forras_azon']}" if e["tipus"] == "youtube"
                else f"https://www.geogebra.org/m/{e['forras_azon']}")
        print(f"| {e['azon']} | `{e['oldal']}` · {e['hely']} | {e['tipus']} | [{e['cim']}]({link}) | "
              f"{e['szerzo']} · [{e['forras']}]({e['forras_url']}) | {e['nyelv']} |")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("gyoker", nargs="?", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--online", action="store_true")
    ap.add_argument("--jelentes", action="store_true")
    a = ap.parse_args(argv)
    gyoker = os.path.abspath(a.gyoker)

    elemek, hibak = katalogus(gyoker)
    h2, figy = ellenoriz(gyoker, elemek)
    hibak += h2
    aktiv = [e for e in elemek if e.get("allapot", "aktiv") == "aktiv" and "azon" in e]
    for f in figy:
        print("  figyelem:", f)
    if a.jelentes:
        jelentes(aktiv)
        return 0
    if a.online:
        print(f"Online ellenőrzés ({len(aktiv)} elem):")
        return 1 if online(aktiv) else 0

    lapok = sorted(set(e["oldal"] for e in aktiv if os.path.isfile(os.path.join(gyoker, e["oldal"])))
                   | set(lapok_markerrel(gyoker)))
    valtozott, uj = 0, {}
    for lap in lapok:
        ut = os.path.join(gyoker, lap)
        regi = open(ut, encoding="utf-8").read()
        s = BLOKK.sub("", regi)
        for e in (x for x in aktiv if x["oldal"] == lap):
            p = pont(s, e["hely"])
            if p is None:
                hibak.append(f"{e['_fajl']} / {e['azon']}: a hely ({e['hely']}) nem található itt: {lap}")
                continue
            poz, behuz = p
            s = s[:poz] + blokk(e, behuz) + s[poz:]
        if s != regi:
            valtozott += 1
            db = len(re.findall(r"<!-- media:begin ", s))
            print(f"  {'ír' if a.apply else 'változna'}: {lap} ({db} médiablokk)")
            uj[ut] = s
    if a.apply and not hibak:  # csak ha minden elem rendben van: vagy mind, vagy semmi
        for ut, s in uj.items():
            open(ut, "w", encoding="utf-8", newline="\n").write(s)
    for h in hibak:
        print("  HIBA:", h)
    if hibak:
        print(f"media.py: {len(hibak)} hiba — semmi nem íródott ki." if a.apply else f"media.py: {len(hibak)} hiba.")
        return 1
    print(f"media.py: {len(aktiv)} aktív elem, {len(lapok)} lap, {valtozott} "
          f"{'módosítva' if a.apply else 'változna (--apply nélkül nem ír)'}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
