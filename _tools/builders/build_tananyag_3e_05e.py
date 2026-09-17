# -*- coding: utf-8 -*-
"""3e/05 — E blokk: a parabola (E1), a parabola es az egyenes (E2).
Mentor: Kanrak (Ter-eb). Kuldetes: A Terkep Halozata."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra
from abra_common import svg_koordsik, svg_kupszelet, KEK, BOROSTYAN, ZOLD, PIROS, SZURKE, LILA

T = dict(tagozat="3e", mappa="05-analitikus-geometria", temakor="Síkbeli analitikus geometria")
FGY = "feladatok-parabola.html"
KUL = "A Térkép Hálózata"
E2F = "../../2e/02-masodfoku-egyenletek-es-fuggvenyek/tananyag-masodfoku-fuggveny.html"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(k_h, k_c, n_h, n_c, tagozat="3e")


# ---------------------------------------------------------------- önteszt
from sympy import Rational, sqrt, simplify, symbols, solve, expand, discriminant, factor
E = []
def chk(n, g, w):
    if isinstance(g, (tuple, list)):
        ok = len(g) == len(w) and all(
            (all(simplify(a - b) == 0 for a, b in zip(u, v)) if isinstance(u, tuple) else simplify(u - v) == 0)
            for u, v in zip(g, w))
    else:
        ok = simplify(g - w) == 0
    if not ok:
        E.append((n, g, w))
x, y, n_ = symbols("x y n")
# E1
chk("fokusz-12", Rational(12, 2)/2, 3)
chk("fokusz-8", Rational(8, 2)/2, 2)
chk("peremi-p", solve(36 - 2*n_*9, n_), [2])
chk("peremi-F-tav", sqrt((9 - 1)**2 + (6 - 0)**2), 10); chk("peremi-vez-tav", 9 - (-1), 10)
chk("kviz-20", Rational(20, 2)/2, 5)
chk("maxi-nem-megy-at", 2*1 + 2, 4)
chk("maxi-nincs-kozos", discriminant(expand((2*x + 2)**2 - 4*x), x), -48)
chk("2e-p", Rational(1, 2*Rational(1, 4)), 2)
chk("x2-4y-F", (0, Rational(4, 2)/2), (0, 1))
# E2
pts = solve([y**2 - 4*x, y - (x - 3)], [x, y]); chk("szelo", sorted(pts), [(1, -2), (9, 6)])
chk("vizszintes", solve((2)**2 - 4*x, x), [1])
chk("erinto-kviz", solve(2*y - 2*(x + 1), y), [x + 1])
chk("erinto-kviz-D", discriminant(expand((x + 1)**2 - 4*x), x), 0)
pts2 = solve([y**2 - 8*x, y - (x - 6)], [x, y]); chk("peremi-metsz", sorted(pts2), [(2, -4), (18, 12)])
chk("erinto-1", solve(-4*y - 4*(x + 2), y), [-x - 2])
chk("erinto-2", expand(12*y - 4*(x + 18)), expand(4*(3*y - x - 18)))
chk("erinto-1-D", discriminant(expand((-x - 2)**2 - 8*x), x), 0)
chk("erinto-2-D", discriminant(expand(((x + 18)/3)**2 - 8*x), x), 0)
chk("feltetel", solve(4 - 2*2*n_, n_), [1])
chk("feltetel-D", factor(expand((2*x + 1)**2 - 8*x)), (2*x - 1)**2)
chk("maxi-2p", solve(2*y - 4*(x + 1), y), [2*x + 2])
assert not E, E
print("sympy önteszt: OK")

# ---------------------------------------------------------------- ábrák
SVG_PAR = svg_kupszelet(
    "parabola", {"p": 4}, pont=(2, 4),
    xr=(-4, 8), yr=(-6, 6), egyseg=26,
    leiras="Az y² = 8x parabola, az F(2;0) fókusz, az x = −2 vezéregyenes és a P(2;4) pont, amely a "
           "fókusztól és a vezéregyenestől is 4 egységre van")
SVG_X2 = svg_kupszelet(
    "parabola", {"p": 2, "tengely": "y"},
    feliratok=[((3.2, 3.9), "x² = 4y  ⇔  y = ¼x²", {"szin": KEK, "meret": 13})],
    xr=(-5, 6), yr=(-2, 5), egyseg=28,
    leiras="Az x² = 4y parabola, ami a 2e-ből ismert y = ¼x² függvény grafikonja, fókusza F(0;1), "
           "vezéregyenese y = −1")
SVG_PAR_EGY = svg_kupszelet(
    "parabola", {"p": 2}, fokuszok=False, vezeregyenes=False,
    egyenesek=[((0, 1, -2), ZOLD, "y = 2", {"hely": 0.9, "dx": -10, "dy": -4, "dolt": False}),
               ((1, -1, 1), BOROSTYAN, "y = x + 1", {"hely": 0.88, "dx": -46, "dy": 4, "dolt": False})],
    pontok=[((1, 2), "P", {"dx": -12, "dy": -8})],
    xr=(-3, 7), yr=(-5, 6), egyseg=26,
    leiras="Az y² = 4x parabola, a tengelyével párhuzamos y = 2 egyenes, amely a P(1;2) pontban metszi, "
           "és az y = x + 1 érintő ugyanabban a pontban")

# ---------------------------------------------------------------- E1
E1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Kanrak:</b> Maxi utolsó eszköze egy <b>parabolatükör</b>: a Kristálypára energiáját '
         'egyetlen pontba, a <b>fókuszba</b> gyűjti. Ha tudjuk, hol a fókusz, tudjuk, hová nem szabad '
         'Tér-ebnek ugrania — és hová kell a tükröt eltalálni.'),
 ]),

 ("A parabola mint mértani hely", [
   doboz("definicio", "A parabola",
         r'<p>Adott a síkban egy $F$ pont (a <b>fókusz</b>) és egy rá nem illeszkedő $v$ egyenes '
         r'(a <b>vezéregyenes</b>, más néven direktrix). A <b>parabola</b> a sík mindazon $P$ '
         r'pontjainak halmaza, amelyek a fókusztól és a vezéregyenestől <b>egyenlő távolságra</b> '
         r'vannak.</p>'
         r'<p>A fókusz és a vezéregyenes távolsága a parabola <b>paramétere</b>, $p$. A parabola '
         r'<b>csúcsa</b> félúton van a fókusz és a vezéregyenes között.</p>',
         hid="def-parabola"),
   doboz("erdekesseg", "Hol találkozol vele?",
         r'<p>A parabolaantenna és a fényszóró tükre olyan felület, amelyet egy parabola tengelye körüli '
         r'megforgatásával kapunk. A tengellyel '
         r'párhuzamosan érkező sugarak a tükörről mind a <b>fókuszba</b> verődnek — ott van az antenna '
         r'vevőfeje. A fényszórónál fordítva: a fókuszba tett izzó fénye párhuzamos nyalábként '
         r'lép ki.</p>'),
 ]),

 ("A parabola egyenlete", [
   doboz("tetel", "A parabola egyenlete",
         r'<p>Ha a csúcs az origó, a fókusz $F\left(\frac p2;0\right)$ és a vezéregyenes '
         r'$x=-\frac p2$ ($p\gt0$), a parabola egyenlete</p>'
         r'$$y^2=2px .$$'
         r'<p>A képlettár négy alakja, a nyílás irányával:</p>'
         r'<div class="tblwrap"><table class="tt-table">'
         r'<tr><th>egyenlet</th><th>nyílik</th><th>fókusz</th><th>vezéregyenes</th></tr>'
         r'<tr><td>$y^2=2px$</td><td>jobbra</td><td>$\left(\frac p2;0\right)$</td><td>$x=-\frac p2$</td></tr>'
         r'<tr><td>$y^2=-2px$</td><td>balra</td><td>$\left(-\frac p2;0\right)$</td><td>$x=\frac p2$</td></tr>'
         r'<tr><td>$x^2=2py$</td><td>felfelé</td><td>$\left(0;\frac p2\right)$</td><td>$y=-\frac p2$</td></tr>'
         r'<tr><td>$x^2=-2py$</td><td>lefelé</td><td>$\left(0;-\frac p2\right)$</td><td>$y=\frac p2$</td></tr>'
         r'</table></div>'
         r'<p><i>Figyelj a betűre: ez a $p$ a parabola paramétere, nem a kör középpontjának '
         r'első koordinátája.</i></p>',
         hid="tetel-parabola-egyenlete"),
   abra(SVG_PAR, 'Az $y^2=8x$ parabola: $2p=8$, $p=4$, a fókusz $F(2;0)$, a vezéregyenes $x=-2$. '
        'A $P(2;4)$ a fókusztól és a vezéregyenestől is $4$ egységre van.'),
   doboz("erdekesseg", "Ismerős görbe",
         r'<p>A 2e-ben a <a href="' + E2F + r'#def-masodfoku-fuggveny">másodfokú függvény</a> '
         r'grafikonját is parabolának neveztük — joggal. Az $y=\frac14x^2$ függvény egyenlete átrendezve '
         r'$x^2=4y$, vagyis $2p=4$, $p=2$: egy felfelé nyíló parabola, fókusza $F(0;1)$, vezéregyenese '
         r'$y=-1$. Általában az $y=cx^2$ ($c\gt0$) grafikonja az $x^2=2py$ parabola, ahol $p=\frac1{2c}$.</p>'
         + abra(SVG_X2, 'A 2e-ből ismert $y=\\frac14x^2$ grafikon mint $x^2=4y$ parabola.')),
   kviz(r'Merre nyílik az $x^2=-4y$ parabola?',
        ['lefelé', 'balra', 'felfelé', 'jobbra'], 0,
        jo="✔ Az x van négyzeten, tehát fel vagy le nyílik; a mínusz miatt lefelé (y ≤ 0).",
        nem="✘ A mínuszjel nem mindig balra fordít: itt az x van négyzeten, ezért a parabola "
            "függőleges tengelyű, és mivel y = −x²/4 ≤ 0, lefelé nyílik."),
 ]),

 ("Adatok és felírás", [
   r'<p><b>Egyenletből az adatok.</b> Az $y^2=2px$ alakban az $x$ együtthatója $2p$: ebből előbb $p$-t, '
   r'aztán a fókusz első koordinátáját, $\frac p2$-t kapjuk. Például $y^2=12x$: $2p=12$, $p=6$, a fókusz $F(3;0)$, a vezéregyenes $x=-3$.</p>'
   r'<p><b>Egy pontból az egyenlet.</b> Ha tudjuk, melyik alak (például jobbra nyílik), a pont '
   r'koordinátáit behelyettesítve megkapjuk a $p$-t.</p>',
   doboz("pelda", "Kristály-kamra szimuláció — hol a tükör fókusza?",
         r'<p>Maxi tükre jobbra nyíló, csúcsa az origó, és a pereme átmegy a $P(9;6)$ ponton. '
         r'Írd fel a tükör egyenletét, és add meg a fókuszát meg a vezéregyenesét! Ellenőrizd, hogy a '
         r'$P$ tényleg egyenlő távolságra van a fókusztól és a vezéregyenestől!</p>',
         hid="pelda-fokusz",
         lenyilo=("Megoldás",
                  r'<p>$y^2=2px$, és a $P(9;6)$ rajta van: $36=2p\cdot9$, tehát $p=2$. Az egyenlet '
                  r'$y^2=4x$.</p>'
                  r'<p>Fókusz: $F\left(\frac22;0\right)=F(1;0)$, vezéregyenes: $x=-1$.</p>'
                  r'<p><i>Ellenőrzés: $|PF|=\sqrt{(9-1)^2+6^2}=\sqrt{100}=10$, a $P$ távolsága az '
                  r'$x=-1$ egyenestől $9-(-1)=10$ ✔.</i></p>'
                  r'<p class="vegeredmeny">$y^2=4x$ · $F(1;0)$ · $x=-1$</p>')),
   doboz("csapda", "Maxi trükkje",
         r'<p>Maxi az $y^2=12x$ tükör fókuszát először $F(12;0)$-ba, aztán $F(6;0)$-ba tette. Tér-eb '
         r'mindkétszer elvétette.</p>'
         r'<p>Az egyenletben $2p$ áll, nem $p$: $2p=12$, $p=6$. A fókusz pedig nem $p$, hanem '
         r'$\frac p2$ távolságra van a csúcstól: $F(3;0)$. Két lépés, két felezés — egyik sem '
         r'maradhat el.</p>'),
   kviz(r'Hol van az $y^2=20x$ parabola fókusza?',
        [r'$F(5;0)$', r'$F(10;0)$', r'$F(20;0)$', r'$F(0;5)$'], 0,
        jo="✔ 2p = 20, p = 10, a fókusz p/2 = 5 távolságra: F(5; 0).",
        nem="✘ Az x együtthatója 2p, nem p: 2p = 20 → p = 10, és a fókusz p/2-re van: F(5; 0). "
            "Az y² miatt a fókusz az x-tengelyen van."),
   GY(FGY + "#alap-1", "A 1–5", FGY + "#kozep-1", "K 1–4"),
   brief('<b>Kanrak:</b> A fókusz megvan: Tér-eb oda nem ugorhat, mert elégetné a Kristálypára. A '
         'tükör peremét csak <b>egyetlen egyenes</b> mentén lehet biztonságosan elérni — egy '
         '<b>érintő</b> mentén. Az utolsó csapás következik.', outro=True),
 ]),
]

# ---------------------------------------------------------------- E2
E2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Kanrak:</b> Az utolsó csapás. Tér-eb a tükör peremét csak úgy érheti el, hogy közben ne '
         'kerüljön a fókusz lángjába: <b>egy érintő mentén</b>. Megkeressük az érintőt — és még egyszer '
         'figyelünk a hiperbolánál látott csapdára.'),
 ]),

 ("Kölcsönös helyzet — az új eset", [
   doboz("tetel", "Egyenes és parabola kölcsönös helyzete",
         r'<p>A <a href="tananyag-kor-es-egyenes.html#tetel-kolcsonos-helyzet-kor">közös recept</a> '
         r'itt is működik: behelyettesítés, majd a kapott egyenlet vizsgálata.</p>'
         r'<ul><li>Ha <b>másodfokú</b> egyenlet jön ki: $D\gt0$ két közös pont, $D=0$ érintő, $D\lt0$ '
         r'nincs közös pont.</li>'
         r'<li>Ha az egyenes <b>párhuzamos a parabola tengelyével</b> (az $y^2=2px$ parabolánál '
         r'vízszintes, $y=c$), <b>elsőfokú</b> egyenlet marad: egy közös pont van, de az egyenes '
         r'<b>nem érintő</b> — ahogy a <a href="tananyag-hiperbola-es-egyenes.html#tetel-kolcsonos-helyzet-hiperbola">'
         r'hiperbola aszimptotájával párhuzamos</a> egyenesnél.</li></ul>',
         hid="tetel-kolcsonos-helyzet-parabola"),
   r'<p><b>Példa.</b> $y^2=4x$ és $y=x-3$. Az $x=y+3$-at beírva $y^2=4y+12$, azaz $y^2-4y-12=0$, '
   r'$D=16+48=64\gt0$: két közös pont, $y=6$ és $y=-2$, vagyis $(9;6)$ és $(1;-2)$.</p>'
   r'<p>Az $y=2$ egyenesnél viszont $4=4x$, $x=1$: egyetlen közös pont, $(1;2)$ — de ez metszés, '
   r'nem érintés.</p>',
   kviz(r'Milyen helyzetű az $y=2$ egyenes és az $y^2=4x$ parabola?',
        ['egy pontban metszi, de nem érinti', 'érinti az $(1;2)$ pontban',
         'nincs közös pontjuk', 'két pontban metszi'], 0,
        jo="✔ A vízszintes egyenes párhuzamos a parabola tengelyével: egyszer átmetsz rajta.",
        nem="✘ A behelyettesítés elsőfokú egyenletet ad (4 = 4x), ezért egy közös pont van, de az "
            "egyenes a parabola tengelyével párhuzamos, átmetszi a görbét — nem érinti."),
 ]),

 ("Az érintő a parabola egy pontjában", [
   doboz("tetel", "A parabola érintője egy pontjában",
         r'<p>Az $y^2=2px$ parabola $T(x_1;y_1)$ pontjában húzott érintő egyenlete</p>'
         r'$$y_1y=p\,(x+x_1) .$$'
         r'<p>A képlet itt is a „fele-fele” mintát követi: az $y^2$ helyére $y_1\cdot y$, a $2x$ '
         r'helyére $x+x_1$ kerül — ezért lesz $2p$ helyett $p$ az együttható.</p>',
         hid="tetel-erinto-parabola"),
   abra(SVG_PAR_EGY, 'Az $y^2=4x$ parabola: az $y=2$ egyenes átmetszi, az $y=x+1$ érinti — '
        'ugyanabban a $P(1;2)$ pontban.'),
   doboz("pelda", "Kristály-kamra szimuláció — két csapásmérési pont",
         r'<p>Maxi drónja az $y=x-6$ egyenes mentén átvág az $y^2=8x$ tükrön.</p>'
         r'<ol type="a"><li>Hol metszi a pálya a tükör peremét?</li>'
         r'<li>Írd fel a tükör érintőjét mindkét metszéspontban!</li></ol>',
         hid="pelda-erinto-parabola",
         lenyilo=("Megoldás",
                  r'<p><b>a)</b> $(x-6)^2=8x$, azaz $x^2-20x+36=0$, $D=400-144=256$, '
                  r'$x_{1,2}=\frac{20\pm16}{2}$: $x=2$ vagy $x=18$. A pontok $T_1(2;-4)$ és $T_2(18;12)$.</p>'
                  r'<p><b>b)</b> Az $y^2=8x$ parabolánál $2p=8$, $p=4$.</p>'
                  r'<ul><li>$T_1$-ben: $-4y=4(x+2)$, azaz $y=-x-2$.</li>'
                  r'<li>$T_2$-ben: $12y=4(x+18)$, azaz $3y=x+18$, rendezve $x-3y+18=0$.</li></ul>'
                  r'<p class="vegeredmeny">a) $(2;-4)$ és $(18;12)$ · b) $y=-x-2$ és $x-3y+18=0$</p>')),
   doboz("csapda", "Maxi trükkje",
         r'<p>Maxi az $y^2=4x$ parabola $P(1;2)$ pontjában a parabola egyenletéből „átmásolta” a '
         r'$2p$-t: $2y=4(x+1)$, azaz $y=2x+2$. Ez az egyenes át sem megy a $P$-n ($2\cdot1+2=4\ne2$), '
         r'sőt a parabolával egyetlen közös pontja sincs. Egyszerű ellenőrzés: az érintési pontnak '
         r'mindig rajta kell lennie az érintőn.</p>'
         r'<p>Az érintőképletben $p$ áll, nem $2p$: $2p=4$, $p=2$, tehát $2y=2(x+1)$, és az érintő '
         r'$y=x+1$.</p>'),
   kviz(r'Melyik egyenes érinti az $y^2=4x$ parabolát a $P(1;2)$ pontban?',
        [r'$y=x+1$', r'$y=2x+2$', r'$y=2x$', r'$y=x-1$'], 0,
        jo="✔ 2p = 4, p = 2: 2y = 2(x + 1), tehát y = x + 1.",
        nem="✘ Az érintőképlet y₁y = p(x + x₁), és p = 2 (nem 4): 2y = 2(x + 1), y = x + 1. "
            "Az y = 2x + 2 a 2p-vel számolt, hibás egyenes."),
 ]),

 ("Az érintési feltétel", [
   doboz("tetel", "A parabola érintési feltétele",
         r'<p>Az $y=kx+n$ egyenes ($k\ne0$) pontosan akkor érinti az $y^2=2px$ parabolát, ha</p>'
         r'$$p=2kn .$$'
         r'<p>A feltétel most is a behelyettesítéses módszer $D=0$ esetéből jön.</p>'
         r'<p>🔴 <b>Kristály-protokoll:</b> az érintési feltétellel dolgozó feladatok a gyűjtemény '
         r'<b>nehéz</b> sávjában vannak.</p>',
         hid="tetel-erintesi-feltetel-parabola"),
   r'<p><b>Példa.</b> Melyik $k=2$ iránytényezőjű egyenes érinti az $y^2=8x$ parabolát? $p=4$: '
   r'$4=2\cdot2\cdot n$, $n=1$. Az érintő $y=2x+1$. <i>Ellenőrzés: $(2x+1)^2=8x$, azaz '
   r'$4x^2-4x+1=0$, $(2x-1)^2=0$, $D=0$ ✔ — az érintési pont $\left(\frac12;2\right)$.</i></p>'
   r'<p>Figyeld meg: az $y^2=2px$ parabolának minden $k\ne0$ irányból <b>pontosan egy</b> érintője '
   r'van. A körnek és az ellipszisnek minden irányból kettő, a hiperbolának kettő, ha '
   r'$|k|\gt\frac ba$, különben egy sem.</p>',
 ]),

 ("🧾 Gyorsismétlő", [
   r'<p>A II. rész négy görbéje egy táblázatban — a 4. dolgozat előtt.</p>'
   r'<div class="tblwrap"><table class="tt-table">'
   r'<tr><th></th><th>egyenlet</th><th>adatok</th><th>érintő a $T(x_1;y_1)$ pontban</th>'
   r'<th>érintési feltétel ($y=kx+n$)</th></tr>'
   r'<tr><td><a href="tananyag-kor-egyenlete.html#tetel-kor-egyenlete">kör</a></td>'
   r'<td>$(x-p)^2+(y-q)^2=r^2$</td><td>$C(p;q)$, $r$</td>'
   r'<td>$(x_1-p)(x-p)+(y_1-q)(y-q)=r^2$</td><td>$r^2(1+k^2)=(kp-q+n)^2$</td></tr>'
   r'<tr><td><a href="tananyag-ellipszis.html#tetel-ellipszis-egyenlete">ellipszis</a></td>'
   r'<td>$\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$</td><td>$e^2=a^2-b^2$, $F(\pm e;0)$</td>'
   r'<td>$\frac{x_1x}{a^2}+\frac{y_1y}{b^2}=1$</td><td>$a^2k^2+b^2=n^2$</td></tr>'
   r'<tr><td><a href="tananyag-hiperbola.html#tetel-hiperbola-egyenlete">hiperbola</a></td>'
   r'<td>$\frac{x^2}{a^2}-\frac{y^2}{b^2}=1$</td><td>$e^2=a^2+b^2$, $F(\pm e;0)$, $y=\pm\frac bax$</td>'
   r'<td>$\frac{x_1x}{a^2}-\frac{y_1y}{b^2}=1$</td><td>$a^2k^2-b^2=n^2$ (ha $|k|\gt\frac ba$)</td></tr>'
   r'<tr><td><a href="tananyag-parabola.html#tetel-parabola-egyenlete">parabola</a></td>'
   r'<td>$y^2=2px$</td><td>$F\left(\frac p2;0\right)$, $x=-\frac p2$</td>'
   r'<td>$y_1y=p(x+x_1)$</td><td>$p=2kn$ ($k\ne0$)</td></tr>'
   r'</table></div>'
   r'<p><b>A kölcsönös helyzet receptje</b> mind a négy görbénél: behelyettesítés → másodfokú '
   r'egyenlet → $D\gt0$ szelő, $D=0$ érintő, $D\lt0$ nincs közös pont. Ha elsőfokú egyenlet jön '
   r'ki (hiperbola: aszimptotával párhuzamos; parabola: tengellyel párhuzamos egyenes), egy közös '
   r'pont van, de <b>nem érintés</b>. (Magának az aszimptotának nincs közös pontja a hiperbolával.)</p>',
   GY(FGY + "#alap-6", "A 6–10", FGY + "#kozep-5", "K 5–8"),
   brief('<b>Kanrak:</b> Maxi bemérve: minden kapuját, mezőjét és tükrét feltérképeztük, Tér-eb '
         'mindegyiken átjutott. De amit elindított, az nem áll meg magától. A Kristálypára-generátor '
         '<b>láncreakciója</b> lépésről lépésre nő tovább — Prizmával együtt most azt kell '
         'kiszámolnunk, hogy az $n$-edik lépésnél hol tart.', outro=True),
 ]),
]

# ---------------------------------------------------------------- lapok
KI = [
 lap(**T, fajl="tananyag-parabola.html", cim="A parabola",
     alcim="A parabola mint mértani hely, az egyenlete, a fókusz és a vezéregyenes, a kapcsolat a "
           "másodfokú függvénnyel, és a parabola felírása adatokból.",
     chip=KUL + " · 12/13", szakaszok=E1,
     elozo=("feladatok-ellipszis-hiperbola.html", "Ellipszis és hiperbola — feladatok"),
     kovetkezo=("tananyag-parabola-es-egyenes.html", "A parabola és az egyenes")),
 lap(**T, fajl="tananyag-parabola-es-egyenes.html", cim="A parabola és az egyenes",
     alcim="Az egyenes és a parabola kölcsönös helyzete, az érintő a parabola egy pontjában, az "
           "érintési feltétel és a II. rész gyorsismétlője.",
     chip=KUL + " · 13/13", szakaszok=E2,
     elozo=("tananyag-parabola.html", "A parabola"),
     kovetkezo=(FGY, "A parabola — feladatok")),
]
for u in KI:
    print("✓", os.path.basename(u))
