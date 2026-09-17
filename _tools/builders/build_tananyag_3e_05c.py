# -*- coding: utf-8 -*-
"""3e/05 — C blokk: a kor egyenlete (C1), a kor es az egyenes (C2).
Mentor: Kanrak (Ter-eb). Kuldetes: A Terkep Halozata."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra
from abra_common import svg_koordsik, svg_kupszelet, KEK, BOROSTYAN, ZOLD, PIROS, SZURKE, LILA

T = dict(tagozat="3e", mappa="05-analitikus-geometria", temakor="Síkbeli analitikus geometria")
FGY = "feladatok-kor.html"
KUL = "A Térkép Hálózata"
E2F = "../../2e/02-masodfoku-egyenletek-es-fuggvenyek/"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(k_h, k_c, n_h, n_c, tagozat="3e")


# ---------------------------------------------------------------- önteszt
from sympy import Rational, sqrt, simplify, symbols, solve, expand, Abs, discriminant, Poly
E = []
def chk(n, g, w):
    if isinstance(g, (tuple, list)):
        ok = len(g) == len(w) and all(simplify(u - v) == 0 for u, v in zip(g, w))
    else:
        ok = simplify(g - w) == 0
    if not ok:
        E.append((n, g, w))
x, y, n_ = symbols("x y n")
def kor(p, q, r2):
    return (x - p)**2 + (y - q)**2 - r2
def rajta(f, P):
    return simplify(f.subs({x: P[0], y: P[1]})) == 0

# C1
K1 = kor(2, -1, 25)
chk("P-rajta", K1.subs({x: 5, y: 3}), 0); chk("Q-belul", (1 - 2)**2 + (1 + 1)**2, 5)
chk("R-kivul", (7 - 2)**2 + (4 + 1)**2, 50)
chk("kviz1", (4, -2, sqrt(9)), (4, -2, 3))
alt = x**2 + y**2 + 4*x - 6*y - 12
chk("teljes-negyzet", expand(kor(-2, 3, 25) - alt), 0)
chk("kepletar", (Rational(-4, 2), Rational(6, 2), 4 + 9 + 12), (-2, 3, 25))
chk("kviz2-nem-kor", expand((x + 1)**2 + y**2 + 3 - (x**2 + y**2 + 2*x + 4)), 0)
for f, r2 in ((x**2 + y**2 - 4*y, 4), (2*x**2 + 2*y**2 - 8, 4), (x**2 + y**2 - 6*x + 8*y, 25)):
    assert r2 > 0
chk("kviz2-b", expand(x**2 + (y - 2)**2 - 4 - (x**2 + y**2 - 4*y)), 0)
chk("kviz2-d", expand((x - 3)**2 + (y + 4)**2 - 25 - (x**2 + y**2 - 6*x + 8*y)), 0)
A, B = (-1, 5), (5, -3)
C = (Rational(A[0] + B[0], 2), Rational(A[1] + B[1], 2)); chk("atmero-C", C, (2, 1))
chk("atmero-r", sqrt((B[0] - A[0])**2 + (B[1] - A[1])**2)/2, 5)
assert rajta(kor(2, 1, 25), A) and rajta(kor(2, 1, 25), B)
chk("kp-pont", (3 + 1)**2 + (5 - 2)**2, 25)
pp = symbols("p")
chk("x-tengely", solve(expand((1 - pp)**2 + 9 - (5 - pp)**2 - 1), pp), [2])
assert rajta(kor(2, 0, 10), (1, 3)) and rajta(kor(2, 0, 10), (5, 1))
# C2
eq = expand(x**2 + (x + 1)**2 - 25)
chk("szelo-egyenlet", eq, 2*x**2 + 2*x - 24)
chk("szelo-D", discriminant(x**2 + x - 12, x), 49)
chk("szelo-gyokok", sorted(solve(eq, x)), [-4, 3])
chk("szelo-d", Abs(1)/sqrt(2), sqrt(2)/2)
chk("hur", sqrt(7**2 + 7**2), 7*sqrt(2)); chk("hur-keplet", 2*sqrt(25 - Rational(1, 2)), 7*sqrt(2))
Kz = kor(4, 3, 25)
chk("korzet-d", Abs(4 + 3 - 2)/sqrt(2), 5/sqrt(2))
gy = sorted(solve(Kz.subs(y, 2 - x), x)); chk("korzet-x", gy, [-1, 4])
chk("korzet-hur", sqrt((4 - (-1))**2 + (-2 - 3)**2), 5*sqrt(2))
chk("korzet-hur-keplet", 2*sqrt(25 - Rational(25, 2)), 5*sqrt(2))
chk("korzet-kozel", round(float(5*sqrt(2)), 2), Rational(707, 100))
Ke = kor(1, -2, 25)
assert rajta(Ke, (4, 2))
tang = 3*x + 4*y - 20
chk("erinto", expand((4 - 1)*(x - 1) + (2 + 2)*(y + 2) - 25), tang)
assert rajta(tang, (4, 2))
chk("erinto-D", discriminant(expand(Ke.subs(y, (20 - 3*x)/4)*16), x), 0)
chk("sugar-meroleges", Rational(4, 3)*Rational(-3, 4), -1)
chk("maxi-pont", (4 - 1)**2 + (3 + 2)**2, 34)
chk("feltetel", solve(5*(1 + 4) - n_**2, n_), [-5, 5])
chk("feltetel-D", discriminant(expand(x**2 + (2*x + 5)**2 - 5), x), 0)
chk("feltetel-d", Abs(5)/sqrt(5), sqrt(5))
assert not E, E
print("sympy önteszt: OK")

# ---------------------------------------------------------------- ábrák
SVG_KOR = svg_kupszelet(
    "kor", {"p": 2, "q": -1, "r": 5}, pont=(5, 3),
    pontok=[((1, 1), "Q", {"szin": ZOLD, "dx": -10, "dy": -6}),
            ((7, 4), "R", {"szin": PIROS, "dx": 10, "dy": -6})],
    xr=(-4, 9), yr=(-7, 6), egyseg=26,
    leiras="A C(2;−1) középpontú, 5 sugarú kör; a P(5;3) a körön, a Q(1;1) belül, az R(7;4) kívül van")
SVG_ATMERO = svg_kupszelet(
    "kor", {"p": 2, "q": 1, "r": 5},
    szakaszok=[((-1, 5), (5, -3), ZOLD, {"sz": 2})],
    pontok=[((-1, 5), "A", {"dx": -10, "dy": -6}), ((5, -3), "B", {"dx": 11, "dy": 12})],
    xr=(-4, 8), yr=(-5, 7), egyseg=26,
    leiras="Az A(−1;5) és B(5;−3) átmérőjű kör, középpontja C(2;1)")
SVG_HELYZET = svg_kupszelet(
    "kor", {"p": 0, "q": 0, "r": 5},
    egyenesek=[((1, -1, 1), ZOLD, "szelő", {"hely": 0.9, "dx": -30, "dolt": False}),
               ((3, 4, -25), BOROSTYAN, "érintő", {"hely": 0.18, "dx": 26, "dy": -4, "dolt": False}),
               ((1, 1, 9), LILA, "elkerülő", {"hely": 0.25, "dx": -24, "dy": 22, "dolt": False})],
    pontok=[((3, 4), "", {"szin": BOROSTYAN}), ((-4, -3), "", {"szin": ZOLD})],
    xr=(-8, 7), yr=(-7, 7), egyseg=22, origo=False,
    leiras="Az x² + y² = 25 kör egy szelővel (két közös pont), egy érintővel (egy közös pont) és egy "
           "egyenessel, amelynek nincs közös pontja a körrel")
SVG_KORZET = svg_kupszelet(
    "kor", {"p": 4, "q": 3, "r": 5},
    egyenesek=[((1, 1, -2), KEK, "Maxi útvonala", {"hely": 0.08, "dx": 58, "dy": -2, "dolt": False})],
    szakaszok=[((4, -2), (-1, 3), PIROS, {"sz": 3.2})],
    merolegesek=[((4, 3), (1, 1, -2), SZURKE, "d")],
    pontok=[((4, -2), "M₁", {"dx": 16, "dy": 12, "szin": PIROS}),
            ((-1, 3), "M₂", {"dx": -16, "dy": -6, "szin": PIROS})],
    xr=(-3, 11), yr=(-4, 10), egyseg=24, szin=ZOLD,
    leiras="Tér-eb (4;3) középpontú, 5 sugarú körzete és Maxi x + y − 2 = 0 útvonala; a körzeten belüli "
           "szakasz a húr, a középpont távolsága az egyenestől d")
SVG_ERINTO = svg_kupszelet(
    "kor", {"p": 1, "q": -2, "r": 5}, pont=(4, 2),
    egyenesek=[((3, 4, -20), BOROSTYAN, "", {})],
    feliratok=[((7.4, 1.5), "3x + 4y − 20 = 0", {"szin": BOROSTYAN, "meret": 13})],
    szogivek=[((4, 2), (1, -2), (8, -1), SZURKE, "")],
    xr=(-5, 10), yr=(-8, 6), egyseg=24,
    leiras="Az (x − 1)² + (y + 2)² = 25 kör érintője a T(4;2) pontban merőleges a CT sugárra")

# ---------------------------------------------------------------- C1
C1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Kanrak:</b> Az egyenes pályákat lezártuk, ezért Maxi kapukat nyitott. Minden '
         'teleport-kapu egy <b>kör</b>: a peremének bármelyik pontja pontosan ugyanolyan messze van a '
         'kapu magjától. Tér-eb csak a peremen tud belépni — ehhez a perem <b>egyenlete</b> kell, nem '
         'a rajza.'),
   r'<p>Ezzel kezdődik a témakör második része: a <b>másodrendű görbék</b>. Mind a négy — a kör, '
   r'az ellipszis, a hiperbola és a parabola — egy-egy kétismeretlenes <b>másodfokú</b> egyenlettel '
   r'írható le, ezért hívjuk őket másodrendű görbéknek.</p>',
 ]),

 ("Kúpszeletek és mértani helyek", [
   doboz("erdekesseg", "Honnan a név?",
         r'<p>Ha egy kettős kúpfelületet (két, csúcsával összeillesztett tölcsért) a csúcsán át nem '
         r'haladó síkkal elmetszünk, a metszet a sík állásától függően négyféle lehet:</p>'
         r'<ul><li>a sík merőleges a kúp tengelyére → <b>kör</b>;</li>'
         r'<li>a sík ferde, és a kúp minden alkotóját metszi → <b>ellipszis</b>;</li>'
         r'<li>a sík párhuzamos a kúp egyik alkotójával → <b>parabola</b>;</li>'
         r'<li>a sík mindkét kúpfelet metszi → <b>hiperbola</b> (két ága van).</li></ul>'
         r'<p>Ezért hívjuk őket <b>kúpszeleteknek</b>. Ha egy zseblámpát a falra irányítasz és '
         r'döntögetsz, a fénykör széle felveszi a kör, az ellipszis, a parabola és a hiperbola egyik ágának alakját.</p>'),
   doboz("definicio", "Mértani hely",
         r'<p>A sík azon pontjainak halmazát, amelyek egy adott tulajdonsággal rendelkeznek, a '
         r'tulajdonsághoz tartozó <b>mértani helynek</b> nevezzük. A mondat mindig így épül: '
         r'„a sík mindazon pontjainak halmaza, amelyekre …”.</p>'
         r'<p>Ilyen például a szakasz <a href="tananyag-ket-egyenes.html#pelda-felezomeroleges">'
         r'felezőmerőlegese</a>: a sík mindazon pontjainak halmaza, amelyek a szakasz két '
         r'végpontjától egyenlő távolságra vannak. A kúpszeleteket is így definiáljuk — és a '
         r'definícióból, a távolságképlet segítségével, egyenlet lesz.</p>',
         hid="def-mertani-hely"),
 ]),

 ("A kör egyenlete", [
   doboz("definicio", "A kör",
         r'<p>A <b>kör</b> a sík mindazon pontjainak halmaza, amelyek egy adott $C$ ponttól (a '
         r'<b>középponttól</b>) adott $r\gt0$ távolságra (a <b>sugárnyira</b>) vannak.</p>',
         hid="def-kor"),
   r'<p>Legyen $C(p;q)$ és $P(x;y)$. A $P$ pontosan akkor van a körön, ha $|PC|=r$, a '
   r'<a href="tananyag-pontok-a-sikban.html#tetel-tavolsag">távolságképlettel</a>: '
   r'$\sqrt{(x-p)^2+(y-q)^2}=r$. Mindkét oldal nemnegatív, ezért négyzetre emelhetünk.</p>',
   doboz("tetel", "A kör középponti egyenlete",
         r'<p>A $C(p;q)$ középpontú, $r$ sugarú kör egyenlete</p>'
         r'$$(x-p)^2+(y-q)^2=r^2 .$$'
         r'<p>Az origó középpontú kör egyenlete $x^2+y^2=r^2$.</p>'
         r'<p>A $P_0(x_0;y_0)$ pont a körön van, ha $(x_0-p)^2+(y_0-q)^2=r^2$; a körön <b>belül</b> '
         r'van, ha a bal oldal $r^2$-nél kisebb, és <b>kívül</b>, ha nagyobb.</p>',
         hid="tetel-kor-egyenlete"),
   r'<p><b>Példa.</b> A $C(2;-1)$ középpontú, $5$ sugarú kör egyenlete $(x-2)^2+(y+1)^2=25$. '
   r'A $P(5;3)$ rajta van: $3^2+4^2=25$. A $Q(1;1)$ belül van: $1+4=5\lt25$. Az $R(7;4)$ kívül van: '
   r'$25+25=50\gt25$.</p>',
   abra(SVG_KOR, 'A kör, a $CP$ sugár, a belső $Q$ és a külső $R$ pont.'),
   doboz("csapda", "Maxi trükkje",
         r'<p>Maxi leolvasta az $(x+3)^2+(y-1)^2=16$ kapu adatait: „középpont $C(3;-1)$, sugár $16$”. '
         r'Tér-eb a rossz síknegyedbe ugrott, és egy négyszer akkora sugarú kört keresett.</p>'
         r'<p>Az egyenlet <b>kivonást</b> ír elő: $x+3=x-(-3)$ és $y-1=y-(+1)$, tehát a középpont '
         r'$C(-3;1)$ — a zárójelben álló számok <b>ellentettje</b>. A jobb oldalon pedig $r^2$ áll: '
         r'$r=\sqrt{16}=4$.</p>'),
   kviz(r'Mi a középpontja és a sugara az $(x-4)^2+(y+2)^2=9$ körnek?',
        [r'$C(4;-2)$, $r=3$', r'$C(-4;2)$, $r=3$', r'$C(4;-2)$, $r=9$', r'$C(-4;2)$, $r=9$'], 0,
        jo="✔ x − 4 → p = 4, y + 2 = y − (−2) → q = −2, és r = √9 = 3.",
        nem="✘ A középpont koordinátái a zárójelben kivont számok: x − 4 → 4, y + 2 = y − (−2) → −2. "
            "A jobb oldal a sugár négyzete: r = √9 = 3."),
 ]),

 ("Az általános alak", [
   r'<p>Ha a középponti egyenletben kibontjuk a zárójeleket, $x^2+y^2-2px-2qy+p^2+q^2-r^2=0$ '
   r'adódik. A képlettár ezt így írja:</p>',
   doboz("tetel", "A kör általános egyenlete",
         r'$$x^2+y^2+dx+ey+f=0,$$'
         r'<p>ahol $p=-\frac d2$, $q=-\frac e2$ és $r^2=p^2+q^2-f$.</p>'
         r'<p>Egy ilyen alakú egyenlet <b>pontosan akkor</b> kör, ha $p^2+q^2-f\gt0$. (Ha $0$, '
         r'egyetlen pontot ír le, ha negatív, egyetlen pontot sem.) Ha az $x^2$ és az $y^2$ '
         r'együtthatója egyenlő, de nem $1$, előbb azzal osztunk; ha különböző, vagy van $xy$-os tag, '
         r'az egyenlet nem kör.</p>'
         r'<p><i>A tanulói képlettárban itt elírás van: „$q=-\frac p2$” áll, helyesen $q=-\frac e2$.</i></p>',
         hid="tetel-altalanos-alak"),
   r'<p>A képlet helyett biztosabb a <b>teljes négyzetté kiegészítés</b>, amelyet a '
   r'<a href="' + E2F + r'tananyag-masodfoku-fuggveny.html#tetel-kanonikus">másodfokú függvény '
   r'kanonikus alakjánál</a> tanultunk: az $x$-es és az $y$-os tagokat külön csoportosítjuk.</p>',
   doboz("pelda", "Általános alakból középpont és sugár",
         r'<p>Határozd meg az $x^2+y^2+4x-6y-12=0$ kör középpontját és sugarát!</p>',
         hid="pelda-teljes-negyzet",
         lenyilo=("Megoldás",
                  r'<p>Csoportosítunk: $(x^2+4x)+(y^2-6y)=12$.</p>'
                  r'<p>Kiegészítjük: $x^2+4x=(x+2)^2-4$ és $y^2-6y=(y-3)^2-9$.</p>'
                  r'<p>Így $(x+2)^2-4+(y-3)^2-9=12$, azaz $(x+2)^2+(y-3)^2=25$.</p>'
                  r'<p><i>Ellenőrzés képlettel: $p=-\frac42=-2$, $q=-\frac{-6}{2}=3$, '
                  r'$r^2=4+9-(-12)=25$ ✔.</i></p>'
                  r'<p class="vegeredmeny">$C(-2;3)$, $r=5$</p>')),
   kviz(r'Melyik egyenlet <b>nem</b> kör egyenlete?',
        [r'$x^2+y^2+2x+4=0$', r'$x^2+y^2-4y=0$', r'$2x^2+2y^2-8=0$', r'$x^2+y^2-6x+8y=0$'], 0,
        jo="✔ (x + 1)² + y² = −3 — a jobb oldal negatív, egyetlen pont sem elégíti ki.",
        nem="✘ Mindegyik alak ugyanúgy néz ki, a döntést az r² adja. Az x² + y² + 2x + 4 = 0 "
            "teljes négyzettel (x + 1)² + y² = −3, és négyzetek összege nem lehet negatív. A másik "
            "három valóban kör."),
 ]),

 ("Kör adott feltételekből", [
   r'<p>A kör egyenletéhez két adat kell: a <b>középpont</b> és a <b>sugár</b>. A feladatok '
   r'ezeket csak ritkán adják meg közvetlenül.</p>'
   r'<ul><li><b>Középpont és egy pont a körön:</b> a sugár a kettő távolsága. $C(-1;2)$ és $P(3;5)$: '
   r'$r^2=4^2+3^2=25$, a kör $(x+1)^2+(y-2)^2=25$.</li>'
   r'<li><b>Az átmérő két végpontja:</b> a középpont a felezőpont, a sugár az átmérő fele.</li>'
   r'<li><b>A középpont egy adott egyenesen van, és két pont a körön:</b> a középpont mindkét '
   r'ponttól egyenlő távolságra van, tehát a két pont szakaszának felezőmerőlegesén fekszik — '
   r'az adott egyenes és a felezőmerőleges metszéspontja. Ha például a középpont az $x$-tengelyen van, $C(p;0)$, és '
   r'a kör átmegy az $A(1;3)$ és a $B(5;1)$ ponton, akkor $(1-p)^2+9=(5-p)^2+1$, ahonnan $p=2$, '
   r'$r^2=10$, a kör $(x-2)^2+y^2=10$.</li></ul>',
   doboz("pelda", "Kristály-kamra szimuláció — a kapu két átellenes pontjából",
         r'<p>A műszerek egy kapu peremén két <b>átellenes</b> pontot mértek be: $A(-1;5)$ és '
         r'$B(5;-3)$. Írd fel a kapu egyenletét középponti és általános alakban!</p>',
         hid="pelda-kapu",
         lenyilo=("Megoldás",
                  r'<p>Az $AB$ átmérő, ezért a középpont a felezőpontja: '
                  r'$C\left(\frac{-1+5}{2};\frac{5-3}{2}\right)=C(2;1)$.</p>'
                  r'<p>Az átmérő hossza $|AB|=\sqrt{6^2+(-8)^2}=10$, tehát $r=5$.</p>'
                  r'<p>Középponti alak: $(x-2)^2+(y-1)^2=25$. Kibontva: '
                  r'$x^2-4x+4+y^2-2y+1=25$, azaz $x^2+y^2-4x-2y-20=0$.</p>'
                  r'<p><i>Ellenőrzés az $A$ ponttal: $(-3)^2+4^2=25$ ✔.</i></p>'
                  + abra(SVG_ATMERO, 'A kapu az $AB$ átmérővel.') +
                  r'<p class="vegeredmeny">$(x-2)^2+(y-1)^2=25$ · $x^2+y^2-4x-2y-20=0$</p>')),
   GY(FGY + "#alap-1", "A 1–8", FGY + "#kozep-1", "K 1–4"),
   brief('<b>Kanrak:</b> A kapu egyenlete megvan. Maxi drónja azonban egy egyenes pályán közelít '
         'felé. <b>Átmetszi</b> a kaput, csak <b>súrolja</b>, vagy <b>elkerüli</b>? Ha csak súrolja, '
         'egyetlen közös pont marad — és Tér-eb pontosan oda fog ugrani.', outro=True),
 ]),
]

# ---------------------------------------------------------------- C2
C2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Kanrak:</b> Maxi pályája és a teleport-kapu: ha a pálya átmetszi a kaput, két helyen '
         'nyílik rés a peremen. Ha csak <b>érinti</b>, egyetlen pont marad — ez a <b>csapásmérési '
         'pont</b>, ahol Tér-eb a kapu szélére ugorhat. Ma két módszert tanulunk arra, hogy '
         'eldöntsük, melyik eset áll fenn.'),
 ]),

 ("Kölcsönös helyzet — két módszer", [
   doboz("tetel", "Egyenes és kör kölcsönös helyzete",
         r'<p><b>1. módszer — behelyettesítés.</b> Az egyenes egyenletéből kifejezzük az egyik '
         r'ismeretlent, és behelyettesítjük a kör egyenletébe. Másodfokú egyenletet kapunk, és a '
         r'<a href="' + E2F + r'tananyag-masodfoku-egyenlet.html#tetel-megoldokeplet">diszkriminánsa</a> '
         r'dönt:</p>'
         r'<ul><li>$D\gt0$: két közös pont — az egyenes <b>szelő</b>;</li>'
         r'<li>$D=0$: egy közös pont — az egyenes <b>érintő</b>;</li>'
         r'<li>$D\lt0$: nincs közös pont — az egyenes <b>elkerüli</b> a kört.</li></ul>'
         r'<p><i>Itt a $D$ a másodfokú egyenlet diszkriminánsa, nem a háromszög területénél használt '
         r'determináns.</i></p>'
         r'<p><b>2. módszer — távolság.</b> Kiszámítjuk a középpont $d$ '
         r'<a href="tananyag-pont-es-egyenes-tavolsaga.html#tetel-tavolsagkeplet">távolságát</a> az '
         r'egyenestől: $d\lt r$ szelő, $d=r$ érintő, $d\gt r$ nincs közös pont.</p>',
         hid="tetel-kolcsonos-helyzet-kor"),
   abra(SVG_HELYZET, 'A három helyzet ugyanazon a körön.'),
   r'<p>Az 1. módszer ugyanaz a recept, mint a '
   r'<a href="' + E2F + r'tananyag-masodfoku-linearis-rendszer.html#tetel-rendszer-esetek">lineáris '
   r'és másodfokú egyenletből álló rendszernél</a>, és a metszéspontokat is megadja. A 2. módszer '
   r'gyorsabb, ha csak a helyzet a kérdés — de <b>csak körnél</b> működik.</p>'
   r'<p><b>Példa.</b> $x^2+y^2=25$ és $y=x+1$. Behelyettesítve $x^2+(x+1)^2=25$, rendezve '
   r'$2x^2+2x-24=0$, azaz $x^2+x-12=0$. $D=1+48=49\gt0$, tehát szelő. Távolsággal: az egyenes '
   r'$x-y+1=0$, $d=\frac{|0-0+1|}{\sqrt2}\approx0{,}71\lt5$ ✔.</p>'
   r'<p><b>A „recept” a többi görbére.</b> Ugyanez a behelyettesítéses módszer működik majd az '
   r'ellipszisnél, a hiperbolánál és a parabolánál is.</p>',
   kviz(r'Egy egyenes és egy kör egyenletéből a behelyettesítés után olyan másodfokú egyenletet '
        r'kaptunk, amelynek diszkriminánsa $D=0$. Mit jelent ez?',
        ['az egyenes érinti a kört', 'az egyenesnek nincs közös pontja a körrel',
         'az egyenes két pontban metszi a kört', 'az egyenes átmegy a kör középpontján'], 0,
        jo="✔ D = 0: a másodfokú egyenletnek egy megoldása van — egy közös pont, érintés.",
        nem="✘ D = 0 esetén a másodfokú egyenletnek pontosan egy (kétszeres) megoldása van: egy "
            "közös pont, az egyenes érinti a kört."),
   kviz(r'Egy kör sugara $r=5$, a középpontja az $e$ egyenestől $d=3$ távolságra van. Milyen az '
        r'egyenes helyzete?',
        ['szelő', 'érintő', 'nincs közös pontjuk', 'nem dönthető el'], 0,
        jo="✔ d = 3 < 5 = r, tehát az egyenes a kör belsejébe is belép: két közös pont.",
        nem="✘ Ha a középpont közelebb van az egyeneshez, mint a sugár (3 < 5), az egyenes "
            "átmegy a kör belsején: szelő."),
 ]),

 ("Metszéspontok és húrhossz", [
   r'<p>Szelő esetén a két metszéspont közötti szakasz a <b>húr</b>. Hossza a két pont '
   r'távolsága, vagy — ha csak a hossz kell — a középpont távolságából, Pitagorasz-tétellel:</p>'
   r'$$h=2\sqrt{r^2-d^2}.$$'
   r'<p>Az előző példában a metszéspontok $x=3$ és $x=-4$ mellett $(3;4)$ és $(-4;-3)$, a húr '
   r'$\sqrt{7^2+7^2}=7\sqrt2\approx9{,}90$. Képlettel: $2\sqrt{25-\frac12}=2\sqrt{\frac{49}{2}}=7\sqrt2$ ✔.</p>',
   doboz("pelda", "Kristály-kamra szimuláció — Maxi átvág a körzeten",
         r'<p>Tér-eb teleport-körzete a $(4;3)$ középpontú, $5$ km sugarú körlap. Maxi drónja az '
         r'$x+y-2=0$ egyenes mentén repül (a koordináta-rendszer egysége $1$ km).</p>'
         r'<ol type="a"><li>Áthalad-e a drón a körzeten?</li>'
         r'<li>Hol lép be és hol lép ki?</li>'
         r'<li>Milyen hosszú az az útszakasz, amelyen Tér-eb körzetében repül? (Két tizedesre kerekíts!)</li></ol>',
         hid="pelda-korzet",
         lenyilo=("Megoldás",
                  r'<p><b>a)</b> $d=\frac{|4+3-2|}{\sqrt{1+1}}=\frac5{\sqrt2}\approx3{,}54\lt5$, tehát '
                  r'igen, átvág a körzeten.</p>'
                  r'<p><b>b)</b> $y=2-x$-et behelyettesítjük: $(x-4)^2+(-1-x)^2=25$, '
                  r'$2x^2-6x-8=0$, azaz $x^2-3x-4=0$, ahonnan $x=4$ vagy $x=-1$. A pontok '
                  r'$M_1(4;-2)$ és $M_2(-1;3)$.</p>'
                  r'<p><b>c)</b> $|M_1M_2|=\sqrt{5^2+5^2}=5\sqrt2\approx7{,}07$ km. Képlettel: '
                  r'$2\sqrt{25-\frac{25}{2}}=5\sqrt2$ ✔.</p>'
                  + abra(SVG_KORZET, 'A körzet, Maxi útvonala és a körzeten belüli szakasz (piros).') +
                  r'<p class="vegeredmeny">a) igen, $d\approx3{,}54\lt5$ · b) $(4;-2)$ és $(-1;3)$ · '
                  r'c) $5\sqrt2\approx7{,}07$ km</p>')),
 ]),

 ("Az érintő a kör egy pontjában", [
   doboz("tetel", "A kör érintője a kör egy pontjában",
         r'<p>A $(x-p)^2+(y-q)^2=r^2$ kör $T(x_1;y_1)$ pontjában húzott érintő egyenlete</p>'
         r'$$(x_1-p)(x-p)+(y_1-q)(y-q)=r^2 .$$'
         r'<p>Origó középpontú körnél: $x_1x+y_1y=r^2$. A képlet csak akkor ad érintőt, ha a $T$ '
         r'pont <b>valóban a körön van</b> — ezt mindig ellenőrizd először.</p>'
         r'<p>Az érintő <b>merőleges</b> az érintési ponthoz húzott sugárra.</p>',
         hid="tetel-erinto-kor"),
   doboz("pelda", "Érintő a kör adott pontjában",
         r'<p>Írd fel az $(x-1)^2+(y+2)^2=25$ kör $T(4;2)$ pontjában húzott érintőjének egyenletét!</p>',
         hid="pelda-erinto-kor",
         lenyilo=("Megoldás",
                  r'<p><b>Ellenőrzés:</b> $(4-1)^2+(2+2)^2=9+16=25$ ✔, a $T$ a körön van.</p>'
                  r'<p><b>Képlet:</b> $(4-1)(x-1)+(2+2)(y+2)=25$, azaz $3x-3+4y+8=25$, '
                  r'rendezve $3x+4y-20=0$.</p>'
                  r'<p><b>Ellenőrzés merőlegességgel:</b> a $CT$ sugár iránytényezője '
                  r'$\frac{2-(-2)}{4-1}=\frac43$, az érintőé $-\frac34$, szorzatuk $-1$ ✔.</p>'
                  + abra(SVG_ERINTO, 'Az érintő a $T$ pontban derékszöget zár be a $CT$ sugárral.') +
                  r'<p class="vegeredmeny">$3x+4y-20=0$</p>')),
   doboz("csapda", "Maxi trükkje",
         r'<p>Maxi a $P(4;3)$ pontot helyettesítette be ugyanennek a körnek az érintőképletébe, és a '
         r'kapott $3(x-1)+5(y+2)=25$ egyenest érintőnek hitte. Tér-eb a kapu belsejébe zuhant.</p>'
         r'<p>A $P(4;3)$ <b>nincs a körön</b>: $(4-1)^2+(3+2)^2=34\ne25$. Az érintőképlet csak a kör '
         r'saját pontjára érvényes; más pontra beírva egy teljesen más egyenest ad.</p>'
         r'<p>A másik gyakori hiba a behelyettesítésnél: $(kx+n)^2$ nem $k^2x^2+n^2$, hanem '
         r'$k^2x^2+2knx+n^2$ — a kétszeres szorzat nem maradhat el.</p>'),
   doboz("erdekesseg", "Hol találkozol vele?",
         r'<p>A kalapácsvető körpályán forgatja a kalapácsot. Abban a pillanatban, amikor elengedi, '
         r'a kalapács az <b>érintő</b> irányában repül tovább — ezért a dobás iránya attól függ, a kör '
         r'melyik pontjában engedi el.</p>'),
 ]),

 ("Az érintési feltétel", [
   r'<p>Eddig a kör egy adott pontjában húztunk érintőt. Mi van, ha az érintő <b>iránya</b> adott — például '
   r'párhuzamos egy egyenessel —, és azt keressük, <b>melyik</b> ilyen egyenes érinti a kört? '
   r'Az $y=kx+n$ egyenes pontosan akkor érintő, ha a középpont távolsága tőle $r$. A '
   r'$kx-y+n=0$ alakra felírva:</p>'
   r'$$\frac{|kp-q+n|}{\sqrt{k^2+1}}=r .$$',
   doboz("tetel", "A kör érintési feltétele",
         r'<p>Az $y=kx+n$ egyenes pontosan akkor érinti a $(x-p)^2+(y-q)^2=r^2$ kört, ha</p>'
         r'$$r^2\,(1+k^2)=(kp-q+n)^2 .$$'
         r'<p>Origó középpontú körnél: $r^2(1+k^2)=n^2$. <i>Ugyanez jön ki a behelyettesítéses '
         r'módszer $D=0$ feltételéből is.</i></p>'
         r'<p>A függőleges érintőket ($x=p+r$ és $x=p-r$) a feltétel nem mutatja, mert nem írhatók '
         r'$y=kx+n$ alakban.</p>'
         r'<p>🔴 <b>Kristály-protokoll:</b> az érintési feltétellel dolgozó feladatok a '
         r'gyűjtemény <b>nehéz</b> sávjában vannak.</p>',
         hid="tetel-erintesi-feltetel-kor"),
   r'<p><b>Példa.</b> Melyik $y=2x+n$ egyenes érinti az $x^2+y^2=5$ kört? A feltétel: '
   r'$5\cdot(1+4)=n^2$, azaz $n^2=25$, $n=\pm5$. Két ilyen érintő van: $y=2x+5$ és $y=2x-5$ — a '
   r'kör két oldalán. <i>Ellenőrzés: $d=\frac{|5|}{\sqrt5}=\sqrt5=r$ ✔.</i></p>',
   GY(FGY + "#alap-9", "A 9–14", FGY + "#kozep-5", "K 5–10"),
   brief('<b>Kanrak:</b> A kör a legszabályosabb kapu: minden irányban ugyanakkora. Maxi '
         'torzító mezői viszont <b>megnyúltak</b> — és nem egy, hanem <b>két magjuk</b> van. '
         'A kör egyenlete itt már nem segít.', outro=True),
 ]),
]

# ---------------------------------------------------------------- lapok
KI = [
 lap(**T, fajl="tananyag-kor-egyenlete.html",
     cim="A kör egyenlete",
     alcim="Kúpszeletek és mértani helyek, a kör középponti és általános egyenlete, a kör felírása "
           "adott feltételekből.",
     chip=KUL + " · 6/13", szakaszok=C1,
     elozo=("feladatok-egyenesek.html", "Egyenesek — feladatok"),
     kovetkezo=("tananyag-kor-es-egyenes.html", "A kör és az egyenes")),
 lap(**T, fajl="tananyag-kor-es-egyenes.html",
     cim="A kör és az egyenes — metszéspont és érintő",
     cim_tiszta="A kör és az egyenes",
     alcim="Az egyenes és a kör kölcsönös helyzete két módszerrel, a húr hossza, az érintő a kör "
           "egy pontjában és az érintési feltétel.",
     chip=KUL + " · 7/13", szakaszok=C2,
     elozo=("tananyag-kor-egyenlete.html", "A kör egyenlete"),
     kovetkezo=(FGY, "A kör — feladatok")),
]
for u in KI:
    print("✓", os.path.basename(u))
