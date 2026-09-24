# -*- coding: utf-8 -*-
"""4e/02 — B es C blokk: a fuggveny hatarerteke (B1), hatarertek-szamitas (B2), hatarertek a vegtelenben (B3),
aszimptotak (C1). Mentor: Nagol (Ved Vilmos a 0/0-nal es a falnal). Kuldetes: Az Aszimptota-fal Attorese.
Specifikacio: projektek/4e/munkafajlok/narrativa_02-fuggvenyek.md
Tiltott adatok: a 24/25–26/27 felmerok kifejezesei (Felmero_elemzes_es_ajanlasok_Fuggvenyek.md) — lent ellenorizve."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra, svg_fuggvenyek

T = dict(tagozat="4e", mappa="02-fuggvenyek", temakor="Függvények")
KUL = "Az Aszimptota-fal Áttörése"
FH = "feladatok-hatarertek-aszimptota.html"
E401 = "../01-sorozatok-hatarerteke/"
E202 = "../../2e/02-masodfoku-egyenletek-es-fuggvenyek/"
KEK, BORO, ZOLD, PIROS, LILA, SOT, SZURKE = "#3b82f6", "#f59e0b", "#047857", "#ef4444", "#7c3aed", "#0f172a", "#64748b"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(k_h, k_c, n_h, n_c, tagozat="4e")


def NEHEZ(tol, ig, szoveg):
    return (f'<p class="lead">⚔️ <b>Az ötösért:</b> {szoveg} — '
            f'<a href="{FH}#nehez-{tol}">Zsoldos-lista II., nehéz {tol}–{ig}</a>.</p>')


# ---------------------------------------------------------------- önteszt
from sympy import symbols, limit, oo, sqrt, simplify, sympify, sin, Rational as R, fraction, together, solve
E = []


def chk(nev, kapott, vart):
    ok = (list(kapott) == list(vart)) if isinstance(kapott, (list, tuple)) else \
        (kapott == vart or simplify(kapott - vart) == 0)
    if not ok:
        E.append((nev, kapott, vart))


x = symbols("x", real=True)
Ex = lambda s: sympify(s, locals={"x": x})
def L(s, a, d="+-"):
    """Határérték; x → −∞ esetén x ↦ −x helyettesítéssel (a sympy 1.14 a limit(2**x, x, -oo)-ra hibásan oo-t ad)."""
    if a == -oo:
        return limit(Ex(s).subs(x, -x), x, oo)
    return limit(Ex(s), x, a) if d == "+-" else limit(Ex(s), x, a, d)
# B1
chk("B1-tabla", [round(float(Ex("(x**2-1)/(x-1)").subs(x, t)), 3) for t in (0.9, 0.99, 0.999, 1.001, 1.01, 1.1)],
    [1.9, 1.99, 1.999, 2.001, 2.01, 2.1])
chk("B1-lim", L("(x**2-1)/(x-1)", 1), 2)
chk("B1-ugras", [L("x+2", 1, "-"), L("x-1", 1, "+")], [3, 0])
# B2
chk("B2-behely", [L("(x**2+1)/(x+3)", 2), L("sqrt(x+4)", 5)], [1, 3])
chk("B2-0per0-1", [simplify(Ex("(x**2+x-6)/(x+3)") - Ex("x-2")), L("(x**2+x-6)/(x+3)", -3)], [0, -5])
chk("B2-0per0-2", [simplify(Ex("(x**2-4)/(x**2-3*x+2)") - Ex("(x+2)/(x-1)")), L("(x**2-4)/(x**2-3*x+2)", 2)], [0, 4])
chk("B2-gyok-1", L("(sqrt(x)-2)/(x-4)", 4), R(1, 4))
chk("B2-gyok-2", L("x/(sqrt(x+1)-1)", 0), 2)
chk("B2-c0", [L("(x+2)/(x-1)", 1, "-"), L("(x+2)/(x-1)", 1, "+")], [-oo, oo])
chk("B2-kviz-1", L("(x**2-9)/(x-3)", 3), 6)
chk("B2-kviz-3", L("1/(x-2)", 2, "-"), -oo)
chk("B2-kviz-2", L("(x**2-3*x)/(x-3)", 3), 3)
# B3
chk("B3-1", [L("(2*x**2-x)/(x**2+3)", oo), L("(5*x+1)/(x**2+4)", oo), L("(x**3+x)/(2*x**2-1)", oo)], [2, 0, oo])
chk("B3-2", [L("(x**3+x)/(2*x**2-1)", -oo), L("(x**4+1)/(x**2+x)", -oo), L("(2*x**2-x)/(x**2+3)", -oo)], [-oo, oo, 2])
chk("B3-elemi", [L("2**x", oo), L("2**x", -oo), L("1/x**2", oo)], [oo, 0, 0])
chk("B3-sinx", [round(math.sin(t) / t, 5) for t in (0.5, 0.1, 0.01)], [0.95885, 0.99833, 0.99998])
chk("B3-kviz", [L("(1-x**3)/(x**2+2)", oo), L("(1-x**3)/(x**2+2)", -oo)], [-oo, oo])


def asz(s):
    f = Ex(s); sz, nv = fraction(together(f))
    fu = [r for r in solve(nv, x) if sz.subs(x, r) != 0]
    h = limit(f, x, oo)
    k = limit(f / x, x, oo)
    return fu, (None if h in (oo, -oo) else h), ((k, limit(f - k * x, x, oo)) if h in (oo, -oo) else None)


chk("C1-fugg", asz("(2*x+1)/(x-3)"), ([3], 2, None))
chk("C1-oldal", [L("(2*x+1)/(x-3)", 3, "-"), L("(2*x+1)/(x-3)", 3, "+")], [-oo, oo])
chk("C1-lyuk", asz("(x**2-4)/(x-2)")[0], [])
chk("C1-metsz", [asz("x/(x**2+1)")[1], Ex("x/(x**2+1)").subs(x, 0)], [0, 0])
chk("C1-ferde", asz("(x**2+1)/(x-1)"), ([1], None, (1, 1)))
chk("C1-teljes", asz("(2*x**2+x)/(x-1)"), ([1], None, (2, 3)))
chk("C1-kviz-1", asz("(x**2-25)/(x+5)")[0], [])

# tiltott adatok: a régi és az idei felmérők kifejezései szó szerint nem szerepelhetnek
REGI = ["(3*x+14)/(2*x**2-5*x-28)", "(x+5)/(x**2+4*x-5)", "(x**2-144)/(x-12)", "(sqrt(x+9)-1)/(x+8)",
        "(5*x-15)/(x-6)", "(x-13)/(sqrt(x-4)-3)", "(x**2-3*x-10)/(x-5)", "(x-3)/(x+2)", "(x-3)/(x**2+4*x-21)",
        "(x**2-49)/(x+7)", "(sqrt(x+5)-4)/(x-11)", "(2*x+25)/(x+8)", "(x-4)/(x**2-x-12)", "(5*x-8)/(3*x+3)",
        "(x**2-121)/(x-11)", "(sqrt(x-3)-1)/(x-4)", "(5*x-18)/(x-5)", "(x+2)/(x**2-x-6)", "(3*x+1)/(2*x-2)",
        "(x-4)/(x**2-16)", "(x-5)/(x**2-25)", "(3*x+2)/(x-5)", "(2*x-3)/(12*x+24)", "(x**2-3)/(x+5)",
        "(2*x**2-3)/(x+5)", "(3*x+5)/(4*x-8)", "(x**2+x)/(x-2)", "(x+6)/(4*x-12)", "(2*x**2-5)/(x-2)",
        "(x-1)/(x+2)", "(2*x**2+1)/(2*x-5)", "(x+1)/(x-2)", "(2*x**2-1)/(2*x+8)", "(x**2-3)/(x+1)",
        "(2*x+1)/(2*x-12)", "(6*x+1)/(2*x-1)", "(2*x**2+1)/(2*x+4)", "(6*x**2+1)/(3*x-6)", "(x**2+1)/(3*x+9)",
        # 2026/27 (A, B, pótló)
        "(3*x**2-x+4)/(x+3)", "(x+4)/(x**2+7*x+12)", "(x**2-x-6)/(x**2-9)", "(sqrt(3*x+7)-4)/(x-3)",
        "(2*x+1)/(x-4)", "(6*x**3-4*x+1)/(3*x**3+2*x**2-5)", "(4*x-3)/(2*x+6)", "(x**2+3*x-2)/(x-1)",
        "(2*x**2+5*x-1)/(x-3)", "(x-5)/(x**2-2*x-15)", "(x**2+5*x+6)/(x**2-4)", "(sqrt(2*x+5)-3)/(x-2)",
        "(3*x-2)/(x+5)", "(4*x**2-7*x+2)/(5-2*x**2)", "(9*x+2)/(3*x-6)", "(x**2-2*x+5)/(x+2)",
        "(x**2+3*x+2)/(x+2)", "(x**2+4*x-5)/(2*x**2-2)", "(x-4)/(sqrt(2*x+1)-3)", "(x+3)/(4-2*x)",
        "(3*x**2+x)/(x**2-5*x+1)", "(8-2*x)/(x+3)", "(2*x**2+x-1)/(x+3)"]
PELDAK = ["(x**2-1)/(x-1)", "(x**2+1)/(x+3)", "(x**2+x-6)/(x+3)", "(x**2-4)/(x**2-3*x+2)", "(sqrt(x)-2)/(x-4)",
          "x/(sqrt(x+1)-1)", "(x+2)/(x-1)", "(x**2-9)/(x-3)", "1/(x-2)", "(2*x**2-x)/(x**2+3)", "(5*x+1)/(x**2+4)",
          "(x**3+x)/(2*x**2-1)", "(x**4+1)/(x**2+x)", "(1-x**3)/(x**2+2)", "(2*x+1)/(x-3)", "(x**2-4)/(x-2)",
          "x/(x**2+1)", "(x**2+1)/(x-1)", "(2*x**2+x)/(x-1)", "(x**2-25)/(x+5)", "(x**2-3*x)/(x-3)"]


def _alak(s):
    a, b = Ex(s).as_numer_denom()
    return (a.expand(), b.expand())


for p in PELDAK:
    for r_ in REGI:
        if _alak(p) == _alak(r_):
            E.append(("tiltott", p, r_))
assert not E, E
print("önteszt: OK")

# ---------------------------------------------------------------- ábrák
W, H = 360, 250


def fugg_vonal(svg, x0, xr, yr, w=W, h=H, szin=SZURKE):
    """Függőleges szaggatott egyenes (aszimptota) a svg_fuggvenyek() koordinátáiban."""
    bal, jobb, fent, lent = 26, 12, 14, 22
    X = 26 + (x0 - xr[0]) / (xr[1] - xr[0]) * (w - bal - jobb)
    vonal = (f'  <line x1="{X:.1f}" y1="{fent}" x2="{X:.1f}" y2="{h - lent}" stroke="{szin}" '
             'stroke-width="1.6" stroke-dasharray="6 4"/>')
    i = svg.find("  </g>") + len("  </g>")
    return svg[:i] + "\n" + vonal + svg[i:]


SVG_LYUK = svg_fuggvenyek(
    [(lambda t: t + 1, KEK, "y = (x² − 1)/(x − 1)", [(-1.6, 3.2)])],
    xr=(-2, 3.4), yr=(-1.2, 4.4), w=W, h=H,
    pontok=[(1, 2, "(1; 2)", "o:" + SOT, 8, 14)],
    leiras="Az y = (x² − 1)/(x − 1) grafikonja egy egyenes, amelyből hiányzik az (1; 2) pont (üres kör)")
XR2, YR2 = (-1, 5.4), (-0.8, 4.6)
SVG_TELI_URES = svg_fuggvenyek(
    [(lambda t: -t + 4, KEK, "g", [(-0.6, 4.4)])], xr=XR2, yr=YR2, w=W, h=H, jelmagyarazat=False,
    pontok=[(2, 2, "", "o:" + SOT), (2, 1, "", SOT)],
    leiras="A g függvény grafikonja: egy csökkenő egyenes, a (2; 2) pontban üres kör, alatta a (2; 1) pontban teli pont")
SVG_UGRAS = svg_fuggvenyek(
    [(lambda t: t + 2, KEK, "h", [(-2, 1)]), (lambda t: t - 1, KEK, "", [(1, 4.2)])],
    xr=(-2.4, 4.6), yr=(-1.2, 4.4), w=W, h=H, jelmagyarazat=False,
    pontok=[(1, 3, "", "o:" + SOT), (1, 0, "", SOT)],
    leiras="A h függvény grafikonja két félegyenes: balról az (1; 3) pont felé tart (üres kör), jobbról az (1; 0) "
           "pontból indul (teli pont)")
XP, YP = (-3.4, 5.4), (-6, 7)
SVG_POLUS = fugg_vonal(svg_fuggvenyek(
    [(lambda t: (t + 2) / (t - 1), KEK, "y = (x + 2)/(x − 1)", [(-3.2, 0.78), (1.22, 5.2)])],
    xr=XP, yr=YP, w=W, h=H,
    leiras="Az y = (x + 2)/(x − 1) grafikonja: az x = 1-től balra lefelé, jobbra felfelé tart a végtelenbe; a "
           "széleken az y = 1 egyeneshez simul"),
    1, XP, YP)
XV, YV = (-3.6, 9.6), (-5, 9)
SVG_FUGG_VIZSZ = fugg_vonal(svg_fuggvenyek(
    [(lambda t: (2 * t + 1) / (t - 3), KEK, "y = (2x + 1)/(x − 3)", [(-3.4, 2.45), (3.55, 9.4)]),
     (lambda t: 2, SZURKE, "y = 2", [(-3.4, 9.4)], "szaggatott")],
    xr=XV, yr=YV, w=380, h=260,
    leiras="Az y = (2x + 1)/(x − 3) grafikonja a szaggatott x = 3 és y = 2 aszimptotával"), 3, XV, YV, w=380, h=260)
SVG_METSZI = svg_fuggvenyek(
    [(lambda t: t / (t * t + 1), KEK, "y = x/(x² + 1)", [(-6, 6)])],
    xr=(-6.4, 6.4), yr=(-1, 1.2), w=380, h=180, egyseg=("1", ""),
    pontok=[(0, 0, "(0; 0)", SOT, 6, -8)],
    leiras="Az y = x/(x² + 1) grafikonja: a vízszintes aszimptota az x tengely, a görbe az origóban metszi")
XF, YF = (-4.4, 6.4), (-5, 9.4)
SVG_FERDE = fugg_vonal(svg_fuggvenyek(
    [(lambda t: (t * t + 1) / (t - 1), KEK, "y = (x² + 1)/(x − 1)", [(-4.2, 0.8), (1.2, 6.2)]),
     (lambda t: t + 1, SZURKE, "y = x + 1", [(-4.2, 6.2)], "szaggatott")],
    xr=XF, yr=YF, w=380, h=270,
    leiras="Az y = (x² + 1)/(x − 1) grafikonja a szaggatott x = 1 és y = x + 1 aszimptotával; a jobb ág az egyenes "
           "fölött, a bal ág alatta halad"), 1, XF, YF, w=380, h=270)
SVG_RECIPROK = svg_fuggvenyek(
    [(lambda t: 1 / t, LILA, "y = 1/x", [(-3.2, -0.22), (0.22, 3.2)])],
    xr=(-3.4, 3.4), yr=(-3.6, 3.6), w=320, h=240,
    leiras="Az y = 1/x hiperbola: ágai az x és az y tengelyhez simulnak, de nem érik el őket")

# ---------------------------------------------------------------- B1
B1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Nagol:</b> A sorozatoknál $n$ egyik természetes számról a következőre ugrált. Most $x$ folyamatosan fut — '
         'és néha egy olyan pont felé, ahol a függvénynek <b>nincs</b> értéke. <b>Véd Vilmos:</b> Akkor ott '
         'nincs határérték sem. <b>Nagol:</b> Dehogynem. A határérték nem azt kérdezi, mennyi a függvény a '
         'pontban, hanem azt, <b>mihez közelít</b>, ha egyre közelebb megyünk.'),
 ]),

 ("Emlékeztető: a sorozat határértéke", [
   r'<p class="lead">A sorozatoknál az $a_n$ tagok egy $A$ számhoz közelítettek, ha $n$ a végtelenbe tart: '
   r'bármilyen keskeny sávot rajzoltunk $A$ köré, egy tagtól kezdve mind benne voltak. A függvényeknél '
   r'ugyanez a kép, csak $x$ tetszőleges módon közelíthet egy $a$ számhoz. Ismétlés: '
   '<a href="' + E401 + 'tananyag-hatarertek-fogalma.html#def-hatarertek">a sorozat határértéke</a>.</p>',
 ]),

 ("Közelítés táblázattal és grafikonon", [
   r'<p class="lead">Vizsgáljuk meg az $f(x)=\dfrac{x^2-1}{x-1}$ függvényt az $x=1$ közelében. Az $1$-ben '
   r'nincs értelmezve (a nevező $0$) — de mi történik a közelében?</p>',
   doboz("pelda", "I.V.H. Akták — közelítés két oldalról",
         r'<div class="tblwrap"><table class="tt-table">'
         r'<tr><th>$x$</th><td>$0{,}9$</td><td>$0{,}99$</td><td>$0{,}999$</td><td>$1$</td><td>$1{,}001$</td>'
         r'<td>$1{,}01$</td><td>$1{,}1$</td></tr>'
         r'<tr><th>$f(x)$</th><td>$1{,}9$</td><td>$1{,}99$</td><td>$1{,}999$</td><td>—</td><td>$2{,}001$</td>'
         r'<td>$2{,}01$</td><td>$2{,}1$</td></tr></table></div>'
         r'<p>Balról és jobbról is a $2$-höz közelítenek az értékek. Az ok: ha $x\ne1$, akkor '
         r'$\dfrac{x^2-1}{x-1}=\dfrac{(x-1)(x+1)}{x-1}=x+1$, és ez az $1$ közelében a $2$ közelében van.</p>'
         r'<p><i>Véd Vilmos széljegyzete:</i> „a táblázat az $x=1$-et kihagyja — és mégis kijön a $2$.”</p>',
         hid="pelda-tablazat-fv"),
   abra(SVG_LYUK, 'A grafikon az $y=x+1$ egyenes, amelyből hiányzik az $(1;\\,2)$ pont: ott „lyuk” van.'),
   kviz(r'Az $f(x)=\dfrac{x^2-1}{x-1}$ az $x=1$-ben nincs értelmezve. Mit mondhatunk a $\lim\limits_{x\to1}f(x)$-ről?',
        [r'létezik, és $2$: a függvény értékei a $2$-höz tartanak',
         r'nem létezik, hiszen $f(1)$ sincs',
         r'$0$, mert a nevező $0$',
         r'$\dfrac00$, tehát $1$'], 0,
        jo="✔ A határérték a pont KÖRNYEZETÉBEN vett viselkedés: az 1-hez közeli x-ekre f(x) ≈ 2. "
           "Maga az f(1) nem számít.",
        nem="✘ A határértékhez nem kell, hogy a függvény a pontban értelmezve legyen: az 1 körüli "
            "x-ekre f(x) = x + 1 ≈ 2, tehát a határérték 2."),
 ]),

 ("A határérték — kimondva", [
   r'<p class="lead">A „közelít” szót most is pontossá tesszük — a sorozatok nyelvén, amelyet már ismerünk.</p>',
   doboz("definicio", "A függvény határértéke",
         r'<p>Legyen $f$ értelmezve az $a$ valamely környezetében, kivéve esetleg magát az $a$-t. '
         r'Az $f$ függvény határértéke az $a$ helyen az $A$ szám, ha bármely $a$-hoz tartó $(x_n)$ '
         r'sorozatra ($x_n\ne a$, $x_n\in D_f$) az $f(x_n)$ függvényértékek sorozata $A$-hoz tart. Jele: '
         r'$\lim\limits_{x\to a}f(x)=A$.</p>'
         r'<p>Szemléletesen: $f(x)$ akármilyen közel vihető $A$-hoz, ha $x$-et elég közel választjuk $a$-hoz '
         r'($x\ne a$).</p>', hid="def-fv-hatarertek"),
   r'<p>A definíció két fontos üzenete: az $x=a$ helyet <b>kihagyjuk</b> (a függvénynek ott nem is kell '
   r'értelmezve lennie), és <b>minden irányból</b> történő közelítésnek ugyanoda kell vezetnie.</p>',
 ]),

 ("Határérték ≠ helyettesítési érték", [
   r'<p class="lead">A grafikonon a <b>teli pont</b> a függvény értékét jelöli, az <b>üres pont</b> azt, '
   r'hogy ott a grafikonnak nincs pontja. A kettő ugyanannál az $x$-nél más magasságban is lehet.</p>',
   abra(SVG_TELI_URES, 'A $g$ függvény: az egyenesből a $(2;\\,2)$ pont hiányzik, és $g(2)=1$.'),
   doboz("pelda", "I.V.H. Akták — teli és üres pont",
         r'<p>Olvassuk le a $g$ grafikonjáról $g(2)$ értékét és a $\lim\limits_{x\to2}g(x)$ határértéket!</p>'
         r'<ul><li>$g(2)=1$ — ez a <b>teli</b> pont magassága;</li>'
         r'<li>$\lim\limits_{x\to2}g(x)=2$ — ahová a görbe mindkét oldalról tart, vagyis az <b>üres</b> pont magassága.</li></ul>'
         r'<p>A kettő különbözik: a határérték a pont környezetéről szól, a helyettesítési érték magáról a pontról.</p>',
         hid="pelda-teli-ures"),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>Véd Vilmos szerint „a határérték az, amit behelyettesítéssel kapok” — ezért a fenti grafikonra '
         r'$\lim\limits_{x\to2}g(x)=1$-et ír.</p>'
         r'<p><b>A határérték nem a pontbeli érték.</b> Sok függvénynél a kettő egyenlő (ezek a folytonos '
         r'függvények), de nem mindig: itt a görbe a $2$-höz tart, a teli pont pedig „kilóg”.</p>'),
   kviz(r'Mennyi a fenti $g$ függvényre a $\lim\limits_{x\to2}g(x)$ határérték?',
        [r'$2$', r'$1$', r'nem létezik, mert a grafikon megszakad', r'$1$ és $2$ is — a $2$-nél két pont van'], 0,
        jo="✔ A görbe mindkét oldalról a 2 magasságú üres ponthoz tart. A teli pont (g(2) = 1) a határértéket nem befolyásolja.",
        nem="✘ Nézd, hová tart a görbe, ha x balról és jobbról a 2-höz közelít: az üres ponthoz, a 2 magasságba. "
            "A teli pont csak a függvényértéket mutatja."),
 ]),

 ("Egyoldali határérték", [
   r'<p class="lead">Előfordul, hogy balról és jobbról közelítve <b>más</b> értékhez jutunk. Ilyenkor '
   r'külön beszélünk bal és jobb oldali határértékről.</p>',
   doboz("definicio", "Egyoldali határérték",
         r'<p>$\lim\limits_{x\to a-0}f(x)$ a <b>bal oldali</b> határérték (csak $a$-nál kisebb $x$-ekkel '
         r'közelítünk), $\lim\limits_{x\to a+0}f(x)$ a <b>jobb oldali</b> (csak $a$-nál nagyobbakkal).</p>'
         r'<p>A $\lim\limits_{x\to a}f(x)$ határérték akkor és csak akkor létezik, ha a két egyoldali '
         r'határérték létezik és egyenlő; ekkor ez a közös érték a határérték.</p>', hid="def-egyoldali"),
   abra(SVG_UGRAS, 'A $h$ függvény az $x=1$-nél „ugrik”: balról a $3$-hoz tart, jobbról a $0$-ból indul.'),
   r'<p>Itt $\lim\limits_{x\to1-0}h(x)=3$ és $\lim\limits_{x\to1+0}h(x)=0$. A kettő különbözik, tehát a '
   r'$\lim\limits_{x\to1}h(x)$ határérték <b>nem létezik</b> — pedig $h(1)=0$ létezik.</p>',
   kviz(r'Tudjuk, hogy $\lim\limits_{x\to a-0}f(x)=5$. Mit mondhatunk a $\lim\limits_{x\to a}f(x)$ határértékről?',
        [r'csak akkor $5$, ha a jobb oldali határérték is $5$',
         r'biztosan $5$',
         r'biztosan nem létezik',
         r'$f(a)$-val egyenlő'], 0,
        jo="✔ A kétoldali határértékhez mindkét oldalnak ugyanoda kell vezetnie — egy oldal még kevés.",
        nem="✘ Egy oldal nem elég: a h függvénynél a bal oldali határérték 3, a jobb oldali 0, és a határérték "
            "nem létezik. Mindkét oldalt meg kell nézni."),
 ]),

 ("Folytonosság", [
   r'<p class="lead">Szemléletesen: ha egy függvény egy intervallumon <b>folytonos</b>, ott a grafikonja a ceruza '
   r'felemelése nélkül megrajzolható — a görbe nem szakad meg és nem „ugrik”.</p>',
   doboz("definicio", "Folytonosság egy pontban",
         r'<p>Az $f$ függvény folytonos az $a\in D_f$ helyen, ha $\lim\limits_{x\to a}f(x)=f(a)$ — vagyis a '
         r'határérték létezik, és egyenlő a helyettesítési értékkel.</p>', hid="def-folytonos"),
   doboz("tetel", "Az elemi függvények folytonossága",
         r'<p>Minden elemi függvény folytonos értelmezési tartományának minden pontjában. (Bizonyítás nélkül.)</p>'
         r'<p>Ezért egy elemi függvény határértéke egy értelmezési tartománybeli pontban '
         r'<b>behelyettesítéssel</b> kiszámolható. A gond ott kezdődik, ahol a képletnek nincs értelme.</p>'
         r'<p>Az $\frac1x$ is folytonos, mert a $0$ nincs az értelmezési tartományában — a grafikon ott mégis megszakad.</p>',
         hid="tetel-folytonos-elemi"),
   r'<p>A grafikon megszakadásának három jellegzetes fajtája: <b>lyuk</b> (a határérték létezik, de a pontbeli érték nincs vagy '
   r'más — mint az $f$ és a $g$ fent), <b>ugrás</b> (a két egyoldali határérték különbözik — mint a $h$), és '
   r'<b>végtelenbe szakadás</b> (a függvény abszolút értéke a pont közelében minden határon túl nő — ebből lesz az aszimptota).</p>',
   doboz("erdekesseg", "Hol találkozol vele?",
         r'<p>Ugró, „lépcsős” függvény a postai díjszabás (20 grammig egy ár, fölötte egy másik) és a '
         r'taxióra: az ár egy-egy határon hirtelen változik, közben nem.</p>'),
   GY(FH + "#alap-1", "A 1–4", FH + "#kozep-1", "K 1–2"),
   brief('<b>Nagol:</b> Grafikon nem mindig van kéznél. Ha csak a képlet van meg, a határértéket ki kell '
         '<b>számolni</b> — és ott jön majd a $\\frac00$. <b>Véd Vilmos:</b> Az egyszerű, az 1. '
         '<b>Nagol:</b> Nem.', outro=True),
 ]),
]

# ---------------------------------------------------------------- B2
B2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Véd Vilmos:</b> 🌮 <i>Burek-matek:</i> „$\\frac00=1$, hiszen minden szám osztva önmagával 1.” '
         '<b>Nagol:</b> A $\\frac00$ nem szám, hanem figyelmeztetés: <b>itt még dolgozni kell</b>. Ma '
         'megtanuljuk, hogyan — szorzattá alakítással, a gyököknél konjugálttal, és azt is, mi történik, ha '
         'csak a nevező tart a nullához.'),
 ]),

 ("Műveletek és behelyettesítés", [
   r'<p class="lead">A függvények határértékére ugyanazok a műveleti szabályok érvényesek, mint a '
   r'sorozatokéra.</p>',
   doboz("tetel", "A határérték műveleti tulajdonságai",
         r'<p>Ha $\lim\limits_{x\to a}f(x)=A$ és $\lim\limits_{x\to a}g(x)=B$ (véges számok), akkor</p>'
         r'<p>$\lim\limits_{x\to a}\big(f(x)\pm g(x)\big)=A\pm B$, &nbsp; $\lim\limits_{x\to a}f(x)\,g(x)=A\cdot B$, '
         r'&nbsp; $\lim\limits_{x\to a}\dfrac{f(x)}{g(x)}=\dfrac AB$, ha $B\ne0$.</p>'
         r'<p>(Bizonyítás nélkül.)</p>', hid="tetel-fv-muveletek"),
   r'<p>Ezekből és az elemi függvények folytonosságából adódik a legfontosabb gyakorlati szabály: '
   r'<b>először mindig helyettesíts be</b>. Ha értelmes számot kapsz, az a határérték:</p>'
   r'<p>$\lim\limits_{x\to2}\dfrac{x^2+1}{x+3}=\dfrac{4+1}{2+3}=1$, &nbsp; '
   r'$\lim\limits_{x\to5}\sqrt{x+4}=\sqrt9=3$.</p>'
   r'<p>Ha a behelyettesítés $\dfrac00$-t ad, átalakítás jön (lásd lent); ha $\dfrac c0$-t ($c\ne0$), '
   r'egyoldali végtelen határérték (a lecke vége).</p>',
   kviz(r'A $\lim\limits_{x\to3}\dfrac{x^2-9}{x-3}$ behelyettesítésnél $\dfrac00$-t kapunk. Mi a helyes következtetés?',
        [r'át kell alakítani; egyszerűsítés után a határérték $6$',
         r'a határérték nem létezik',
         r'a határérték $0$',
         r'a határérték $1$'], 0,
        jo="✔ Itt a 0/0 azt jelzi, hogy a számlálóban és a nevezőben is ott van az (x − 3) tényező: (x − 3)(x + 3)/(x − 3) = x + 3 → 6.",
        nem="✘ A 0/0 határozatlan alak: nem eredmény, hanem jelzés. (x² − 9)/(x − 3) = x + 3, ha x ≠ 3, "
            "így a határérték 3 + 3 = 6."),
 ]),

 ("0/0: szorzattá alakítás és egyszerűsítés", [
   r'<p class="lead">Ha a számláló és a nevező is polinom, és mindkettő $0$ az $x=a$ helyen, akkor mindkettőben ott van az $(x-a)$ '
   r'tényező. Szorzattá alakítunk, egyszerűsítünk, és utána helyettesítünk be. Másodfokú kifejezésnél a '
   r'gyöktényezős alak segít ('
   '<a href="' + E202 + 'tananyag-viete-es-szorzatta-alakitas.html">ismétlés, 2e</a>).</p>',
   doboz("pelda", "I.V.H. Akták — egyszerűsítés",
         r'<p>a) $\lim\limits_{x\to-3}\dfrac{x^2+x-6}{x+3}=\lim\limits_{x\to-3}\dfrac{(x+3)(x-2)}{x+3}'
         r'=\lim\limits_{x\to-3}(x-2)=-5$</p>'
         r'<p>b) $\lim\limits_{x\to2}\dfrac{x^2-4}{x^2-3x+2}=\lim\limits_{x\to2}\dfrac{(x-2)(x+2)}{(x-2)(x-1)}'
         r'=\lim\limits_{x\to2}\dfrac{x+2}{x-1}=\dfrac41=4$</p>'
         r'<p><i>Véd Vilmos széljegyzete:</i> „az egyszerűsítés csak azért szabad, mert $x\ne a$ — a '
         r'határértékben az $a$-t kihagyjuk.”</p>', hid="pelda-szorzatta"),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>Véd Vilmos így számol: $\lim\limits_{x\to1}\dfrac{x^2-1}{x-1}=\dfrac{1-1}{1-1}=\dfrac00=1$.</p>'
         r'<p><b>A $\frac00$ nem $1$ és nem $0$.</b> Ha egyszerűsítünk, $\dfrac{x^2-1}{x-1}=x+1\to2$. Ugyanez az '
         r'alak más függvénynél bármi lehet — ezért hívjuk határozatlannak.</p>'),
   kviz(r'Véd Vilmos: „$\lim\limits_{x\to3}\dfrac{x^2-3x}{x-3}=\dfrac00=1$.” Mi a hiba?',
        [r'a $\frac00$ határozatlan: egyszerűsítés után $x\to3$',
         r'nincs hiba, a határérték $1$',
         r'a határérték $0$, mert a számláló $0$',
         r'ilyen határérték nem létezik, mert a nevező $0$'], 0,
        jo="✔ x(x − 3)/(x − 3) = x, és ez a 3 közelében 3-hoz tart. A 0/0 alakból önmagában semmi nem következik.",
        nem="✘ A 0/0 határozatlan alak. Emeld ki az x-et: x(x − 3)/(x − 3) = x, és ez 3-hoz tart."),
    doboz("erdekesseg", "Egy nevezetes határérték",
         r'<p>A $\dfrac{\sin x}{x}$ az $x=0$-ban nincs értelmezve, a határértéke mégis szép:</p>'
         r'<div class="tblwrap"><table class="tt-table">'
         r'<tr><th>$x$</th><td>$0{,}5$</td><td>$0{,}1$</td><td>$0{,}01$</td></tr>'
         r'<tr><th>$\frac{\sin x}{x}$</th><td>$\approx0{,}95885$</td><td>$\approx0{,}99833$</td><td>$\approx0{,}99998$</td></tr>'
         r'</table></div>'
         r'<p>$\lim\limits_{x\to0}\dfrac{\sin x}{x}=1$ (radiánban, bizonyítás nélkül). Kis szögekre ezért '
         r'$\sin x\approx x$ — ezt használják a fizikusok az inga lengésénél.</p>'),
]),

 ("Gyökös 0/0: bővítés a konjugálttal", [
   r'<p class="lead">Ha a $\dfrac00$ alakban gyök szerepel, a <b>konjugálttal</b> bővítünk: '
   r'$(\sqrt u-c)(\sqrt u+c)=u-c^2$. Így a gyök „átköltözik”, és a közös tényező előbújik.</p>',
   doboz("pelda", "I.V.H. Akták — konjugált",
         r'<p>a) A gyök a számlálóban:</p>'
         r'<p>$\lim\limits_{x\to4}\dfrac{\sqrt x-2}{x-4}=\lim\limits_{x\to4}\dfrac{(\sqrt x-2)(\sqrt x+2)}{(x-4)(\sqrt x+2)}'
         r'=\lim\limits_{x\to4}\dfrac{x-4}{(x-4)(\sqrt x+2)}=\lim\limits_{x\to4}\dfrac{1}{\sqrt x+2}=\dfrac14$</p>'
         r'<p>b) A gyök a nevezőben:</p>'
         r'<p>$\lim\limits_{x\to0}\dfrac{x}{\sqrt{x+1}-1}=\lim\limits_{x\to0}\dfrac{x(\sqrt{x+1}+1)}{(x+1)-1}'
         r'=\lim\limits_{x\to0}\dfrac{x(\sqrt{x+1}+1)}{x}=\lim\limits_{x\to0}(\sqrt{x+1}+1)=2$</p>', hid="pelda-konjugalt"),
   doboz("erdekesseg", "Miért éppen a konjugált?",
         r'<p>Az $(a-b)(a+b)=a^2-b^2$ nevezetes szorzatot használjuk „visszafelé”: ha $a=\sqrt u$, akkor a '
         r'négyzetre emelés eltünteti a gyököt. Ugyanez a trükk tüntette el a gyököt a törtek nevezőjéből is.</p>'),
 ]),

 ("c/0: egyoldali végtelen határérték", [
   r'<p class="lead">Ha a behelyettesítésnél a számláló egy $c\ne0$ szám, a nevező pedig $0$, akkor a tört '
   r'abszolút értéke minden határon túl nő. Az előjelet a számláló és a nevező előjele adja — ez a pont két '
   r'oldalán eltérhet.</p>',
   doboz("pelda", "I.V.H. Akták — előjelvizsgálat",
         r'<p>Vizsgáljuk az $\dfrac{x+2}{x-1}$ egyoldali határértékeit az $x=1$ helyen: ott a számláló $3$ (pozitív), a nevező $0$.</p>'
         r'<ul><li>balról ($x\lt1$) a nevező kicsi <b>negatív</b> szám: $\lim\limits_{x\to1-0}\dfrac{x+2}{x-1}=-\infty$;</li>'
         r'<li>jobbról ($x\gt1$) a nevező kicsi <b>pozitív</b> szám: $\lim\limits_{x\to1+0}\dfrac{x+2}{x-1}=+\infty$.</li></ul>'
         r'<p>A két egyoldali határérték különbözik, a kétoldali határérték nem létezik.</p>', hid="pelda-c-per-0"),
   abra(SVG_POLUS, 'Az $y=\\frac{x+2}{x-1}$ grafikonja az $x=1$ két oldalán ellentétes irányba „szakad el”.'),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>Véd Vilmos szerint „$\frac30=0$”, egy másik nap szerint „$\frac30=\infty$, és kész”.</p>'
         r'<p><b>Nullával nem osztunk — itt határértékről van szó, és az előjel számít.</b> A tört a pont '
         r'egyik oldalán $+\infty$, a másikon $-\infty$ felé tarthat; mindkét oldalt külön meg kell vizsgálni.</p>'),
   kviz(r'Mennyi a $\lim\limits_{x\to2-0}\dfrac{1}{x-2}$ határérték?',
        [r'$-\infty$', r'$+\infty$', r'$0$', r'nincs értelme a kérdésnek'], 0,
        jo="✔ Ha x kicsit kisebb 2-nél, x − 2 kicsi negatív szám, így 1/(x − 2) nagy abszolút értékű negatív szám.",
        nem="✘ Balról közelítve x − 2 negatív (pl. 1,99 − 2 = −0,01), tehát a tört egyre nagyobb abszolút értékű "
            "NEGATÍV szám: −∞."),
   GY(FH + "#alap-5", "A 5–10", FH + "#kozep-3", "K 3–7"),
   brief('<b>Nagol:</b> Eddig egy konkrét pont felé mentünk. Mi történik, ha $x$ nem áll meg sehol, hanem '
         'a végtelenbe fut? <b>Véd Vilmos:</b> Azt már tudom, a sorozatoknál csináltuk. <b>Nagol:</b> Félig. '
         '$x$ most a negatív végtelen felé is futhat.', outro=True),
 ]),
]

# ---------------------------------------------------------------- B3
B3 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Nagol:</b> A sorozatoknál $n\\to\\infty$ volt. A függvényeknél $x$ a $+\\infty$ és a $-\\infty$ felé is '
         'futhat. <b>Véd Vilmos:</b> Mindkét irányban ugyanaz jön ki. <b>Nagol:</b> Nem mindig. Ma kiderül, '
         'mikor igen és mikor nem — és hogy mit árul el ez a grafikon két széléről.'),
 ]),

 ("Racionális törtfüggvény — a fokszám-szabály", [
   r'<p class="lead">$x\to\pm\infty$ esetén a racionális törtfüggvényeket ugyanúgy kezeljük, mint a '
   r'sorozatokat: a számlálót és a nevezőt is elosztjuk a nevezőben szereplő legmagasabb $x$-hatvánnyal. Az eredményt a '
   '<a href="' + E401 + 'tananyag-racionalis-tortek.html#tetel-fokszam">fokszám-szabály</a> adja.</p>',
   doboz("tetel", "Fokszám-szabály függvényekre",
         r'<p>Ha a számláló $p$-edfokú ($a$ főegyütthatóval), a nevező $r$-edfokú ($b$ főegyütthatóval), akkor '
         r'$x\to\pm\infty$ esetén a tört határértéke</p>'
         r'<ul><li>$0$, ha $p\lt r$;</li><li>$\dfrac ab$, ha $p=r$;</li>'
         r'<li>$+\infty$ vagy $-\infty$, ha $p\gt r$ — az előjel a főtagok hányadosának, $\dfrac ab\,x^{p-r}$-nek az előjele.</li></ul>',
         hid="tetel-fokszam-fv"),
   doboz("pelda", "I.V.H. Akták — határérték a végtelenben",
         r'<p>$\lim\limits_{x\to+\infty}\dfrac{2x^2-x}{x^2+3}=\lim\limits_{x\to+\infty}\dfrac{2-\frac1x}{1+\frac3{x^2}}=2$ '
         r'&nbsp; ($p=r$)</p>'
         r'<p>$\lim\limits_{x\to+\infty}\dfrac{5x+1}{x^2+4}=0$ &nbsp; ($p\lt r$), &nbsp; '
         r'$\lim\limits_{x\to+\infty}\dfrac{x^3+x}{2x^2-1}=+\infty$ &nbsp; ($p\gt r$)</p>', hid="pelda-vegtelen-tort"),
 ]),

 ("x → −∞ és az előjel", [
   r'<p class="lead">Ha $p\le r$, a két irány ugyanazt adja. Ha $p\gt r$, a főtagok hányadosa $\dfrac ab\,x^{p-r}$, '
   r'és ennek előjele a $-\infty$ felé függ a $p-r$ paritásától: páratlan kitevőnél előjelet vált, párosnál nem.</p>',
   doboz("pelda", "I.V.H. Akták — a két irány",
         r'<ul><li>$\dfrac{x^3+x}{2x^2-1}$: a főtagok hányadosa $\dfrac x2$ → $x\to+\infty$: $+\infty$, de $x\to-\infty$: $-\infty$.</li>'
         r'<li>$\dfrac{x^4+1}{x^2+x}$: a főtagok hányadosa $x^2$ → mindkét irányban $+\infty$.</li>'
         r'<li>$\dfrac{2x^2-x}{x^2+3}$: $p=r$ → mindkét irányban $2$.</li></ul>', hid="pelda-minusz-vegtelen"),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>Véd Vilmos az $x\to-\infty$ esetre is $+\infty$-t ír, „mert a végtelen az végtelen”.</p>'
         r'<p><b>A $-\infty$ felé a páratlan hatványok negatívak.</b> Írd fel a főtagok hányadosát, és '
         r'helyettesíts be gondolatban egy nagy negatív számot (pl. $-1000$-et).</p>'),
   kviz(r'Mennyi a $\lim\limits_{x\to-\infty}\dfrac{1-x^3}{x^2+2}$ határérték? (Tudjuk: $x\to+\infty$ esetén $-\infty$.)',
        [r'$+\infty$', r'$-\infty$, mint a másik irányban', r'$-1$', r'$0$'], 0,
        jo="✔ A főtagok hányadosa −x³/x² = −x; ha x → −∞, akkor −x → +∞.",
        nem="✘ A főtagok hányadosa −x. Nagy negatív x-re (pl. −1000) ez +1000 — tehát a −∞ felé a határérték +∞."),
 ]),

 ("Elemi függvények a végtelenben", [
   r'<p class="lead">Néhány határértéket az elemi függvények grafikonjáról azonnal leolvasunk.</p>',
   doboz("tetel", "Elemi függvények a végtelenben",
         r'<ul><li>$\lim\limits_{x\to\pm\infty}\dfrac{c}{x^k}=0$ ($k$ pozitív egész);</li>'
         r'<li>$a\gt1$ esetén $\lim\limits_{x\to+\infty}a^x=+\infty$ és $\lim\limits_{x\to-\infty}a^x=0$ (ha $0\lt a\lt1$, fordítva);</li>'
         r'<li>$a\gt1$ esetén $\lim\limits_{x\to+\infty}\log_a x=+\infty$;</li>'
         r'<li>a $\sin x$-nek és a $\cos x$-nek nincs határértéke a végtelenben — $-1$ és $1$ között hullámzanak.</li></ul>',
         hid="tetel-elemi-vegtelen"),
   kviz(r'Melyik igaz a $2^x$ függvényre?',
        [r'$x\to-\infty$ esetén $0$-hoz, $x\to+\infty$ esetén $+\infty$-hez tart',
         r'$x\to+\infty$ esetén $0$-hoz tart',
         r'mindkét irányban $+\infty$-hez tart',
         r'$x\to-\infty$ esetén $-\infty$-hez tart'], 0,
        jo="✔ 2¹⁰ = 1024, 2⁻¹⁰ = 1/1024: jobbra meredeken nő, balra a 0-hoz simul (de sosem negatív).",
        nem="✘ Próbáld ki: 2¹⁰ = 1024, 2⁻¹⁰ ≈ 0,001. Jobbra a végtelenbe nő, balra a 0-hoz közelít — "
            "negatív értéket sosem vesz fel."),
   GY(FH + "#alap-11", "A 11–14", FH + "#kozep-8", "K 8–9"),
   brief('<b>Nagol:</b> Ha a határérték a végtelenben egy szám, a görbe a széleken egy vízszintes egyeneshez '
         'simul. Ha egy pontban végtelen, egy függőlegeshez. Ezek az egyenesek a fejezet címszereplői — az '
         'aszimptoták. <b>Véd Vilmos:</b> A fal. <b>Nagol:</b> A fal.', outro=True),
 ]),
]

# ---------------------------------------------------------------- C1
C1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Véd Vilmos:</b> Futok a fal felé. Minden lépéssel közelebb vagyok, de valahogy soha nem érek '
         'oda. Áttöröm! <b>Nagol:</b> Nem fogod. Ez egy <b>aszimptota</b>: a görbe végtelenbe nyúló ága egyre '
         'közelebb simul hozzá. A feladat nem áttörni, hanem kiszámolni, <b>hol van</b>.'),
 ]),

 ("Mi az aszimptota?", [
   r'<p class="lead">Az aszimptota olyan egyenes, amelyhez a grafikon egy végtelenbe nyúló ága egyre közelebb '
   r'simul.</p>',
   doboz("definicio", "Aszimptota",
         r'<p>Az $\ell$ egyenes a görbe <b>aszimptotája</b>, ha a görbének van olyan végtelenbe nyúló ága, amelyen '
         r'haladva a pont $\ell$-től mért távolsága $0$-hoz tart. Három fajtáját vizsgáljuk: a <b>függőleges</b> '
         r'($x=a$), a <b>vízszintes</b> ($y=c$) és a <b>ferde</b> ($y=kx+n$) aszimptotát.</p>', hid="def-aszimptota"),
   abra(SVG_RECIPROK, 'Az $y=\\frac1x$ két aszimptotája a két koordinátatengely: $x=0$ és $y=0$.'),
   r'<p>Az A1 leckében megígért első aszimptota: a $\log_2 x$ függőleges aszimptotája az $x=0$, mert '
   r'$\lim\limits_{x\to0+0}\log_2x=-\infty$.</p>',
   doboz("erdekesseg", "Hol találkozol vele?",
         r'<p>A kihűlő tea hőmérséklete a szoba hőmérsékletéhez közelít, de (elméletben) sosem éri el: a '
         r'hőmérséklet–idő grafikon vízszintes aszimptotája a szobahőmérséklet.</p>'),
 ]),

 ("Függőleges aszimptota", [
   r'<p class="lead">Racionális törtfüggvénynél függőleges aszimptota ott lehet, ahol a nevező $0$. Ha ott a '
   r'számláló <b>nem</b> $0$, akkor $c/0$ alakot kapunk: a függvény egyoldali határértéke $\pm\infty$, és '
   r'az $x=a$ egyenes függőleges aszimptota. Ha a számláló is $0$, előbb egyszerűsíteni kell, és újra megnézni.</p>',
   doboz("pelda", "I.V.H. Akták — függőleges aszimptota",
         r'<p>$f(x)=\dfrac{2x+1}{x-3}$: a nevező $x=3$-ban $0$, a számláló ott $7\ne0$.</p>'
         r'<p>$\lim\limits_{x\to3-0}f(x)=-\infty$, &nbsp; $\lim\limits_{x\to3+0}f(x)=+\infty$ → a függőleges '
         r'aszimptota: $x=3$.</p>', hid="pelda-fuggoleges"),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>Véd Vilmos szerint a $g(x)=\dfrac{x^2-4}{x-2}$ függvénynek az $x=2$ függőleges aszimptotája, '
         r'„mert ott a nevező nulla”.</p>'
         r'<p><b>Ha a számláló is $0$, még nem dőlt el semmi: egyszerűsíts, és nézd meg újra.</b> Itt $g(x)=x+2$ '
         r'(ha $x\ne2$), és $\lim\limits_{x\to2}g(x)=4$ véges — ez <b>lyuk</b>, nem aszimptota. A grafikon egy egyenes, '
         r'amelyből a $(2;\,4)$ pont hiányzik.</p>'),
   kviz(r'Hol van a $g(x)=\dfrac{x^2-25}{x+5}$ függvény függőleges aszimptotája?',
        [r'sehol: az $x=-5$-ben csak egy lyuk van',
         r'az $x=-5$ egyenes',
         r'az $x=5$ és az $x=-5$ egyenes',
         r'az $y=-10$ egyenes'], 0,
        jo="✔ Az x = −5-ben a számláló is 0: (x − 5)(x + 5)/(x + 5) = x − 5 → −10. Véges határérték, "
           "tehát ott lyuk van, nem aszimptota.",
        nem="✘ Nézd meg a számlálót is: x = −5-nél az is 0. Egyszerűsítve g(x) = x − 5, a határérték −10 — ez "
            "lyuk, nem függőleges aszimptota."),
 ]),

 ("Vízszintes aszimptota", [
   r'<p class="lead">Ha $\lim\limits_{x\to+\infty}f(x)=c$ (vagy $x\to-\infty$ esetén), akkor az $y=c$ egyenes '
   r'vízszintes aszimptota. Racionális törtfüggvénynél ez a fokszám-szabályból jön: $p\lt r$ esetén $y=0$, '
   r'$p=r$ esetén $y=\dfrac ab$; ha $p\gt r$, nincs vízszintes aszimptota.</p>',
   doboz("pelda", "I.V.H. Akták — vízszintes aszimptota",
         r'<p>$f(x)=\dfrac{2x+1}{x-3}$: $\lim\limits_{x\to\pm\infty}\dfrac{2x+1}{x-3}=\dfrac21=2$ → a vízszintes '
         r'aszimptota: $y=2$.</p>', hid="pelda-vizszintes"),
   abra(SVG_FUGG_VIZSZ, 'Az $y=\\frac{2x+1}{x-3}$ grafikonja és két aszimptotája: $x=3$ és $y=2$ (szaggatott).'),
   doboz("csapda", "Véd Vilmos csapda",
         r'<p>Véd Vilmos szerint „a görbe <b>soha</b> nem metszheti az aszimptotáját”.</p>'
         r'<p><b>A vízszintes aszimptotát a görbe metszheti</b> — az aszimptota csak a végtelenbe tartó ágakról '
         r'szól. Az $y=\dfrac{x}{x^2+1}$ vízszintes aszimptotája az $y=0$, és a görbe az origóban át is megy rajta.</p>'),
   abra(SVG_METSZI, 'Az $y=\\frac{x}{x^2+1}$ az origóban metszi a vízszintes aszimptotáját, a két szélén mégis hozzá simul.'),
   kviz(r'Metszheti-e egy függvény grafikonja a saját vízszintes aszimptotáját?',
        [r'igen; az aszimptota csak a végtelenbe tartó ágak viselkedését írja le',
         r'nem, soha',
         r'csak akkor, ha a függvény páros',
         r'csak a függőleges aszimptotáját metszheti'], 0,
        jo="✔ Példa: az x/(x² + 1) grafikonja átmegy az origón, pedig vízszintes aszimptotája az y = 0.",
        nem="✘ A „sosem éri el” csak a görbe két szélére vonatkozik. Az x/(x² + 1) grafikonja például az "
            "origóban metszi a vízszintes aszimptotáját (y = 0)."),
 ]),

 ("Ferde aszimptota", [
   r'<p class="lead">Ha a számláló foka <b>eggyel nagyobb</b> a nevezőénél ($p=r+1$), nincs vízszintes '
   r'aszimptota, a görbe viszont egy <b>ferde</b> egyeneshez simul. Ez a fejezet legnehezebb része.</p>',
   doboz("tetel", "A ferde aszimptota",
         r'<p>Az $y=kx+n$ egyenes ferde aszimptota $x\to+\infty$ esetén, ha</p>'
         r'<p>$k=\lim\limits_{x\to+\infty}\dfrac{f(x)}{x}$ &nbsp; (véges és nem $0$), &nbsp; és &nbsp; '
         r'$n=\lim\limits_{x\to+\infty}\big(f(x)-kx\big)$ &nbsp; (véges).</p>'
         r'<p>$x\to-\infty$ esetén ugyanígy; racionális törtfüggvénynél a két irány ugyanazt adja.</p>', hid="tetel-ferde"),
   doboz("pelda", "I.V.H. Akták — ferde aszimptota",
         r'<p>$f(x)=\dfrac{x^2+1}{x-1}$ (a számláló másodfokú, a nevező elsőfokú):</p>'
         r'<p>$k=\lim\limits_{x\to+\infty}\dfrac{x^2+1}{x(x-1)}=\lim\limits_{x\to+\infty}\dfrac{x^2+1}{x^2-x}=1$</p>'
         r'<p>$n=\lim\limits_{x\to+\infty}\left(\dfrac{x^2+1}{x-1}-x\right)=\lim\limits_{x\to+\infty}\dfrac{x^2+1-x^2+x}{x-1}'
         r'=\lim\limits_{x\to+\infty}\dfrac{x+1}{x-1}=1$</p>'
         r'<p>A ferde aszimptota: $y=x+1$. (Függőleges aszimptota is van: $x=1$, mert ott a számláló $2\ne0$.)</p>',
         hid="pelda-ferde"),
   abra(SVG_FERDE, 'Az $y=\\frac{x^2+1}{x-1}$ grafikonja a két aszimptotájával: $x=1$ és $y=x+1$.'),
   NEHEZ(1, 4, "ferde aszimptota racionális függvénynél"),
 ]),

 ("Aszimptota-vizsgálat lépésről lépésre", [
   r'<p class="lead">Egy racionális törtfüggvény aszimptotáit mindig ugyanabban a sorrendben keressük.</p>'
   r'<ol class="reszfeladatok"><li><b>Függőleges:</b> egyszerűsítsd a törtet, amennyire lehet; utána a nevező zérushelyei.</li>'
   r'<li><b>Vízszintes:</b> $\lim\limits_{x\to\pm\infty}f(x)$ — ha véges szám, megvan.</li>'
   r'<li><b>Ferde:</b> csak ha $p=r+1$; $k$ és $n$ a fenti képletekkel.</li></ol>',
   doboz("pelda", "I.V.H. Akták — teljes vizsgálat",
         r'<p>$f(x)=\dfrac{2x^2+x}{x-1}$</p>'
         r'<ul><li>függőleges: $x=1$ (a számláló ott $3\ne0$);</li>'
         r'<li>vízszintes: nincs, mert $p=2\gt r=1$;</li>'
         r'<li>ferde: $k=\lim\limits_{x\to+\infty}\dfrac{2x^2+x}{x^2-x}=2$, &nbsp; '
         r'$n=\lim\limits_{x\to+\infty}\left(\dfrac{2x^2+x}{x-1}-2x\right)=\lim\limits_{x\to+\infty}\dfrac{3x}{x-1}=3$ → $y=2x+3$.</li></ul>',
         hid="pelda-teljes"),
   kviz(r'Lehet-e egy racionális törtfüggvénynek vízszintes <b>és</b> ferde aszimptotája is?',
        [r'nem: $p\le r$ esetén vízszintes van, $p=r+1$ esetén ferde',
         r'igen, ha a számláló foka nagyobb a nevezőénél',
         r'igen, ha a nevezőnek két zérushelye van',
         r'csak akkor, ha a számláló és a nevező foka egyenlő'], 0,
        jo="✔ A fokszámok döntenek: vagy a határérték véges (vízszintes), vagy p = r + 1 és ferde. Egyszerre nem.",
        nem="✘ Racionális törtfüggvénynél a kettő kizárja egymást: p ≤ r esetén a határérték véges (vízszintes "
            "aszimptota), p = r + 1 esetén a függvény ±∞-be tart, és ferde aszimptotája van."),
   GY(FH + "#alap-15", "A 15–18", FH + "#kozep-10", "K 10–12"),
   brief('<b>Nagol:</b> A falat nem kellett áttörni: tudjuk, hol van, és azt is, hogyan közelít hozzá a görbe. '
         'A határértékkel viszont ennél többet is meg lehet fogni: azt, hogy egy mennyiség <b>egy pillanat alatt</b> '
         'mennyit változik. Ez lesz a derivált. <b>Véd Vilmos:</b> Pillanatnyi? Én mindig pillanatnyi vagyok.',
         outro=True),
 ]),
]

# ---------------------------------------------------------------- lapok
KI = [
 lap(**T, fajl="tananyag-fuggveny-hatarerteke.html",
     cim="A függvény határértéke",
     cim_tiszta="A függvény határértéke",
     alcim="Mihez közelít a függvény: közelítés táblázattal és grafikonon, határérték és helyettesítési érték, "
           "egyoldali határérték, folytonosság.",
     chip=KUL + " · 4/7", szakaszok=B1,
     elozo=("tananyag-fuggvenytulajdonsagok.html", "Paritás, periodicitás, monotonitás"),
     kovetkezo=("tananyag-hatarertek-szamolasa.html", "Határérték-számítás")),
 lap(**T, fajl="tananyag-hatarertek-szamolasa.html",
     cim="Határérték-számítás",
     alcim="Behelyettesítés, a 0/0 alak szorzattá alakítással és konjugálttal, a c/0 alak egyoldali végtelen "
           "határértékkel.",
     chip=KUL + " · 5/7", szakaszok=B2,
     elozo=("tananyag-fuggveny-hatarerteke.html", "A függvény határértéke"),
     kovetkezo=("tananyag-hatarertek-vegtelenben.html", "Határérték a végtelenben")),
 lap(**T, fajl="tananyag-hatarertek-vegtelenben.html",
     cim="Határérték a végtelenben",
     alcim="Racionális törtfüggvények a plusz és a mínusz végtelenben, az előjel szerepe, elemi függvények a végtelenben.",
     chip=KUL + " · 6/7", szakaszok=B3,
     elozo=("tananyag-hatarertek-szamolasa.html", "Határérték-számítás"),
     kovetkezo=("tananyag-aszimptotak.html", "Aszimptoták")),
 lap(**T, fajl="tananyag-aszimptotak.html",
     cim="Aszimptoták",
     alcim="Az aszimptota-fal: függőleges, vízszintes és ferde aszimptota racionális törtfüggvényeknél, lépésről lépésre.",
     chip=KUL + " · 7/7", szakaszok=C1,
     elozo=("tananyag-hatarertek-vegtelenben.html", "Határérték a végtelenben"),
     kovetkezo=("feladatok-tulajdonsagok.html", "Zsoldos-lista I. — Tulajdonságok")),
]
for u in KI:
    print("✓", os.path.basename(u))
