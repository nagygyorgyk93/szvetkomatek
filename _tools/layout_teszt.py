# -*- coding: utf-8 -*-
"""Böngésző-réteg (a web-verifikacio skill 4. rétege): Playwright + fej nélküli Chromium.

Minden kiválasztott lapot megnyit telefon- és asztali szélességen, és jelzi:
  - vízszintes túlcsordulás (a lap szélesebb a képernyőnél) + a túllógó elemeket
    (ami egy saját gördíthető dobozban lóg ki — pl. .tblwrap, .katex-display —, az nem hiba);
  - JS-kivétel és konzolhiba;
  - KaTeX-hiba (.katex-error).
A külső kéréseket (YouTube, GeoGebra, …) blokkolja — gyors és nem szivárog semmi.

Használat (a web-gyökérből):
  python _tools/layout_teszt.py                    minden lap, 360/390/1280 px
  python _tools/layout_teszt.py 4e/05-*/           csak egy témakör
  python _tools/layout_teszt.py --szelessegek 390  csak egy szélesség (gyors)
  python _tools/layout_teszt.py --kepek            képernyőképek a _layout/ mappába (gitignore)
  python _tools/layout_teszt.py --nyomtatas        + nyomtatási nézet képe (a --kepek mellé)
Előfeltétel: pip install playwright; böngésző: a gépen lévő Chromium (PLAYWRIGHT_BROWSERS_PATH)
vagy  python -m playwright install chromium.  Kilépési kód: 1, ha volt hiba.
"""
import argparse, functools, glob, http.server, os, socketserver, sys, threading

GYOKER = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
KIHAGY = ("_tools", "_sablonok", "_docs", "_layout", "assets", "node_modules", ".git", ".github", ".claude")

TULLOGOK = """() => {
  const W = document.documentElement.clientWidth, ki = [];
  const sajatGordul = el => { for (let p = el.parentElement; p && p !== document.body; p = p.parentElement) {
      const o = getComputedStyle(p).overflowX; if (o === 'auto' || o === 'scroll' || o === 'hidden') return true; }
    return false; };
  document.querySelectorAll('body *').forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.right <= W + 1) return;
    if ([...el.children].some(c => c.getBoundingClientRect().right > W + 1)) return;  // csak a legbelső
    if (sajatGordul(el)) return;
    const cls = (el.className && el.className.baseVal !== undefined) ? el.className.baseVal : el.className;
    ki.push(el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + (cls ? '.' + String(cls).trim().split(/\\s+/).join('.') : '')
            + ' (+' + Math.round(r.right - W) + ' px)');
  });
  return {tobblet: document.documentElement.scrollWidth - W, ki: ki.slice(0, 4),
          katex: document.querySelectorAll('.katex-error').length};
}"""


def lapok(mintak):
    if not mintak:
        mintak = ["."]
    ki = []
    for m in mintak:
        for ut in sorted(glob.glob(os.path.join(GYOKER, m))):
            if os.path.isdir(ut):
                for d, dirs, files in os.walk(ut):
                    dirs[:] = sorted(x for x in dirs if x not in KIHAGY)
                    ki += [os.path.join(d, f) for f in sorted(files) if f.endswith(".html")]
            elif ut.endswith(".html"):
                ki.append(ut)
    return [os.path.relpath(u, GYOKER).replace(os.sep, "/") for u in dict.fromkeys(ki)]


class _Csendes(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a, **k):
        pass


def szerver():
    kezelo = functools.partial(_Csendes, directory=GYOKER)
    srv = socketserver.ThreadingTCPServer(("127.0.0.1", 0), kezelo)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, f"http://127.0.0.1:{srv.server_address[1]}/"


def bongeszo(p):
    try:
        return p.chromium.launch()
    except Exception as ex:  # noqa: BLE001 — próbáljuk a gépen lévő Chromiumot
        for jelolt in [os.environ.get("CHROMIUM_PATH"), "/opt/pw-browsers/chromium",
                       *glob.glob("/opt/pw-browsers/chromium*/chrome-linux*/chrome"),
                       "/usr/bin/chromium", "/usr/bin/chromium-browser", "/usr/bin/google-chrome"]:
            if jelolt and os.path.isfile(jelolt):
                return p.chromium.launch(executable_path=jelolt)
        sys.exit(f"Nincs indítható Chromium ({ex}). Telepítés: python -m playwright install chromium")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mintak", nargs="*")
    ap.add_argument("--szelessegek", default="360,390,1280")
    ap.add_argument("--kepek", action="store_true")
    ap.add_argument("--nyomtatas", action="store_true")
    a = ap.parse_args(argv)
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit("Nincs Playwright: pip install playwright")
    szel = [int(x) for x in a.szelessegek.split(",") if x.strip()]
    lista = lapok(a.mintak)
    if not lista:
        sys.exit("Nincs ilyen lap.")
    srv, alap = szerver()
    kepdir = os.path.join(GYOKER, "_layout")
    hibas = 0
    with sync_playwright() as p:
        b = bongeszo(p)
        for lap in lista:
            jelzes = {}  # üzenet → szélességek (ami minden szélességen előjön, egyszer írjuk ki)
            for w in szel:
                pg = b.new_page(viewport={"width": w, "height": 900})
                hibak = []
                pg.on("pageerror", lambda e: hibak.append(f"JS-kivétel: {e}"))
                pg.on("console", lambda m: hibak.append(f"konzol: {m.text}")
                      if m.type == "error" and not m.text.startswith("Failed to load resource") else None)
                pg.on("response", lambda r: hibak.append(f"hiányzó fájl ({r.status}): /{r.url[len(alap):]}")
                      if r.status >= 400 and r.url.startswith(alap) else None)
                pg.route("**/*", lambda r: r.continue_() if r.request.url.startswith(alap) else r.abort())
                try:
                    pg.goto(alap + lap, wait_until="load", timeout=30000)
                    pg.wait_for_timeout(400)
                    e = pg.evaluate(TULLOGOK)
                except Exception as ex:  # noqa: BLE001
                    jelzes.setdefault(f"betöltési hiba: {ex}", []).append(w)
                    pg.close()
                    continue
                if e["tobblet"] > 0:
                    jelzes.setdefault(f"vízszintes túlcsordulás +{e['tobblet']} px — "
                                      f"{', '.join(e['ki']) or '?'}", []).append(w)
                if e["katex"]:
                    jelzes.setdefault(f"{e['katex']} KaTeX-hiba", []).append(w)
                for h in dict.fromkeys(hibak):
                    jelzes.setdefault(h, []).append(w)
                if a.kepek:
                    os.makedirs(kepdir, exist_ok=True)
                    nev = lap.replace("/", "__").replace(".html", "")
                    pg.screenshot(path=os.path.join(kepdir, f"{nev}__{w}.png"), full_page=True)
                    if a.nyomtatas and w == max(szel):
                        pg.emulate_media(media="print")
                        pg.screenshot(path=os.path.join(kepdir, f"{nev}__nyomtatas.png"), full_page=True)
                pg.close()
            if jelzes:
                hibas += 1
                print(f"✗ {lap}")
                for uz, ws in jelzes.items():
                    hol = "minden szélesség" if len(ws) == len(szel) else "/".join(map(str, ws)) + " px"
                    print(f"    [{hol}] {uz}")
        b.close()
    srv.shutdown()
    print(f"layout_teszt: {len(lista)} lap × {len(szel)} szélesség — "
          f"{'minden rendben' if not hibas else f'{hibas} lapon van jelzés'}."
          + (f" Képek: {os.path.relpath(kepdir, GYOKER)}/" if a.kepek else ""))
    return 1 if hibas else 0


if __name__ == "__main__":
    sys.exit(main())
