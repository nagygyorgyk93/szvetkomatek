# -*- coding: utf-8 -*-
"""
Matematikai ábra-generátorok a Szvetkó matek oldalhoz — inline SVG.

A `tananyag_common.py`-ban már ott van két generátor (`svg_fuggvenyek`,
`svg_egysegkor`, 40 oldalon használva) — azok maradnak a helyükön, hogy a meglévő
builderek ne törjenek el. Ez a modul a HIÁNYZÓ, visszatérő ábratípusokat adja.

KÁNON (a `_WEBOLDAL_workflow.md` 4c. pontja): az oldal sötét témájú, de az ábra
„tervrajz-lapja" világos (`.svgcard`, `.venn .vbox`, `.svgwrap>svg`), ezért minden SVG
**sötét tintával, világos lapon** rajzol. Minden ábra kap `role="img"` és `aria-label`
attribútumot. A méretek `viewBox`-osak, tehát reszponzívak.

Használat a builderben:

    from abra_common import svg_szamegyenes, svg_haromszog, svg_venn
    from tananyag_common import abra

    ki.append(abra(svg_szamegyenes(intervallumok=[(-1, 3, "zart", "nyilt")]),
                   "A megoldáshalmaz a számegyenesen"))
"""

from __future__ import annotations

import math

TINTA = "#0f172a"
HALVANY = "#cbd5e1"
SZURKE = "#475569"
ZOLD = "#047857"
KEK = "#3b82f6"
BOROSTYAN = "#f59e0b"
PIROS = "#ef4444"
LILA = "#8b5cf6"

__all__ = ["svg_szamegyenes", "svg_haromszog", "svg_venn",
           "svg_parhuzamosok", "svg_sokszog_szogek",
           "svg_hasab", "svg_gula", "svg_csonkagula", "svg_haztest",
           "svg_terelem", "svg_halo", "svg_platoni", "svg_sikidom",
           "svg_henger", "svg_kup", "svg_csonkakup", "svg_gomb",
           "svg_forgatas", "svg_osszetett"]


def _fej(w: int, h: int, leiras: str) -> list[str]:
    return [f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
            f'aria-label="{leiras}">',
            '  <defs><marker id="nyil" viewBox="0 0 8 8" refX="6" refY="4" '
            'markerWidth="6" markerHeight="6" orient="auto">'
            f'<path d="M0,0 L8,4 L0,8 z" fill="{TINTA}"/></marker></defs>']


# =====================================================================
# 1. Számegyenes — pontok, intervallumok, egyenlőtlenségek
# =====================================================================

def svg_szamegyenes(xr=(-4, 4), pontok=None, intervallumok=None, w=520, h=96,
                    leiras="Számegyenes", lepes=1, cimkek=None):
    """Számegyenes intervallumokkal és kiemelt pontokkal.

    `pontok` = [(x, felirat, szin), …]
    `intervallumok` = [(a, b, a_tipus, b_tipus, szin?), …] ahol a típus
        `"zart"` (tömör kör, ≤/≥) vagy `"nyilt"` (üres kör, </>).
        A `-inf` / `inf` végpont nyílban végződik.
    `cimkek` = {x: "felirat"} — saját feliratok az osztásokra (pl. törtek, π).

    MIÉRT kell: egyenlőtlenség, abszolút érték, értelmezési tartomány és
    megoldáshalmaz mind számegyenesen a legérthetőbb — ez a leggyakoribb ábra,
    amit eddig kézzel kellett volna rajzolni.
    """
    pontok = pontok or []
    intervallumok = intervallumok or []
    cimkek = cimkek or {}
    x0, x1 = xr
    bal, jobb = 26, 26
    px = w - bal - jobb
    yv = h - 40                                    # a vonal magassága

    def X(x):
        x = max(x0, min(x1, x))
        return bal + (x - x0) / (x1 - x0) * px

    ki = _fej(w, h, leiras)
    # a tengely mindkét végén nyíl
    ki.append(f'  <line x1="{bal - 12}" y1="{yv}" x2="{w - jobb + 12}" y2="{yv}" '
              f'stroke="{TINTA}" stroke-width="1.4" marker-end="url(#nyil)"/>')

    # osztások
    t = math.ceil(x0)
    while t <= x1:
        x = X(t)
        ki.append(f'  <line x1="{x:.1f}" y1="{yv - 5}" x2="{x:.1f}" y2="{yv + 5}" '
                  f'stroke="{TINTA}" stroke-width="1"/>')
        # tipográfiai mínusz (U+2212), nem ASCII kötőjel
        felirat = cimkek.get(t, str(t).replace("-", "\u2212"))
        if t % lepes == 0 or t in cimkek:
            ki.append(f'  <text x="{x:.1f}" y="{yv + 20}" font-size="11" fill="{SZURKE}" '
                      f'text-anchor="middle">{felirat}</text>')
        t += 1

    # intervallumok — a vonal fölött, hogy ne fedje az osztásokat
    for i, iv in enumerate(intervallumok):
        a, b = iv[0], iv[1]
        a_tip = iv[2] if len(iv) > 2 else "zart"
        b_tip = iv[3] if len(iv) > 3 else "zart"
        szin = iv[4] if len(iv) > 4 else ZOLD
        y = yv - 14 - i * 13
        xa, xb = X(a), X(b)
        ki.append(f'  <line x1="{xa:.1f}" y1="{y}" x2="{xb:.1f}" y2="{y}" '
                  f'stroke="{szin}" stroke-width="3.4" stroke-linecap="round"/>')
        for x, tip, szel in ((xa, a_tip, a), (xb, b_tip, b)):
            if szel in (float("-inf"), float("inf")) or tip == "nyil":
                # nyílban végződik: a szakasz kilóg a képből
                continue
            if tip == "zart":
                ki.append(f'  <circle cx="{x:.1f}" cy="{y}" r="4.2" fill="{szin}"/>')
            else:
                ki.append(f'  <circle cx="{x:.1f}" cy="{y}" r="4.2" fill="#ffffff" '
                          f'stroke="{szin}" stroke-width="2"/>')

    # kiemelt pontok a vonalon
    for p in pontok:
        x, felirat = p[0], p[1] if len(p) > 1 else ""
        szin = p[2] if len(p) > 2 else PIROS
        ki.append(f'  <circle cx="{X(x):.1f}" cy="{yv}" r="4.2" fill="{szin}"/>')
        if felirat:
            ki.append(f'  <text x="{X(x):.1f}" y="{yv - 10}" font-size="11" fill="{szin}" '
                      f'font-weight="600" text-anchor="middle">{felirat}</text>')

    ki.append("</svg>")
    return "\n".join(ki)


# =====================================================================
# 2. Háromszög — feliratozott csúcsok, oldalak, szögek, magasság
# =====================================================================

def svg_haromszog(csucsok=None, cimkek=("A", "B", "C"), oldalcimkek=None,
                  szogek=(), derekszog=None, magassag=None, w=340, h=250,
                  leiras="Háromszög", kitolt=None):
    """Feliratozott háromszög.

    `csucsok` = [(x, y), (x, y), (x, y)] matematikai koordinátákban (y felfelé);
        ha None, egy jól látható általános háromszög az alapértelmezés.
    `oldalcimkek` = ("c", "a", "b") — az AB, BC, CA oldalak felirata.
    `szogek` = a szögjelöléssel ellátandó csúcsok indexei, pl. (0, 1).
    `derekszog` = csúcs indexe, ahol derékszög-jelölés (kis négyzet) kell.
    `magassag` = csúcs indexe, ahonnan magasságot húzunk a szemközti oldalra.
    """
    if csucsok is None:
        csucsok = [(0.0, 0.0), (4.0, 0.0), (1.2, 2.6)]
    kitolt = kitolt or "#eff6ff"

    xs = [p[0] for p in csucsok]
    ys = [p[1] for p in csucsok]
    hx, hy = max(xs) - min(xs) or 1, max(ys) - min(ys) or 1
    keret = 34
    sk = min((w - 2 * keret) / hx, (h - 2 * keret) / hy)
    ox, oy = min(xs), min(ys)

    def P(p):
        return (keret + (p[0] - ox) * sk, h - keret - (p[1] - oy) * sk)

    Pk = [P(p) for p in csucsok]
    ki = _fej(w, h, leiras)
    ki.append('  <polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in Pk) +
              f'" fill="{kitolt}" stroke="{TINTA}" stroke-width="1.8" '
              'stroke-linejoin="round"/>')

    # magasság
    if magassag is not None:
        i = magassag
        a, b = Pk[(i + 1) % 3], Pk[(i + 2) % 3]
        c = Pk[i]
        vx, vy = b[0] - a[0], b[1] - a[1]
        hossz2 = vx * vx + vy * vy or 1
        t = ((c[0] - a[0]) * vx + (c[1] - a[1]) * vy) / hossz2
        tx, ty = a[0] + t * vx, a[1] + t * vy
        ki.append(f'  <line x1="{c[0]:.1f}" y1="{c[1]:.1f}" x2="{tx:.1f}" y2="{ty:.1f}" '
                  f'stroke="{BOROSTYAN}" stroke-width="1.6" stroke-dasharray="5 3"/>')
        # talpponti derékszög-jel
        n = math.hypot(vx, vy) or 1
        ux, uy = vx / n * 8, vy / n * 8
        wx, wy = (c[0] - tx), (c[1] - ty)
        nw = math.hypot(wx, wy) or 1
        wx, wy = wx / nw * 8, wy / nw * 8
        ki.append(f'  <path d="M{tx + ux:.1f},{ty + uy:.1f} L{tx + ux + wx:.1f},'
                  f'{ty + uy + wy:.1f} L{tx + wx:.1f},{ty + wy:.1f}" fill="none" '
                  f'stroke="{BOROSTYAN}" stroke-width="1.2"/>')

    # szögjelölések
    for i in szogek:
        c = Pk[i]
        a, b = Pk[(i + 1) % 3], Pk[(i + 2) % 3]
        r = 22
        sz = []
        for q in (a, b):
            dx, dy = q[0] - c[0], q[1] - c[1]
            n = math.hypot(dx, dy) or 1
            sz.append((c[0] + dx / n * r, c[1] + dy / n * r))
        ki.append(f'  <path d="M{sz[0][0]:.1f},{sz[0][1]:.1f} A{r},{r} 0 0 '
                  f'{1 if _elojel(c, a, b) > 0 else 0} {sz[1][0]:.1f},{sz[1][1]:.1f}" '
                  f'fill="none" stroke="{ZOLD}" stroke-width="1.6"/>')

    # derékszög
    if derekszog is not None:
        i = derekszog
        c = Pk[i]
        a, b = Pk[(i + 1) % 3], Pk[(i + 2) % 3]
        v = []
        for q in (a, b):
            dx, dy = q[0] - c[0], q[1] - c[1]
            n = math.hypot(dx, dy) or 1
            v.append((dx / n * 13, dy / n * 13))
        ki.append(f'  <path d="M{c[0] + v[0][0]:.1f},{c[1] + v[0][1]:.1f} '
                  f'L{c[0] + v[0][0] + v[1][0]:.1f},{c[1] + v[0][1] + v[1][1]:.1f} '
                  f'L{c[0] + v[1][0]:.1f},{c[1] + v[1][1]:.1f}" fill="none" '
                  f'stroke="{TINTA}" stroke-width="1.3"/>')

    # csúcsfeliratok — a háromszög súlypontjától kifelé tolva
    sx = sum(p[0] for p in Pk) / 3
    sy = sum(p[1] for p in Pk) / 3
    for (x, y), cimke in zip(Pk, cimkek):
        dx, dy = x - sx, y - sy
        n = math.hypot(dx, dy) or 1
        ki.append(f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{TINTA}"/>')
        ki.append(f'  <text x="{x + dx / n * 16:.1f}" y="{y + dy / n * 16 + 4:.1f}" '
                  f'font-size="13" font-style="italic" fill="{TINTA}" '
                  f'text-anchor="middle">{cimke}</text>')

    # oldalfeliratok
    if oldalcimkek:
        for i, cimke in enumerate(oldalcimkek):
            if not cimke:
                continue
            a, b = Pk[i], Pk[(i + 1) % 3]
            mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
            dx, dy = mx - sx, my - sy
            n = math.hypot(dx, dy) or 1
            ki.append(f'  <text x="{mx + dx / n * 14:.1f}" y="{my + dy / n * 14 + 4:.1f}" '
                      f'font-size="12" font-style="italic" fill="{SZURKE}" '
                      f'text-anchor="middle">{cimke}</text>')

    ki.append("</svg>")
    return "\n".join(ki)


def _elojel(c, a, b) -> float:
    return (a[0] - c[0]) * (b[1] - c[1]) - (a[1] - c[1]) * (b[0] - c[0])


# =====================================================================
# 3. Venn-diagram — 2 vagy 3 halmaz, árnyékolt tartományokkal
# =====================================================================

def svg_venn(cimkek=("A", "B"), arnyekolt=(), alaphalmaz="U", w=340, h=230,
             leiras="Venn-diagram", szinek=None):
    """2 vagy 3 halmaz Venn-diagramja, megadott tartományok kiemelésével.

    `arnyekolt` = a kiemelendő tartományok kódjai. A kód azt mondja meg, MELY
    halmazokban van benne a tartomány:
        2 halmaznál: "A", "B", "AB", "-"  (a `-` az alaphalmaz maradéka)
        3 halmaznál: "A", "B", "C", "AB", "AC", "BC", "ABC", "-"
    Példák: metszet → `("AB",)` · unió → `("A","B","AB")` ·
    szimmetrikus differencia → `("A","B")` · komplementer → `("-",)`.

    MIÉRT kódokkal: így a builderben az látszik, MIT ábrázolunk (halmazművelet),
    nem az, hogy melyik köríves útvonalat kell kirajzolni.
    """
    n = len(cimkek)
    if n not in (2, 3):
        raise ValueError("Venn-diagram csak 2 vagy 3 halmazra készül")
    szinek = szinek or [ZOLD, KEK, LILA]
    ki = _fej(w, h, leiras)
    ki.append(f'  <rect x="6" y="6" width="{w - 12}" height="{h - 12}" rx="6" '
              f'fill="#f8fafc" stroke="{HALVANY}" stroke-width="1.2"/>')
    ki.append(f'  <text x="{w - 14}" y="{h - 12}" font-size="12" font-style="italic" '
              f'fill="{SZURKE}" text-anchor="end">{alaphalmaz}</text>')

    if n == 2:
        r = min(w, h) * 0.27
        kozep = [(w / 2 - r * 0.62, h / 2), (w / 2 + r * 0.62, h / 2)]
    else:
        r = min(w, h) * 0.24
        kozep = [(w / 2 - r * 0.6, h / 2 - r * 0.34),
                 (w / 2 + r * 0.6, h / 2 - r * 0.34),
                 (w / 2, h / 2 + r * 0.66)]

    # Az árnyékolást clipPath-ok metszésével építjük: minden halmazhoz egy kör,
    # a tartomány = a benne lévők metszete MÍNUSZ a kívüliek.
    # Két clipPath-készlet halmazonként:
    #   k{i}  = a kör BELSEJE  (a „benne van" tartományokhoz)
    #   kk{i} = a kör KÜLSEJE  (a „nincs benne" tartományokhoz)
    # A külső clip egyetlen kört lyukaszt ki even-odd szabállyal — egy körnél ez
    # helyes, és a beágyazott clipek metszése adja a több halmazra vonatkozó
    # kizárást. (Maszkkal is megoldható lenne, de a renderelők egy része nem
    # alkalmazza clip-path alatti csoportra — ezért clipPath.)
    for i, (cx, cy) in enumerate(kozep):
        ki.append(f'  <clipPath id="k{i}"><circle cx="{cx:.1f}" cy="{cy:.1f}" '
                  f'r="{r:.1f}"/></clipPath>')
        d = (f"M0,0 h{w} v{h} h-{w} Z "
             f"M{cx - r:.1f},{cy:.1f} a{r:.1f},{r:.1f} 0 1,0 {2 * r:.1f},0 "
             f"a{r:.1f},{r:.1f} 0 1,0 -{2 * r:.1f},0")
        ki.append(f'  <clipPath id="kk{i}"><path d="{d}" clip-rule="evenodd"/></clipPath>')

    for kod in arnyekolt:
        if kod == "-":
            # alaphalmaz maradéka: a téglalap, kilyukasztva a körökkel
            d = f"M6,6 h{w - 12} v{h - 12} h-{w - 12} Z "
            for cx, cy in kozep:
                d += (f"M{cx - r:.1f},{cy:.1f} a{r:.1f},{r:.1f} 0 1,0 {2 * r:.1f},0 "
                      f"a{r:.1f},{r:.1f} 0 1,0 -{2 * r:.1f},0 ")
            ki.append(f'  <path d="{d}" fill="{BOROSTYAN}" fill-opacity=".22" '
                      'fill-rule="evenodd"/>')
            continue
        benne = [i for i, c in enumerate(cimkek) if c in kod]
        if not benne:
            continue
        kivul = [i for i in range(n) if i not in benne]
        # benne → belső clip; kívül → külső clip; a beágyazás metszi őket
        nyit = ("".join(f'<g clip-path="url(#k{i})">' for i in benne)
                + "".join(f'<g clip-path="url(#kk{i})">' for i in kivul))
        zar = "</g>" * (len(benne) + len(kivul))
        torzs = (f'<rect x="0" y="0" width="{w}" height="{h}" fill="{BOROSTYAN}" '
                 'fill-opacity=".30"/>')
        ki.append("  " + nyit + torzs + zar)

    for i, ((cx, cy), cimke) in enumerate(zip(kozep, cimkek)):
        ki.append(f'  <circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="none" '
                  f'stroke="{szinek[i % len(szinek)]}" stroke-width="2"/>')
        fx = cx + (r * 0.72 if i == 1 or n == 2 and i == 1 else -r * 0.72 if i == 0 else 0)
        fy = cy - r * 0.78 if n == 2 else (cy + r * 0.86 if i == 2 else cy - r * 0.8)
        ki.append(f'  <text x="{fx:.1f}" y="{fy:.1f}" font-size="13" font-style="italic" '
                  f'fill="{szinek[i % len(szinek)]}" font-weight="600" '
                  f'text-anchor="middle">{cimke}</text>')

    ki.append("</svg>")
    return "\n".join(ki)


# =====================================================================
# 4. Párhuzamosok transzverzálissal — szögszámító feladatokhoz
# =====================================================================

def svg_parhuzamosok(szog=58, cimkek=None, nevek=("a", "b"), w=460, h=250,
                     leiras="Két párhuzamos egyenest transzverzális metsz"):
    """Két vízszintes párhuzamos, amelyet egy ferde egyenes (transzverzális) metsz.

    A nyolc keletkező szög számozása **a bal felsőtől, az óramutató járása szerint**:

        1 2          (felső metszéspont)
        4 3
        5 6          (alsó metszéspont)
        8 7

    `cimkek` = {2: "48°23′", 5: "α"} — csak a megjelölendő szögek. A felirat sima
      SVG-szöveg (nem KaTeX), tehát a °, ′ és a görög betűk közvetlenül írhatók.
    `szog`   = a transzverzális hajlásszöge a párhuzamosokhoz, fokban.
    """
    cimkek = cimkek or {}
    ya, yb = 74.0, 178.0
    bal, jobb = 28.0, w - 34.0

    th = math.radians(max(20.0, min(80.0, szog)))
    dx = (yb - ya) / math.tan(th)
    x_fent = w * 0.42 - dx / 2.0
    x_lent = x_fent + dx

    vx, vy = dx, (yb - ya)                       # transzverzális iránya (lefelé-jobbra)
    vn = math.hypot(vx, vy) or 1.0
    vx, vy = vx / vn, vy / vn
    fok_v = math.degrees(math.atan2(vy, vx))     # képernyő-szög (y lefelé)

    # a négy szektor: (kezdő szög, záró szög) képernyő-fokban
    szektor = {1: (180.0, 180.0 + fok_v),
               2: (180.0 + fok_v, 360.0),
               3: (0.0, fok_v),
               4: (fok_v, 180.0)}

    ki = _fej(w, h, leiras)

    tny = 52.0
    ki.append(f'  <line x1="{x_fent - vx * tny:.1f}" y1="{ya - vy * tny:.1f}" '
              f'x2="{x_lent + vx * tny:.1f}" y2="{yb + vy * tny:.1f}" '
              f'stroke="{SZURKE}" stroke-width="1.9"/>')

    for y, nev in ((ya, nevek[0]), (yb, nevek[1])):
        ki.append(f'  <line x1="{bal}" y1="{y}" x2="{jobb}" y2="{y}" '
                  f'stroke="{TINTA}" stroke-width="2.2"/>')
        ki.append(f'  <text x="{jobb + 7:.1f}" y="{y + 5:.1f}" font-size="15" '
                  f'font-style="italic" fill="{TINTA}">{nev}</text>')
        for k in (0, 1):                          # párhuzamosság-jel
            x = bal + 20 + k * 10
            ki.append(f'  <path d="M{x:.1f},{y - 5:.1f} L{x + 6:.1f},{y:.1f} '
                      f'L{x:.1f},{y + 5:.1f}" fill="none" stroke="{TINTA}" '
                      'stroke-width="1.5"/>')

    for eltolas, (px, py) in ((0, (x_fent, ya)), (4, (x_lent, yb))):
        for k in (1, 2, 3, 4):
            felirat = cimkek.get(k + eltolas)
            if felirat is None:
                continue
            a1, a2 = szektor[k]
            r = 26.0
            x1 = px + r * math.cos(math.radians(a1))
            y1 = py + r * math.sin(math.radians(a1))
            x2 = px + r * math.cos(math.radians(a2))
            y2 = py + r * math.sin(math.radians(a2))
            nagy = 1 if (a2 - a1) > 180 else 0
            ki.append(f'  <path d="M{x1:.1f},{y1:.1f} A{r},{r} 0 {nagy} 1 {x2:.1f},{y2:.1f}" '
                      f'fill="none" stroke="{PIROS}" stroke-width="1.8"/>')
            kozep = math.radians((a1 + a2) / 2.0)
            rt = 45.0
            tx, ty = px + rt * math.cos(kozep), py + rt * math.sin(kozep)
            ki.append(f'  <text x="{tx:.1f}" y="{ty + 5:.1f}" font-size="15" '
                      f'text-anchor="middle" fill="{PIROS}" font-weight="700">{felirat}</text>')

    for px, py in ((x_fent, ya), (x_lent, yb)):
        ki.append(f'  <circle cx="{px:.1f}" cy="{py:.1f}" r="3.2" fill="{TINTA}"/>')

    ki.append('</svg>')
    return "\n".join(ki)


# =====================================================================
# 5. Sokszög belső (és külső) szögekkel — négyszög, trapéz, paralelogramma
# =====================================================================

def svg_sokszog_szogek(csucsok, cimkek=None, szogek=None, atlok=(), oldaljelek=None,
                       parhuzamos=(), kulso=(), oldalcimkek=None, derekszogek=(),
                       kor=False, w=380, h=270, leiras="Sokszög", kitolt="#eff6ff"):
    """Tetszőleges sokszög feliratozott belső szögekkel.

    `csucsok`   = [(x, y), …] matematikai koordináták (y felfelé), az óramutatóval
                  ELLENTÉTES körüljárás a természetes.
    `cimkek`    = ["A", "B", "C", "D"] csúcsfeliratok (vagy None).
    `szogek`    = {csúcs_index: "felirat"} — szögív + felirat a sokszögön belül.
    `atlok`     = [(i, j), …] szaggatott átlók.
    `oldaljelek`= {oldal_index: darabszám} — egyenlőség-vonalkák az i→i+1 oldalon.
    `parhuzamos`= [(i, j), …] — nyílhegy-jel két párhuzamos oldalon.
    `kulso`     = [(csúcs, szomszéd, "felirat"), …] — a szomszéd→csúcs oldal
                  meghosszabbítása a csúcson túl, és az ott keletkező külső szög.
    `derekszogek` = csúcsindexek, ahol derékszög-jel (kis négyzet) kell.
    """
    cimkek = cimkek or [None] * len(csucsok)
    szogek = szogek or {}
    oldaljelek = oldaljelek or {}
    oldalcimkek = oldalcimkek or {}
    n = len(csucsok)

    xs = [p[0] for p in csucsok]
    ys = [p[1] for p in csucsok]
    hx, hy = (max(xs) - min(xs)) or 1, (max(ys) - min(ys)) or 1
    keret = 46
    sk = min((w - 2 * keret) / hx, (h - 2 * keret) / hy)
    ox, oy = min(xs), min(ys)

    def P(p):
        return (keret + (p[0] - ox) * sk, h - keret - (p[1] - oy) * sk)

    Pk = [P(p) for p in csucsok]

    def egys(a, b):
        dx, dy = b[0] - a[0], b[1] - a[1]
        d = math.hypot(dx, dy) or 1.0
        return dx / d, dy / d

    ki = _fej(w, h, leiras)

    # külső szögek: előbb a meghosszabbítás, hogy a sokszög rákerüljön
    for cs, szo, felirat in kulso:
        A, B = Pk[szo], Pk[cs]
        ux, uy = egys(A, B)
        vx_, vy_ = B[0] + ux * 46, B[1] + uy * 46
        ki.append(f'  <line x1="{B[0]:.1f}" y1="{B[1]:.1f}" x2="{vx_:.1f}" y2="{vy_:.1f}" '
                  f'stroke="{SZURKE}" stroke-width="1.7" stroke-dasharray="6 4"/>')

    if kor:                                   # körülírt kör az első három csúcson át
        (x1_, y1_), (x2_, y2_), (x3_, y3_) = Pk[0], Pk[1], Pk[2]
        d_ = 2 * (x1_ * (y2_ - y3_) + x2_ * (y3_ - y1_) + x3_ * (y1_ - y2_))
        if abs(d_) > 1e-6:
            ux_ = ((x1_**2 + y1_**2) * (y2_ - y3_) + (x2_**2 + y2_**2) * (y3_ - y1_)
                   + (x3_**2 + y3_**2) * (y1_ - y2_)) / d_
            uy_ = ((x1_**2 + y1_**2) * (x3_ - x2_) + (x2_**2 + y2_**2) * (x1_ - x3_)
                   + (x3_**2 + y3_**2) * (x2_ - x1_)) / d_
            r_ = math.hypot(x1_ - ux_, y1_ - uy_)
            ki.append(f'  <circle cx="{ux_:.1f}" cy="{uy_:.1f}" r="{r_:.1f}" '
                      f'fill="none" stroke="{KEK}" stroke-width="1.6"/>')

    ki.append('  <polygon points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in Pk) +
              f'" fill="{kitolt}" stroke="{TINTA}" stroke-width="2.1" '
              'stroke-linejoin="round"/>')

    for i, j in atlok:
        ki.append(f'  <line x1="{Pk[i][0]:.1f}" y1="{Pk[i][1]:.1f}" '
                  f'x2="{Pk[j][0]:.1f}" y2="{Pk[j][1]:.1f}" '
                  f'stroke="{SZURKE}" stroke-width="1.5" stroke-dasharray="5 3"/>')

    # egyenlőség-vonalkák
    for i, db in oldaljelek.items():
        A, B = Pk[i], Pk[(i + 1) % n]
        ux, uy = egys(A, B)
        mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
        for k in range(db):
            e = (k - (db - 1) / 2) * 7
            cx, cy = mx + ux * e, my + uy * e
            ki.append(f'  <line x1="{cx - uy * 6:.1f}" y1="{cy + ux * 6:.1f}" '
                      f'x2="{cx + uy * 6:.1f}" y2="{cy - ux * 6:.1f}" '
                      f'stroke="{TINTA}" stroke-width="1.6"/>')

    # párhuzamosság-nyilak
    for i in parhuzamos:
        A, B = Pk[i], Pk[(i + 1) % n]
        ux, uy = egys(A, B)
        mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
        ki.append(f'  <path d="M{mx - ux * 5 - uy * 5:.1f},{my - uy * 5 + ux * 5:.1f} '
                  f'L{mx + ux * 5:.1f},{my + uy * 5:.1f} '
                  f'L{mx - ux * 5 + uy * 5:.1f},{my - uy * 5 - ux * 5:.1f}" '
                  f'fill="none" stroke="{TINTA}" stroke-width="1.5"/>')

    # oldalfeliratok
    for i, sz in oldalcimkek.items():
        A, B = Pk[i], Pk[(i + 1) % n]
        ux, uy = egys(A, B)
        mx, my = (A[0] + B[0]) / 2, (A[1] + B[1]) / 2
        ki.append(f'  <text x="{mx - uy * 22:.1f}" y="{my + ux * 22 + 5:.1f}" font-size="13.5" '
                  f'text-anchor="middle" fill="{SZURKE}" font-style="italic">{sz}</text>')

    # belső szögek
    for i, felirat in szogek.items():
        C = Pk[i]
        A, B = Pk[(i - 1) % n], Pk[(i + 1) % n]
        a1 = math.degrees(math.atan2(*reversed(egys(C, A))))
        a2 = math.degrees(math.atan2(*reversed(egys(C, B))))
        d = (a2 - a1) % 360
        nagy = 1 if d > 180 else 0
        r = 27.0
        x1, y1 = C[0] + r * math.cos(math.radians(a1)), C[1] + r * math.sin(math.radians(a1))
        x2, y2 = C[0] + r * math.cos(math.radians(a2)), C[1] + r * math.sin(math.radians(a2))
        if i in derekszogek:
            u1 = egys(C, A); u2 = egys(C, B)
            s = 15.0
            ki.append(f'  <path d="M{C[0] + u1[0] * s:.1f},{C[1] + u1[1] * s:.1f} '
                      f'L{C[0] + (u1[0] + u2[0]) * s:.1f},{C[1] + (u1[1] + u2[1]) * s:.1f} '
                      f'L{C[0] + u2[0] * s:.1f},{C[1] + u2[1] * s:.1f}" fill="none" '
                      f'stroke="{PIROS}" stroke-width="1.7"/>')
        else:
            ki.append(f'  <path d="M{x1:.1f},{y1:.1f} A{r},{r} 0 {nagy} 1 {x2:.1f},{y2:.1f}" '
                      f'fill="none" stroke="{PIROS}" stroke-width="1.9"/>')
        kozep = math.radians(a1 + ((a2 - a1) % 360) / 2.0)
        rt = 46.0
        ki.append(f'  <text x="{C[0] + rt * math.cos(kozep):.1f}" '
                  f'y="{C[1] + rt * math.sin(kozep) + 5:.1f}" font-size="14.5" '
                  f'text-anchor="middle" fill="{PIROS}" font-weight="700">{felirat}</text>')

    # külső szögek feliratozása
    for cs, szo, felirat in kulso:
        C = Pk[cs]
        A = Pk[szo]
        masik = Pk[(cs + 1) % n] if (cs + 1) % n != szo else Pk[(cs - 1) % n]
        ux, uy = egys(A, C)                      # a meghosszabbítás iránya
        a1 = math.degrees(math.atan2(uy, ux))
        a2 = math.degrees(math.atan2(*reversed(egys(C, masik))))
        d = (a2 - a1) % 360
        nagy = 1 if d > 180 else 0
        r = 24.0
        x1, y1 = C[0] + r * math.cos(math.radians(a1)), C[1] + r * math.sin(math.radians(a1))
        x2, y2 = C[0] + r * math.cos(math.radians(a2)), C[1] + r * math.sin(math.radians(a2))
        ki.append(f'  <path d="M{x1:.1f},{y1:.1f} A{r},{r} 0 {nagy} 1 {x2:.1f},{y2:.1f}" '
                  f'fill="none" stroke="{BOROSTYAN}" stroke-width="1.9"/>')
        kozep = math.radians(a1 + d / 2.0)
        rt = 43.0
        ki.append(f'  <text x="{C[0] + rt * math.cos(kozep):.1f}" '
                  f'y="{C[1] + rt * math.sin(kozep) + 5:.1f}" font-size="14.5" '
                  f'text-anchor="middle" fill="{BOROSTYAN}" font-weight="700">{felirat}</text>')

    # csúcsfeliratok
    kx = sum(p[0] for p in Pk) / n
    kyy = sum(p[1] for p in Pk) / n
    for i, nev in enumerate(cimkek):
        if not nev:
            continue
        px, py = Pk[i]
        dx, dy = px - kx, py - kyy
        dd = math.hypot(dx, dy) or 1.0
        ki.append(f'  <text x="{px + dx / dd * 17:.1f}" y="{py + dy / dd * 17 + 5:.1f}" '
                  f'font-size="14.5" text-anchor="middle" fill="{TINTA}" '
                  f'font-weight="700">{nev}</text>')

    ki.append('</svg>')
    return "\n".join(ki)


# =====================================================================
# 6. TÉRGEOMETRIA — poliéderek axonometrikus képe (3e/01 óta)
# =====================================================================
#
# Egyszerű **kavalier-féle** párhuzamos vetítés: a z tengely felfelé, az x
# jobbra, az y „hátrafelé" (a mélység) — az utóbbi K_MELY arányban rövidül és
# A_MELY szögben dől. Konvex testnél a takart éleket a vetített csúcsok konvex
# burkából határozzuk meg: amelyik ALAP-csúcs nem kerül a burokra, az hátul van,
# és a hozzá csatlakozó élek szaggatottak.
#
# A feliratok eltolása a VETÍTETT képen kifelé mutató irányt követi (`_kifele`) —
# 3D-ben számolva a hátsó csúcs felirata a testre esne.

K_MELY = 0.52          # a mélységi rövidülés aránya
A_MELY = math.radians(34)


def _vet(p):
    """(x, y, z) → (X, Y) matematikai koordinátákban (Y felfelé)."""
    x, y, z = p
    return (x + K_MELY * y * math.cos(A_MELY), z + K_MELY * y * math.sin(A_MELY))


def _hull(pts):
    """Andrew monotone chain — a burok pontjainak INDEXEI (ccw)."""
    idx = sorted(range(len(pts)), key=lambda i: (round(pts[i][0], 6), round(pts[i][1], 6)))
    def keresztszorzat(o, a, b):
        return ((pts[a][0]-pts[o][0])*(pts[b][1]-pts[o][1])
                - (pts[a][1]-pts[o][1])*(pts[b][0]-pts[o][0]))
    also = []
    for i in idx:
        while len(also) >= 2 and keresztszorzat(also[-2], also[-1], i) <= 1e-9:
            also.pop()
        also.append(i)
    felso = []
    for i in reversed(idx):
        while len(felso) >= 2 and keresztszorzat(felso[-2], felso[-1], i) <= 1e-9:
            felso.pop()
        felso.append(i)
    return set(also + felso)


def _alap(tipus, a=1.0, b=None, n=None):
    """Alapsokszög a z=0 síkban, a középpont az origóban.

    Visszaad: [(x, y), …] úgy, hogy az ELÜLSŐ él vízszintes legyen.
    """
    if tipus == "teglalap":
        b = b if b is not None else a * 0.62
        return [(-a/2, -b/2), (a/2, -b/2), (a/2, b/2), (-a/2, b/2)]
    if tipus == "negyzet":
        return _alap("teglalap", a, a)
    n = {"haromszog": 3, "otszog": 5, "hatszog": 6}.get(tipus, n or 4)
    R = a / (2 * math.sin(math.pi / n))          # a = oldalhossz → köréírt sugár
    # az elülső él vízszintes: a csúcsok a -90° ± (180/n) körül induljanak
    kezd = -math.pi/2 + math.pi/n
    return [(R * math.cos(kezd + 2*math.pi*i/n), R * math.sin(kezd + 2*math.pi*i/n))
            for i in range(n)]


class _Rajz:
    """Vetített pontok gyűjtője + automatikus méretezés és SVG-kiírás."""

    def __init__(self, w, h, leiras, parnazas=26):
        self.w, self.h, self.leiras, self.par = w, h, leiras, parnazas
        self.pontok = []          # 3D pontok, amiket a kép be kell foglaljon
        self.elemek = []          # (reteg, svg-darab) — a reteg a rajzolási sorrend

    def befoglal(self, *pts):
        self.pontok.extend(pts)

    def _skala(self):
        vp = [_vet(p) for p in self.pontok]
        xs = [p[0] for p in vp]; ys = [p[1] for p in vp]
        dx = max(xs) - min(xs) or 1.0
        dy = max(ys) - min(ys) or 1.0
        s = min((self.w - 2*self.par) / dx, (self.h - 2*self.par) / dy)
        kx = (self.w - s*dx) / 2 - s*min(xs)
        ky = (self.h - s*dy) / 2 + s*max(ys)
        return s, kx, ky

    def P(self, p):
        """3D pont → SVG-koordináta."""
        s, kx, ky = self._sk
        X, Y = _vet(p)
        return (kx + s*X, ky - s*Y)

    # --- rajzoló primitívek (3D bemenettel) ---
    def vonal(self, p, q, szin=TINTA, sz=1.6, szaggat=None, reteg=1, opacity=None):
        self.elemek.append((reteg, ("vonal", p, q, szin, sz, szaggat, opacity)))

    def sokszog(self, pts, kitolt="none", szin=TINTA, sz=1.6, szaggat=None,
                atlatszo=0.16, reteg=0):
        self.elemek.append((reteg, ("sokszog", list(pts), kitolt, szin, sz, szaggat, atlatszo)))

    def felirat(self, p, szoveg, dx=0, dy=0, szin=TINTA, meret=13, dolt=True,
                horgony="middle", reteg=3, sulyos=True):
        self.elemek.append((reteg, ("text", p, szoveg, dx, dy, szin, meret, dolt,
                                    horgony, sulyos)))

    def derekszog(self, sarok, p1, p2, meret=11, szin=SZURKE, reteg=2):
        self.elemek.append((reteg, ("dsz", sarok, p1, p2, meret, szin)))

    def kesz(self):
        self._sk = self._skala()
        ki = [f'<svg viewBox="0 0 {self.w} {self.h}" width="{self.w}" height="{self.h}" '
              f'role="img" aria-label="{self.leiras}">']
        for _, e in sorted(self.elemek, key=lambda t: t[0]):
            t = e[0]
            if t == "vonal":
                _, p, q, szin, sz, szag, op = e
                x1, y1 = self.P(p); x2, y2 = self.P(q)
                d = f' stroke-dasharray="{szag}"' if szag else ""
                o = f' opacity="{op}"' if op else ""
                ki.append(f'  <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                          f'stroke="{szin}" stroke-width="{sz}" stroke-linecap="round"{d}{o}/>')
            elif t == "sokszog":
                _, pts, kitolt, szin, sz, szag, atl = e
                d = " ".join(f"{self.P(p)[0]:.1f},{self.P(p)[1]:.1f}" for p in pts)
                dd = f' stroke-dasharray="{szag}"' if szag else ""
                fill = "none" if kitolt == "none" else kitolt
                fo = "" if kitolt == "none" else f' fill-opacity="{atl}"'
                ki.append(f'  <polygon points="{d}" fill="{fill}"{fo} stroke="{szin}" '
                          f'stroke-width="{sz}" stroke-linejoin="round"{dd}/>')
            elif t == "text":
                _, p, sz_, dx, dy, szin, meret, dolt, horgony, sulyos = e
                x, y = self.P(p)
                st = ' font-style="italic"' if dolt else ""
                fw = ' font-weight="600"' if sulyos else ""
                ki.append(f'  <text x="{x+dx:.1f}" y="{y+dy:.1f}" font-size="{meret}" '
                          f'fill="{szin}" text-anchor="{horgony}"{st}{fw} '
                          f'font-family="Cambria, Georgia, serif">{sz_}</text>')
            elif t == "dsz":
                _, s, p1, p2, m, szin = e
                sx, sy = self.P(s)
                def egys(q):
                    qx, qy = self.P(q)
                    d = math.hypot(qx-sx, qy-sy) or 1
                    return ((qx-sx)/d, (qy-sy)/d)
                u = egys(p1); v = egys(p2)
                a = (sx+u[0]*m, sy+u[1]*m)
                b = (sx+v[0]*m, sy+v[1]*m)
                c = (sx+(u[0]+v[0])*m, sy+(u[1]+v[1])*m)
                ki.append(f'  <path d="M{a[0]:.1f},{a[1]:.1f} L{c[0]:.1f},{c[1]:.1f} '
                          f'L{b[0]:.1f},{b[1]:.1f}" fill="none" stroke="{szin}" stroke-width="1.2"/>')
        ki.append("</svg>")
        return "\n".join(ki)


def _kifele(p, kozep, tav):
    """A felirat eltolása a VETÍTETT képen kifelé mutató irányban (dx, dy px)."""
    X, Y = _vet(p)
    Xc, Yc = _vet(kozep)
    vx, vy = X - Xc, -(Y - Yc)          # SVG: y lefelé nő
    d = math.hypot(vx, vy) or 1.0
    return tav * vx / d, tav * vy / d


def _betuk(n, also=True):
    ABC = "ABCDEFGH"
    return [ABC[i] for i in range(n)] if also else [f"{ABC[i]}<tspan font-size='9' dy='3'>1</tspan>" for i in range(n)]


def _kirajzol_test(r, also3, felso3, cimkez, csucsbetuk=True, felso_betuk=True):
    """Hasáb/csonkagúla váz: alaplap + fedőlap + oldalélek, takart élek szaggatva."""
    n = len(also3)
    minden = also3 + felso3
    vp = [_vet(p) for p in minden]
    burok = _hull(vp)
    takart = [i for i in range(n) if i not in burok]     # hátsó ALAP-csúcsok
    def szag(i, j=None):
        return "5 4" if (i in takart or (j is not None and j in takart)) else None
    # alaplap élei
    for i in range(n):
        j = (i+1) % n
        r.vonal(also3[i], also3[j], sz=1.7, szaggat=szag(i, j))
    # fedőlap élei (mindig láthatók)
    for i in range(n):
        j = (i+1) % n
        r.vonal(felso3[i], felso3[j], sz=1.7)
    # oldalélek
    for i in range(n):
        r.vonal(also3[i], felso3[i], sz=1.7, szaggat=szag(i))
    r.befoglal(*minden)
    if not cimkez:
        return
    ABC = "ABCDEFGH"
    for i, p in enumerate(also3):
        dx, dy = _kifele(p, (0.0, 0.0, 0.0), 15)
        r.felirat(p, ABC[i], dx=dx, dy=dy + 5, meret=13)
    if felso_betuk:
        for i, p in enumerate(felso3):
            dx, dy = _kifele(p, (0.0, 0.0, p[2]), 17)
            r.felirat(p, f"{ABC[i]}<tspan font-size='9' dy='3'>1</tspan>",
                      dx=dx, dy=dy - 3, meret=13)


def _elso_el(poly):
    """Annak az élnek az indexe, amelynek a felezőpontja legelöl (legkisebb y) van."""
    n = len(poly)
    return min(range(n), key=lambda i: (poly[i][1] + poly[(i+1) % n][1]) / 2)


def svg_hasab(alap="negyzet", a=1.0, b=None, m=1.4, w=340, h=280,
              leiras="Egyenes hasáb", cimkez=True, magassag=False,
              testatlo=False, lapatlo=False, alapatlo=False, metszet=None,
              feliratok=None):
    """Egyenes hasáb axonometrikus képe.

    `alap`: "haromszog" | "negyzet" | "teglalap" | "otszog" | "hatszog"
    `metszet`: None | "atlos" (két szemközti oldalélen átmenő) | "parhuzamos"
    `feliratok`: {"a": "a", "H": "H", "D": "D", "d": "d"} — élhossz/magasság feliratok.
    A JELÖLÉS-KÁNON (`_JELOLESEK.md`): H testmagasság · h oldallap-magasság ·
    s oldalél/alkotó · r apotéma · R köré írt sugár · D testátló · d lapátló.
    """
    feliratok = feliratok or {}
    poly = _alap(alap, a, b)
    also3 = [(x, y, 0.0) for x, y in poly]
    felso3 = [(x, y, m) for x, y in poly]
    n = len(poly)
    r = _Rajz(w, h, leiras)
    if metszet == "atlos" and n >= 4:
        k = n // 2
        pts = [also3[0], also3[k], felso3[k], felso3[0]]
        r.sokszog(pts, kitolt=KEK, szin=KEK, sz=1.6, atlatszo=0.20, reteg=0)
    if metszet == "parhuzamos":
        z = m * 0.55
        pts = [(x, y, z) for x, y in poly]
        r.sokszog(pts, kitolt=ZOLD, szin=ZOLD, sz=1.6, atlatszo=0.20, reteg=2)
    _kirajzol_test(r, also3, felso3, cimkez)
    if magassag:
        kp = (0.0, 0.0)
        r.vonal((0, 0, 0), (0, 0, m), szin=PIROS, sz=1.5, szaggat="4 3", reteg=2)
        r.derekszog((0, 0, 0), (0, 0, m), also3[0], szin=PIROS)
        r.felirat((0, 0, m/2), feliratok.get("H", "H"), dx=8, dy=0, szin=PIROS,
                  horgony="start")
    if testatlo and n >= 4:
        k = n // 2
        r.vonal(also3[0], felso3[k], szin=KEK, sz=1.5)
        if "D" in feliratok:
            r.felirat(((also3[0][0]+felso3[k][0])/2, (also3[0][1]+felso3[k][1])/2,
                       (also3[0][2]+felso3[k][2])/2), feliratok["D"],
                      dx=6, dy=-4, szin=KEK, horgony="start")
    if lapatlo:
        r.vonal(also3[0], felso3[1], szin=BOROSTYAN, sz=1.5)
    if alapatlo and n >= 4:
        k = n // 2
        r.vonal(also3[0], also3[k], szin=BOROSTYAN, sz=1.6)
        p, q = also3[0], also3[k]
        r.felirat(((p[0]+q[0])/2, (p[1]+q[1])/2, 0), feliratok.get("d", "d"),
                  dx=0, dy=-6, szin=BOROSTYAN)
    if "a" in feliratok:
        i = _elso_el(poly); j = (i + 1) % n
        p, q = also3[i], also3[j]
        r.felirat(((p[0]+q[0])/2, (p[1]+q[1])/2, 0), feliratok["a"], dy=17, meret=12)
    return r.kesz()


def svg_gula(alap="negyzet", a=1.0, b=None, m=1.5, w=340, h=290,
             leiras="Egyenes gúla", cimkez=True, magassag=True,
             apotema=False, oldalel=False, sugar=False, metszet=None, arany=0.5,
             feliratok=None):
    """Szabályos gúla; magasság talpponttal, oldallap-magasság (apotéma), oldalél."""
    feliratok = feliratok or {}
    poly = _alap(alap, a, b)
    n = len(poly)
    also3 = [(x, y, 0.0) for x, y in poly]
    csucs = (0.0, 0.0, m)
    r = _Rajz(w, h, leiras)
    vp = [_vet(p) for p in also3 + [csucs]]
    burok = _hull(vp)
    takart = [i for i in range(n) if i not in burok]
    if metszet == "parhuzamos":
        k = 1 - arany
        pts = [(x*k, y*k, m*arany) for x, y in poly]
        r.sokszog(pts, kitolt=ZOLD, szin=ZOLD, sz=1.6, atlatszo=0.22, reteg=2)
    for i in range(n):
        j = (i+1) % n
        szag = "5 4" if (i in takart or j in takart) else None
        r.vonal(also3[i], also3[j], sz=1.7, szaggat=szag)
    for i in range(n):
        r.vonal(also3[i], csucs, sz=1.7, szaggat=("5 4" if i in takart else None))
    r.befoglal(*(also3 + [csucs]))
    ABC = "ABCDEFGH"
    if cimkez:
        for i, p in enumerate(also3):
            dx, dy = _kifele(p, (0.0, 0.0, 0.0), 15)
            r.felirat(p, ABC[i], dx=dx, dy=dy + 5, meret=13)
        r.felirat(csucs, ABC[n], dy=-9, meret=13)
    if magassag:
        r.vonal((0, 0, 0), csucs, szin=PIROS, sz=1.5, szaggat="4 3", reteg=2)
        r.felirat((0, 0, m/2), feliratok.get("H", "H"), dx=7, szin=PIROS, horgony="start")
        r.derekszog((0, 0, 0), csucs, also3[0], szin=PIROS)
    if apotema:
        i0 = _elso_el(poly)
        e0, e1 = poly[i0], poly[(i0 + 1) % n]
        fp = ((e0[0]+e1[0])/2, (e0[1]+e1[1])/2, 0.0)
        r.vonal((0, 0, 0), fp, szin=ZOLD, sz=1.5, szaggat="3 3", reteg=2)
        r.felirat((fp[0]/2, fp[1]/2, 0), feliratok.get("r", "r"),
                  dx=0, dy=14, szin=ZOLD, meret=13)
        r.vonal(fp, csucs, szin=BOROSTYAN, sz=1.6, reteg=2)
        r.felirat(((fp[0]+csucs[0])/2, (fp[1]+csucs[1])/2, (fp[2]+csucs[2])/2),
                  feliratok.get("h", "h"),
                  dx=-9, dy=2, szin=BOROSTYAN, horgony="end")
        r.derekszog(fp, csucs, (0, 0, 0), szin=BOROSTYAN, meret=9)
    if sugar:
        r.vonal((0, 0, 0), also3[1], szin=LILA, sz=1.4, szaggat="3 3", reteg=2)
        r.felirat((also3[1][0]/2, also3[1][1]/2, 0), feliratok.get("R", "R"),
                  dx=6, dy=-4, szin=LILA, horgony="start", meret=13)
    if oldalel:
        r.vonal(also3[1], csucs, szin=KEK, sz=2.0, reteg=2)
        p = also3[1]
        r.felirat(((p[0]+csucs[0])/2, (p[1]+csucs[1])/2, (p[2]+csucs[2])/2),
                  feliratok.get("s", "s"), dx=9, dy=-2, szin=KEK, horgony="start")
    if "a" in feliratok:
        i0 = _elso_el(poly); j0 = (i0 + 1) % n
        p, q = also3[i0], also3[j0]
        # az él NEGYEDELŐPONTJA alá: a felezőpontban az apotéma talppontja van
        r.felirat((p[0] + (q[0]-p[0])*0.25, p[1] + (q[1]-p[1])*0.25, 0),
                  feliratok["a"], dy=17, meret=12)
    return r.kesz()


def svg_csonkagula(alap="negyzet", a=1.0, a1=0.5, m=1.1, w=340, h=280,
                   leiras="Csonkagúla", cimkez=True, magassag=False,
                   kiegeszites=False, feliratok=None):
    """Csonkagúla; `kiegeszites=True` esetén a levágott csúcs szaggatva."""
    feliratok = feliratok or {}
    poly = _alap(alap, a)
    k = a1 / a
    also3 = [(x, y, 0.0) for x, y in poly]
    felso3 = [(x*k, y*k, m) for x, y in poly]
    r = _Rajz(w, h, leiras)
    _kirajzol_test(r, also3, felso3, cimkez)
    if kiegeszites and k < 1:
        M = m / (1 - k)
        csucs = (0.0, 0.0, M)
        for i in range(len(poly)):
            r.vonal(felso3[i], csucs, szin=SZURKE, sz=1.3, szaggat="4 4")
        r.befoglal(csucs)
    if magassag:
        r.vonal((0, 0, 0), (0, 0, m), szin=PIROS, sz=1.5, szaggat="4 3", reteg=2)
        r.felirat((0, 0, m/2), feliratok.get("H", "H"), dx=7, szin=PIROS, horgony="start")
        r.derekszog((0, 0, 0), (0, 0, m), also3[0], szin=PIROS)
    return r.kesz()


def svg_haztest(a=1.0, b=0.7, m=0.8, mt=0.6, w=340, h=290,
                leiras="Összetett test: téglatest és rá állított gúla",
                cimkez=False, feliratok=None):
    """Téglatest + rá állított szabályos négyoldalú gúla („ház")."""
    feliratok = feliratok or {}
    poly = _alap("teglalap", a, b)
    also3 = [(x, y, 0.0) for x, y in poly]
    felso3 = [(x, y, m) for x, y in poly]
    csucs = (0.0, 0.0, m + mt)
    r = _Rajz(w, h, leiras)
    vp = [_vet(p) for p in also3 + felso3 + [csucs]]
    burok = _hull(vp)
    takart = [i for i in range(4) if i not in burok]
    for i in range(4):
        j = (i+1) % 4
        r.vonal(also3[i], also3[j], sz=1.7, szaggat=("5 4" if (i in takart or j in takart) else None))
        r.vonal(felso3[i], felso3[j], sz=1.7,
                szaggat=("5 4" if (i in takart or j in takart) else None))
        r.vonal(also3[i], felso3[i], sz=1.7, szaggat=("5 4" if i in takart else None))
        r.vonal(felso3[i], csucs, sz=1.7, szaggat=("5 4" if i in takart else None))
    r.befoglal(*(also3 + felso3 + [csucs]))
    return r.kesz()

# ---------------------------------------------------------------------
# 6b. Térelemek — sík és egyenes kölcsönös helyzete, merőlegesség, diéder
# ---------------------------------------------------------------------

def _sik(r, z=0.0, meret=(1.5, 1.05), szin=SZURKE, reteg=0, atlatszo=0.10, dolt=None):
    """Sík paralelogrammaként. `dolt`: (szog_fok) esetén az x tengely körül döntve."""
    a, b = meret
    pts = [(-a, -b), (a, -b), (a, b), (-a, b)]
    if dolt is None:
        p3 = [(x, y, z) for x, y in pts]
    else:
        s = math.sin(math.radians(dolt)); c = math.cos(math.radians(dolt))
        p3 = [(x, y * c, z + y * s) for x, y in pts]
    r.sokszog(p3, kitolt=szin, szin=szin, sz=1.3, atlatszo=atlatszo, reteg=reteg)
    r.befoglal(*p3)
    return p3


def svg_terelem(tipus="meroleges", w=360, h=250, leiras=None, cimkek=True):
    """Térelemek kölcsönös helyzete — a sík paralelogrammaként.

    `tipus`:
      "dofes"        — az egyenes döfi a síkot (egy közös pont)
      "benne"        — az egyenes a síkban van
      "parhuzamos"   — az egyenes párhuzamos a síkkal (nincs közös pont)
      "ket-sik"      — két metsző sík a metszésvonallal
      "parhuzamos-sikok" — két párhuzamos sík
      "meroleges"    — egyenes ⟂ sík: a síkban KÉT metsző egyenesre merőleges
      "hajlasszog"   — ferde egyenes, merőleges vetülete és a hajlásszög
      "dieder"       — két félsík közös élen, a lapszöggel
    """
    SZOVEG = {
        "dofes": "Az egyenes döfi a síkot: pontosan egy közös pontjuk van",
        "benne": "Az egyenes a síkban fekszik",
        "parhuzamos": "Az egyenes párhuzamos a síkkal: nincs közös pontjuk",
        "ket-sik": "Két metsző sík és a metszésvonaluk",
        "parhuzamos-sikok": "Két párhuzamos sík",
        "meroleges": "Az egyenes merőleges a síkra, mert a sík két metsző egyenesére merőleges",
        "hajlasszog": "Ferde egyenes, a merőleges vetülete és a hajlásszöge a síkkal",
        "dieder": "Diéder: két félsík közös élen, a lapszög a metszésvonalra merőlegesen mérve",
    }
    r = _Rajz(w, h, leiras or SZOVEG.get(tipus, "Térelemek a térben"))

    if tipus in ("dofes", "benne", "parhuzamos", "meroleges", "hajlasszog"):
        _sik(r)
        r.felirat((-1.35, -0.85, 0), "α", dx=-4, dy=14, szin=SZURKE, meret=13)

    if tipus == "dofes":
        A, B = (-0.9, -0.5, 1.0), (0.75, 0.45, -0.85)
        r.vonal(A, B, sz=1.7, reteg=1)
        r.sokszog([(0, 0, 0)], reteg=2)
        r.elemek.append((2, ("text", (0, 0, 0), "•", 0, 5, PIROS, 20, False, "middle", True)))
        if cimkek:
            r.felirat(A, "a", dx=-6, dy=-4, horgony="end")
            r.felirat((0, 0, 0), "P", dx=10, dy=-6, szin=PIROS, horgony="start")
        r.befoglal(A, B)
    elif tipus == "benne":
        A, B = (-1.15, -0.55, 0.0), (1.15, 0.55, 0.0)
        r.vonal(A, B, sz=1.9, reteg=2)
        if cimkek:
            r.felirat(B, "a", dx=10, dy=-2, horgony="start")
        r.befoglal(A, B)
    elif tipus == "parhuzamos":
        A, B = (-1.15, -0.55, 0.62), (1.15, 0.55, 0.62)
        r.vonal(A, B, sz=1.9, reteg=2)
        r.vonal((-1.15, -0.55, 0.0), (1.15, 0.55, 0.0), szin=HALVANY, sz=1.2,
                szaggat="4 4", reteg=1)
        if cimkek:
            r.felirat(B, "a", dx=10, dy=-2, horgony="start")
        r.befoglal(A, B)
    elif tipus == "meroleges":
        r.vonal((0, 0, -0.05), (0, 0, 1.15), sz=1.9, szin=PIROS, reteg=2)
        e1 = ((-1.0, -0.45, 0), (1.0, 0.45, 0))
        e2 = ((-0.95, 0.6, 0), (0.95, -0.6, 0))
        r.vonal(*e1, sz=1.6, reteg=1)
        r.vonal(*e2, sz=1.6, reteg=1)
        r.derekszog((0, 0, 0), (0, 0, 1.15), e1[1], szin=PIROS, meret=10)
        r.derekszog((0, 0, 0), (0, 0, 1.15), e2[0], szin=PIROS, meret=10)
        if cimkek:
            r.felirat((0, 0, 1.15), "a", dx=0, dy=-8, szin=PIROS)
            r.felirat(e1[1], "b", dx=9, dy=4, horgony="start")
            r.felirat(e2[0], "c", dx=-9, dy=4, horgony="end")
        r.befoglal((0, 0, 1.2))
    elif tipus == "hajlasszog":
        A = (-0.95, -0.5, 0.0)
        P = (0.7, 0.4, 0.95)
        Pv = (0.7, 0.4, 0.0)
        r.vonal(A, P, sz=1.9, szin=KEK, reteg=2)
        r.vonal(A, Pv, sz=1.7, szin=ZOLD, reteg=2)
        r.vonal(P, Pv, sz=1.4, szin=PIROS, szaggat="4 3", reteg=2)
        r.derekszog(Pv, P, A, szin=PIROS, meret=10)
        r.szogiv = None
        if cimkek:
            r.felirat(P, "P", dx=0, dy=-8, szin=KEK)
            r.felirat(A, "A", dx=-8, dy=8, horgony="end")
            r.felirat(Pv, "P'", dx=8, dy=12, szin=ZOLD, horgony="start")
            r.felirat((-0.45, -0.24, 0.06), "φ", dx=14, dy=-2, szin=BOROSTYAN, meret=13)
        r.befoglal(A, P, Pv)
    elif tipus in ("ket-sik", "parhuzamos-sikok"):
        if tipus == "ket-sik":
            _sik(r, meret=(1.4, 0.95))
            _sik(r, meret=(1.4, 0.95), dolt=62, szin=KEK, atlatszo=0.12, reteg=1)
            r.vonal((-1.4, 0, 0), (1.4, 0, 0), sz=1.9, szin=PIROS, reteg=2)
            if cimkek:
                r.felirat((-1.35, -0.8, 0), "α", dx=-4, dy=14, szin=SZURKE, meret=13)
                r.felirat((-1.3, 0, 0.78), "β", dx=-6, dy=0, szin=KEK, meret=13, horgony="end")
                r.felirat((1.4, 0, 0), "p", dx=10, dy=6, szin=PIROS, horgony="start")
        else:
            _sik(r, z=0.0, meret=(1.4, 0.95))
            _sik(r, z=0.95, meret=(1.4, 0.95), szin=KEK, atlatszo=0.12, reteg=1)
            if cimkek:
                r.felirat((-1.35, -0.8, 0), "α", dx=-4, dy=14, szin=SZURKE, meret=13)
                r.felirat((-1.35, -0.8, 0.95), "β", dx=-4, dy=14, szin=KEK, meret=13)
    elif tipus == "dieder":
        # Az ÉL a mélységi (y) irányba fut, így a lapszöget szemből látjuk.
        h_, m_ = 1.25, 1.30
        fok = 68
        c = math.cos(math.radians(fok)); sn = math.sin(math.radians(fok))
        also = [(0, -h_, 0), (m_, -h_, 0), (m_, h_, 0), (0, h_, 0)]
        felso = [(0, -h_, 0), (m_ * c, -h_, m_ * sn), (m_ * c, h_, m_ * sn), (0, h_, 0)]
        r.sokszog(also, kitolt=SZURKE, szin=SZURKE, sz=1.3, atlatszo=0.10, reteg=0)
        r.sokszog(felso, kitolt=KEK, szin=KEK, sz=1.3, atlatszo=0.12, reteg=1)
        r.vonal((0, -h_, 0), (0, h_, 0), sz=2.2, szin=PIROS, reteg=2)
        szar = 0.85
        r.vonal((0, 0, 0), (szar, 0, 0), szin=TINTA, sz=2.0, reteg=2)
        r.vonal((0, 0, 0), (szar * c, 0, szar * sn), szin=TINTA, sz=2.0, reteg=2)
        r.derekszog((0, 0, 0), (szar, 0, 0), (0, h_, 0), szin=SZURKE, meret=11)
        if cimkek:
            kx = szar * 0.62 * (1 + c) / 2
            kz = szar * 0.62 * sn / 2
            r.felirat((kx, 0, kz), "φ", dx=2, dy=6, szin=BOROSTYAN, meret=14, horgony="middle")
            r.felirat((0, -h_, 0), "p", dx=-8, dy=12, szin=PIROS, horgony="end")
            r.felirat((m_, h_, 0), "α", dx=10, dy=6, szin=SZURKE, meret=13, horgony="start")
            r.felirat((m_ * c, h_, m_ * sn), "β", dx=6, dy=-6, szin=KEK, meret=13,
                      horgony="start")
        r.befoglal(*also, *felso)
    return r.kesz()


# ---------------------------------------------------------------------
# 6c. Hálók — a test síkba kiterítve (2D, vetítés nélkül)
# ---------------------------------------------------------------------

def _fej2(w, h, leiras):
    return [f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
            f'aria-label="{leiras}">']


_TESTNEV = {"kocka": "kocka", "hasab": "hasáb", "gula": "gúla",
            "henger": "henger", "kup": "kúp"}


def svg_halo(test="kocka", n=4, hibas=False, w=340, h=260, leiras=None):
    """Kiterített háló: `test` = "kocka" | "hasab" | "gula".

    `hibas=True` (csak kockánál): olyan hatnégyzetes alakzat, amely NEM hajtható
    kockává — a térlátás-kvízhez.
    """
    ki = _fej2(w, h, leiras or f"A {_TESTNEV.get(test, test)} hálója síkba kiterítve")
    def negyzet(x, y, o, szin=ZOLD, felirat=""):
        ki.append(f'  <rect x="{x:.1f}" y="{y:.1f}" width="{o:.1f}" height="{o:.1f}" '
                  f'fill="{szin}" fill-opacity="0.10" stroke="{TINTA}" stroke-width="1.4"/>')
        if felirat:
            ki.append(f'  <text x="{x + o/2:.1f}" y="{y + o/2 + 4:.1f}" font-size="11" '
                      f'fill="{SZURKE}" text-anchor="middle">{felirat}</text>')
    if test == "kocka":
        o = min(w / 5.0, h / 4.6)
        bx, by = (w - 4 * o) / 2, (h - 3 * o) / 2
        if not hibas:
            # kereszt alakú kiterítés
            for i in range(4):
                negyzet(bx + i * o, by + o, o)
            negyzet(bx + o, by, o)
            negyzet(bx + o, by + 2 * o, o)
        else:
            # „lépcsős" alakzat: hat négyzet, de nem hajtható kockává
            for i in range(4):
                negyzet(bx + i * o, by + o, o)
            negyzet(bx, by, o)
            negyzet(bx + o, by, o)
    elif test == "hasab":
        # két szabályos n-szög + a palást osztott téglalapja
        o = min(w / (n + 2.2), h / 3.4)
        m = o * 1.5
        bx, by = (w - n * o) / 2, (h - m) / 2
        ki.append(f'  <rect x="{bx:.1f}" y="{by:.1f}" width="{n * o:.1f}" height="{m:.1f}" '
                  f'fill="{ZOLD}" fill-opacity="0.08" stroke="{TINTA}" stroke-width="1.5"/>')
        for i in range(1, n):
            ki.append(f'  <line x1="{bx + i * o:.1f}" y1="{by:.1f}" x2="{bx + i * o:.1f}" '
                      f'y2="{by + m:.1f}" stroke="{HALVANY}" stroke-width="1.1"/>')
        # A két alaplap ÉLBEN csatlakozik a paláshoz: a felső a bal szélső osztás fölé,
        # az alsó a jobb szélső osztás alá, mindkettő a saját oldalára illesztve.
        R = o / (2 * math.sin(math.pi / n))
        rho = o / (2 * math.tan(math.pi / n))
        for jel, xk in ((-1, bx + o / 2), (1, bx + (n - 0.5) * o)):
            cy = by - rho if jel < 0 else by + m + rho
            kezd = math.pi / 2 - math.pi / n if jel < 0 else -math.pi / 2 - math.pi / n
            pts = " ".join(f"{xk + R * math.cos(kezd - jel * 2*math.pi*k/n):.1f},"
                           f"{cy - R * math.sin(kezd - jel * 2*math.pi*k/n):.1f}"
                           for k in range(n))
            ki.append(f'  <polygon points="{pts}" fill="{KEK}" fill-opacity="0.10" '
                      f'stroke="{TINTA}" stroke-width="1.4"/>')
        ki.append(f'  <text x="{bx + n * o / 2:.1f}" y="{by + m / 2 + 4:.1f}" font-size="12" '
                  f'fill="{SZURKE}" text-anchor="middle">palást</text>')
        ki.append(f'  <text x="{bx + n * o / 2:.1f}" y="{by + m + 15:.1f}" font-size="12" '
                  f'fill="{TINTA}" text-anchor="middle" font-style="italic" '
                  f'font-weight="600">K</text>')
        ki.append(f'  <text x="{bx - 9:.1f}" y="{by + m / 2 + 4:.1f}" font-size="12" '
                  f'fill="{TINTA}" text-anchor="end" font-style="italic" '
                  f'font-weight="600">H</text>')
    elif test == "gula":
        o = min(w, h) * 0.30
        cx, cy = w / 2, h / 2
        x0, y0 = cx - o / 2, cy - o / 2
        negyzet(x0, y0, o, szin=KEK, felirat="alaplap")
        mo = o * 0.78
        haromszogek = [
            ((x0, y0), (x0 + o, y0), (cx, y0 - mo)),
            ((x0, y0 + o), (x0 + o, y0 + o), (cx, y0 + o + mo)),
            ((x0, y0), (x0, y0 + o), (x0 - mo, cy)),
            ((x0 + o, y0), (x0 + o, y0 + o), (x0 + o + mo, cy)),
        ]
        for t in haromszogek:
            pts = " ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in t)
            ki.append(f'  <polygon points="{pts}" fill="{ZOLD}" fill-opacity="0.10" '
                      f'stroke="{TINTA}" stroke-width="1.4"/>')
    elif test == "henger":
        # palást = téglalap (2rπ × H) + két alapkör
        rr = min(w * 0.115, h * 0.16)
        tw, th = 2 * math.pi * rr, rr * 2.4
        bx, by = (w - tw) / 2, (h - th) / 2
        ki.append(f'  <rect x="{bx:.1f}" y="{by:.1f}" width="{tw:.1f}" height="{th:.1f}" '
                  f'fill="{ZOLD}" fill-opacity="0.08" stroke="{TINTA}" stroke-width="1.5"/>')
        for cy2 in (by - rr - 3, by + th + rr + 3):
            ki.append(f'  <circle cx="{bx + tw / 2:.1f}" cy="{cy2:.1f}" r="{rr:.1f}" '
                      f'fill="{KEK}" fill-opacity="0.10" stroke="{TINTA}" '
                      f'stroke-width="1.4"/>')
        ki.append(f'  <text x="{bx + tw / 2:.1f}" y="{by + th / 2 + 4:.1f}" font-size="12" '
                  f'fill="{SZURKE}" text-anchor="middle">palást</text>')
        ki.append(f'  <text x="{bx + tw / 2:.1f}" y="{by + th + 15:.1f}" font-size="12" '
                  f'fill="{TINTA}" text-anchor="middle" font-style="italic" '
                  f'font-weight="600">2rπ</text>')
        ki.append(f'  <text x="{bx - 9:.1f}" y="{by + th / 2 + 4:.1f}" font-size="12" '
                  f'fill="{TINTA}" text-anchor="end" font-style="italic" '
                  f'font-weight="600">H</text>')
    elif test == "kup":
        # palást = körcikk (sugara s, ívhossza 2rπ) + az alapkör
        R2 = min(w * 0.30, h * 0.42)
        r2 = R2 * 0.42                       # r / s arány → a középponti szög
        fi = 2 * math.pi * r2 / R2           # φ radiánban
        cx2, cy2 = w * 0.36, h * 0.52
        a1 = -fi / 2 - math.pi / 2
        a2 = fi / 2 - math.pi / 2
        p1 = (cx2 + R2 * math.cos(a1), cy2 + R2 * math.sin(a1))
        p2 = (cx2 + R2 * math.cos(a2), cy2 + R2 * math.sin(a2))
        nagy = 1 if fi > math.pi else 0
        ki.append(f'  <path d="M{cx2:.1f},{cy2:.1f} L{p1[0]:.1f},{p1[1]:.1f} '
                  f'A{R2:.1f},{R2:.1f} 0 {nagy} 1 {p2[0]:.1f},{p2[1]:.1f} z" '
                  f'fill="{ZOLD}" fill-opacity="0.10" stroke="{TINTA}" stroke-width="1.5"/>')
        ki.append(f'  <text x="{cx2:.1f}" y="{cy2 - R2 * 0.55:.1f}" font-size="12" '
                  f'fill="{SZURKE}" text-anchor="middle">palást</text>')
        ki.append(f'  <text x="{cx2 + (p1[0] - cx2) * 0.62 - 12:.1f}" '
                  f'y="{cy2 + (p1[1] - cy2) * 0.62 + 4:.1f}" '
                  f'font-size="12" fill="{TINTA}" text-anchor="middle" '
                  f'font-style="italic" font-weight="600">s</text>')
        ki.append(f'  <text x="{cx2:.1f}" y="{cy2 + 16:.1f}" font-size="12" '
                  f'fill="{BOROSTYAN}" text-anchor="middle" font-style="italic" '
                  f'font-weight="600">φ</text>')
        ki.append(f'  <circle cx="{w * 0.80:.1f}" cy="{cy2:.1f}" r="{r2:.1f}" '
                  f'fill="{KEK}" fill-opacity="0.10" stroke="{TINTA}" stroke-width="1.4"/>')
        ki.append(f'  <text x="{w * 0.80:.1f}" y="{cy2 + r2 + 16:.1f}" font-size="12" '
                  f'fill="{SZURKE}" text-anchor="middle">alapkör</text>')
    ki.append("</svg>")
    return "\n".join(ki)


# ---------------------------------------------------------------------
# 6d. Az öt szabályos (platóni) test — drótváz-ikonsor
# ---------------------------------------------------------------------

_FI = (1 + 5 ** 0.5) / 2


def _platoni_csucsok(nev):
    f = _FI
    if nev == "tetraeder":
        return [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
    if nev == "kocka":
        return [(x, y, z) for x in (-1, 1) for y in (-1, 1) for z in (-1, 1)]
    if nev == "oktaeder":
        return [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    if nev == "dodekaeder":
        p = [(x, y, z) for x in (-1, 1) for y in (-1, 1) for z in (-1, 1)]
        p += [(0, y / f, z * f) for y in (-1, 1) for z in (-1, 1)]
        p += [(x / f, y * f, 0) for x in (-1, 1) for y in (-1, 1)]
        p += [(x * f, 0, z / f) for x in (-1, 1) for z in (-1, 1)]
        return p
    if nev == "ikozaeder":
        p = [(0, y, z * f) for y in (-1, 1) for z in (-1, 1)]
        p += [(x, y * f, 0) for x in (-1, 1) for y in (-1, 1)]
        p += [(x * f, 0, z) for x in (-1, 1) for z in (-1, 1)]
        return p
    raise ValueError(nev)


def _elek(csucsok, tur=1e-6):
    """Élek = a legrövidebb csúcstávolsággal összekötött párok (szabályos testre pontos)."""
    def d(a, b):
        return math.dist(a, b)
    tavok = [d(csucsok[i], csucsok[j])
             for i in range(len(csucsok)) for j in range(i + 1, len(csucsok))]
    e_min = min(tavok)
    return [(i, j) for i in range(len(csucsok)) for j in range(i + 1, len(csucsok))
            if abs(d(csucsok[i], csucsok[j]) - e_min) < 1e-6 + tur]


def svg_platoni(w=560, h=140, leiras="Az öt szabályos poliéder: tetraéder, kocka, "
                                     "oktaéder, dodekaéder, ikozaéder", nevek=True):
    """Az öt szabályos test drótváz-ikonja egy sorban. A hátrébb futó élek halványabbak."""
    testek = [("tetraéder", "tetraeder"), ("kocka", "kocka"), ("oktaéder", "oktaeder"),
              ("dodekaéder", "dodekaeder"), ("ikozaéder", "ikozaeder")]
    ki = _fej2(w, h, leiras)
    cella = w / len(testek)
    sugar = min(cella * 0.34, (h - (22 if nevek else 8)) * 0.42)
    for k, (cim, nev) in enumerate(testek):
        cs = _platoni_csucsok(nev)
        norm = max(math.dist((0, 0, 0), p) for p in cs)
        cs = [(p[0] / norm, p[1] / norm, p[2] / norm) for p in cs]
        vet = [_vet(p) for p in cs]
        cx = cella * (k + 0.5)
        cy = (h - (20 if nevek else 0)) / 2
        # mélység a nézőirány szerint (a kavalier vetítés magja: y a „hátra")
        mely = [p[1] for p in cs]
        m0, m1 = min(mely), max(mely)
        for i, j in _elek(cs):
            x1, y1 = cx + vet[i][0] * sugar, cy - vet[i][1] * sugar
            x2, y2 = cx + vet[j][0] * sugar, cy - vet[j][1] * sugar
            t = ((mely[i] + mely[j]) / 2 - m0) / ((m1 - m0) or 1)
            op = 1.0 - 0.72 * t
            ki.append(f'  <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                      f'stroke="{TINTA}" stroke-width="1.2" opacity="{op:.2f}" '
                      'stroke-linecap="round"/>')
        if nevek:
            ki.append(f'  <text x="{cx:.1f}" y="{h - 5:.1f}" font-size="11" fill="{SZURKE}" '
                      f'text-anchor="middle">{cim}</text>')
    ki.append("</svg>")
    return "\n".join(ki)


# ---------------------------------------------------------------------
# 6e. Síkidomok, amelyek a testek alaplapjaként kellenek
# ---------------------------------------------------------------------

def svg_sikidom(tipus="trapez", a=1.0, c=0.55, m=0.55, n=6, w=340, h=210,
                leiras=None, cimkek=True):
    """`tipus` = "trapez" (magassággal) | "sokszog" (szabályos n-szög apotémával)."""
    SZOVEG = {"trapez": "Trapéz a párhuzamos oldalakkal és a magassággal",
              "sokszog": f"Szabályos {n} oldalú sokszög az apotémával és a köréírt kör sugarával"}
    ki = _fej2(w, h, leiras or SZOVEG.get(tipus, "Síkidom"))
    par = 30

    if tipus == "trapez":
        el = (a - c) / 2 + 0.12
        pts = [(0.0, 0.0), (a, 0.0), (a - el + 0.02, m), (el, m)]
        xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
        s = min((w - 2 * par) / (max(xs) - min(xs)), (h - 2 * par) / (max(ys) - min(ys)))
        def P(p):
            return (par + (p[0] - min(xs)) * s, h - par - (p[1] - min(ys)) * s)
        d = " ".join(f"{P(p)[0]:.1f},{P(p)[1]:.1f}" for p in pts)
        ki.append(f'  <polygon points="{d}" fill="{ZOLD}" fill-opacity="0.08" '
                  f'stroke="{TINTA}" stroke-width="1.6" stroke-linejoin="round"/>')
        talp = (el, 0.0)
        x1, y1 = P((el, m)); x2, y2 = P(talp)
        ki.append(f'  <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                  f'stroke="{PIROS}" stroke-width="1.4" stroke-dasharray="4 3"/>')
        j = 9
        ki.append(f'  <path d="M{x2 + j:.1f},{y2:.1f} L{x2 + j:.1f},{y2 - j:.1f} '
                  f'L{x2:.1f},{y2 - j:.1f}" fill="none" stroke="{PIROS}" stroke-width="1.1"/>')
        if cimkek:
            for p, sz, dx, dy, szin in (((a / 2, 0.0), "a", 0, 18, TINTA),
                                        (((a + 0.02) / 2, m), "b", 0, -8, TINTA),
                                        ((el, m / 2), "h", -8, 4, PIROS)):
                X, Y = P(p)
                ki.append(f'  <text x="{X + dx:.1f}" y="{Y + dy:.1f}" font-size="13" '
                          f'fill="{szin}" text-anchor="middle" font-style="italic" '
                          'font-weight="600">' + sz + '</text>')
    else:
        R = 1.0
        rho = R * math.cos(math.pi / n)
        kezd = -math.pi / 2 + math.pi / n
        pts = [(R * math.cos(kezd + 2 * math.pi * k / n),
                R * math.sin(kezd + 2 * math.pi * k / n)) for k in range(n)]
        s = min((w - 2 * par) / 2.0, (h - 2 * par) / 2.0)
        cx, cy = w / 2, h / 2
        def P(p):
            return (cx + p[0] * s, cy - p[1] * s)
        d = " ".join(f"{P(p)[0]:.1f},{P(p)[1]:.1f}" for p in pts)
        ki.append(f'  <polygon points="{d}" fill="{ZOLD}" fill-opacity="0.08" '
                  f'stroke="{TINTA}" stroke-width="1.6" stroke-linejoin="round"/>')
        for k in range(n):
            X, Y = P(pts[k])
            ki.append(f'  <line x1="{cx:.1f}" y1="{cy:.1f}" x2="{X:.1f}" y2="{Y:.1f}" '
                      f'stroke="{HALVANY}" stroke-width="1"/>')
        fel = ((pts[0][0] + pts[1][0]) / 2, (pts[0][1] + pts[1][1]) / 2)
        Xf, Yf = P(fel)
        ki.append(f'  <line x1="{cx:.1f}" y1="{cy:.1f}" x2="{Xf:.1f}" y2="{Yf:.1f}" '
                  f'stroke="{BOROSTYAN}" stroke-width="1.7"/>')
        X1, Y1 = P(pts[1])
        ki.append(f'  <line x1="{cx:.1f}" y1="{cy:.1f}" x2="{X1:.1f}" y2="{Y1:.1f}" '
                  f'stroke="{KEK}" stroke-width="1.7"/>')
        if cimkek:
            ki.append(f'  <text x="{(cx + Xf) / 2 - 10:.1f}" y="{(cy + Yf) / 2 + 12:.1f}" '
                      f'font-size="13" fill="{BOROSTYAN}" text-anchor="middle" '
                      'font-style="italic" font-weight="600">r</text>')
            ki.append(f'  <text x="{(cx + X1) / 2 + 10:.1f}" y="{(cy + Y1) / 2 - 4:.1f}" '
                      f'font-size="13" fill="{KEK}" text-anchor="middle" '
                      'font-style="italic" font-weight="600">R</text>')
            fx, fy = fel
            hossz = math.hypot(fx, fy) or 1.0
            Xa, Ya = P((fx * (1 + 0.16 / hossz), fy * (1 + 0.16 / hossz)))
            ki.append(f'  <text x="{Xa:.1f}" y="{Ya + 4:.1f}" font-size="13" fill="{TINTA}" '
                      'text-anchor="middle" font-style="italic" font-weight="600">a</text>')
    ki.append("</svg>")
    return "\n".join(ki)


# =====================================================================
# 9. Forgástestek — henger, kúp, csonkakúp, gömb, forgatás, összetett
#    JELÖLÉS-KÁNON (_JELOLESEK.md): r/R sugár · H testmagasság · s alkotó
# =====================================================================

LAPULT = 0.30          # az alapkör ellipszisének ry/rx aránya (rálátás)


def _ell(cx, cy, rx, ry, szin=TINTA, sz=1.6, kitolt="none", op=None, szaggat=None):
    d = f' stroke-dasharray="{szaggat}"' if szaggat else ""
    o = f' fill-opacity="{op}"' if (op is not None and kitolt != "none") else ""
    return (f'  <ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" '
            f'fill="{kitolt}"{o} stroke="{szin}" stroke-width="{sz}"{d}/>')


def _iv(cx, cy, rx, ry, elso=True, szin=TINTA, sz=1.6, szaggat=None):
    """Fél-ellipszis: `elso=True` az elülső (lefelé hajló), False a hátsó ív."""
    d = f' stroke-dasharray="{szaggat}"' if szaggat else ""
    sw = 1 if elso else 0
    return (f'  <path d="M{cx - rx:.1f},{cy:.1f} A{rx:.1f},{ry:.1f} 0 0 {sw} '
            f'{cx + rx:.1f},{cy:.1f}" fill="none" stroke="{szin}" '
            f'stroke-width="{sz}"{d}/>')


def _von(p, q, szin=TINTA, sz=1.6, szaggat=None):
    d = f' stroke-dasharray="{szaggat}"' if szaggat else ""
    return (f'  <line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" '
            f'stroke="{szin}" stroke-width="{sz}"{d}/>')


def _txt(p, szoveg, dx=0, dy=0, szin=TINTA, meret=13, horgony="middle", dolt=True):
    st = ' font-style="italic"' if dolt else ""
    return (f'  <text x="{p[0] + dx:.1f}" y="{p[1] + dy:.1f}" font-size="{meret}" '
            f'fill="{szin}" text-anchor="{horgony}"{st} font-weight="600">{szoveg}</text>')


def _dszog(sarok, ir1, ir2, szin=PIROS, meret=9):
    """Derékszög-jel a `sarok` pontban, az `ir1`/`ir2` pontok felé mutató irányban."""
    def egys(p):
        vx, vy = p[0] - sarok[0], p[1] - sarok[1]
        n = math.hypot(vx, vy) or 1
        return vx / n * meret, vy / n * meret
    ax, ay = egys(ir1)
    bx, by = egys(ir2)
    return (f'  <path d="M{sarok[0] + ax:.1f},{sarok[1] + ay:.1f} '
            f'L{sarok[0] + ax + bx:.1f},{sarok[1] + ay + by:.1f} '
            f'L{sarok[0] + bx:.1f},{sarok[1] + by:.1f}" fill="none" '
            f'stroke="{szin}" stroke-width="1.1"/>')


class _Forg:
    """2D-rajzoló forgástestekhez. Modellkoordináta: x jobbra, **y felfelé**,
    az origó az alaplap középpontja. A `P(x, y)` vált pixelre."""

    def __init__(self, w, h, leiras, szeles, magas, par=24, also_ry=0.0):
        self.w, self.h, self.leiras = w, h, leiras
        self.s = min((w - 2 * par) / max(szeles, 1e-9),
                     (h - 2 * par) / max(magas, 1e-9))
        self.cx = w / 2
        self.alap_y = h - par - also_ry * self.s
        self.ki = []

    def P(self, x, y):
        return (self.cx + x * self.s, self.alap_y - y * self.s)

    def ell(self, y, r, **kw):
        c = self.P(0, y)
        self.ki.append(_ell(c[0], c[1], r * self.s, r * self.s * LAPULT, **kw))

    def iv(self, y, r, elso=True, **kw):
        c = self.P(0, y)
        self.ki.append(_iv(c[0], c[1], r * self.s, r * self.s * LAPULT, elso, **kw))

    def von(self, p, q, **kw):
        self.ki.append(_von(self.P(*p), self.P(*q), **kw))

    def txt(self, p, szoveg, **kw):
        self.ki.append(_txt(self.P(*p), szoveg, **kw))

    def kesz(self):
        return "\n".join(_fej2(self.w, self.h, self.leiras) + self.ki + ["</svg>"])


def _plt(r, H):
    """A palást halvány kitöltése (henger) — a testszerűség kedvéért."""
    return None


def svg_henger(r=1.0, H=1.7, w=300, h=270, leiras="Egyenes henger",
               tengely=False, alkoto=False, sugar=True, magassag=True,
               tengelymetszet=False, parhuzamos_metszet=False, ferde=False,
               feliratok=None):
    """Egyenes (vagy `ferde=True` esetén ferde) körhenger.

    `sugar`/`magassag`/`alkoto` — az $r$, $H$, $s$ jelölések kiírása.
    `tengelymetszet` — a tengelyen átmenő téglalap kiemelve.
    `parhuzamos_metszet` — az alaplappal párhuzamos metszetkör kiemelve.
    """
    f = feliratok or {}
    d = 0.55 if ferde else 0.0             # a felső lap eltolása
    R = _Forg(w, h, leiras, 2 * r + abs(d) + 0.9, H + 2 * r * LAPULT + 0.5,
              also_ry=r * LAPULT)
    # palást
    p1, p2 = R.P(-r, 0), R.P(-r + d, H)
    q1, q2 = R.P(r, 0), R.P(r + d, H)
    ftop = R.P(d, H)
    R.ki.append(f'  <path d="M{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} '
                f'A{r * R.s:.1f},{r * R.s * LAPULT:.1f} 0 0 0 {q2[0]:.1f},{q2[1]:.1f} '
                f'L{q1[0]:.1f},{q1[1]:.1f} '
                f'A{r * R.s:.1f},{r * R.s * LAPULT:.1f} 0 0 1 {p1[0]:.1f},{p1[1]:.1f} z" '
                f'fill="{ZOLD}" fill-opacity="0.08" stroke="none"/>')
    if tengelymetszet:
        a1, a2 = R.P(-r, 0), R.P(r, 0)
        b1, b2 = R.P(-r + d, H), R.P(r + d, H)
        R.ki.append(f'  <polygon points="{a1[0]:.1f},{a1[1]:.1f} {a2[0]:.1f},{a2[1]:.1f} '
                    f'{b2[0]:.1f},{b2[1]:.1f} {b1[0]:.1f},{b1[1]:.1f}" fill="{KEK}" '
                    f'fill-opacity="0.18" stroke="{KEK}" stroke-width="1.6"/>')
    R.iv(0, r, elso=False, szaggat="5 4", szin=SZURKE)       # takart hátsó ív
    R.iv(0, r, elso=True)                                     # látható elülső ív
    R.von((-r, 0), (-r + d, H))
    R.von((r, 0), (r + d, H))
    if parhuzamos_metszet:
        R.ell(H * 0.55, r, szin=ZOLD, sz=1.6, kitolt=ZOLD, op=0.22)
    c = R.P(d, H)
    R.ki.append(_ell(c[0], c[1], r * R.s, r * R.s * LAPULT, kitolt="#ffffff", op=0.55))
    if tengely:
        R.von((0, 0), (d, H), szin=SZURKE, sz=1.2, szaggat="4 3")
    if sugar:
        R.von((0, 0), (r, 0), szin=LILA, sz=1.5)
        R.txt((r / 2, 0), f.get("r", "r"), dy=15, szin=LILA)
        R.ki.append('  <circle cx="%.1f" cy="%.1f" r="2.6" fill="%s"/>'
                    % (*R.P(0, 0), LILA))
    if magassag:
        x0 = -r - 0.28
        R.von((x0, 0), (x0, H), szin=PIROS, sz=1.4, szaggat="4 3")
        R.von((x0 - 0.07, 0), (x0 + 0.07, 0), szin=PIROS, sz=1.2)
        R.von((x0 - 0.07, H), (x0 + 0.07, H), szin=PIROS, sz=1.2)
        R.txt((x0, H / 2), f.get("H", "H"), dx=-7, szin=PIROS, horgony="end")
    if alkoto:
        R.von((r, 0), (r + d, H), szin=BOROSTYAN, sz=2.0)
        R.txt((r + d / 2, H / 2), f.get("s", "s"), dx=8, szin=BOROSTYAN, horgony="start")
    return R.kesz()


def svg_kup(r=1.0, H=1.9, w=300, h=280, leiras="Egyenes körkúp",
            alkoto=True, tengely=False, sugar=True, magassag=True,
            tengelymetszet=False, parhuzamos_metszet=False, ferde=False,
            haromszog=False, feliratok=None):
    """Egyenes (vagy ferde) körkúp. `haromszog=True`: a jellemző derékszögű
    háromszög ($r$, $H$, $s$) kiemelve."""
    f = feliratok or {}
    d = 0.7 if ferde else 0.0
    R = _Forg(w, h, leiras, 2 * r + abs(d) + 0.9, H + 2 * r * LAPULT + 0.45,
              also_ry=r * LAPULT)
    cs = (d, H)
    p1, q1 = R.P(-r, 0), R.P(r, 0)
    C = R.P(*cs)
    R.ki.append(f'  <path d="M{p1[0]:.1f},{p1[1]:.1f} L{C[0]:.1f},{C[1]:.1f} '
                f'L{q1[0]:.1f},{q1[1]:.1f} '
                f'A{r * R.s:.1f},{r * R.s * LAPULT:.1f} 0 0 1 {p1[0]:.1f},{p1[1]:.1f} z" '
                f'fill="{ZOLD}" fill-opacity="0.08" stroke="none"/>')
    if tengelymetszet:
        R.ki.append(f'  <polygon points="{p1[0]:.1f},{p1[1]:.1f} {q1[0]:.1f},{q1[1]:.1f} '
                    f'{C[0]:.1f},{C[1]:.1f}" fill="{KEK}" fill-opacity="0.18" '
                    f'stroke="{KEK}" stroke-width="1.6"/>')
    if haromszog:
        o = R.P(0, 0)
        R.ki.append(f'  <polygon points="{o[0]:.1f},{o[1]:.1f} {q1[0]:.1f},{q1[1]:.1f} '
                    f'{C[0]:.1f},{C[1]:.1f}" fill="{BOROSTYAN}" fill-opacity="0.16" '
                    f'stroke="none"/>')
    R.iv(0, r, elso=False, szaggat="5 4", szin=SZURKE)
    R.iv(0, r, elso=True)
    R.von((-r, 0), cs)
    R.von((r, 0), cs)
    if parhuzamos_metszet:
        k = 0.45
        R.ell(H * (1 - k), r * k, szin=ZOLD, sz=1.6, kitolt=ZOLD, op=0.22)
    if tengely or magassag or haromszog:
        R.von((0, 0), cs if ferde else (0, H), szin=SZURKE, sz=1.2, szaggat="4 3")
    if magassag:
        R.von((0, 0), (0, H), szin=PIROS, sz=1.5, szaggat="4 3")
        R.txt((0, H * 0.28), f.get("H", "H"), dx=-7, szin=PIROS, horgony="end")
        R.ki.append(_dszog(R.P(0, 0), R.P(0, H), R.P(r, 0)))
    if sugar:
        R.von((0, 0), (r, 0), szin=LILA, sz=1.5)
        R.txt((r / 2, 0), f.get("r", "r"), dy=15, szin=LILA)
    if alkoto:
        R.von((r, 0), cs, szin=BOROSTYAN, sz=2.0)
        R.txt(((r + d) / 2, H / 2), f.get("s", "s"), dx=9, dy=-2,
              szin=BOROSTYAN, horgony="start")
    R.ki.append('  <circle cx="%.1f" cy="%.1f" r="2.8" fill="%s"/>' % (*C, TINTA))
    return R.kesz()


def svg_csonkakup(R_=1.0, r=0.5, H=1.15, w=300, h=250, leiras="Csonkakúp",
                  alkoto=True, sugarak=True, magassag=True, kiegeszites=False,
                  trapez=False, tengelymetszet=False, feliratok=None):
    """Csonkakúp. `kiegeszites=True`: a levágott kúp szaggatva.
    `trapez=True`: a jellemző derékszögű háromszög ($H$, $R-r$, $s$) kiemelve."""
    f = feliratok or {}
    teljes = H * R_ / (R_ - r) if R_ > r else H
    magas = (teljes if kiegeszites else H) + 2 * R_ * LAPULT + 0.45
    F = _Forg(w, h, leiras, 2 * R_ + 1.0, magas, also_ry=R_ * LAPULT)
    p1, q1 = F.P(-R_, 0), F.P(R_, 0)
    p2, q2 = F.P(-r, H), F.P(r, H)
    F.ki.append(f'  <path d="M{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} '
                f'A{r * F.s:.1f},{r * F.s * LAPULT:.1f} 0 0 0 {q2[0]:.1f},{q2[1]:.1f} '
                f'L{q1[0]:.1f},{q1[1]:.1f} '
                f'A{R_ * F.s:.1f},{R_ * F.s * LAPULT:.1f} 0 0 1 {p1[0]:.1f},{p1[1]:.1f} z" '
                f'fill="{ZOLD}" fill-opacity="0.08" stroke="none"/>')
    if tengelymetszet:
        F.ki.append(f'  <polygon points="{p1[0]:.1f},{p1[1]:.1f} {q1[0]:.1f},{q1[1]:.1f} '
                    f'{q2[0]:.1f},{q2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{KEK}" '
                    f'fill-opacity="0.18" stroke="{KEK}" stroke-width="1.6"/>')
    if trapez:
        o, t = F.P(0, 0), F.P(0, H)
        F.ki.append(f'  <polygon points="{o[0]:.1f},{o[1]:.1f} {q1[0]:.1f},{q1[1]:.1f} '
                    f'{q2[0]:.1f},{q2[1]:.1f} {t[0]:.1f},{t[1]:.1f}" fill="{BOROSTYAN}" '
                    f'fill-opacity="0.16" stroke="none"/>')
        F.von((r, H), (R_, H), szin=SZURKE, sz=1.2, szaggat="3 3")
        F.txt(((r + R_) / 2, H), f.get("kul", "R − r"), dy=-6, szin=SZURKE, meret=12)
        F.ki.append(_dszog(F.P(R_, H), F.P(r, H), F.P(R_, 0), szin=SZURKE))
    if kiegeszites and R_ > r:
        cs = (0.0, teljes)
        F.von((-r, H), cs, szin=SZURKE, sz=1.3, szaggat="4 4")
        F.von((r, H), cs, szin=SZURKE, sz=1.3, szaggat="4 4")
        F.ki.append('  <circle cx="%.1f" cy="%.1f" r="2.4" fill="%s"/>'
                    % (*F.P(*cs), SZURKE))
    F.iv(0, R_, elso=False, szaggat="5 4", szin=SZURKE)
    F.iv(0, R_, elso=True)
    F.von((-R_, 0), (-r, H))
    F.von((R_, 0), (r, H))
    c = F.P(0, H)
    F.ki.append(_ell(c[0], c[1], r * F.s, r * F.s * LAPULT, kitolt="#ffffff", op=0.55))
    if magassag:
        F.von((0, 0), (0, H), szin=PIROS, sz=1.5, szaggat="4 3")
        F.txt((0, H / 2), f.get("H", "H"), dx=-7, szin=PIROS, horgony="end")
    if sugarak:
        F.von((0, 0), (R_, 0), szin=LILA, sz=1.5)
        F.txt((R_ / 2, 0), f.get("R", "R"), dy=15, szin=LILA)
        F.von((0, H), (-r, H), szin=LILA, sz=1.5)
        F.txt((-r / 2, H), f.get("r", "r"), dy=-7, szin=LILA)
    if alkoto:
        F.von((R_, 0), (r, H), szin=BOROSTYAN, sz=2.0)
        F.txt(((R_ + r) / 2, H / 2), f.get("s", "s"), dx=9, szin=BOROSTYAN,
              horgony="start")
    return F.kesz()


def svg_gomb(R_=1.0, w=280, h=260, leiras="Gömb", sik=None, sugar=True,
             metszetkor=False, focor=True, korulirt_henger=False,
             tavolsag=False, feliratok=None):
    """Gömb. `sik`: None | "metszo" | "erinto" | "elkerulo" — a sík helyzete.
    `metszetkor=True`: a metszetkör és a sugara ($r$) kiemelve."""
    f = feliratok or {}
    F = _Forg(w, h, leiras, 2 * R_ + 1.4 + (1.0 if sik else 0.0),
              2 * R_ + 0.6 + (0.5 if korulirt_henger else 0.0), also_ry=0.0)
    kp = (0.0, R_)                                   # a gömb középpontja
    C = F.P(*kp)
    if korulirt_henger:
        F.ki.append(f'  <rect x="{C[0] - R_ * F.s:.1f}" y="{C[1] - R_ * F.s:.1f}" '
                    f'width="{2 * R_ * F.s:.1f}" height="{2 * R_ * F.s:.1f}" '
                    f'fill="none" stroke="{SZURKE}" stroke-width="1.3" '
                    f'stroke-dasharray="5 4"/>')
        for yy in (0.0, 2 * R_):
            c2 = F.P(0, yy)
            F.ki.append(_ell(c2[0], c2[1], R_ * F.s, R_ * F.s * LAPULT,
                             szin=SZURKE, sz=1.3, szaggat="5 4"))
    F.ki.append(f'  <circle cx="{C[0]:.1f}" cy="{C[1]:.1f}" r="{R_ * F.s:.1f}" '
                f'fill="{ZOLD}" fill-opacity="0.08" stroke="{TINTA}" stroke-width="1.8"/>')
    if focor:
        F.ki.append(_ell(C[0], C[1], R_ * F.s, R_ * F.s * LAPULT, szin=SZURKE, sz=1.3))
    tav = {"metszo": 0.55, "erinto": 1.0, "elkerulo": 1.35}.get(sik or "", None)
    if tav is not None:
        y = R_ + tav * R_
        w2 = R_ * 1.5
        a, b = F.P(-w2, y), F.P(w2, y)
        F.ki.append(f'  <path d="M{a[0]:.1f},{a[1] + 9:.1f} L{a[0] + 22:.1f},{a[1] - 9:.1f} '
                    f'L{b[0]:.1f},{b[1] - 9:.1f} L{b[0] - 22:.1f},{b[1] + 9:.1f} z" '
                    f'fill="{KEK}" fill-opacity="0.12" stroke="{KEK}" stroke-width="1.5"/>')
        if sik == "metszo":
            rm = math.sqrt(max(R_ ** 2 - (tav * R_) ** 2, 0.0))
            c3 = F.P(0, y)
            F.ki.append(_ell(c3[0], c3[1], rm * F.s, rm * F.s * LAPULT,
                             szin=ZOLD, sz=1.8, kitolt=ZOLD, op=0.20))
            if metszetkor:
                vy = rm * LAPULT * 0.9
                F.von((0, y), (rm * 0.72, y - vy), szin=ZOLD, sz=1.7)
                F.txt((rm * 0.42, y - vy * 0.55), f.get("r", "r"), dx=2, dy=14,
                      szin=ZOLD)
        if tavolsag:
            F.von(kp, (0, y), szin=PIROS, sz=1.5, szaggat="4 3")
            F.txt((0, (kp[1] + y) / 2), f.get("d", "d"), dx=-8, dy=4, szin=PIROS,
                  horgony="end")
    if sugar:
        vx, vy = (R_ * 0.75, -R_ * 0.62) if sik else (R_ * 0.72, R_ * 0.70)
        F.von(kp, (vx, kp[1] + vy), szin=LILA, sz=1.7)
        F.txt((vx / 2, kp[1] + vy / 2), f.get("R", "R"), dx=8, dy=-2, szin=LILA,
              horgony="start")
        F.ki.append('  <circle cx="%.1f" cy="%.1f" r="2.8" fill="%s"/>' % (*C, TINTA))
    return F.kesz()


def svg_forgatas(tipus="teglalap", w=420, h=250, leiras=None, cimkek=True):
    """Síkidom + forgástengely → a keletkező forgástest (két panel, nyíllal).

    `tipus`: "teglalap" (→ henger) | "haromszog" (→ kúp) | "felkor" (→ gömb)
             | "trapez" (→ csonkakúp)
    """
    NEV = {"teglalap": ("téglalap", "henger"), "haromszog": ("derékszögű háromszög", "kúp"),
           "felkor": ("félkör", "gömb"), "trapez": ("derékszögű trapéz", "csonkakúp")}
    n1, n2 = NEV.get(tipus, NEV["teglalap"])
    leiras = leiras or f"A(z) {n1} forgatása a tengely körül: {n2}"
    ki = _fej2(w, h, leiras)
    bal_w = w * 0.42
    # ── bal panel: a síkidom és a tengely ──────────────────────────────
    cx, alap = bal_w * 0.55, h - 46
    S = min(bal_w * 0.30, (h - 96) / 2.0)
    def P(x, y):
        return (cx + x * S, alap - y * S)
    ki.append(_von((cx, alap + 22), (cx, alap - 2.6 * S), szin=SZURKE, sz=1.4,
                   szaggat="7 4"))
    ki.append(_txt((cx, alap + 36), "tengely", szin=SZURKE, meret=11, dolt=False))
    if tipus == "teglalap":
        pts = [P(0, 0), P(1.0, 0), P(1.0, 1.7), P(0, 1.7)]
        cim = [((0.5, 0), "r", 0, 15), ((1.0, 0.85), "H", 8, 4)]
    elif tipus == "haromszog":
        pts = [P(0, 0), P(1.0, 0), P(0, 1.9)]
        cim = [((0.5, 0), "r", 0, 15), ((0, 0.95), "H", -8, 4)]
    elif tipus == "felkor":
        A, B = P(0, 0), P(0, 2.0)
        ki.append(f'  <path d="M{A[0]:.1f},{A[1]:.1f} A{S:.1f},{S:.1f} 0 0 1 '
                  f'{B[0]:.1f},{B[1]:.1f} z" fill="{ZOLD}" fill-opacity="0.14" '
                  f'stroke="{TINTA}" stroke-width="1.7"/>')
        pts, cim = None, [((0.55, 1.0), "R", 4, 4)]
        ki.append(_von(P(0, 1.0), P(1.0, 1.0), szin=LILA, sz=1.5))
    else:
        pts = [P(0, 0), P(1.2, 0), P(0.6, 1.4), P(0, 1.4)]
        cim = [((0.6, 0), "R", 0, 15), ((0.3, 1.4), "r", 0, -7), ((0, 0.7), "H", -8, 4)]
    if pts:
        d = " ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in pts)
        ki.append(f'  <polygon points="{d}" fill="{ZOLD}" fill-opacity="0.14" '
                  f'stroke="{TINTA}" stroke-width="1.7"/>')
    if cimkek:
        for (mx, my), sz, dx, dy in cim:
            ki.append(_txt(P(mx, my), sz, dx, dy, szin=LILA if sz in "rR" else PIROS))
    # ── nyíl ──────────────────────────────────────────────────────────
    ny = h / 2
    ki.append(f'  <line x1="{bal_w + 4:.1f}" y1="{ny:.1f}" x2="{bal_w + 40:.1f}" '
              f'y2="{ny:.1f}" stroke="{TINTA}" stroke-width="1.8" '
              f'marker-end="url(#nyil2)"/>')
    ki.insert(1, '  <defs><marker id="nyil2" viewBox="0 0 8 8" refX="6" refY="4" '
                 'markerWidth="6" markerHeight="6" orient="auto">'
                 f'<path d="M0,0 L8,4 L0,8 z" fill="{TINTA}"/></marker></defs>')
    # ── jobb panel: a keletkező test ──────────────────────────────────
    jw, jx = w - bal_w - 52, bal_w + 52
    gen = {"teglalap": lambda: svg_henger(1.0, 1.7, w=int(jw), h=h, sugar=cimkek,
                                          magassag=cimkek, leiras=n2),
           "haromszog": lambda: svg_kup(1.0, 1.9, w=int(jw), h=h, alkoto=False,
                                        sugar=cimkek, magassag=cimkek, leiras=n2),
           "felkor": lambda: svg_gomb(1.0, w=int(jw), h=h, sugar=cimkek, leiras=n2),
           "trapez": lambda: svg_csonkakup(1.2, 0.6, 1.4, w=int(jw), h=h, alkoto=False,
                                           sugarak=cimkek, magassag=cimkek, leiras=n2)}
    belso = gen[tipus]().split("\n")[1:-1]
    ki.append(f'  <g transform="translate({jx:.1f},0)">')
    ki.extend("  " + s for s in belso if not s.strip().startswith("<defs"))
    ki.append("  </g>")
    ki.append("</svg>")
    return "\n".join(ki)


def svg_osszetett(tipus="henger-felgomb", w=300, h=290, leiras=None, cimkek=True,
                  feliratok=None):
    """Összetett forgástestek.

    `tipus`: "henger-felgomb" (víztorony) | "henger-kup" (torony/tölcsér)
             | "cso" (üreges henger) | "kup-kup" (átfogó körüli forgatás)
             | "furt-henger" (hengerből kifúrt kúp)
    """
    f = feliratok or {}
    NEV = {"henger-felgomb": "Henger félgömb tetővel", "henger-kup": "Henger kúp tetővel",
           "cso": "Cső: üreges henger", "kup-kup": "Két kúp közös alaplappal",
           "furt-henger": "Hengerből kifúrt kúp"}
    leiras = leiras or NEV.get(tipus, "Összetett forgástest")
    r, H = 1.0, 1.5
    if tipus == "kup-kup":
        F = _Forg(w, h, leiras, 2 * r + 1.0, 2 * H + 2 * r * LAPULT,
                  also_ry=H + r * LAPULT)
        for elo, cs in ((True, (0.0, H)), (True, (0.0, -H))):
            p1, q1, C = F.P(-r, 0), F.P(r, 0), F.P(*cs)
            F.ki.append(f'  <path d="M{p1[0]:.1f},{p1[1]:.1f} L{C[0]:.1f},{C[1]:.1f} '
                        f'L{q1[0]:.1f},{q1[1]:.1f} z" fill="{ZOLD}" fill-opacity="0.08" '
                        f'stroke="{TINTA}" stroke-width="1.6"/>')
        F.ell(0, r, szin=SZURKE, sz=1.4, szaggat="5 4")
        F.iv(0, r, elso=True)
        if cimkek:
            F.von((0, 0), (r, 0), szin=LILA, sz=1.5)
            F.txt((r / 2, 0), f.get("r", "r"), dy=-6, szin=LILA)
            F.von((0, 0), (0, H), szin=PIROS, sz=1.4, szaggat="4 3")
            F.txt((0, H / 2), f.get("H", "H"), dx=-7, szin=PIROS, horgony="end")
        return F.kesz()

    magas = {"henger-felgomb": H + r, "henger-kup": H + 1.0, "cso": H,
             "furt-henger": H}[tipus] + 2 * r * LAPULT + 0.4
    F = _Forg(w, h, leiras, 2 * r + 1.0, magas, also_ry=r * LAPULT)
    p1, q1 = F.P(-r, 0), F.P(r, 0)
    p2, q2 = F.P(-r, H), F.P(r, H)
    F.ki.append(f'  <path d="M{p1[0]:.1f},{p1[1]:.1f} L{p2[0]:.1f},{p2[1]:.1f} '
                f'A{r * F.s:.1f},{r * F.s * LAPULT:.1f} 0 0 0 {q2[0]:.1f},{q2[1]:.1f} '
                f'L{q1[0]:.1f},{q1[1]:.1f} '
                f'A{r * F.s:.1f},{r * F.s * LAPULT:.1f} 0 0 1 {p1[0]:.1f},{p1[1]:.1f} z" '
                f'fill="{ZOLD}" fill-opacity="0.08" stroke="none"/>')
    F.iv(0, r, elso=False, szaggat="5 4", szin=SZURKE)
    F.iv(0, r, elso=True)
    F.von((-r, 0), (-r, H))
    F.von((r, 0), (r, H))
    if tipus == "henger-felgomb":
        c = F.P(0, H)
        F.ki.append(f'  <path d="M{c[0] - r * F.s:.1f},{c[1]:.1f} '
                    f'A{r * F.s:.1f},{r * F.s:.1f} 0 0 1 {c[0] + r * F.s:.1f},{c[1]:.1f}" '
                    f'fill="{ZOLD}" fill-opacity="0.10" stroke="{TINTA}" '
                    f'stroke-width="1.7"/>')
        F.ki.append(_ell(c[0], c[1], r * F.s, r * F.s * LAPULT, szin=SZURKE, sz=1.3,
                         szaggat="5 4"))
        if cimkek:
            F.txt((0, H + r * 0.62), f.get("felgomb", "félgömb"), szin=SZURKE, meret=11,
                  dolt=False)
    elif tipus == "henger-kup":
        cs = (0.0, H + 1.0)
        C = F.P(*cs)
        F.ki.append(f'  <path d="M{p2[0]:.1f},{p2[1]:.1f} L{C[0]:.1f},{C[1]:.1f} '
                    f'L{q2[0]:.1f},{q2[1]:.1f} z" fill="{ZOLD}" fill-opacity="0.10" '
                    f'stroke="{TINTA}" stroke-width="1.7"/>')
        F.ki.append(_ell(*F.P(0, H), r * F.s, r * F.s * LAPULT, szin=SZURKE, sz=1.3,
                         szaggat="5 4"))
    elif tipus in ("cso", "furt-henger"):
        c = F.P(0, H)
        F.ki.append(_ell(c[0], c[1], r * F.s, r * F.s * LAPULT, kitolt="#ffffff", op=0.6))
        rb = 0.55 * r
        if tipus == "cso":
            F.ki.append(_ell(c[0], c[1], rb * F.s, rb * F.s * LAPULT, kitolt=SZURKE,
                             op=0.14, szin=TINTA, sz=1.5))
            F.von((-rb, H), (-rb, 0.12), szin=SZURKE, sz=1.3, szaggat="4 3")
            F.von((rb, H), (rb, 0.12), szin=SZURKE, sz=1.3, szaggat="4 3")
            if cimkek:
                F.von((0, H), (rb, H), szin=LILA, sz=1.5)
                F.txt((rb / 2, H), f.get("r", "r"), dy=-8, szin=LILA)
                F.von((0, 0), (-r, 0), szin=LILA, sz=1.5)
                F.txt((-r / 2, 0), f.get("R", "R"), dy=15, szin=LILA)
                x0 = r + 0.26
                F.von((x0, 0), (x0, H), szin=PIROS, sz=1.4, szaggat="4 3")
                F.txt((x0, H / 2), f.get("H", "H"), dx=7, szin=PIROS, horgony="start")
        else:
            F.von((-rb, H), (0, 0), szin=SZURKE, sz=1.4, szaggat="4 3")
            F.von((rb, H), (0, 0), szin=SZURKE, sz=1.4, szaggat="4 3")
            F.ki.append(_ell(c[0], c[1], rb * F.s, rb * F.s * LAPULT, szin=SZURKE,
                             sz=1.4, szaggat="4 3"))
    if cimkek and tipus not in ("cso",):
        F.von((0, 0), (r, 0), szin=LILA, sz=1.5)
        F.txt((r / 2, 0), f.get("r", "r"), dy=15, szin=LILA)
        x0 = -r - 0.26
        F.von((x0, 0), (x0, H), szin=PIROS, sz=1.4, szaggat="4 3")
        F.txt((x0, H / 2), f.get("H", "H"), dx=-7, szin=PIROS, horgony="end")
    return F.kesz()
