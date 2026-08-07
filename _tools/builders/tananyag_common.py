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


def kviz(kerdes: str, opciok: list[str], jo_idx: int = 0, jo: str = "", nem: str = "") -> str:
    """Gyors kérdés. FONTOS: a `jo_idx` a `opciok` lista 0-alapú indexe."""
    gombok = "".join(f"<button>{o}</button>" for o in opciok)
    extra = ""
    if jo:
        extra += f' data-jo="{jo}"'
    if nem:
        extra += f' data-nem="{nem}"'
    return (f'<div class="kviz" data-answer="{jo_idx}"{extra}>\n'
            f'  <p class="kviz-cim">🎯 Gyors kérdés</p>\n'
            f'  <p>{kerdes}</p>\n'
            f'  <div class="opciok">{gombok}</div>\n'
            f'  <p class="visszajelzes" aria-live="polite"></p>\n'
            f'</div>')


def gyakorolj(konnyu_href: str, konnyu_cimke: str, normal_href: str, normal_cimke: str,
              bevezeto: str = "Válaszd a bevetésed:") -> str:
    """Differenciált sávok — 2e köntös: 🐾 Bestia-protokoll / 🔥 Főnix-protokoll."""
    return ('<div class="gyakorolj"><span class="ikon">🎯</span><div>'
            f'<p><b>Gyakorolj!</b> {bevezeto}</p><div class="savok">'
            f'<a class="sav henrik" href="{konnyu_href}">🐾 Bestia-protokoll <span class="cimke">{konnyu_cimke}</span></a>'
            f'<a class="sav bruno" href="{normal_href}">🔥 Főnix-protokoll <span class="cimke">{normal_cimke}</span></a>'
            '</div></div></div>')


def abra(svg: str, felirat: str = "") -> str:
    cap = f'\n<p class="cap">{felirat}</p>' if felirat else ""
    return f'<div class="svgcard">\n{svg.strip()}\n</div>{cap}'


def svg_fuggvenyek(gorbek, xr=(-2.6, 2.6), yr=(-2.6, 4.2), w=360, h=250,
                   leiras="Függvénygrafikonok koordináta-rendszerben", jelmagyarazat=True,
                   pontok=None):
    """`pontok` = [(x, y, felirat, szin, dx, dy), …] — kiemelt pontok felirattal."""
    """Koordináta-rendszer + görbék inline SVG-ként, SÖTÉT tintával, világos lapon.

    `gorbek` = [(f, szin, cimke, [(lo, hi), …] szakaszok), …]
    A y-értékeket a rajzterületre vágjuk (a pólusok nem lógnak ki).
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
    ki.append(f'  <text x="{X(x1) - 4:.1f}" y="{Y(0) + 14:.1f}" font-size="11" font-style="italic" '
              'fill="#0f172a" text-anchor="end">x</text>')
    ki.append(f'  <text x="{X(0) - 8:.1f}" y="{Y(y1) + 12:.1f}" font-size="11" font-style="italic" '
              'fill="#0f172a" text-anchor="end">y</text>')
    ki.append(f'  <text x="{X(1):.1f}" y="{Y(0) + 13:.1f}" font-size="10" fill="#475569" '
              'text-anchor="middle">1</text>')
    ki.append(f'  <text x="{X(0) - 5:.1f}" y="{Y(1) + 4:.1f}" font-size="10" fill="#475569" '
              'text-anchor="end">1</text>')
    # görbék
    for f, szin, cimke, szakaszok in gorbek:
        for lo, hi in szakaszok:
            pts = []
            n = 100
            for i in range(n + 1):
                x = lo + (hi - lo) * i / n
                try:
                    y = f(x)
                except ZeroDivisionError:
                    continue
                if y < y0 - 0.4 or y > y1 + 0.4:
                    continue
                pts.append(f"{X(x):.1f},{Y(y):.1f}")
            if len(pts) > 1:
                ki.append(f'  <polyline points="{" ".join(pts)}" fill="none" stroke="{szin}" '
                          'stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/>')
    for pt in (pontok or []):
        px_, py_, felirat, szin = pt[0], pt[1], pt[2], pt[3]
        dx, dy = (pt[4] if len(pt) > 4 else 8), (pt[5] if len(pt) > 5 else -8)
        ki.append(f'  <circle cx="{X(px_):.1f}" cy="{Y(py_):.1f}" r="4" fill="{szin}"/>')
        if felirat:
            ki.append(f'  <text x="{X(px_) + dx:.1f}" y="{Y(py_) + dy:.1f}" font-size="11" '
                      f'fill="{szin}" font-weight="600">{felirat}</text>')
    if jelmagyarazat:
        ly = fent + 4
        szeles = 4 + max(len(c) for _, _, c, _ in gorbek) * 6.6 + 26
        bx = max(6, w - szeles - 6)          # a doboz mindig beleférjen a rajzterületbe
        ki.append(f'  <rect x="{bx:.0f}" y="{fent - 1}" width="{szeles:.0f}" '
                  f'height="{len(gorbek) * 17 + 6}" rx="4" fill="#ffffff" fill-opacity=".88"/>')
        for f, szin, cimke, _ in gorbek:
            ki.append(f'  <line x1="{bx + 4:.0f}" y1="{ly + 4}" x2="{bx + 22:.0f}" y2="{ly + 4}" '
                      f'stroke="{szin}" stroke-width="2.4"/>')
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
        f.write(html)
    return ut
