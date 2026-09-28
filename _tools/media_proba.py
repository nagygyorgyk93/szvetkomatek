#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Szvetkó matek — a beágyazott GeoGebra-szimulációk kipróbálása telefon-szélességen.

A layout_teszt.py minden külső kérést blokkol; ez az eszköz épp fordítva: megnyitja a lapot,
rákattint a GeoGebra-blokkokra (media.py), megvárja, hogy az applet betöltődjön, és a keretről
képernyőképet ment a _layout/media/ mappába (gitignore). Így ellenőrizhető a media-beagyazas
skill szabálya: „mobilon (390 px) kipróbálva” — kifér-e, olvasható-e, nem csak egy darabja látszik-e.

Használat (a web-gyökérből):
  python _tools/media_proba.py 1e/05-geometria/tananyag-haromszogek.html
  python _tools/media_proba.py 1e/ --szelesseg 360        minden GeoGebra-blokk a mappa lapjain
  python _tools/media_proba.py <lap> --azon 1e05-szogosszeg-ggb --var 20
Hálózat kell (www.geogebra.org). Felhős munkamenetben a konténer proxyján megy át; ha van
proxy-CA (/root/.ccr/agent-proxy-ca.crt), a böngésző csak ennek a kulcsát fogadja el pluszban.
Kilépési kód: 1, ha egy applet nem töltődött be (nincs rajzvászon), vagy a lap vízszintesen kilóg.
"""
import argparse, glob, os, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from layout_teszt import GYOKER, szerver  # noqa: E402

CA = "/root/.ccr/agent-proxy-ca.crt"


def bongeszo(p):
    opc = {}
    if os.environ.get("HTTPS_PROXY"):
        # Nem a Playwright proxy-opciója: az a helyi címeket (127.0.0.1) is a proxyra küldi
        # (<-loopback>), és ha a proxy csak HTTPS-alagutat fogad, a saját lapunk 405-öt kap.
        opc["args"] = ["--proxy-server=" + os.environ["HTTPS_PROXY"],
                       "--proxy-bypass-list=127.0.0.1;localhost"]
        if os.path.isfile(CA):
            spki = subprocess.run(f"openssl x509 -in {CA} -pubkey -noout | openssl pkey -pubin -outform der"
                                  " | openssl dgst -sha256 -binary | base64", shell=True,
                                  capture_output=True, text=True).stdout.strip()
            if spki:
                opc["args"].append("--ignore-certificate-errors-spki-list=" + spki)
    try:
        return p.chromium.launch(**opc)
    except Exception as ex:  # noqa: BLE001 — a gépen lévő Chromium
        for jelolt in [os.environ.get("CHROMIUM_PATH"), *glob.glob("/opt/pw-browsers/chromium*/chrome-linux*/chrome"),
                       "/usr/bin/chromium", "/usr/bin/chromium-browser", "/usr/bin/google-chrome"]:
            if jelolt and os.path.isfile(jelolt):
                return p.chromium.launch(executable_path=jelolt, **opc)
        sys.exit(f"Nincs indítható Chromium ({ex}).")


def lapok(mintak):
    ki = []
    for m in mintak:
        ut = os.path.join(GYOKER, m)
        if os.path.isdir(ut):
            ki += sorted(os.path.relpath(f, GYOKER) for f in glob.glob(os.path.join(ut, "**", "*.html"), recursive=True))
        else:
            ki.append(m)
    return [l for l in ki if 'data-tipus="geogebra"' in open(os.path.join(GYOKER, l), encoding="utf-8").read()]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mintak", nargs="+")
    ap.add_argument("--azon", nargs="*", default=None, help="csak ezek a média-azonosítók")
    ap.add_argument("--szelesseg", type=int, default=390)
    ap.add_argument("--var", type=int, default=15, help="ennyi másodpercet vár a betöltésre")
    a = ap.parse_args(argv)
    from playwright.sync_api import sync_playwright
    kidir = os.path.join(GYOKER, "_layout", "media")
    os.makedirs(kidir, exist_ok=True)
    srv, alap = szerver()
    hiba = 0
    with sync_playwright() as p:
        b = bongeszo(p)
        for lap in lapok(a.mintak):
            pg = b.new_page(viewport={"width": a.szelesseg, "height": 844}, is_mobile=True, has_touch=True)
            pg.goto(alap + lap)
            pg.wait_for_timeout(600)
            figs = pg.locator('figure.media[data-tipus="geogebra"]')
            azonok = [figs.nth(i).get_attribute("id")[len("media-"):] for i in range(figs.count())]
            azonok = [z for z in azonok if a.azon is None or z in a.azon]
            for z in azonok:
                f = pg.locator(f"#media-{z}")
                f.scroll_into_view_if_needed()
                f.locator(".media-indito").click()
            pg.wait_for_timeout(a.var * 1000)
            for z in azonok:
                f = pg.locator(f"#media-{z}")
                f.scroll_into_view_if_needed()
                pg.wait_for_timeout(300)
                keret = f.locator(".media-keret")
                kep = os.path.join(kidir, f"{z}_{a.szelesseg}.png")
                keret.screenshot(path=kep)
                fr = keret.locator("iframe").element_handle().content_frame() if keret.locator("iframe").count() else None
                try:
                    vaszon = fr.evaluate("document.querySelectorAll('canvas').length") if fr else 0
                except Exception:  # noqa: BLE001
                    vaszon = 0
                bb = keret.bounding_box()
                allapot = "OK  " if vaszon else "HIBA"
                hiba += not vaszon
                print(f"  {allapot} {z:<34} {round(bb['width'])}×{round(bb['height'])} px, vászon: {vaszon}  → {os.path.relpath(kep, GYOKER)}")
            sz = pg.evaluate("document.documentElement.scrollWidth")
            if sz > a.szelesseg + 1:
                hiba += 1
                print(f"  HIBA {lap}: a lap vízszintesen kilóg (+{sz - a.szelesseg} px)")
            pg.close()
        b.close()
    srv.shutdown()
    print(f"media_proba: {'minden applet betöltődött' if not hiba else f'{hiba} hiba'} ({a.szelesseg} px).")
    return 1 if hiba else 0


if __name__ == "__main__":
    sys.exit(main())
