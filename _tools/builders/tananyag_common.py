# -*- coding: utf-8 -*-
"""Közös váz a tananyag-egység oldalakhoz (workflow 4b. KÁNON).

A tartalmat a témakör-builderek adják; itt csak a fix burok él:
fejléc · morzsa · hero · main.lap.toc-os · lapozó · lábléc · KaTeX + ui.js + quiz.js.

Rövidítő jelölés a tartalomban:
  $...$    → <span class="math inline">\\( ... \\)</span>
  $$...$$  → <span class="math display">\\[ ... \\]</span>
"""
from __future__ import annotations
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from egyedi_id import egyedi_idk  # noqa: E402  (a _tools mappából)

GYOKER = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

_DISPLAY = re.compile(r"\$\$(.+?)\$\$", re.S)
_INLINE = re.compile(r"\$(.+?)\$", re.S)


def mat(szoveg: str) -> str:
    """A $…$ / $$…$$ rövidítéseket KaTeX-es span-okra cseréli."""
    szoveg = _DISPLAY.sub(
        lambda m: '<span class="math display">\\[' + m.group(1).strip() + '\\]</span>', szoveg)
    szoveg = _INLINE.sub(
        lambda m: '<span class="math inline">\\(' + m.group(1).strip() + '\\)</span>', szoveg)
    return szoveg


_TABLA = re.compile(r'(<div class="tblwrap">\s*)?(<table class="tt-table\b[^>]*>.*?</table>)', re.S)


def tablak_gorgethetok(html: str) -> str:
    """Minden `table.tt-table` saját gördíthető burkot kap (`<div class="tblwrap">`).

    A képletes cella nem törik, így a táblázat telefonon szélesebb lehet a lapnál; burok
    nélkül az egész lap oldalra csúszik, a burokban csak a táblázat gördül (kánon). Az írás
    előtt fut (`lap`, `fgy_common.oldal`), a már burkolt táblázatot nem bántja (idempotens).
    """
    return _TABLA.sub(lambda m: m.group(0) if m.group(1) else f'<div class="tblwrap">{m.group(2)}</div>', html)


# ------------------------------------------------------------------ dobozok

IKON = {"definicio": "📗", "tetel": "📘", "pelda": "✏️", "csapda": "⚠️", "erdekesseg": "💡"}


def doboz(tipus: str, cim: str, torzs: str, hid: str = "", lenyilo: tuple | None = None) -> str:
    """`.doboz.<tipus>` a KÁNON szerinti FIX ikonnal. `lenyilo` = (összefoglaló, tartalom)."""
    azon = f' id="{hid}"' if hid else ""
    ki = [f'<div class="doboz {tipus}"{azon}>',
          f'  <p class="cim"><span class="ikon">{IKON[tipus]}</span> {cim}</p>',
          f'  {torzs.strip()}']
    if lenyilo:
        ossz, tart = lenyilo
        ki.append(f'  <details><summary>{ossz}</summary><div class="bel">{tart.strip()}</div></details>')
    ki.append('</div>')
    return "\n".join(ki)


def brief(szoveg: str, outro: bool = False) -> str:
    attr = " data-outro" if outro else ""
    return f'<div class="brief"{attr}><p>📡 {szoveg.strip()}</p></div>'


def _attr(szoveg: str) -> str:
    """Attribútumérték: a $…$ előbb KaTeX-spanná, majd az idézőjel `&quot;`-tá.

    Enélkül a visszajelzésbe írt képlet `class="math inline"` idézőjelei ELTÖRIK az
    attribútumot (a `verify_web.py` „záró </span> nyitó nélkül" hibaként fogja meg).
    """
    return mat(szoveg).replace('"', "&quot;")


_ZARO = ("egyik sem", "egyikben sem", "egyik se", "mindegyik", "mindhárom",
         "mindkettő", "egyik állítás sem")


def _kever(kerdes: str, opciok: list[str], jo_idx: int):
    """A helyes válasz ne mindig az ELSŐ gomb legyen.

    A lista determinisztikus (a kérdés szövegéből számolt) eltolással forog, ezért
    minden újrafuttatás ugyanazt a sorrendet adja. Kimarad a keverésből az olyan
    kvíz, amelynek az utolsó opciója összefoglaló jellegű („egyik sem”, „mindegyik”),
    mert annak a helye kötött.
    """
    n = len(opciok)
    if n < 2:
        return opciok, jo_idx
    if any(o.strip().lower().lstrip("$„”\"'").startswith(_ZARO) for o in opciok):
        return opciok, jo_idx
    el = sum(ord(c) for c in kerdes) % n
    return opciok[el:] + opciok[:el], (jo_idx - el) % n


def kviz(kerdes: str, opciok: list[str], jo_idx: int = 0, jo: str = "", nem: str = "") -> str:
    """Gyors kérdés. FONTOS: a `jo_idx` a `opciok` lista 0-alapú indexe.

    A megjelenített sorrendet a `_kever` determinisztikusan elforgatja, hogy a helyes
    válasz ne mindig az első gomb legyen — a `jo_idx` ehhez igazodik.
    """
    opciok, jo_idx = _kever(kerdes, opciok, jo_idx)
    gombok = "".join(f"<button>{o}</button>" for o in opciok)
    # a `data-kevert` jelzi, hogy a sorrend MÁR át van rendezve — a `_tools/kviz_kever.py`
    # (a builder nélküli, kézi oldalakhoz) ennek alapján hagyja békén ezt a kvízt
    kevert = ' data-kevert="1"'
    extra = ""
    if jo:
        extra += f' data-jo="{_attr(jo)}"'
    if nem:
        extra += f' data-nem="{_attr(nem)}"'
    return (f'<div class="kviz" data-answer="{jo_idx}"{kevert}{extra}>\n'
            f'  <p class="kviz-cim">🎯 Gyors kérdés</p>\n'
            f'  <p>{kerdes}</p>\n'
            f'  <div class="opciok">{gombok}</div>\n'
            f'  <p class="visszajelzes" aria-live="polite"></p>\n'
            f'</div>')


# A sávok OSZTÁLYNEVE évadtól függetlenül `.sav.henrik` (könnyített) és `.sav.bruno`
# (normál) — csak a FELIRAT évadfüggő (világ-biblia 5b.).
SAV_FELIRAT = {
    "1e": ("🐜 Henrik-bevetés", "💥 Brúnó-bevetés"),
    "2e": ("🐾 Bestia-protokoll", "🔥 Főnix-protokoll"),
    "3e": ("🐕 Tér-eb-ugrás", "👑 Királyi Gárda"),
    "4e": ("🐶 Véd-eb nyomravezető", "⚔️ Maximális erőbedobás"),
}


def gyakorolj(konnyu_href: str, konnyu_cimke: str, normal_href: str, normal_cimke: str,
              bevezeto: str = "Válaszd ki a bevetésed:", tagozat: str = "2e") -> str:
    """Differenciált sávok. A felirat az évadból jön (`SAV_FELIRAT`), az osztálynév fix."""
    konnyu_nev, normal_nev = SAV_FELIRAT[tagozat]
    return ('<div class="gyakorolj"><span class="ikon">🎯</span><div>'
            f'<p><b>Gyakorolj!</b> {bevezeto}</p><div class="savok">'
            f'<a class="sav henrik" href="{konnyu_href}">{konnyu_nev} <span class="cimke">{konnyu_cimke}</span></a>'
            f'<a class="sav bruno" href="{normal_href}">{normal_nev} <span class="cimke">{normal_cimke}</span></a>'
            '</div></div></div>')


def abra(svg: str, felirat: str = "") -> str:
    cap = f'\n<p class="cap">{felirat}</p>' if felirat else ""
    return f'<div class="svgcard">\n{svg.strip()}\n</div>{cap}'


def svg_fuggvenyek(gorbek, xr=(-2.6, 2.6), yr=(-2.6, 4.2), w=360, h=250,
                   leiras="Függvénygrafikonok koordináta-rendszerben", jelmagyarazat=True,
                   pontok=None, tengely=("x", "y"), egyseg=("1", "1"), terulet=None):
    """`pontok` = [(x, y, felirat, szin, dx, dy), …] — kiemelt pontok felirattal.
    `terulet` = [(f, g, lo, hi, szin[, átlátszóság]), …] — árnyékolt tartomány f és g között a [lo; hi]-n
    (g=None: az x tengelyig); a görbék alá kerül."""
    """Koordináta-rendszer + görbék inline SVG-ként, SÖTÉT tintával, világos lapon.

    `gorbek` = [(f, szin, cimke, [(lo, hi), …] szakaszok[, "szaggatott"]), …] — az opcionális
    5. elem szaggatott vonalat kér (aszimptotákhoz).
    A y-értékeket a rajzterületre vágjuk (a pólusok nem lógnak ki).
    `pontok` színe „o:#rrggbb” alakban ÜRES (fehér kitöltésű) pontot rajzol — a „lyukhoz”.
    """
    bal, jobb, fent, lent = 26, 12, 14, 22
    px, py = w - bal - jobb, h - fent - lent
    x0, x1 = xr
    y0, y1 = yr

    def X(x):
        return bal + (x - x0) / (x1 - x0) * px

    def Y(y):
        return fent + (y1 - y) / (y1 - y0) * py

    ki = [f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{leiras}">',
          '  <g stroke="#cbd5e1" stroke-width=".6">']
    t = int(x0) if x0 == int(x0) else int(x0) + 1
    while t <= x1:
        if t != 0:
            ki.append(f'    <line x1="{X(t):.1f}" y1="{Y(y0):.1f}" x2="{X(t):.1f}" y2="{Y(y1):.1f}"/>')
        t += 1
    t = int(y0) if y0 == int(y0) else int(y0) + 1
    while t <= y1:
        if t != 0:
            ki.append(f'    <line x1="{X(x0):.1f}" y1="{Y(t):.1f}" x2="{X(x1):.1f}" y2="{Y(t):.1f}"/>')
        t += 1
    ki.append('  </g>')
    # tengelyek
    ki.append(f'  <line x1="{X(x0):.1f}" y1="{Y(0):.1f}" x2="{X(x1):.1f}" y2="{Y(0):.1f}" '
              'stroke="#0f172a" stroke-width="1.4" marker-end="url(#nyil)"/>')
    ki.append(f'  <line x1="{X(0):.1f}" y1="{Y(y0):.1f}" x2="{X(0):.1f}" y2="{Y(y1):.1f}" '
              'stroke="#0f172a" stroke-width="1.4" marker-end="url(#nyil)"/>')
    ki.insert(1, '  <defs><marker id="nyil" viewBox="0 0 8 8" refX="6" refY="4" markerWidth="6" '
                 'markerHeight="6" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#0f172a"/></marker></defs>')
    # tengelyfeliratok
    # A tengelynevek és az egységfeliratok felülírhatók: ha a rajz egysége nem 1
    # (pl. 10 perc vagy 1000 dinár), a puszta „1” félrevezető.
    xnev, ynev = tengely
    xegys, yegys = egyseg
    ki.append(f'  <text x="{X(x1) - 4:.1f}" y="{Y(0) + 14:.1f}" font-size="11" font-style="italic" '
              f'fill="#0f172a" text-anchor="end">{xnev}</text>')
    if len(ynev) > 1:
        # a hosszabb tengelynév a tengelytől JOBBRA fér el (balra kilógna a rajzterületről)
        ki.append(f'  <text x="{X(0) + 6:.1f}" y="{Y(y1) + 12:.1f}" font-size="11" '
                  f'font-style="italic" fill="#0f172a" text-anchor="start">{ynev}</text>')
    else:
        ki.append(f'  <text x="{X(0) - 8:.1f}" y="{Y(y1) + 12:.1f}" font-size="11" '
                  f'font-style="italic" fill="#0f172a" text-anchor="end">{ynev}</text>')
    if xegys:
        ki.append(f'  <text x="{X(1):.1f}" y="{Y(0) + 13:.1f}" font-size="10" fill="#475569" '
                  f'text-anchor="middle">{xegys}</text>')
    if yegys:
        # a hosszabb felirat a tengelytől JOBBRA kerül, különben kilóg a rajzterületről
        if len(yegys) > 2:
            ki.append(f'  <text x="{X(0) + 6:.1f}" y="{Y(1) - 4:.1f}" font-size="10" '
                      f'fill="#475569" text-anchor="start">{yegys}</text>')
        else:
            ki.append(f'  <text x="{X(0) - 5:.1f}" y="{Y(1) + 4:.1f}" font-size="10" '
                      f'fill="#475569" text-anchor="end">{yegys}</text>')
    # árnyékolt területek (a görbék alatt)
    for tr in (terulet or []):
        ff, gg, lo, hi, szin = tr[:5]
        op = tr[5] if len(tr) > 5 else 0.35
        n = 120
        fel, le = [], []
        for i in range(n + 1):
            xx = lo + (hi - lo) * i / n
            ya = min(max(ff(xx), y0), y1)
            yb = min(max(gg(xx) if gg else 0.0, y0), y1)
            fel.append(f"{X(xx):.1f},{Y(ya):.1f}")
            le.append(f"{X(xx):.1f},{Y(yb):.1f}")
        ki.append(f'  <polygon points="{" ".join(fel + le[::-1])}" fill="{szin}" fill-opacity="{op}" stroke="none"/>')
    # görbék
    for g in gorbek:
        f, szin, cimke, szakaszok = g[:4]
        szagg = len(g) > 4 and g[4]
        vonal = ('stroke-width="1.6" stroke-dasharray="6 4"' if szagg else 'stroke-width="2.1"')
        for lo, hi in szakaszok:
            pts = []
            n = 100
            for i in range(n + 1):
                x = lo + (hi - lo) * i / n
                try:
                    y = f(x)
                except (ZeroDivisionError, ValueError):
                    continue
                if y < y0 - 0.4 or y > y1 + 0.4:
                    continue
                pts.append(f"{X(x):.1f},{Y(y):.1f}")
            if len(pts) > 1:
                ki.append(f'  <polyline points="{" ".join(pts)}" fill="none" stroke="{szin}" '
                          f'{vonal} stroke-linecap="round" stroke-linejoin="round"/>')
    for pt in (pontok or []):
        px_, py_, felirat, szin = pt[0], pt[1], pt[2], pt[3]
        dx, dy = (pt[4] if len(pt) > 4 else 8), (pt[5] if len(pt) > 5 else -8)
        if szin.startswith("o:"):
            szin = szin[2:]
            ki.append(f'  <circle cx="{X(px_):.1f}" cy="{Y(py_):.1f}" r="4" fill="#ffffff" '
                      f'stroke="{szin}" stroke-width="1.8"/>')
        else:
            ki.append(f'  <circle cx="{X(px_):.1f}" cy="{Y(py_):.1f}" r="4" fill="{szin}"/>')
        if felirat:
            ki.append(f'  <text x="{X(px_) + dx:.1f}" y="{Y(py_) + dy:.1f}" font-size="11" '
                      f'fill="{szin}" font-weight="600">{felirat}</text>')
    if jelmagyarazat:
        ly = fent + 4
        szeles = 4 + max(len(g[2]) for g in gorbek) * 6.6 + 26
        bx = max(6, w - szeles - 6)          # a doboz mindig beleférjen a rajzterületbe
        ki.append(f'  <rect x="{bx:.0f}" y="{fent - 1}" width="{szeles:.0f}" '
                  f'height="{len(gorbek) * 17 + 6}" rx="4" fill="#ffffff" fill-opacity=".88"/>')
        for g in gorbek:
            f, szin, cimke = g[:3]
            da = ' stroke-dasharray="5 3"' if len(g) > 4 and g[4] else ''
            ki.append(f'  <line x1="{bx + 4:.0f}" y1="{ly + 4}" x2="{bx + 22:.0f}" y2="{ly + 4}" '
                      f'stroke="{szin}" stroke-width="2.4"{da}/>')
            ki.append(f'  <text x="{bx + 27:.0f}" y="{ly + 8}" font-size="11" '
                      f'fill="#0f172a">{cimke}</text>')
            ly += 17
    ki.append('</svg>')
    return "\n".join(ki)


def svg_egysegkor(szogek=(), w=340, h=340, leiras="A trigonometrikus kör",
                  negyedek=False, tengelycimke=True, sugar_cimke=None, extra="", iv=None,
                  vetulet=False):
    """Trigonometrikus (egység)kör sötét tintával, világos lapon.

    `szogek` = [(fok, felirat, szin), …] — sugár + pont + felirat a körvonalon.
    `negyedek` = True → I–IV római számok a negyedekben.
    `sugar_cimke` = pl. "r = 1" — felirat az első sugárra.
    `extra` = tetszőleges nyers SVG-részlet a végére (pl. tangensegyenes).
    `iv` = (fok, felirat, szin) — vastag körív a 0°-tól a megadott szögig, felirattal.
    `vetulet` = True → az ELSŐ szög pontjából szaggatott vetítővonal mindkét tengelyre,
    „cos α” és „sin α” felirattal, plusz az α szögív — ez maga a definíció.
    """
    import math
    cx, cy = w / 2, h / 2
    R = min(w, h) / 2 - 46

    def X(fok, r=1.0):
        return cx + R * r * math.cos(math.radians(fok))

    def Y(fok, r=1.0):
        return cy - R * r * math.sin(math.radians(fok))

    ki = [f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{leiras}">',
          '  <defs><marker id="nyilk" viewBox="0 0 8 8" refX="6" refY="4" markerWidth="6" '
          'markerHeight="6" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#0f172a"/></marker></defs>']
    # tengelyek
    ki.append(f'  <line x1="{cx - R - 26:.1f}" y1="{cy:.1f}" x2="{cx + R + 26:.1f}" y2="{cy:.1f}" '
              'stroke="#0f172a" stroke-width="1.3" marker-end="url(#nyilk)"/>')
    ki.append(f'  <line x1="{cx:.1f}" y1="{cy + R + 26:.1f}" x2="{cx:.1f}" y2="{cy - R - 26:.1f}" '
              'stroke="#0f172a" stroke-width="1.3" marker-end="url(#nyilk)"/>')
    # kör
    ki.append(f'  <circle cx="{cx:.1f}" cy="{cy:.1f}" r="{R:.1f}" fill="none" '
              'stroke="#334155" stroke-width="1.6"/>')
    if tengelycimke:
        ki.append(f'  <text x="{cx + R + 22:.1f}" y="{cy + 15:.1f}" font-size="11" '
                  'font-style="italic" fill="#0f172a" text-anchor="end">x</text>')
        ki.append(f'  <text x="{cx - 8:.1f}" y="{cy - R - 20:.1f}" font-size="11" '
                  'font-style="italic" fill="#0f172a" text-anchor="end">y</text>')
        for fok, txt, dx, dy in ((0, "1", 4, 14), (90, "1", -8, -6),
                                 (180, "−1", -4, 14), (270, "−1", -10, 12)):
            ki.append(f'  <text x="{X(fok) + dx:.1f}" y="{Y(fok) + dy:.1f}" font-size="10" '
                      f'fill="#475569" text-anchor="middle">{txt}</text>')
    if negyedek:
        for fok, txt in ((45, "I."), (135, "II."), (225, "III."), (315, "IV.")):
            ki.append(f'  <text x="{X(fok, 0.62):.1f}" y="{Y(fok, 0.62) + 4:.1f}" font-size="13" '
                      f'fill="#94a3b8" font-weight="700" text-anchor="middle">{txt}</text>')
    if iv:
        _f, _cim, _sz = iv
        _nagy = 1 if _f % 360 > 180 else 0
        ki.append(f'  <path d="M {X(0):.1f},{Y(0):.1f} A {R:.1f},{R:.1f} 0 {_nagy},0 '
                  f'{X(_f):.1f},{Y(_f):.1f}" fill="none" stroke="{_sz}" stroke-width="4" '
                  'stroke-linecap="round"/>')
        if _cim:
            ki.append(f'  <text x="{X(_f / 2, 1.09):.1f}" y="{Y(_f / 2, 1.09) + 4:.1f}" '
                      f'font-size="11" fill="{_sz}" font-weight="700" '
                      f'text-anchor="middle">{_cim}</text>')
    for i, (fok, felirat, szin) in enumerate(szogek):
        ki.append(f'  <line x1="{cx:.1f}" y1="{cy:.1f}" x2="{X(fok):.1f}" y2="{Y(fok):.1f}" '
                  f'stroke="{szin}" stroke-width="2"/>')
        ki.append(f'  <circle cx="{X(fok):.1f}" cy="{Y(fok):.1f}" r="4" fill="{szin}"/>')
        if felirat:
            r = 1.20
            anchor = "middle"
            ki.append(f'  <text x="{X(fok, r):.1f}" y="{Y(fok, r) + 4:.1f}" font-size="11" '
                      f'fill="{szin}" font-weight="600" text-anchor="{anchor}">{felirat}</text>')
        if i == 0 and sugar_cimke:
            ki.append(f'  <text x="{X(fok, 0.5):.1f}" y="{Y(fok, 0.5) - 6:.1f}" font-size="10" '
                      f'fill="{szin}" text-anchor="middle">{sugar_cimke}</text>')
    if vetulet and szogek:
        _f, _, _sz = szogek[0]
        px, py = X(_f), Y(_f)
        for x2, y2 in ((px, cy), (cx, py)):
            ki.append(f'  <line x1="{px:.1f}" y1="{py:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                      f'stroke="{_sz}" stroke-width="1.2" stroke-dasharray="4 3" '
                      'opacity=".8"/>')
        ki.append(f'  <text x="{px:.1f}" y="{cy + 17:.1f}" font-size="10" fill="{_sz}" '
                  'text-anchor="middle">cos α</text>')
        ki.append(f'  <text x="{cx - 7:.1f}" y="{py + 4:.1f}" font-size="10" fill="{_sz}" '
                  'text-anchor="end">sin α</text>')
        _r = 0.30
        ki.append(f'  <path d="M {X(0, _r):.1f},{Y(0, _r):.1f} A {R * _r:.1f},{R * _r:.1f} '
                  f'0 0,0 {X(_f, _r):.1f},{Y(_f, _r):.1f}" fill="none" stroke="#0f172a" '
                  'stroke-width="1.3"/>')
        ki.append(f'  <text x="{X(_f / 2, _r + 0.13):.1f}" y="{Y(_f / 2, _r + 0.13) + 4:.1f}" '
                  'font-size="11" fill="#0f172a" font-style="italic" '
                  'text-anchor="middle">α</text>')
    if extra:
        ki.append(extra)
    ki.append('</svg>')
    return "\n".join(ki)


# ------------------------------------------------------------------ interaktív ábra
_IV_SZAMLALO = [0]


def _poly(a, x):
    v = 0.0
    for c in reversed(a):
        v = v * x + c
    return v


def _poly_d(a):
    return [i * a[i] for i in range(1, len(a))] or [0.0]


def _fmt(v):
    r = round(v * 100) / 100
    if abs(r) < 0.005:
        r = 0.0
    s = str(int(round(r))) if abs(r - round(r)) < 1e-9 else f"{r:.2f}".rstrip("0")
    return s.replace(".", ",").replace("-", "−")


def _iv_ut(a, C, xr, yr, X, Y, n=160):
    """a polinom + C görbéje SVG-útvonalként; a rajzterületből kilógó szakaszoknál megszakad (JS: ut())"""
    d, lent = [], True
    for i in range(n + 1):
        x = xr[0] + (xr[1] - xr[0]) * i / n
        y = _poly(a, x) + C
        if yr[0] - 0.5 <= y <= yr[1] + 0.5:
            d.append(("M" if lent else "L") + f"{X(x):.1f},{Y(y):.1f}")
            lent = False
        else:
            lent = True
    return " ".join(d)


def _iv_teglalapok(a, ab, n, X, Y):
    """alsó és felső közelítő téglalapok (szakaszonként monoton f-re) — útvonalak és összegek (JS: teglak())"""
    lo_d, hi_d, lo_s, hi_s = [], [], 0.0, 0.0
    dx = (ab[1] - ab[0]) / n
    for i in range(n):
        xl, xr_ = ab[0] + i * dx, ab[0] + (i + 1) * dx
        fl, fr = _poly(a, xl), _poly(a, xr_)
        m, M = min(fl, fr), max(fl, fr)
        lo_s += m * dx; hi_s += M * dx
        lo_d.append(f"M{X(xl):.1f},{Y(0):.1f} V{Y(m):.1f} H{X(xr_):.1f} V{Y(0):.1f} Z")
        hi_d.append(f"M{X(xl):.1f},{Y(0):.1f} V{Y(M):.1f} H{X(xr_):.1f} V{Y(0):.1f} Z")
    return " ".join(lo_d), " ".join(hi_d), lo_s, hi_s


_IV_STATIKUS = ('<p class="iv-statikus">Az ábra kezdőállapotát látod. '
                'Az interaktív vezérléshez JavaScript szükséges.</p>\n')


def _iv_modell_keret(mod, svg, vezerlok, kijelzo, felirat, *, cap_id="", attr=""):
    """Címkézett vezérlők, közös visszaállítás és szöveges állapot az új szemléltetésekhez."""
    azon = f"iv-{mod}"
    leiras_id = cap_id or f"{azon}-leiras"
    svg = svg.replace('role="img"', f'role="img" aria-describedby="{azon}-kijelzo {leiras_id}"', 1)
    return (f'<div class="svgcard interaktiv iv-modell" data-mod="{mod}" {attr}>\n{svg}\n'
            + _IV_STATIKUS + vezerlok
            + '<div class="iv-vezerlo iv-gombsor"><button type="button" class="iv-alaphelyzet">'
              'Kezdőállapot</button></div>\n'
            + f'<p class="iv-kijelzo" id="{azon}-kijelzo" aria-live="polite" aria-atomic="true">{kijelzo}</p>\n'
            + f'<p class="cap iv-leiras" id="{leiras_id}">{felirat}</p>\n</div>\n'
            + '<script src="../../assets/js/interaktiv.js"></script>')


def svg_homotecia_interaktiv():
    """Az 1e meglévő homotécia-példája; az előjel és az arány nagysága külön állítható."""
    from abra_common import svg_homotecia
    vezerlok = ('<div class="iv-vezerlo"><label for="iv-homotecia-oldal">A kép helye</label>'
                '<select id="iv-homotecia-oldal" class="iv-homo-oldal" aria-describedby="iv-homotecia-kijelzo">'
                '<option value="1">Pozitív arány: azonos félegyenes</option>'
                '<option value="-1">Negatív arány: ellenkező félegyenes</option></select></div>\n'
                '<div class="iv-vezerlo"><label for="iv-homotecia-arany">$|k|$ = '
                '<span class="iv-homo-ertek">2</span></label>'
                '<input id="iv-homotecia-arany" class="iv-homo-arany" type="range" '
                'min="0.25" max="2.5" step="0.25" value="2" aria-valuetext="Az arány nagysága: 2" '
                'aria-describedby="iv-homotecia-kijelzo"></div>\n')
    return _iv_modell_keret('homotecia', svg_homotecia(), vezerlok,
        'A homotécia aránya 2. A képpontok a középpontból induló azonos félegyenesre kerülnek. '
        'A megfelelő oldalak és a kerületek aránya 2, a területek aránya 4.',
        'A kék $F$ az eredeti háromszög, a narancssárga, szaggatott $F_1$ a képe. '
        'Változtasd az arány nagyságát és előjelét! Figyeld az $A$ és $A_1$ pont helyét: '
        r'$OA_1 = |k|\cdot OA$. A szögek változatlanok; a hossz- és kerületarány $|k|$, a területarány $k^2$.',
        cap_id='abra-homotecia-es-hasonlosag-1')


def _iv_exp_ut(alap, xr, yr, w, h):
    """Az exponenciális görbe látható része; a felső határnál pontosan vágjuk el."""
    import math
    bal, jobb, fent, lent = 26, 12, 14, 22
    lo, hi = xr
    felso_x = math.log(yr[1]) / math.log(alap)
    if alap > 1:
        hi = min(hi, felso_x)
    else:
        lo = max(lo, felso_x)
    pontok = []
    for i in range(161):
        x = lo + (hi-lo) * i/160
        y = alap ** x
        X = bal + (x-xr[0])/(xr[1]-xr[0]) * (w-bal-jobb)
        Y = fent + (yr[1]-y)/(yr[1]-yr[0]) * (h-fent-lent)
        pontok.append(f'{"M" if i == 0 else "L"}{X:.2f},{Y:.2f}')
    return ' '.join(pontok)


def svg_exponencialis_interaktiv():
    """Változtatható alapú alapgrafikon: a > 0, a ≠ 1, eltolás nélkül."""
    xr, yr, w, h = (-3.4, 3.4), (-0.4, 5), 440, 280
    svg = svg_fuggvenyek([], xr=xr, yr=yr, w=w, h=h, jelmagyarazat=False,
        leiras='Az y = aˣ exponenciális függvény alapgrafikonja, kezdetben a = 2',
        pontok=[(0, 1, '(0; 1)', '#0f172a', 8, 16)])
    rajz = ('<defs><clipPath id="iv-exp-clip"><rect x="26" y="14" width="402" height="244"/>'
            '</clipPath></defs>\n'
            f'<path class="iv-exp-gorbe" d="{_iv_exp_ut(2, xr, yr, w, h)}" fill="none" '
            'stroke="#047857" stroke-width="2.5" clip-path="url(#iv-exp-clip)"/>\n'
            '<text class="iv-exp-cimke" x="414" y="35" font-size="14" text-anchor="end" '
            'fill="#0f172a">y = 2ˣ</text>\n')
    svg = svg.replace('</svg>', rajz + '</svg>')
    vezerlok = ('<div class="iv-vezerlo"><label for="iv-exponencialis-tipus">Alaptartomány</label>'
                '<select id="iv-exponencialis-tipus" class="iv-exp-tipus" aria-describedby="iv-exponencialis-kijelzo">'
                '<option value="no">Növekvő: 1-nél nagyobb alap</option>'
                '<option value="csokken">Csökkenő: 0 és 1 közötti alap</option></select></div>\n'
                '<div class="iv-vezerlo"><label for="iv-exponencialis-alap">$a$ = '
                '<span class="iv-exp-ertek">2</span></label>'
                '<input id="iv-exponencialis-alap" class="iv-exp-alap" type="range" min="101" max="500" '
                'step="1" value="200" aria-valuetext="Az exponenciális függvény alapja: 2" '
                'aria-describedby="iv-exponencialis-kijelzo"></div>\n')
    return _iv_modell_keret('exponencialis', svg, vezerlok,
        'Az alap 2: a függvény szigorúan növekvő. Az értéke −1-nél közelítőleg 0,5; 0-nál 1; 1-nél 2.',
        'Válassz alaptartományt, majd változtasd az $a$ alapot! Minden görbe átmegy a $(0; 1)$ ponton. '
        'Figyeld, melyik irányban nőnek az értékek! A görbe mindig az $x$-tengely fölött halad; '
        'a rajz csak a megjelenített ablakba eső részét mutatja.',
        attr=f'data-xr="{xr[0]},{xr[1]}" data-yr="{yr[0]},{yr[1]}" data-w="{w}" data-h="{h}"')


def svg_sorozat_interaktiv():
    """A meglévő aₙ = 2 + 1/n példa; a sáv nyílt, a besorolás egész számokkal pontos."""
    w, h, db, szazad = 480, 270, 12, 30
    xr, yr = (0, db+1), (0, 3.4)
    X = lambda n: 26 + n/(db+1) * (w-38)
    Y = lambda y: 14 + (yr[1]-y)/yr[1] * (h-36)
    svg = svg_fuggvenyek([], xr=xr, yr=yr, w=w, h=h, jelmagyarazat=False,
        tengely=('n', 'aₙ'), egyseg=('', '1'),
        leiras='Az aₙ = 2 + 1/n sorozat: pontok és a 2 körüli nyílt sáv')
    # A függőleges rácsot a tagszám változásával együtt rajzolja újra a közös JS.
    racs = '<g class="iv-sor-racs">'
    for y in range(1, 4):
        racs += f'<line x1="26" y1="{Y(y):.2f}" x2="{w-12}" y2="{Y(y):.2f}" stroke="#cbd5e1" stroke-width=".6"/>'
    for n in range(2, db+1, 2):
        racs += f'<line x1="{X(n):.2f}" y1="14" x2="{X(n):.2f}" y2="{Y(0):.2f}" stroke="#cbd5e1" stroke-width=".6"/>'
    racs += '</g>'
    svg = re.sub(r'<g stroke="#cbd5e1".*?</g>', racs, svg, count=1, flags=re.S)
    svg = re.sub(r'<text[^>]*>n</text>', f'<text x="{w-16}" y="{Y(0)-6:.1f}" '
                 'font-size="11" font-style="italic" fill="#0f172a" text-anchor="end">n</text>', svg, count=1)
    band = ('<rect class="iv-sor-sav" x="26" '
            f'y="{Y(2.3):.2f}" width="{w-38}" height="{Y(1.7)-Y(2.3):.2f}" '
            'fill="#10b981" fill-opacity=".16"/>\n')
    for y, cls in [(1.7, 'iv-sor-also'), (2.3, 'iv-sor-felso'), (2, 'iv-sor-cel')]:
        band += (f'<line class="{cls}" x1="26" y1="{Y(y):.2f}" x2="{w-12}" y2="{Y(y):.2f}" '
                 'stroke="#047857" stroke-width="1.3" stroke-dasharray="5 4"/>\n')
    band += (f'<text x="{w-18}" y="{Y(2)+16:.2f}" font-size="13" text-anchor="end" fill="#065f46">A = 2</text>\n'
             '<g class="iv-sor-pontok">')
    for n in range(1, db+1):
        belul = n*szazad > 100
        band += (f'<circle data-n="{n}" data-hely="{"belul" if belul else "kivul"}" '
                 f'cx="{X(n):.2f}" cy="{Y(2+1/n):.2f}" r="4" '
                 f'fill="{"#047857" if belul else "#dc2626"}"/>')
    band += '</g>\n<g class="iv-sor-tengely">'
    for n in range(2, db+1, 2):
        band += f'<text x="{X(n):.2f}" y="{Y(0)+14:.2f}" font-size="11" fill="#475569" text-anchor="middle">{n}</text>'
    band += '</g>\n'
    svg = svg.replace('</svg>', band + '</svg>')
    vezerlok = (r'<div class="iv-vezerlo"><label for="iv-sorozat-sav">$\varepsilon$ = '
                '<span class="iv-sor-eps">0,3</span></label>'
                '<input id="iv-sorozat-sav" class="iv-sor-szelesseg" type="range" min="5" max="50" '
                'step="5" value="30" aria-valuetext="A sáv félszélessége: 0,3" '
                'aria-describedby="iv-sorozat-kijelzo"></div>\n'
                '<div class="iv-vezerlo"><label for="iv-sorozat-tagszam">Látható tagok: '
                '<span class="iv-sor-db">12</span></label>'
                '<input id="iv-sorozat-tagszam" class="iv-sor-tagszam" type="range" min="12" max="60" '
                'step="1" value="12" aria-describedby="iv-sorozat-kijelzo"></div>\n')
    return _iv_modell_keret('sorozat', svg, vezerlok,
        'A sáv félszélessége 0,3: a nyílt sáv 1,7 és 2,3 között van. A 4. tagtól kezdve minden további tag benne van. '
        'Az első 12 tagból 9 belül, 3 kívül van; határra eső tag nincs.',
        r'A sorozat $a_n = 2 + \frac1n$. Szűkítsd a $2$ körüli sávot, és figyeld, hányadik tagtól kerül '
        'minden további tag belülre! Zöld, teli pont: belül; piros, teli pont: kívül; '
        'narancssárga, üres pont: a határon. A sáv széle nem tartozik bele.',
        attr=f'data-w="{w}" data-h="{h}" data-yr="{yr[0]},{yr[1]}"')


def svg_interaktiv(mod, poly, *, xr, yr, x0=0.0, csuszka=(-2.0, 2.0, 0.01, 1.0), w=360, h=250,
                   gorbe_cimke="f", f2=False, felirat="", leiras="Interaktív függvényábra",
                   pont_cimke="P", szin="#2563eb", ab=(0.0, 1.0), pontos="", sereg_c=(-2, -1, 1, 2)):
    """Interaktív ábra (új kánon, 2026-09-24): statikus SVG = az első képkocka + csúszka + élő kijelző.

    `mod`: "szelo" (rögzített P, a csúszka Δx-et állít), "erinto" (a csúszka x0-t mozgatja), "sereg" (a `poly` egy
    primitív függvény, a csúszka a C-t állítja; érintő az x0-ban — a meredekség nem függ C-től) vagy "osszeg"
    (a `poly` az f, az `ab` intervallumon n téglalapos alsó és felső közelítő összeg; `pontos` a pontos érték szövege).
    `poly` = [a0, a1, a2, …] — a polinom együtthatói (a0 + a1·x + …); a JS nem használ eval-t.
    `csuszka` = (min, max, lépés, kezdőérték). A logikát az `assets/js/interaktiv.js` adja (közös modul).
    A kezdőállapotot itt, Pythonban számoljuk ugyanúgy, mint a JS — JS nélkül is értelmes kép.
    """
    _IV_SZAMLALO[0] += 1
    n = _IV_SZAMLALO[0]
    a = [float(c) for c in poly]
    d1 = _poly_d(a)
    d2 = _poly_d(d1)
    lo, hi, lepes, kezdo = csuszka
    bal, jobb, fent, lent = 26, 12, 14, 22
    px, py = w - bal - jobb, h - fent - lent

    def X(x):
        return bal + (x - xr[0]) / (xr[1] - xr[0]) * px

    def Y(y):
        return fent + (yr[1] - y) / (yr[1] - yr[0]) * py

    if mod == "sereg":
        tagok = [(lambda t, c=c: _poly(a, t) + c, "#94a3b8", "", [(xr[0], xr[1])]) for c in sereg_c]
        alap = svg_fuggvenyek(tagok, xr=xr, yr=yr, w=w, h=h, jelmagyarazat=False, leiras=leiras)
    else:
        alap = svg_fuggvenyek([(lambda t: _poly(a, t), "#0f172a", gorbe_cimke, [(xr[0], xr[1])])],
                              xr=xr, yr=yr, w=w, h=h, jelmagyarazat=False, leiras=leiras)
    clip = f"ivc{n}"
    ki = [f'  <defs><clipPath id="{clip}"><rect x="{bal}" y="{fent}" width="{px}" height="{py}"/></clipPath></defs>']

    def egyenes_attr(xa, ya, m):
        return (f'x1="{X(xr[0]):.1f}" y1="{Y(ya + m * (xr[0] - xa)):.1f}" '
                f'x2="{X(xr[1]):.1f}" y2="{Y(ya + m * (xr[1] - xa)):.1f}"')

    if mod == "szelo":
        yP = _poly(a, x0)
        m0 = _poly(d1, x0)
        xQ = x0 + kezdo
        yQ = _poly(a, xQ)
        m = (yQ - yP) / kezdo
        ki.append(f'  <line class="iv-erinto-halvany" {egyenes_attr(x0, yP, m0)} stroke="#047857" '
                  f'stroke-width="1.3" stroke-dasharray="5 4" opacity=".7" clip-path="url(#{clip})"/>')
        ki.append(f'  <line class="iv-egyenes" {egyenes_attr(x0, yP, m)} stroke="{szin}" stroke-width="2" '
                  f'clip-path="url(#{clip})"/>')
        ki.append(f'  <circle class="iv-Q" cx="{X(xQ):.1f}" cy="{Y(yQ):.1f}" r="4.5" fill="{szin}"/>')
        ki.append(f'  <text class="iv-Q-cimke" x="{X(xQ) + 7:.1f}" y="{Y(yQ) - 7:.1f}" font-size="12" '
                  f'font-weight="600" fill="{szin}">Q</text>')
        ki.append(f'  <circle class="iv-P" cx="{X(x0):.1f}" cy="{Y(yP):.1f}" r="4.5" fill="#0f172a"/>')
        ki.append(f'  <text x="{X(x0) - 16:.1f}" y="{Y(yP) - 8:.1f}" font-size="12" font-weight="600" '
                  f'fill="#0f172a">{pont_cimke}</text>')
        cimke = "Δx"
        kijelzo = (f"Δx = {_fmt(kezdo)},  Δy = {_fmt(yQ - yP)},  a szelő meredeksége Δy/Δx = {_fmt(m)}.")
    elif mod == "sereg":
        C = kezdo
        m1 = _poly(d1, x0)
        ki.append(f'  <path class="iv-gorbe" d="{_iv_ut(a, C, xr, yr, X, Y)}" fill="none" stroke="#0f172a" '
                  f'stroke-width="2.3" stroke-linejoin="round" clip-path="url(#{clip})"/>')
        ki.append(f'  <line class="iv-egyenes" {egyenes_attr(x0, _poly(a, x0) + C, m1)} stroke="#047857" '
                  f'stroke-width="2" clip-path="url(#{clip})"/>')
        ki.append(f'  <circle class="iv-P" cx="{X(x0):.1f}" cy="{Y(_poly(a, x0) + C):.1f}" r="4.5" fill="#0f172a"/>')
        cimke = "C"
        kijelzo = (f"C = {_fmt(C)}:  az x₀ = {_fmt(x0)} helyen az érintő meredeksége {_fmt(m1)} — "
                   f"minden C-re ugyanannyi, mert (F + C)′ = F′ = f.")
    elif mod == "osszeg":
        nn = int(kezdo)
        lo_d, hi_d, lo_s, hi_s = _iv_teglalapok(a, ab, nn, X, Y)
        felso = (f'  <path class="iv-felso" d="{hi_d}" fill="#bfdbfe" fill-opacity=".75" stroke="#3b82f6" '
                 f'stroke-width=".8" clip-path="url(#{clip})"/>')
        also = (f'  <path class="iv-also" d="{lo_d}" fill="#2563eb" fill-opacity=".55" stroke="#1d4ed8" '
                f'stroke-width=".8" clip-path="url(#{clip})"/>')
        alap = alap.replace('  <polyline', felso + "\n" + also + "\n  <polyline", 1)
        cimke = "n"
        kijelzo = (f"n = {nn}:  alsó összeg ≈ {_fmt(lo_s)},  felső összeg ≈ {_fmt(hi_s)};  "
                   f"a pontos terület: {pontos}.")
    else:
        y0 = _poly(a, kezdo)
        m1 = _poly(d1, kezdo)
        m2 = _poly(d2, kezdo)
        sz = "#047857" if m1 > 0.01 else ("#dc2626" if m1 < -0.01 else "#64748b")
        ki.append(f'  <line class="iv-egyenes" {egyenes_attr(kezdo, y0, m1)} stroke="{sz}" stroke-width="2" '
                  f'clip-path="url(#{clip})"/>')
        ki.append(f'  <circle class="iv-P" cx="{X(kezdo):.1f}" cy="{Y(y0):.1f}" r="4.5" fill="#0f172a"/>')
        cimke = "x₀"
        mon = ("pozitív → itt a függvény nő" if m1 > 0.01 else
               "negatív → itt a függvény csökken" if m1 < -0.01 else "0 → vízszintes érintő (stacionárius hely)")
        kijelzo = f"x₀ = {_fmt(kezdo)}:  f′(x₀) = {_fmt(m1)}, {mon}."
        if f2:
            gorb = ("pozitív → konvex (∪), a görbe az érintő fölött van" if m2 > 0.01 else
                    "negatív → konkáv (∩), a görbe az érintő alatt van" if m2 < -0.01 else
                    "0 → itt válthat a görbülés (inflexió?)")
            kijelzo += f"  f″(x₀) = {_fmt(m2)}, {gorb}."
    svg = alap.replace("</svg>", "\n".join(ki) + "\n</svg>")
    attr = (f'data-mod="{mod}" data-poly="{",".join(repr(c) for c in a)}" data-xr="{xr[0]},{xr[1]}" '
            f'data-yr="{yr[0]},{yr[1]}" data-w="{w}" data-h="{h}" data-x0="{x0}"' + (' data-f2="1"' if f2 else "")
            + (f' data-ab="{ab[0]},{ab[1]}" data-pontos="{pontos}"' if mod == "osszeg" else ""))
    cap = f'\n<p class="cap">{felirat}</p>' if felirat else ""
    return (f'<div class="svgcard interaktiv" {attr}>\n{svg}\n' + _IV_STATIKUS +
            f'<div class="iv-vezerlo"><label for="iv{n}">{cimke} = <span class="iv-ertek">{_fmt(kezdo)}</span></label>'
            f'<input type="range" id="iv{n}" min="{lo}" max="{hi}" step="{lepes}" value="{kezdo}" '
            f'aria-describedby="ivk{n}"></div>\n'
            f'<p class="iv-kijelzo" id="ivk{n}" aria-live="polite">{kijelzo}</p>\n</div>{cap}\n'
            f'<script src="../../assets/js/interaktiv.js"></script>')


# ------------------------------------------------------------------ interaktív Pascal-háromszög (2026-09-26)
_FELSO = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")


def pascal_kifejtes(n):
    """(a + b)^n kifejtése Unicode-felső indexekkel — ugyanezt írja az interaktiv.js `pascal` módja."""
    from math import comb as _c
    tagok = []
    for k in range(n + 1):
        c, ea, eb = _c(n, k), n - k, k
        t = "" if (c == 1 and (ea or eb)) else str(c)
        if ea:
            t += "a" + (str(ea).translate(_FELSO) if ea > 1 else "")
        if eb:
            t += "b" + (str(eb).translate(_FELSO) if eb > 1 else "")
        tagok.append(t)
    return " + ".join(tagok)


def pascal_szoveg(n):
    return (f"n = {n}:  (a + b){str(n).translate(_FELSO)} = {pascal_kifejtes(n)};  "
            f"a sor összege {2 ** n} = 2{str(n).translate(_FELSO)}.")


def svg_pascal(n_max=7, kezdo=4, w=380, h=252, felirat="", leiras="Interaktív Pascal-háromszög"):
    """Interaktív Pascal-háromszög (`data-mod="pascal"`): a 0…n_max. sor, a csúszka az n-edik sort emeli ki, a
    kijelző az (a + b)^n kifejtését és a sorösszeget írja. A statikus SVG = a `kezdo` sor kiemelve (JS nélkül is jó)."""
    from math import comb as _c
    _IV_SZAMLALO[0] += 1
    nn = _IV_SZAMLALO[0]
    dx, dy, r0, y0 = 44, 28.5, 13, 22
    ki = [f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{leiras}" '
          f'xmlns="http://www.w3.org/2000/svg" font-family="Inter, system-ui, sans-serif">']
    for r in range(n_max + 1):
        ki.append(f'  <g class="iv-psor" data-n="{r}">')
        cy = y0 + r * dy
        ki.append(f'    <text x="10" y="{cy + 4:.1f}" font-size="10.5" fill="#64748b">{r}.</text>')
        for k in range(r + 1):
            cx = w / 2 + (k - r / 2) * dx
            ki_ = r == kezdo
            ki.append(f'    <circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r0}" fill="{"#2563eb" if ki_ else "#ffffff"}" '
                      f'stroke="{"#1d4ed8" if ki_ else "#94a3b8"}" stroke-width="1.2"/>')
            ki.append(f'    <text x="{cx:.1f}" y="{cy + 4.2:.1f}" text-anchor="middle" font-size="12.5" '
                      f'font-weight="600" fill="{"#ffffff" if ki_ else "#0f172a"}">{_c(r, k)}</text>')
        ki.append('  </g>')
    ki.append('</svg>')
    cap = f'\n<p class="cap">{felirat}</p>' if felirat else ""
    return (f'<div class="svgcard interaktiv" data-mod="pascal" data-nmax="{n_max}">\n' + "\n".join(ki) + '\n' + _IV_STATIKUS +
            f'<div class="iv-vezerlo"><label for="iv{nn}">n = <span class="iv-ertek">{kezdo}</span></label>'
            f'<input type="range" id="iv{nn}" min="0" max="{n_max}" step="1" value="{kezdo}" '
            f'aria-describedby="ivk{nn}"></div>\n'
            f'<p class="iv-kijelzo" id="ivk{nn}" aria-live="polite">{pascal_szoveg(kezdo)}</p>\n</div>{cap}\n'
            f'<script src="../../assets/js/interaktiv.js"></script>')


# ------------------------------------------------------------------ oldalváz

VAZ = """<!DOCTYPE html>
<html lang="hu" data-root="../..">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{itt} | {tagozat} | Szvetkó matek</title>
<link rel="icon" href="../../assets/img/common/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../../assets/css/theme.css">
<link rel="stylesheet" href="../../assets/css/print.css">
<link rel="stylesheet" href="../../assets/katex/katex.min.css">
</head>
<body data-tagozat="{tagozat}" data-hatter="altalanos">
<div id="progress"></div>
<header class="fejlec">
  <div class="fejlec-bel">
    <a class="logo" href="../../index.html"><span class="jel">√</span><span class="nev">Szvetkó <b>matek</b></span></a>
    <span class="ter"></span>
    <form class="kereso-mini"><input type="search" placeholder="Keresés…" aria-label="Keresés az oldalon"><button type="submit">Keres</button></form>
  </div>
</header>
<nav class="morzsa">
  <a href="../../index.html">Főhadiszállás</a> ›
  <a href="../index.html"><span class="tagozat-jel">{tagozat}</span></a> ›
  <a href="index.html">{temakor}</a> ›
  <span class="itt">{itt}</span>
</nav>
<div class="hero">
  <h1>{cim}</h1>
  <p class="alcim">{alcim}</p>
  <div class="meta-sor"><span class="chip ora">{chip_tipus}</span><span class="chip">{chip}</span></div>
</div>
<main class="lap toc-os">
  <div class="tartalom">
{torzs}
    <div class="lapozo">
      <a class="elozo" href="{elozo_href}"><span class="irany">← Előző</span><span class="hova">{elozo_cim}</span></a>
      <a class="kov" href="{kov_href}"><span class="irany">Következő →</span><span class="hova">{kov_cim}</span></a>
    </div>
  </div>
  <nav class="toc" id="toc" aria-label="Tartalomjegyzék"></nav>
</main>
<footer class="lablec">
  <div class="lablec-bel">
    <span><b>Szvetkó matek</b> · Nagygyörgy Kristóf — Svetozar Marković Gimnázium, Szabadka</span>
    <span>Legyél szvetkós!</span>
  </div>
</footer>
<script src="../../assets/katex/katex.min.js"></script>
<script src="../../assets/katex/auto-render.min.js"></script>
<script>
  renderMathInElement(document.body, {{delimiters:[
    {{left:'\\\\(', right:'\\\\)', display:false}},
    {{left:'\\\\[', right:'\\\\]', display:true}}
  ]}});
</script>
<script src="../../assets/js/ui.js"></script>
<script src="../../assets/js/quiz.js"></script>
</body>
</html>
"""


def lap(*, tagozat: str, mappa: str, fajl: str, temakor: str, cim: str, cim_tiszta: str | None = None,
        alcim: str, chip: str, szakaszok: list, elozo: tuple, kovetkezo: tuple,
        chip_tipus: str = "tananyag", itt: str | None = None) -> str:
    """Egy tananyag-egység HTML-je. `szakaszok` = [(h2_cim, [blokk, …]), …].

    Az első szakasz címe a KÁNON szerint mindig „📡 Küldetés-eligazítás" (id=s0).
    """
    reszek = []
    for i, (h2, blokkok) in enumerate(szakaszok):
        # A h2 cím IS átmegy a mat()-on: különben a címben lévő $…$ nyersen jelenik
        # meg (a diák dollárjeleket lát), és a TOC-ban duplán is. 2026-08-06-ig hiányzott.
        reszek.append(f'    <h2 id="s{i}">{mat(h2)}</h2>')
        for b in blokkok:
            reszek.append("    " + mat(b).replace("\n", "\n    "))
    torzs = "\n\n".join(reszek)

    html = VAZ.format(
        tagozat=tagozat, temakor=temakor, cim=mat(cim),
        cim_tiszta=cim_tiszta or cim, itt=itt or f"{cim_tiszta or cim} — tananyag",
        alcim=mat(alcim), chip=chip, chip_tipus=chip_tipus, torzs=torzs,
        elozo_href=elozo[0], elozo_cim=elozo[1], kov_href=kovetkezo[0], kov_cim=kovetkezo[1])

    ut = os.path.join(GYOKER, tagozat, mappa, fajl)
    os.makedirs(os.path.dirname(ut), exist_ok=True)
    with open(ut, "w", encoding="utf-8") as f:
        f.write(egyedi_idk(tablak_gorgethetok(html)))
    return ut
