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

__all__ = ["svg_szamegyenes", "svg_haromszog", "svg_venn"]


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
