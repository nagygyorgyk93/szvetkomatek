# -*- coding: utf-8 -*-
"""3e/05 — D blokk: ellipszis (D1), ellipszis es egyenes (D2), hiperbola (D3), hiperbola es egyenes (D4).
Mentor: Kanrak (Ter-eb). Kuldetes: A Terkep Halozata."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra
from abra_common import svg_koordsik, svg_kupszelet, KEK, BOROSTYAN, ZOLD, PIROS, SZURKE, LILA

T = dict(tagozat="3e", mappa="05-analitikus-geometria", temakor="Síkbeli analitikus geometria")
FGY = "feladatok-ellipszis-hiperbola.html"
KUL = "A Térkép Hálózata"
V03 = "../03-linearis-rendszerek/"
E2H = "../../2e/01-hatvanyozas-gyokvonas-komplex-szamok/tananyag-hatvanyfuggveny.html"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(k_h, k_c, n_h, n_c, tagozat="3e")


# ---------------------------------------------------------------- önteszt
from sympy import Rational, sqrt, simplify, symbols, solve, expand, discriminant, Abs, factor
E = []
def chk(n, g, w):
    if isinstance(g, (tuple, list)):
        ok = len(g) == len(w) and all(simplify(u - v) == 0 for u, v in zip(g, w))
    else:
        ok = simplify(g - w) == 0
    if not ok:
        E.append((n, g, w))
x, y, u, v, n_ = symbols("x y u v n")
def tav(P, Q):
    return sqrt((P[0] - Q[0])**2 + (P[1] - Q[1])**2)

# D1
chk("e-5-3", sqrt(25 - 9), 4); chk("kviz-e", sqrt(25 - 16), 3)
chk("adatok-oszt", (sqrt(400/16), sqrt(400/25)), (5, 4))
chk("adatok-e", sqrt(25 - 16), 3)
Py = sqrt(16*(1 - Rational(9, 25))); chk("P-y", Py, Rational(16, 5))
chk("vezersugar", tav((3, Py), (-3, 0)) + tav((3, Py), (3, 0)), 10)
chk("maxi-jo", (sqrt(144/9), sqrt(144/16)), (4, 3)); chk("maxi-e", sqrt(16 - 9), sqrt(7))
chk("a-e", sqrt(25 - 16), 3)
s = solve([16*u + v - 1, 4*u + 4*v - 1], [u, v]); chk("ket-pont", (1/s[u], 1/s[v]), (20, 5))
chk("kviz-adatok", (sqrt(36/4), sqrt(36/9)), (3, 2))
# D2
xs = solve(expand((7 - 2*y)**2 + 4*y**2 - 25), y); chk("szelo-y", sorted(xs), [Rational(3, 2), 2])
chk("szelo-D", discriminant(2*y**2 - 7*y + 6, y), 1)
chk("hur", tav((3, 2), (4, Rational(3, 2))), sqrt(5)/2)
assert simplify(Rational(9, 25) + Rational(16, 25) - 1) == 0          # P(3; 16/5) rajta van
chk("erinto-ell", expand((3*x/25 + (Rational(16, 5))*y/16 - 1)*25), 3*x + 5*y - 25)
chk("kviz-erinto", expand((2*x/8 + y/2 - 1)*4), x + 2*y - 4)
chk("feltetel", solve(8*Rational(1, 4) + 2 - n_**2, n_), [-2, 2])
chk("feltetel-D", discriminant(expand((x**2/8 + (x/2 + 2)**2/2 - 1)*8), x), 0)
# D3
a3, b3 = 2, Rational(3, 2)
chk("hip-e", sqrt(a3**2 + b3**2), Rational(5, 2))
chk("hip-alak", expand(36*(x**2/4 - y**2/b3**2)), 9*x**2 - 16*y**2)
Py3 = sqrt(b3**2*(Rational(16, 4) - 1)); chk("hip-P", Py3, 3*sqrt(3)/2)
chk("hip-vezersugar", Abs(tav((4, Py3), (-Rational(5, 2), 0)) - tav((4, Py3), (Rational(5, 2), 0))), 4)
chk("kviz-aszimp", sqrt(9)/sqrt(4), Rational(3, 2))
s3 = solve(16/4 - 9*v - 1, v); chk("hip-ket-pont", 1/s3[0], 3)
chk("kviz-felismer", expand((x**2/4 - y**2/16 - 1)*16), 4*x**2 - y**2 - 16)
# D4
sol = solve(expand(x**2 - 4*(x/2 + 3)**2 - 4), x); chk("aszimp-par", sol, [Rational(-10, 3)])
chk("aszimp-par-y", Rational(-10, 3)/2 + 3, Rational(4, 3))
chk("erinto-hip-D", factor(expand(3*x**2 - 4*(x - 1)**2 - 12)), -(x - 4)**2)
chk("erinto-hip-keplet", expand((4*x/4 - 3*y/3 - 1)), x - y - 1)
chk("hip-rajta", Rational(16, 4) - Rational(9, 3), 1)
chk("kviz-erinto-hip", expand((4*x/8 - 2*y/4 - 1)*2), x - y - 2)
chk("hip-feltetel", solve(4*1 - 3 - n_**2, n_), [-1, 1])
assert 1 > math.sqrt(3)/2
assert all(sp_ ** 2 < 0 or True for sp_ in [1])
assert not E, E
print("sympy önteszt: OK")

# ---------------------------------------------------------------- ábrák
SVG_ELL = svg_kupszelet(
    "ellipszis", {"a": 5, "b": 4}, pont=(3, 3.2),
    xr=(-6, 6), yr=(-5, 5), egyseg=30,
    leiras="Az x²/25 + y²/16 = 1 ellipszis az F₁(−3;0) és F₂(3;0) fókuszokkal; a P(3;3,2) pont "
           "vezérsugarainak összege 10")
SVG_ELL_EGY = svg_kupszelet(
    "ellipszis", {"a": 5, "b": 2.5}, fokuszok=False,
    egyenesek=[((1, 2, -7), ZOLD, "", {}), ((3, 8, -25), BOROSTYAN, "", {})],
    feliratok=[((4.6, -2.9), "x + 2y − 7 = 0", {"szin": ZOLD, "meret": 13}),
               ((4.6, -3.6), "3x + 8y − 25 = 0", {"szin": BOROSTYAN, "meret": 13})],
    pontok=[((3, 2), "", {"szin": ZOLD}), ((4, 1.5), "", {"szin": ZOLD})],
    xr=(-6, 8), yr=(-4, 5), egyseg=28,
    leiras="Az x² + 4y² = 25 ellipszis a (3;2) és (4;1,5) pontban metsző egyenessel, és a (3;2) "
           "pontbeli érintővel")
SVG_HIP = svg_kupszelet(
    "hiperbola", {"a": 2, "b": 1.5}, pont=(4, 3 * math.sqrt(3) / 2),
    szakaszok=[((-2, -1.5), (2, -1.5), SZURKE, {"sz": 1, "szaggat": "3 3"}),
               ((2, -1.5), (2, 1.5), SZURKE, {"sz": 1, "szaggat": "3 3"}),
               ((2, 1.5), (-2, 1.5), SZURKE, {"sz": 1, "szaggat": "3 3"}),
               ((-2, 1.5), (-2, -1.5), SZURKE, {"sz": 1, "szaggat": "3 3"})],
    xr=(-6, 6), yr=(-4, 4), egyseg=30,
    leiras="Az x²/4 − y²/(9/4) = 1 hiperbola két ága, szaggatott aszimptoták a 4-szer 3-as téglalap "
           "átlóin, az F₁(−2,5;0) és F₂(2,5;0) fókusz és egy P pont a két vezérsugárral")


def _mini(tipus, par, cim):
    return svg_kupszelet(tipus, par, fokuszok=False, aszimptotak=False, vezeregyenes=False,
                         xr=(-4, 4), yr=(-3.5, 3.5), egyseg=17, szamok=False, racs=True, origo=False,
                         feliratok=[((-2.6, 2.9), cim, {"szin": LILA, "meret": 15})],
                         leiras=f"{cim} ábra")


def _racs2x2(svgk, leiras):
    """Negy azonos meretu SVG egy kozos SVG-ben, 2x2-es elrendezesben (beagyazott <svg>)."""
    import re
    w, h = (int(v) for v in re.search(r'width="(\d+)" height="(\d+)"', svgk[0]).groups())
    ki = [f'<svg viewBox="0 0 {2 * w + 16} {2 * h + 16}" width="{2 * w + 16}" height="{2 * h + 16}" '
          f'role="img" aria-label="{leiras}">']
    for i, s in enumerate(svgk):
        belso = re.sub(r"^<svg[^>]*>", "", s.strip()).rsplit("</svg>", 1)[0]
        ki.append(f'<g transform="translate({(i % 2) * (w + 16)},{(i // 2) * (h + 16)})">{belso}</g>')
    ki.append("</svg>")
    return "\n".join(ki)


SVG_FELISMER = _racs2x2([
    _mini("hiperbola", {"a": 2, "b": 1}, "1."), _mini("ellipszis", {"a": 3, "b": 2}, "2."),
    _mini("parabola", {"p": 2}, "3."), _mini("kor", {"p": 0, "q": 0, "r": 3}, "4.")],
    "Négy mező: 1. hiperbola, 2. ellipszis, 3. jobbra nyíló parabola, 4. kör")
SVG_HIP_PAR = svg_kupszelet(
    "hiperbola", {"a": 2, "b": 1}, fokuszok=False,
    egyenesek=[((1, -2, 6), ZOLD, "y = ½x + 3", {"hely": 0.85, "dx": -40, "dy": -4, "dolt": False})],
    pontok=[((-10 / 3, 4 / 3), "M", {"szin": ZOLD, "dx": -12, "dy": -6})],
    xr=(-7, 5), yr=(-4, 6), egyseg=28,
    leiras="Az x²/4 − y² = 1 hiperbola és az aszimptotájával párhuzamos y = ½x + 3 egyenes: egyetlen "
           "közös pontjuk van, M, de az egyenes nem érintő")
SVG_HIP_ER = svg_kupszelet(
    "hiperbola", {"a": 2, "b": math.sqrt(3)}, fokuszok=False,
    egyenesek=[((1, -1, -1), BOROSTYAN, "", {})],
    feliratok=[((4.9, 2.1), "y = x − 1", {"szin": BOROSTYAN, "meret": 13})],
    pontok=[((4, 3), "T", {"szin": BOROSTYAN, "dx": 12, "dy": 4})],
    xr=(-6, 6), yr=(-5, 5), egyseg=28,
    leiras="Az x²/4 − y²/3 = 1 hiperbola és az y = x − 1 egyenes, amely a T(4;3) pontban érinti")

# ---------------------------------------------------------------- D1
D1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Kanrak:</b> Ez a torzító mező nem kör: megnyúlt, és <b>két magja</b> van. A műszerek '
         'szerint a perem minden pontjára igaz, hogy a két magtól mért távolsága <b>együtt</b> mindig '
         'ugyanannyi. Ebből az egy mondatból felírjuk a perem egyenletét.'),
 ]),

 ("Az ellipszis mint mértani hely", [
   doboz("definicio", "Az ellipszis",
         r'<p>Adott a síkban két pont, $F_1$ és $F_2$ (a <b>fókuszok</b>), és egy $2a$ hosszúság, '
         r'amely nagyobb a fókuszok $2e$ távolságánál. Az <b>ellipszis</b> a sík mindazon $P$ '
         r'pontjainak halmaza, amelyekre</p>'
         r'$$|PF_1|+|PF_2|=2a .$$'
         r'<p>A $PF_1$ és $PF_2$ szakaszok a $P$ pont <b>vezérsugarai</b>.</p>',
         hid="def-ellipszis"),
   r'<p><b>Kertész-szerkesztés.</b> Ha két cövekhez egy $2a$ hosszú zsinór két végét kötjük, és egy '
   r'pálcával feszesen tartva körbevezetjük, a pálca ellipszist rajzol: a zsinór két darabja mindig '
   r'$2a$ hosszú együtt. Így jelölik ki a kertészek az ellipszis alakú virágágyásokat.</p>',
   doboz("erdekesseg", "Hol találkozol vele?",
         r'<p>Kepler felismerése szerint a bolygók <b>ellipszispályán</b> keringenek, és a Nap az '
         r'ellipszis egyik <b>fókuszában</b> van. A Föld pályája alig tér el a körtől, az '
         r'üstökösöké viszont nagyon megnyúlt: a Halley-üstökös nagyjából hetvenhat évente tér vissza a Nap '
         r'közelébe.</p>'),
 ]),

 ("Az ellipszis egyenlete", [
   doboz("tetel", "Az ellipszis egyenlete",
         r'<p>Ha a fókuszok $F_1(-e;0)$ és $F_2(e;0)$, akkor az ellipszis egyenlete</p>'
         r'$$\frac{x^2}{a^2}+\frac{y^2}{b^2}=1,\qquad\text{ahol}\qquad e^2=a^2-b^2\quad(a\gt b\gt0).$$'
         r'<ul><li>$a$ a <b>nagy féltengely</b>, $b$ a <b>kis féltengely</b>, $e$ a <b>lineáris '
         r'excentricitás</b> (a középpont és a fókusz távolsága);</li>'
         r'<li>a csúcspontok: $(\pm a;0)$ és $(0;\pm b)$.</li></ul>'
         r'<p>A képlet a definícióból, a távolságképlettel jön ki; a levezetést nem kérjük.</p>',
         hid="tetel-ellipszis-egyenlete"),
   abra(SVG_ELL, 'Az $\\frac{x^2}{25}+\\frac{y^2}{16}=1$ ellipszis: $a=5$, $b=4$, $e=3$. A $P(3;3{,}2)$ '
        'vezérsugarai $6{,}8$ és $3{,}2$, összegük $10=2a$.'),
   r'<p>Miért $e^2=a^2-b^2$? A $(0;b)$ csúcspont mindkét fókusztól egyenlő távolságra van, és a '
   r'két távolság összege $2a$ — tehát mindkettő $a$. A $(0;0)$, $(e;0)$, $(0;b)$ derékszögű '
   r'háromszögben az átfogó $a$: $a^2=b^2+e^2$.</p>',
   kviz(r'Egy ellipszis féltengelyei $a=5$ és $b=4$. Mennyi a lineáris excentricitása?',
        ['$3$', r'$\sqrt{41}$', '$1$', '$9$'], 0,
        jo="✔ e² = a² − b² = 25 − 16 = 9, tehát e = 3.",
        nem="✘ Ellipszisnél e² = a² − b² (a fókusz a csúcsponton belül van): 25 − 16 = 9, e = 3. "
            "A √41 a hiperbola képletéből jönne."),
 ]),

 ("Az egyenletből az adatok", [
   r'<p>Az ellipszis egyenlete gyakran $b^2x^2+a^2y^2=a^2b^2$ alakban adott, törtek nélkül. Ilyenkor '
   r'<b>a jobb oldallal osztunk</b>, hogy $1$ legyen, és csak ezután olvassuk le a nevezőket.</p>',
   doboz("pelda", "Az ellipszis adatai",
         r'<p>Határozd meg a $16x^2+25y^2=400$ ellipszis féltengelyeit, lineáris excentricitását és '
         r'fókuszait!</p>',
         hid="pelda-ellipszis-adatai",
         lenyilo=("Megoldás",
                  r'<p>Osztunk $400$-zal: $\frac{x^2}{25}+\frac{y^2}{16}=1$. Így $a^2=25$, $b^2=16$, '
                  r'vagyis $a=5$, $b=4$.</p>'
                  r'<p>$e^2=25-16=9$, $e=3$; a fókuszok $F_1(-3;0)$, $F_2(3;0)$.</p>'
                  r'<p><i>Ez éppen a fenti ábra ellipszise. A $P(3;3{,}2)$ rajta van: '
                  r'$\frac{9}{25}+\frac{10{,}24}{16}=0{,}36+0{,}64=1$ ✔.</i></p>'
                  r'<p class="vegeredmeny">$a=5$, $b=4$, $e=3$, $F_1(-3;0)$, $F_2(3;0)$</p>')),
   doboz("csapda", "Maxi trükkje",
         r'<p>Maxi a $9x^2+16y^2=144$ mezőről ezt jelentette: „$a=9$, $b=16$”. A mező ennél jóval '
         r'kisebb.</p>'
         r'<p>Az együtthatók <b>nem</b> a féltengelyek. Előbb $144$-gyel osztunk: '
         r'$\frac{x^2}{16}+\frac{y^2}{9}=1$, tehát $a^2=16$ és $b^2=9$, azaz $a=4$, $b=3$, '
         r'$e=\sqrt{16-9}=\sqrt7$. Figyeld meg azt is, hogy az $x^2$ <b>alá</b> a $16$ került, pedig '
         r'az egyenletben a $9$ állt előtte.</p>'
         r'<p>A másik gyakori hiba az $e^2=a^2+b^2$ — ez a hiperbola képlete, ellipszisnél a fókusz '
         r'a görbén kívülre kerülne.</p>'),
   kviz(r'Mennyi a $4x^2+9y^2=36$ ellipszis két féltengelye?',
        [r'$a=3$, $b=2$', r'$a=4$, $b=9$', r'$a=2$, $b=3$', r'$a=9$, $b=4$'], 0,
        jo="✔ 36-tal osztva x²/9 + y²/4 = 1, tehát a = 3, b = 2.",
        nem="✘ Előbb a jobb oldallal kell osztani: x²/9 + y²/4 = 1. Az x² alatti szám a² = 9, az y² "
            "alatti b² = 4, így a = 3, b = 2."),
 ]),

 ("Ellipszis felírása adatokból", [
   r'<ul><li><b>$a$ és $b$ adott:</b> behelyettesítünk. $a=6$, $b=2$: $\frac{x^2}{36}+\frac{y^2}{4}=1$.</li>'
   r'<li><b>$a$ és $e$ adott:</b> $b^2=a^2-e^2$. $a=5$, $e=4$: $b^2=9$, $\frac{x^2}{25}+\frac{y^2}{9}=1$.</li>'
   r'<li><b>Két pontja adott:</b> a pontok koordinátáit beírjuk az egyenletbe. Két egyenletet kapunk, '
   r'amely az $\frac1{a^2}$ és $\frac1{b^2}$ ismeretlenekre nézve '
   r'<a href="' + V03 + r'tananyag-ket-ismeretlen.html#def-rendszer">lineáris rendszer</a>.</li></ul>',
   doboz("pelda", "Kristály-kamra szimuláció — a mező két peremi pontjából",
         r'<p>A műszerek egy origó középpontú, $x$-tengelyen fekvő fókuszú, ellipszis alakú mező peremén két pontot '
         r'mértek be: $M(4;1)$ és $N(2;2)$. Írd fel a mező egyenletét!</p>',
         hid="pelda-ket-pont-ellipszis",
         lenyilo=("Megoldás",
                  r'<p>Legyen $u=\frac1{a^2}$ és $v=\frac1{b^2}$. A két pontot beírva:</p>'
                  r'$$16u+v=1,\qquad 4u+4v=1 .$$'
                  r'<p>Az elsőből $v=1-16u$; a másodikba: $4u+4-64u=1$, azaz $-60u=-3$, $u=\frac1{20}$, '
                  r'és $v=1-\frac{16}{20}=\frac15$.</p>'
                  r'<p>Tehát $a^2=20$, $b^2=5$, és az egyenlet $\frac{x^2}{20}+\frac{y^2}{5}=1$.</p>'
                  r'<p><i>Ellenőrzés: $\frac{16}{20}+\frac15=1$ ✔, $\frac4{20}+\frac45=1$ ✔.</i></p>'
                  r'<p class="vegeredmeny">$\frac{x^2}{20}+\frac{y^2}{5}=1$</p>')),
   GY(FGY + "#alap-1", "A 1–6", FGY + "#kozep-1", "K 1–4"),
   brief('<b>Kanrak:</b> A mező peremét leírtuk. Maxi drónja most egyenes pályán közelít felé: '
         'átvág rajta, vagy csak súrolja? Ahol a pálya éppen csak érinti a peremet, ott a mező a '
         'leggyengébb.', outro=True),
 ]),
]

# ---------------------------------------------------------------- D2
D2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Kanrak:</b> Maxi a torzító mezőn át akar kitörni. Ahol a pályája éppen csak súrolja a '
         'mező peremét, ott egyetlen közös pont marad — ez Tér-eb következő <b>csapásmérési pontja</b>. '
         'A módszert már ismered a körnél; most ellipszisre alkalmazzuk.'),
 ]),

 ("Kölcsönös helyzet és húr", [
   r'<p>A <a href="tananyag-kor-es-egyenes.html#tetel-kolcsonos-helyzet-kor">körnél megismert '
   r'recept</a> változtatás nélkül működik: az egyenesből kifejezünk egy ismeretlent, beírjuk az '
   r'ellipszis egyenletébe, és a kapott másodfokú egyenlet diszkriminánsa dönt — $D\gt0$ szelő, '
   r'$D=0$ érintő, $D\lt0$ nincs közös pont. <i>(A távolságos módszer itt nem használható: az '
   r'ellipszisnek nincs egyetlen sugara.)</i></p>',
   doboz("pelda", "Egyenes és ellipszis metszéspontjai",
         r'<p>Határozd meg az $x^2+4y^2=25$ ellipszis és az $x+2y-7=0$ egyenes kölcsönös helyzetét, '
         r'a közös pontokat és a húr hosszát (két tizedesre kerekítve)!</p>',
         hid="pelda-metszespontok-ellipszis",
         lenyilo=("Megoldás",
                  r'<p>$x=7-2y$. Behelyettesítve: $(7-2y)^2+4y^2=25$, azaz $49-28y+8y^2=25$, '
                  r'rendezve $8y^2-28y+24=0$, osztva $4$-gyel: $2y^2-7y+6=0$.</p>'
                  r'<p>$D=49-48=1\gt0$ — szelő. $y_{1,2}=\frac{7\pm1}{4}$, tehát $y_1=2$, $y_2=\frac32$; '
                  r'hozzá $x_1=3$, $x_2=4$.</p>'
                  r'<p>A húr: $\sqrt{(4-3)^2+\left(\frac32-2\right)^2}=\sqrt{1+\frac14}=\frac{\sqrt5}{2}\approx1{,}12$.</p>'
                  r'<p><i>Az ábrán a $(3;2)$ pontbeli érintő is látszik: $3x+8y=25$.</i></p>'
                  + abra(SVG_ELL_EGY, 'Az ellipszis, a szelő (zöld) és a $(3;2)$ pontbeli érintő (borostyán).') +
                  r'<p class="vegeredmeny">szelő · $(3;2)$ és $\left(4;\frac32\right)$ · húr $\approx1{,}12$</p>')),
   kviz(r'Egy origó középpontú ellipszis kis féltengelye $b=3$ (az $y$-tengelyen). Hány közös pontja '
        r'van az $y=5$ egyenessel?',
        ['egy sem', 'egy', 'kettő', 'a nagy féltengelytől függ'], 0,
        jo="✔ Az ellipszis pontjaira |y| ≤ b = 3, így az y = 5 magasságig nem ér fel.",
        nem="✘ Az ellipszis a (0; ±3) csúcspontoknál magasabbra nem nyúlik, bármekkora is az a. "
            "Az y = 5 egyenes fölötte halad: nincs közös pont."),
 ]),

 ("Az érintő az ellipszis egy pontjában", [
   doboz("tetel", "Az ellipszis érintője egy pontjában",
         r'<p>Az $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$ ellipszis $T(x_1;y_1)$ pontjában húzott érintő '
         r'egyenlete</p>'
         r'$$\frac{x_1x}{a^2}+\frac{y_1y}{b^2}=1 .$$'
         r'<p>Előbb ellenőrizzük, hogy a $T$ az ellipszisen van.</p>',
         hid="tetel-erinto-ellipszis"),
   doboz("pelda", "Kristály-kamra szimuláció — érintő a mező peremén",
         r'<p>Tér-eb a $\frac{x^2}{25}+\frac{y^2}{16}=1$ mező $T(3;3{,}2)$ pontjába ugrik. Melyik '
         r'egyenes mentén csúszhat tovább úgy, hogy ne lépjen be a mezőbe? Írd fel az érintő '
         r'egyenletét!</p>',
         hid="pelda-erinto-ellipszis",
         lenyilo=("Megoldás",
                  r'<p><b>Ellenőrzés:</b> $\frac9{25}+\frac{10{,}24}{16}=0{,}36+0{,}64=1$ ✔.</p>'
                  r'<p><b>Képlet:</b> $\frac{3x}{25}+\frac{3{,}2\,y}{16}=1$, azaz $\frac{3x}{25}+\frac y5=1$. '
                  r'Szorozva $25$-tel: $3x+5y=25$.</p>'
                  r'<p class="vegeredmeny">$3x+5y-25=0$</p>')),
   doboz("csapda", "Maxi trükkje",
         r'<p>Maxi a $T(x_1;y_1)$ pont koordinátáit mindkét helyre beírta, és ezt kapta: '
         r'$\frac{x_1^2}{a^2}+\frac{y_1^2}{b^2}=1$. Ebben nincs se $x$, se $y$ — ez nem egyenes, hanem '
         r'csak annak az ellenőrzése, hogy a $T$ rajta van az ellipszisen.</p>'
         r'<p>Az érintőképletben az $x^2$ helyére $x_1\cdot x$ kerül: az egyik tényező a pont '
         r'koordinátája, a másik a változó marad.</p>'
         r'<p>Behelyettesítésnél a másik hiba itt is él: $(kx+n)^2\ne k^2x^2+n^2$.</p>'),
   kviz(r'Melyik egyenes érinti az $\frac{x^2}{8}+\frac{y^2}{2}=1$ ellipszist a $P(2;1)$ pontban?',
        [r'$x+2y=4$', r'$2x+y=5$', r'$x+y=3$', r'$\frac{4}{8}+\frac{1}{2}=1$'], 0,
        jo="✔ 2x/8 + 1·y/2 = 1, szorozva 4-gyel: x + 2y = 4.",
        nem="✘ A képlet: x₁x/a² + y₁y/b² = 1 → 2x/8 + y/2 = 1 → x + 2y = 4. A 4/8 + 1/2 = 1 csak az "
            "illeszkedés ellenőrzése, nem egyenes."),
 ]),

 ("Az érintési feltétel", [
   doboz("tetel", "Az ellipszis érintési feltétele",
         r'<p>Az $y=kx+n$ egyenes pontosan akkor érinti az $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$ '
         r'ellipszist, ha</p>'
         r'$$a^2k^2+b^2=n^2 .$$'
         r'<p>A feltétel a behelyettesítéses módszer $D=0$ esetéből jön. Minden nem függőleges '
         r'irányból pontosan két érintő van: $n=\pm\sqrt{a^2k^2+b^2}$.</p>'
         r'<p>🔴 <b>Kristály-protokoll:</b> az érintési feltétellel dolgozó feladatok a gyűjtemény '
         r'<b>nehéz</b> sávjában vannak.</p>',
         hid="tetel-erintesi-feltetel-ellipszis"),
   r'<p><b>Példa.</b> Melyik $\frac12$ iránytényezőjű egyenes érinti az $\frac{x^2}{8}+\frac{y^2}{2}=1$ '
   r'ellipszist? $a^2=8$, $b^2=2$, $k=\frac12$: $8\cdot\frac14+2=n^2$, $n^2=4$, $n=\pm2$. Az érintők: '
   r'$y=\frac12x+2$ és $y=\frac12x-2$.</p>'
   r'<p><i>Ellenőrzés az elsőre: behelyettesítve és $8$-cal szorozva $2x^2+8x+8=0$, azaz '
   r'$2(x+2)^2=0$, $D=0$ ✔.</i></p>',
   GY(FGY + "#alap-7", "A 7–10", FGY + "#kozep-5", "K 5–8"),
   brief('<b>Kanrak:</b> Az ellipszis-mező meggyengült. De a Kamra legveszélyesebb mezője még hátravan: '
         'a <b>hiperbola</b>. Ott a tér <b>két ágra szakad</b>, és a szakadás vonalai a végtelenbe '
         'nyúlnak.', outro=True),
 ]),
]

# ---------------------------------------------------------------- D3
D3 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Kanrak:</b> Itt a tér két ágra szakad. A mezőnek most is két magja van, de a perem '
         'pontjaira nem az összeg, hanem a <b>különbség</b> állandó. És van két vonal, amelyhez a '
         'szakadás egyre közelebb húzódik, de soha nem éri el — ezek az <b>aszimptoták</b>.'),
 ]),

 ("A hiperbola mint mértani hely", [
   doboz("definicio", "A hiperbola",
         r'<p>Adott két pont, $F_1$ és $F_2$ (a <b>fókuszok</b>), és egy $2a$ hosszúság, amely '
         r'<b>kisebb</b> a fókuszok $2e$ távolságánál ($0\lt2a\lt2e$). A <b>hiperbola</b> a sík mindazon $P$ '
         r'pontjainak halmaza, amelyekre</p>'
         r'$$\bigl|\,|PF_1|-|PF_2|\,\bigr|=2a .$$'
         r'<p>Az abszolút érték miatt két ág van: az egyiken a $P$ az $F_2$-höz, a másikon az '
         r'$F_1$-hez van közelebb.</p>',
         hid="def-hiperbola"),
   r'<p>Vesd össze az <a href="tananyag-ellipszis.html#def-ellipszis">ellipszissel</a>: ott a két '
   r'távolság <b>összege</b> állandó, és $2a\gt2e$; itt a <b>különbségük</b>, és $2a\lt2e$.</p>',
   doboz("erdekesseg", "Hol találkozol vele?",
         r'<p>Ha két rádióállomás egyszerre ad jelet, és a hajó műszere azt méri, hogy az egyik jel '
         r'mennyivel később érkezett, akkor ismert, hogy a hajó mennyivel van közelebb az egyik '
         r'állomáshoz, mint a másikhoz — vagyis a hajó egy hiperbola egyik ágán van. Egy harmadik '
         r'állomással egy második hiperbolát kapunk, a helyet a kettő metszéspontja adja. Így működött '
         r'például a LORAN-rendszer.</p>'),
 ]),

 ("A hiperbola egyenlete", [
   doboz("tetel", "A hiperbola egyenlete",
         r'<p>Ha a fókuszok $F_1(-e;0)$ és $F_2(e;0)$, akkor a hiperbola egyenlete</p>'
         r'$$\frac{x^2}{a^2}-\frac{y^2}{b^2}=1,\qquad\text{ahol}\qquad e^2=a^2+b^2 .$$'
         r'<ul><li>$a$ a <b>valós féltengely</b>, $b$ a <b>képzetes féltengely</b>, $e$ a '
         r'<b>lineáris excentricitás</b>;</li>'
         r'<li>a csúcspontok $(\pm a;0)$; az $y$-tengelyt a hiperbola <b>nem metszi</b>.</li></ul>',
         hid="tetel-hiperbola-egyenlete"),
   doboz("csapda", "Maxi trükkje",
         r'<p>Maxi az ellipszisnél megszokott képlettel számolt: $e^2=a^2-b^2$. Az $a=2$, $b=1{,}5$ '
         r'hiperbolánál így $e\approx1{,}32$ jött ki — a fókusz a $(\pm2;0)$ csúcsokon <b>belülre</b> '
         r'került, oda, ahol a hiperbolának nincs is pontja.</p>'
         r'<p>Hiperbolánál a fókusz <b>kívül</b> van a csúcsokon: $e^2=a^2+b^2$, itt '
         r'$e=\sqrt{4+2{,}25}=2{,}5$.</p>'),
 ]),

 ("Az aszimptoták", [
   doboz("tetel", "A hiperbola aszimptotái",
         r'<p>Az $\frac{x^2}{a^2}-\frac{y^2}{b^2}=1$ hiperbola aszimptotái az</p>'
         r'$$y=\frac bax\qquad\text{és}\qquad y=-\frac bax$$'
         r'<p>egyenesek. A hiperbola ágai egyre közelebb kerülnek hozzájuk, de soha nem érik el őket. '
         r'Az aszimptota fogalmával a <a href="' + E2H + r'#def-aszimptota">hatványfüggvényeknél</a> '
         r'már találkoztunk.</p>'
         r'<p><b>Vázlat:</b> rajzold meg a $(\pm a;\pm b)$ csúcsú téglalapot; az aszimptoták az átlói, '
         r'a hiperbola a $(\pm a;0)$ csúcsokból indul.</p>',
         hid="tetel-aszimptotak"),
   doboz("pelda", "A hiperbola adatai és vázlata",
         r'<p>Határozd meg a $9x^2-16y^2=36$ hiperbola féltengelyeit, lineáris excentricitását, '
         r'fókuszait és aszimptotáit, és vázold a hiperbolát!</p>',
         hid="pelda-hiperbola-adatai",
         lenyilo=("Megoldás",
                  r'<p>Osztunk $36$-tal: $\frac{x^2}{4}-\frac{y^2}{\frac94}=1$, tehát $a=2$, $b=\frac32$.</p>'
                  r'<p>$e^2=4+\frac94=\frac{25}4$, $e=\frac52$; a fókuszok $F_1(-2{,}5;0)$, $F_2(2{,}5;0)$.</p>'
                  r'<p>Az aszimptoták: $y=\pm\frac{3/2}{2}x=\pm\frac34x$.</p>'
                  + abra(SVG_HIP, 'A hiperbola, a $4\\times3$-as téglalap, az aszimptoták és a '
                         '$P(4;\\approx2{,}6)$ pont vezérsugarai: $7-3=4=2a$.') +
                  r'<p class="vegeredmeny">$a=2$, $b=1{,}5$, $e=2{,}5$, $F_{1,2}(\pm2{,}5;0)$, $y=\pm\frac34x$</p>')),
   kviz(r'Melyik egyenes aszimptotája az $\frac{x^2}{4}-\frac{y^2}{9}=1$ hiperbolának?',
        [r'$y=\frac32x$', r'$y=\frac23x$', r'$y=\frac94x$', r'$y=\frac49x$'], 0,
        jo="✔ a = 2, b = 3, az aszimptoták y = ±(b/a)x = ±(3/2)x.",
        nem="✘ Az aszimptota iránytényezője b/a (a képzetes féltengely osztva a valós féltengellyel): a = 2, b = 3, "
            "tehát ±3/2. A négyzetek (9/4) és a fordított arány (2/3) nem jó."),
 ]),

 ("Adatokból egyenlet — melyik görbe?", [
   r'<ul><li><b>$a$ és $e$ adott:</b> $b^2=e^2-a^2$.</li>'
   r'<li><b>Két pont adott:</b> ahogy az ellipszisnél, lineáris rendszer az $\frac1{a^2}$ és '
   r'$\frac1{b^2}$ ismeretlenre. Ha az egyik pont csúcspont, $(\pm a;0)$, az rögtön megadja az '
   r'$a$-t. Például a $(2;0)$ és a $(4;3)$ ponton átmenő hiperbolánál $a^2=4$, és '
   r'$\frac{16}4-\frac9{b^2}=1$-ből $b^2=3$: $\frac{x^2}4-\frac{y^2}3=1$.</li></ul>'
   r'<p><b>Melyik görbe?</b> Ha az egyenlet a tanult alapalakok egyikére hozható, és valóban '
   r'görbét ír le (a körnél és az ellipszisnél a rendezés után a jobb oldal pozitív, a parabolánál '
   r'a másik változó elsőfokon szerepel), akkor az alakjáról ránézésre eldönthető, melyik:</p>'
   r'<div class="tblwrap"><table class="tt-table">'
   r'<tr><th>az egyenletben</th><th>görbe</th></tr>'
   r'<tr><td>$x^2$ és $y^2$ azonos előjellel, egyenlő együtthatóval</td><td>kör</td></tr>'
   r'<tr><td>$x^2$ és $y^2$ azonos előjellel, különböző együtthatóval</td><td>ellipszis</td></tr>'
   r'<tr><td>$x^2$ és $y^2$ ellentétes előjellel</td><td>hiperbola</td></tr>'
   r'<tr><td>csak az egyik változó szerepel négyzeten</td><td>parabola</td></tr>'
   r'</table></div>',
   doboz("pelda", "Kristály-kamra szimuláció — melyik mező melyik?",
         r'<p>A műszer négy mező egyenletét rögzítette: (A) $x^2+y^2=9$, (B) $\frac{x^2}9+\frac{y^2}4=1$, '
         r'(C) $\frac{x^2}4-y^2=1$, (D) $y^2=4x$. Párosítsd az egyenleteket az ábrákkal! <i>(A parabolát a 12. lapon részletezzük; itt '
         r'elég annyi, hogy csak az egyik változó van négyzeten.)</i></p>'
         + abra(SVG_FELISMER, 'Négy mező a Kamrában, $1.$–$4.$ sorszámmal.'),
         hid="pelda-felismeres",
         lenyilo=("Megoldás",
                  r'<p>(A) egyenlő együtthatók → kör; (B) két pozitív, különböző nevező → ellipszis; '
                  r'(C) ellentétes előjel → hiperbola; (D) csak az $y$ van négyzeten → parabola.</p>'
                  r'<p class="vegeredmeny">(A) – 4. · (B) – 2. · (C) – 1. · (D) – 3.</p>')),
   kviz(r'Melyik görbét írja le a $4x^2-y^2=16$ egyenlet?',
        ['hiperbola', 'ellipszis', 'kör', 'parabola'], 0,
        jo="✔ Az x² és y² ellentétes előjelű: 16-tal osztva x²/4 − y²/16 = 1, hiperbola.",
        nem="✘ Nem az számít, hogy két négyzetes tag van, hanem az előjelük: x²/4 − y²/16 = 1, "
            "a mínusz miatt hiperbola."),
   GY(FGY + "#alap-11", "A 11–16", FGY + "#kozep-9", "K 9–12"),
   brief('<b>Kanrak:</b> A szakadás vonalai megvannak. Maxi azonban éppen ezek mentén próbál '
         'átcsúszni — és itt vár ránk a mező legcsalókább tulajdonsága: egyetlen közös pont még '
         '<b>nem</b> jelent érintést.', outro=True),
 ]),
]

# ---------------------------------------------------------------- D4
D4 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Kanrak:</b> Maxi a szakadás mentén próbál átcsúszni a hiperbola-mezőn. Vigyázat: itt '
         '<b>egyetlen közös pont még nem jelent érintést</b>. Aki ezt elnézi, rossz helyre küldi '
         'Tér-ebet.'),
 ]),

 ("Kölcsönös helyzet — az új eset", [
   doboz("tetel", "Egyenes és hiperbola kölcsönös helyzete",
         r'<p>A <a href="tananyag-kor-es-egyenes.html#tetel-kolcsonos-helyzet-kor">közös recept</a>: '
         r'behelyettesítés, majd a kapott egyenlet vizsgálata.</p>'
         r'<ul><li>Ha <b>másodfokú</b> egyenlet jön ki: $D\gt0$ két közös pont (szelő), $D=0$ érintő, '
         r'$D\lt0$ nincs közös pont.</li>'
         r'<li>Ha az egyenes <b>párhuzamos valamelyik aszimptotával</b>, de nem maga az aszimptota '
         r'($k=\pm\frac ba$, $n\ne0$), az $x^2$-es tagok kiesnek, és <b>elsőfokú</b> egyenlet marad: '
         r'pontosan <b>egy közös pont</b> van, de az egyenes <b>nem érintő</b> — átmetszi az egyik ágat.</li>'
         r'<li>Magának az aszimptotának nincs közös pontja a hiperbolával.</li></ul>',
         hid="tetel-kolcsonos-helyzet-hiperbola"),
   doboz("pelda", "Egy közös pont, mégsem érintő",
         r'<p>Vizsgáld meg az $\frac{x^2}4-y^2=1$ hiperbola és az $y=\frac12x+3$ egyenes kölcsönös '
         r'helyzetét!</p>',
         hid="pelda-aszimptotaval-parhuzamos",
         lenyilo=("Megoldás",
                  r'<p>A hiperbola aszimptotái $y=\pm\frac12x$ — az egyenes párhuzamos az egyikkel.</p>'
                  r'<p>$4$-gyel szorozva a hiperbola $x^2-4y^2=4$. Behelyettesítve: '
                  r'$x^2-4\left(\frac14x^2+3x+9\right)=4$, azaz $x^2-x^2-12x-36=4$, tehát $-12x=40$, '
                  r'$x=-\frac{10}3$, és $y=-\frac53+3=\frac43$.</p>'
                  r'<p>Egyetlen közös pont van, $M\left(-\frac{10}3;\frac43\right)$, de az egyenes '
                  r'<b>metszi</b> a hiperbola bal ágát, nem érinti.</p>'
                  + abra(SVG_HIP_PAR, 'Az aszimptotával párhuzamos egyenes átmegy az ágon.') +
                  r'<p class="vegeredmeny">egy közös pont, $M\left(-\frac{10}3;\frac43\right)$ — '
                  r'metszi, nem érinti</p>')),
   doboz("csapda", "Maxi trükkje",
         r'<p>Maxi a fenti számolás végén elégedetten felírta: „egy megoldás, tehát az egyenes '
         r'érinti a hiperbolát”. Tér-eb a mező közepébe ugrott.</p>'
         r'<p>Az „egy közös pont = érintő” szabály a <b>körnél és az ellipszisnél</b> igaz. A '
         r'hiperbolánál (és majd a parabolánál) csak akkor, ha a behelyettesítés <b>másodfokú</b> '
         r'egyenletre vezetett, és annak $D=0$. Ha elsőfokú lett, az egyenes metsző.</p>'),
   kviz(r'Egy egyenes és egy hiperbola egyenletéből a behelyettesítés <b>elsőfokú</b> egyenletet adott, '
        r'egyetlen megoldással. Mit mondhatunk az egyenesről?',
        ['egy pontban metszi a hiperbolát, de nem érinti', 'érinti a hiperbolát',
         'nincs közös pontja a hiperbolával', 'ez maga az aszimptota'], 0,
        jo="✔ Az egyenes párhuzamos egy aszimptotával: egy ágat egyszer átmetsz, érintés nincs.",
        nem="✘ Érintésről csak másodfokú egyenlet D = 0 esetén beszélünk. Az elsőfokú egyenlet azt "
            "jelzi, hogy az egyenes aszimptotával párhuzamos: egyszer metsz, nem érint."),
 ]),

 ("Az érintő a hiperbola egy pontjában", [
   doboz("tetel", "A hiperbola érintője egy pontjában",
         r'<p>Az $\frac{x^2}{a^2}-\frac{y^2}{b^2}=1$ hiperbola $T(x_1;y_1)$ pontjában húzott érintő '
         r'egyenlete</p>'
         r'$$\frac{x_1x}{a^2}-\frac{y_1y}{b^2}=1 .$$'
         r'<p>A képlet ugyanúgy épül, mint az ellipszisé — csak a <b>mínuszjel</b> marad meg.</p>',
         hid="tetel-erinto-hiperbola"),
   doboz("pelda", "Kristály-kamra szimuláció — súrolja-e Maxi pályája a mezőt?",
         r'<p>Maxi drónja az $y=x-1$ egyenes mentén repül, a mező az $\frac{x^2}4-\frac{y^2}3=1$ '
         r'hiperbola.</p>'
         r'<ol type="a"><li>Hány közös pontja van a pályának és a mezőnek?</li>'
         r'<li>Ha érinti, hol? Ellenőrizd az érintőképlettel!</li></ol>',
         hid="pelda-erinto-hiperbola",
         lenyilo=("Megoldás",
                  r'<p><b>a)</b> $12$-vel szorozva a hiperbola $3x^2-4y^2=12$. Behelyettesítve: '
                  r'$3x^2-4(x-1)^2=12$, azaz $-x^2+8x-16=0$, vagyis $x^2-8x+16=0$. '
                  r'$D=64-64=0$ — egy közös pont, és mivel az egyenlet másodfokú, ez <b>érintés</b>.</p>'
                  r'<p><b>b)</b> $x=4$, $y=3$: $T(4;3)$. Rajta van: $\frac{16}4-\frac93=4-3=1$ ✔. Az '
                  r'érintőképlettel: $\frac{4x}4-\frac{3y}3=1$, azaz $x-y=1$, ami éppen $y=x-1$ ✔.</p>'
                  + abra(SVG_HIP_ER, 'A pálya a $T(4;3)$ pontban érinti a mezőt.') +
                  r'<p class="vegeredmeny">a) egy közös pont (érintés) · b) $T(4;3)$</p>')),
   kviz(r'Melyik egyenes érinti az $\frac{x^2}{8}-\frac{y^2}{4}=1$ hiperbolát a $P(4;2)$ pontban?',
        [r'$x-y=2$', r'$x+y=2$', r'$x+y=6$', r'$2x-y=6$'], 0,
        jo="✔ 4x/8 − 2y/4 = 1, szorozva 2-vel: x − y = 2.",
        nem="✘ A hiperbola érintőképletében megmarad a mínusz: 4x/8 − 2y/4 = 1 → x − y = 2. Az "
            "x + y = 2 (az ellipszis képletéből) át sem megy a P-n; a hiperbolát ugyan érinti, de a "
            "(4; −2) pontban."),
 ]),

 ("Az érintési feltétel", [
   doboz("tetel", "A hiperbola érintési feltétele",
         r'<p>Ha $|k|\gt\frac ba$, az $y=kx+n$ egyenes pontosan akkor érinti az '
         r'$\frac{x^2}{a^2}-\frac{y^2}{b^2}=1$ hiperbolát, ha</p>'
         r'$$a^2k^2-b^2=n^2 .$$'
         r'<p>Ha $|k|\le\frac ba$ (az egyenes nem meredekebb az aszimptotáknál), nincs ilyen irányú '
         r'érintő. Vigyázat: az aszimptota ($|k|=\frac ba$, $n=0$) kielégíti az egyenlőséget, mégsem '
         r'érintő.</p>'
         r'<p>🔴 <b>Kristály-protokoll:</b> az érintési feltétellel dolgozó feladatok a gyűjtemény '
         r'<b>nehéz</b> sávjában vannak.</p>',
         hid="tetel-erintesi-feltetel-hiperbola"),
   r'<p><b>Példa.</b> Melyik $k=1$ iránytényezőjű egyenes érinti az $\frac{x^2}4-\frac{y^2}3=1$ '
   r'hiperbolát? $\frac ba=\frac{\sqrt3}2\approx0{,}87\lt1$, tehát van ilyen. $4\cdot1-3=n^2$, '
   r'$n=\pm1$: az érintők $y=x+1$ és $y=x-1$. Az utóbbi a fenti példa pályája.</p>',
   GY(FGY + "#alap-17", "A 17–20", FGY + "#kozep-13", "K 13–16"),
   brief('<b>Kanrak:</b> A hiperbola-mező is lezárva. Maxi azonban az utolsó eszközét is bevetette: '
         'egy <b>parabolatükröt</b>, amely a Kristálypára energiáját egyetlen pontba gyűjti. Meg kell '
         'találnunk ezt a pontot.', outro=True),
 ]),
]

# ---------------------------------------------------------------- lapok
KI = [
 lap(**T, fajl="tananyag-ellipszis.html", cim="Az ellipszis",
     alcim="Az ellipszis mint mértani hely, az egyenlete, a féltengelyek és a fókuszok, valamint "
           "az ellipszis felírása adatokból.",
     chip=KUL + " · 8/13", szakaszok=D1,
     elozo=("feladatok-kor.html", "A kör — feladatok"),
     kovetkezo=("tananyag-ellipszis-es-egyenes.html", "Az ellipszis és az egyenes")),
 lap(**T, fajl="tananyag-ellipszis-es-egyenes.html", cim="Az ellipszis és az egyenes",
     alcim="Az egyenes és az ellipszis kölcsönös helyzete, a húr, az érintő az ellipszis egy "
           "pontjában és az érintési feltétel.",
     chip=KUL + " · 9/13", szakaszok=D2,
     elozo=("tananyag-ellipszis.html", "Az ellipszis"),
     kovetkezo=("tananyag-hiperbola.html", "A hiperbola")),
 lap(**T, fajl="tananyag-hiperbola.html", cim="A hiperbola",
     alcim="A hiperbola mint mértani hely, az egyenlete, az aszimptotái, a felírása adatokból, és "
           "a négy görbe felismerése az egyenletből.",
     chip=KUL + " · 10/13", szakaszok=D3,
     elozo=("tananyag-ellipszis-es-egyenes.html", "Az ellipszis és az egyenes"),
     kovetkezo=("tananyag-hiperbola-es-egyenes.html", "A hiperbola és az egyenes")),
 lap(**T, fajl="tananyag-hiperbola-es-egyenes.html", cim="A hiperbola és az egyenes",
     alcim="Az egyenes és a hiperbola kölcsönös helyzete — az aszimptotával párhuzamos egyenes "
           "esetével —, az érintő a hiperbola egy pontjában és az érintési feltétel.",
     chip=KUL + " · 11/13", szakaszok=D4,
     elozo=("tananyag-hiperbola.html", "A hiperbola"),
     kovetkezo=(FGY, "Ellipszis és hiperbola — feladatok")),
]
for u in KI:
    print("✓", os.path.basename(u))
