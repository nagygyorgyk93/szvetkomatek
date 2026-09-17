# -*- coding: utf-8 -*-
"""3e/05 — B blokk: az egyenes egyenlete (B1), ket egyenes (B2), pont es egyenes tavolsaga (B3).
Mentor: Kanrak (Ter-eb). Kuldetes: A Terkep Halozata."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra
from abra_common import svg_koordsik, KEK, BOROSTYAN, ZOLD, PIROS, SZURKE, LILA

T = dict(tagozat="3e", mappa="05-analitikus-geometria", temakor="Síkbeli analitikus geometria")
FGY = "feladatok-egyenesek.html"
KUL = "A Térkép Hálózata"
V04 = "../04-vektorok/"
V03 = "../03-linearis-rendszerek/"
E1 = "../../1e/07-linearis-egyenletek-es-rendszerek/tananyag-linearis-fuggveny.html"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(k_h, k_c, n_h, n_c, tagozat="3e")


# ---------------------------------------------------------------- önteszt
from sympy import (Rational, sqrt, simplify, symbols, solve, atan, deg, N, Abs, Matrix, expand,
                   Eq)
E = []
def chk(n, g, w, tur=None):
    if tur is not None:
        ok = abs(float(N(g)) - float(w)) <= tur
    elif isinstance(g, (tuple, list)):
        ok = len(g) == len(w) and all(simplify(u - v) == 0 for u, v in zip(g, w))
    else:
        ok = simplify(g - w) == 0
    if not ok:
        E.append((n, g, w))
x, y = symbols("x y")

def rajta(egy, P):          # egy = a*x + b*y + c kifejezés
    return simplify(egy.subs({x: P[0], y: P[1]})) == 0

def d(P, a, b, c):
    return Abs(a*P[0] + b*P[1] + c)/sqrt(a*a + b*b)

def tgphi(k1, k2):
    return Abs((k2 - k1)/(1 + k1*k2))

# B1
chk("k-AB", Rational(8 - 2, 4 - 1), 2)
chk("alfa-2", deg(atan(2)), 63.43, tur=0.005)
chk("alfa-10szazalek", deg(atan(Rational(1, 10))), 5.7, tur=0.02)
chk("illeszk-P", Rational(-1, 2)*4 + 3, 1); assert Rational(-1, 2)*2 + 3 != 3
e1 = 2*x - 3*y + 6
chk("atvaltas-explicit", solve(e1, y)[0], Rational(2, 3)*x + 2)
chk("maxi-k", Rational(-2, -3), Rational(2, 3))
chk("kviz-k", Rational(-3, 6), Rational(-1, 2))
chk("tengelymetszet-m", solve(e1.subs(y, 0), x)[0], -3); chk("tengelymetszet-n", solve(e1.subs(x, 0), y)[0], 2)
chk("normalvektor", 2*3 + (-3)*2, 0)
chk("pont-k", expand(-1 + 3*(x - 2)), 3*x - 7)
kk = Rational(-4 - 4, 3 - (-1)); chk("ket-pont-k", kk, -2)
e2 = 2*x + y - 2
assert rajta(e2, (-1, 4)) and rajta(e2, (3, -4)) and rajta(e2, (5, -8)) and rajta(e2, (1, 0)) and rajta(e2, (0, 2))
# B2
M = solve([y - (2*x - 3), x + y - 6], [x, y]); chk("metszespont", (M[x], M[y]), (3, 3))
assert simplify((4*x - 2*y + 6) - 2*(-(y - (2*x + 3)))) == 0          # egybeeső
chk("kviz-meroleges", -1/Rational(4), Rational(-1, 4))
p_par = 3*x - 4*y + 18; p_mer = 4*x + 3*y - 1
assert rajta(p_par, (-2, 3)) and rajta(p_mer, (-2, 3))
chk("par-k", Rational(-3, -4), Rational(3, 4)); chk("mer-k", Rational(-4, 3)*Rational(3, 4), -1)
F = (Rational(-2 + 4, 2), Rational(1 + 5, 2)); chk("felezo", F, (1, 3))
fm = 3*x + 2*y - 9
assert rajta(fm, F)
chk("felezo-k", Rational(-3, 2)*Rational(5 - 1, 4 + 2), -1)
chk("fm-egyenlo-tav", (x - (-2))**2 + (y - 1)**2 - ((x - 4)**2 + (y - 5)**2) - 4*fm, 0)
chk("szog-45", tgphi(2, -3), 1)
chk("szog-kalk", deg(atan(tgphi(3, Rational(-1, 2)))), 81.9, tur=0.05)
chk("szog-fugg", 90 - deg(atan(2)), 26.6, tur=0.05)
chk("normal-cos", Abs(2*3 + (-1)*1)/(sqrt(5)*sqrt(10)), 1/sqrt(2))
Mm = solve([y - 2*x, y - (-x/2 + 5)], [x, y]); chk("meroleges-abra", (Mm[x], Mm[y]), (2, 4))
Ms = solve([y - (2*x + 1), y - (-3*x + 4)], [x, y]); chk("szog-abra", (Ms[x], Ms[y]), (Rational(3, 5), Rational(11, 5)))
# B3
chk("riasztas", d((2, 3), 4, 3, -27), 2)
chk("maxi-jo", d((1, 4), 3, -4, 8), 1)
chk("maxi-rossz", Abs(Rational(3, 4)*1 + 4 + 2)/sqrt(Rational(9, 16) + 1), Rational(27, 5))
chk("kviz-tav", d((1, 1), 2, -1, 1), 2/sqrt(5))
chk("kviz-tav-rossz", Abs(2 + 1 + 1)/sqrt(5), 4/sqrt(5))
assert rajta(3*x + 4*y - 7, (1, 1))
chk("parhuzamos-tav", d((1, 1), 3, 4, 8), 3)
A, B, C = (-2, -1), (6, 3), (1, 5)
AB = x - 2*y
assert rajta(AB, A) and rajta(AB, B)
hc = 2*x + y - 7
assert rajta(hc, C); chk("hc-meroleges", Rational(1, 2)*(-2), -1)
chk("hc-hossz", d(C, 1, -2, 0), 9/sqrt(5)); chk("hc-kozel", 9/sqrt(5), 4.02, tur=0.005)
chk("AB-hossz", sqrt(8**2 + 4**2), 4*sqrt(5))
chk("T-magassag", Rational(1, 2)*4*sqrt(5)*9/sqrt(5), 18)
chk("T-D", Rational(1, 2)*Abs(Matrix([[A[0], A[1], 1], [B[0], B[1], 1], [C[0], C[1], 1]]).det()), 18)
Tp = solve([AB, hc], [x, y]); chk("talppont", (Tp[x], Tp[y]), (Rational(14, 5), Rational(7, 5)))
Fab = (Rational(A[0] + B[0], 2), Rational(A[1] + B[1], 2)); chk("F-AB", Fab, (2, 1))
sc = 4*x + y - 9
assert rajta(sc, C) and rajta(sc, Fab)
assert not E, E
print("sympy önteszt: OK")

# ---------------------------------------------------------------- ábrák
SVG_IRANY = svg_koordsik(
    xr=(-4, 5), yr=(-3, 5),
    egyenesek=[((2, -1, 1), KEK, "", {}),
               ((1, 1, -3), PIROS, "k = −1", {"hely": 0.12, "dx": 10, "dolt": False}),
               ((0, 1, 2), ZOLD, "k = 0", {"hely": 0.88, "dolt": False}),
               ((1, 0, -3), LILA, "nincs k", {"hely": 0.62, "dx": 30, "dolt": False})],
    szogivek=[((-0.5, 0), (2, 0), (1, 3), KEK, "α")],
    feliratok=[((1.0, 4.3), "k = 2", {"szin": KEK, "meret": 13})],
    leiras="Négy egyenes: emelkedő (k = 2), csökkenő (k = −1), vízszintes (k = 0) és függőleges, "
           "amelynek nincs iránytényezője; a kék egyenes α hajlásszöge")
SVG_TENGELY = svg_koordsik(
    xr=(-5, 4), yr=(-2, 5),
    egyenesek=[((2, -3, 6), KEK, "", {})],
    feliratok=[((1.9, 4.3), "2x − 3y + 6 = 0", {"szin": KEK, "meret": 13})],
    pontok=[((-3, 0), "m = −3", {"dx": -26, "dy": -12, "szin": PIROS, "dolt": False}),
            ((0, 2), "n = 2", {"dx": -26, "dy": -2, "szin": PIROS, "dolt": False})],
    leiras="A 2x − 3y + 6 = 0 egyenes a tengelyeket a (−3;0) és a (0;2) pontban metszi")
SVG_KET_PONT = svg_koordsik(
    xr=(-3, 6), yr=(-9, 5), egyseg=24,
    egyenesek=[((2, 1, -2), KEK, "", {})],
    pontok=[((-1, 4), "A", {"dx": 11, "dy": -4}), ((3, -4), "B", {"dx": 11, "dy": -2}),
            ((5, -8), "K", {"szin": PIROS, "dx": -12, "dy": 0})],
    leiras="A két észlelési ponton, A(−1;4)-en és B(3;−4)-en átmenő pálya átmegy a K(5;−8) bázison is")
SVG_MEROLEGES = svg_koordsik(
    xr=(-2, 6), yr=(-1, 7),
    egyenesek=[((2, -1, 0), KEK, "y = 2x", {"hely": 0.9, "dx": 30, "dolt": False}),
               ((1, 2, -10), PIROS, "y = −½x + 5", {"hely": 0.86, "dx": -10, "dy": 26, "dolt": False})],
    szogivek=[((2, 4), (3, 6), (4, 3), SZURKE, "")],
    pontok=[((2, 4), "M", {"dx": -12, "dy": -6})],
    leiras="Két merőleges egyenes, iránytényezőik 2 és −½, derékszög-jellel az M(2;4) metszéspontban")
SVG_SZOG = svg_koordsik(
    xr=(-3, 4), yr=(-2, 6), egyseg=36,
    egyenesek=[((2, -1, 1), KEK, "", {}), ((3, 1, -4), PIROS, "", {})],
    szogivek=[((0.6, 2.2), (2.1, 5.2), (1.6, 4.2 - 3.0 - 0.0), LILA, "")],
    pontok=[((0.6, 2.2), "", {"szin": LILA})],
    feliratok=[((1.95, 2.2), "φ = 45°", {"szin": LILA, "meret": 14}),
               ((3.0, 5.2), "y = 2x + 1", {"szin": KEK, "meret": 13}),
               ((-1.9, 5.2), "y = −3x + 4", {"szin": PIROS, "meret": 13})],
    leiras="Az y = 2x + 1 és az y = −3x + 4 egyenes 45 fokos szöget zár be")
SVG_TAVOLSAG = svg_koordsik(
    xr=(-1, 8), yr=(-1, 8), egyseg=30,
    egyenesek=[((4, 3, -27), KEK, "pálya", {"hely": 0.8, "dx": 22, "dolt": False})],
    merolegesek=[((2, 3), (4, 3, -27), PIROS, "d")],
    pontok=[((2, 3), "K", {"dx": -12, "dy": -4})],
    leiras="A K(2;3) bázis és a 4x + 3y − 27 = 0 pálya távolsága a merőleges talppontig mért d szakasz")
A_, B_, C_ = (-2, -1), (6, 3), (1, 5)
SVG_HAROMSZOG = svg_koordsik(
    xr=(-3, 7), yr=(-2, 6), egyseg=34,
    sokszogek=[([A_, B_, C_], KEK, {"kitolt": 0.10})],
    szakaszok=[((1, 5), (2.8, 1.4), PIROS, {"sz": 2, "felirat": "m", "dx": 10, "dy": -2}),
               ((1, 5), (2, 1), ZOLD, {"sz": 2, "szaggat": "6 4", "felirat": "s", "dx": -10, "dy": 8})],
    pontok=[(A_, "A", {"dx": -10, "dy": 14}), (B_, "B", {"dx": 11, "dy": 4}), (C_, "C", {"dx": 0, "dy": -10}),
            ((2.8, 1.4), "M", {"szin": PIROS, "dx": 8, "dy": 15, "r": 2.6}),
            ((2, 1), "F", {"szin": ZOLD, "dx": -2, "dy": 17, "r": 2.6})],
    szogivek=[((2.8, 1.4), (6, 3), (1, 5), PIROS, "")],
    leiras="Az ABC háromszög a C csúcsból húzott magassággal (piros, a talppont M) és súlyvonallal "
           "(zöld szaggatott, az AB felezőpontjába)")

# ---------------------------------------------------------------- B1
B1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Kanrak:</b> Maxi drónjai <b>egyenes pályán</b> repülnek. Egy pálya — egy egyenlet. '
         'Ha az egyenlet pontos, Tér-eb a pálya bármelyik pontjára odaugrik, és elvágja az utat. '
         'Az egyenletet háromféleképpen is felírhatjuk, és mindegyik alak mást árul el a pályáról: '
         'milyen meredek, hol metszi a tengelyeket, hogyan kell átrendezni.'),
 ]),

 ("Az egyenes iránytényezője", [
   doboz("definicio", "Hajlásszög és iránytényező",
         r'<p>Egy egyenes <b>hajlásszöge</b> az az $\alpha$ szög ($0^\circ\le\alpha\lt180^\circ$), '
         r'amellyel az $x$-tengely pozitív felét az óramutató járásával ellentétes irányban el kell '
         r'forgatni, hogy párhuzamos legyen az egyenessel. Ha $\alpha\ne90^\circ$, az egyenes '
         r'<b>iránytényezője</b></p>'
         r'$$k=\operatorname{tg}\alpha .$$'
         r'<p>Ha az egyenes átmegy az $A(x_1;y_1)$ és a $B(x_2;y_2)$ ponton ($x_1\ne x_2$), akkor</p>'
         r'$$k=\frac{y_2-y_1}{x_2-x_1}.$$'
         r'<p>Az iránytényező megmutatja, mennyit változik az $y$, ha az $x$ eggyel nő — az 1e-ben '
         r'ezt <a href="' + E1 + r'#def-meredekseg">meredekségnek</a> hívtuk.</p>',
         hid="def-iranytenyezo"),
   abra(SVG_IRANY, 'Emelkedő egyenesnél $k\\gt0$, csökkenőnél $k\\lt0$, vízszintesnél $k=0$. '
        'A függőleges egyenesnek ($\\alpha=90^\\circ$) <b>nincs</b> iránytényezője, mert a '
        '$\\operatorname{tg}90^\\circ$ nem értelmezett.'),
   r'<p><b>Példa.</b> Az $A(1;2)$ és a $B(4;8)$ ponton átmenő egyenes iránytényezője '
   r'$k=\frac{8-2}{4-1}=2$, hajlásszöge $\alpha=\operatorname{arctg}2\approx63{,}4^\circ$ '
   r'(számológépen $\tan^{-1}$, fok üzemmódban).</p>',
   doboz("erdekesseg", "Hol találkozol vele?",
         r'<p>A „10%-os emelkedő” közlekedési tábla azt jelenti, hogy vízszintesen mért $100$ méteren '
         r'$10$ métert emelkedik az út: $k=0{,}1$, a hajlásszög $\operatorname{arctg}0{,}1\approx5{,}7^\circ$. '
         r'Ami a táblán ijesztően hangzik, szögben alig több mint öt fok.</p>'),
 ]),

 ("Az iránytényezős alak", [
   doboz("tetel", "Az egyenes iránytényezős (explicit) egyenlete",
         r'<p>A $(0;n)$ pontban az $y$-tengelyt metsző, $k$ iránytényezőjű egyenes egyenlete</p>'
         r'$$y=kx+n .$$'
         r'<p>Egy pont pontosan akkor van az egyenesen, ha a koordinátái kielégítik az '
         r'egyenletet.</p>',
         hid="tetel-explicit"),
   r'<p><b>Ábrázolás.</b> Az $y=-\frac12x+3$ egyenes átmegy a $(0;3)$ ponton, és onnan '
   r'$2$ egységet jobbra lépve $1$ egységet süllyed, tehát a $(2;2)$ is rajta van. A két pontot '
   r'összekötve kész a rajz.</p>'
   r'<p><b>Illeszkedés.</b> A $P(4;1)$ rajta van, mert $-\frac12\cdot4+3=1$. A $Q(2;3)$ nincs '
   r'rajta, mert $-\frac12\cdot2+3=2\ne3$.</p>',
 ]),

 ("Az általános alak", [
   doboz("tetel", "Az egyenes általános (implicit) egyenlete",
         r'<p>Minden egyenes egyenlete felírható</p>'
         r'$$ax+by+c=0\qquad(a^2+b^2\ne0)$$'
         r'<p>alakban — a függőleges is —, és minden ilyen egyenlet egyenest ír le. Ha $b\ne0$, $y$-ra rendezve megkapjuk az explicit alakot:</p>'
         r'$$y=-\frac ab\,x-\frac cb,\qquad\text{vagyis}\qquad k=-\frac ab,\quad n=-\frac cb .$$'
         r'<p>Ha $b=0$, az egyenes függőleges: $x=-\frac ca$. Ha $a=0$, vízszintes: $y=-\frac cb$.</p>'
         r'<p>Egy egyenesnek végtelen sok általános egyenlete van: a $2x-3y+6=0$ és a '
         r'$4x-6y+12=0$ ugyanazt az egyenest írja le (nem nulla számmal szoroztunk).</p>',
         hid="tetel-altalanos"),
   doboz("csapda", "Maxi trükkje",
         r'<p>Maxi a $2x-3y+6=0$ egyenletre ránézett, és kijelentette: „az iránytényező $2$, hiszen '
         r'az van az $x$ előtt”.</p>'
         r'<p>Az $x$ előtti szám csak az <b>explicit</b> alakban iránytényező. Előbb $y$-ra kell '
         r'rendezni: $-3y=-2x-6$, azaz $y=\frac23x+2$. A helyes iránytényező $k=-\frac ab='
         r'-\frac{2}{-3}=\frac23$.</p>'),
   kviz(r'Mennyi a $3x+6y-12=0$ egyenes iránytényezője?',
        [r'$-\frac12$', '$3$', '$-2$', r'$\frac12$'], 0,
        jo="✔ y-ra rendezve 6y = −3x + 12, y = −½x + 2, tehát k = −½.",
        nem="✘ Az x együtthatója csak az y = kx + n alakban iránytényező. Rendezd y-ra: "
            "y = −½x + 2, így k = −a/b = −3/6 = −½."),
   doboz("erdekesseg", "Vektorokkal nézve",
         r'<p>Az $ax+by+c=0$ egyenesre az $\vec N=(a;b)$ vektor <b>merőleges</b> — ezt nevezzük az '
         r'egyenes <b>normálvektorának</b>. A $2x-3y+6=0$ egyenes egyik irányvektora például '
         r'$\vec v=(3;2)$ (hiszen $k=\frac23$), és valóban $\vec N\cdot\vec v=2\cdot3+(-3)\cdot2=0$, '
         r'tehát a két vektor <a href="' + V04 + r'tananyag-skalaris-szorzat.html#tetel-merolegesseg">'
         r'merőleges</a>.</p>'),
 ]),

 ("A tengelymetszetes alak", [
   doboz("tetel", "Az egyenes tengelymetszetes (szegmens) egyenlete",
         r'<p>Ha az egyenes az $x$-tengelyt az $(m;0)$, az $y$-tengelyt a $(0;n)$ pontban metszi, '
         r'és $m\ne0$, $n\ne0$, akkor egyenlete</p>'
         r'$$\frac xm+\frac yn=1 .$$'
         r'<p>Nincs ilyen alakja az <b>origón átmenő</b> egyenesnek (ott $m=n=0$), és a '
         r'<b>tengellyel párhuzamos</b> egyenesnek sem (annak csak egy tengelymetszete van).</p>',
         hid="tetel-tengelymetszetes"),
   doboz("pelda", "Egy egyenes, három alak",
         r'<p>Írd fel a $2x-3y+6=0$ egyenletet explicit és tengelymetszetes alakban, és rajzold meg '
         r'az egyenest!</p>',
         hid="pelda-atvaltas",
         lenyilo=("Megoldás",
                  r'<p><b>Explicit alak:</b> $-3y=-2x-6$, tehát $y=\frac23x+2$.</p>'
                  r'<p><b>Tengelymetszetes alak:</b> a konstanst átvisszük a jobb oldalra, és '
                  r'<b>a jobb oldallal osztunk</b>, hogy $1$ legyen: $2x-3y=-6$, osztva $-6$-tal: '
                  r'$\frac{2x}{-6}+\frac{-3y}{-6}=1$, azaz $\frac{x}{-3}+\frac y2=1$.</p>'
                  r'<p>A két tengelymetszet $m=-3$ és $n=2$: az egyenes a $(-3;0)$ és a $(0;2)$ '
                  r'ponton megy át. Az explicit alak $n=2$-je ugyanez a szám.</p>'
                  + abra(SVG_TENGELY, 'A rajzhoz elég a két tengelymetszet.') +
                  r'<p class="vegeredmeny">$y=\frac23x+2$ · $\frac{x}{-3}+\frac y2=1$</p>')),
   kviz(r'Az $x=2$ egyenesnek melyik alakja <b>nem</b> írható fel?',
        ['sem az iránytényezős, sem a tengelymetszetes', 'csak az általános',
         'csak a tengelymetszetes', 'csak az iránytényezős'], 0,
        jo="✔ Függőleges egyenes: nincs iránytényezője, és az y-tengelyt sem metszi. Általános "
           "alakban viszont felírható: x − 2 = 0.",
        nem="✘ Az x = 2 függőleges: iránytényezője nincs (tg 90° nem értelmezett), az y-tengelyt "
            "nem metszi, így tengelymetszetes alakja sincs. Az általános alak, x − 2 = 0, létezik."),
 ]),

 ("Egyenes adott pontból", [
   doboz("tetel", "Adott ponton, illetve két adott ponton átmenő egyenes",
         r'<p>Az $A(x_1;y_1)$ ponton átmenő, $k$ iránytényezőjű egyenes egyenlete</p>'
         r'$$y-y_1=k\,(x-x_1).$$'
         r'<p>Az $A(x_1;y_1)$ és a $B(x_2;y_2)$ ponton átmenő egyenesnél ($x_1\ne x_2$) előbb '
         r'kiszámítjuk az iránytényezőt, és ugyanezt a képletet használjuk:</p>'
         r'$$y-y_1=\frac{y_2-y_1}{x_2-x_1}\,(x-x_1).$$'
         r'<p>Ha $x_1=x_2$, az egyenes függőleges: $x=x_1$.</p>',
         hid="tetel-ket-pont"),
   r'<p><b>Példa.</b> A $P(2;-1)$ ponton átmenő, $k=3$ iránytényezőjű egyenes: '
   r'$y-(-1)=3(x-2)$, azaz $y=3x-7$.</p>',
   doboz("pelda", "Kristály-kamra szimuláció — a pálya két észlelésből",
         r'<p>A radar Maxi drónját előbb az $A(-1;4)$, majd a $B(3;-4)$ pontban észlelte. A drón '
         r'egyenes pályán halad.</p>'
         r'<ol type="a"><li>Írd fel a pálya egyenletét iránytényezős, általános és tengelymetszetes '
         r'alakban!</li>'
         r'<li>Átrepül-e a drón a $K(5;-8)$ bázis fölött, ha tovább halad?</li></ol>',
         hid="pelda-ket-pont",
         lenyilo=("Megoldás",
                  r'<p><b>a)</b> $k=\frac{-4-4}{3-(-1)}=\frac{-8}{4}=-2$. Az $A$ ponttal: '
                  r'$y-4=-2(x+1)$, azaz $y=-2x+2$. Általános alakban $2x+y-2=0$. '
                  r'Tengelymetszetes alakban $2x+y=2$, osztva $2$-vel: $\frac x1+\frac y2=1$.</p>'
                  r'<p><i>Ellenőrzés a $B$ ponttal: $-2\cdot3+2=-4$ ✔.</i></p>'
                  r'<p><b>b)</b> $-2\cdot5+2=-8$, tehát a $K$ rajta van a pályán. Mivel a drón az $A$-ból a '
                  r'$B$ felé halad (nő az $x$), és $x_K=5\gt3=x_B$, a bázis a haladási irányban van: '
                  r'igen, átrepül fölötte.</p>'
                  + abra(SVG_KET_PONT, 'A pálya és a $K$ bázis.') +
                  r'<p class="vegeredmeny">a) $y=-2x+2$ · $2x+y-2=0$ · $\frac x1+\frac y2=1$ · '
                  r'b) igen, $K$ a pályán van</p>')),
   GY(FGY + "#alap-1", "A 1–10", FGY + "#kozep-1", "K 1–6"),
   brief('<b>Kanrak:</b> Egy pályát már le tudunk írni. A mi járőrvonalunk is egy egyenes — '
         'a kérdés az, <b>hol keresztezi</b> Maxi pályája a miénket, és <b>milyen szögben</b>. '
         'Mert ha a két pálya párhuzamos, soha nem érjük utol.', outro=True),
 ]),
]

# ---------------------------------------------------------------- B2
B2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Kanrak:</b> Két pálya, két egyenlet. Találkoznak? Ha igen, hol — és milyen szögben? '
         'A párhuzamos pályán repülő drónt Tér-eb sosem éri utol, a merőleges vonal viszont a '
         'leggyorsabb elzárás. Ma megtanuljuk két egyenletből kiolvasni, melyik eset áll fenn.'),
 ]),

 ("Két egyenes kölcsönös helyzete", [
   doboz("tetel", "Két egyenes három lehetséges helyzete",
         r'<p>Legyen $e_1\colon y=k_1x+n_1$ és $e_2\colon y=k_2x+n_2$ (egyik sem függőleges). A két egyenes</p>'
         r'<ul><li><b>metszi</b> egymást (pontosan egy közös pont), ha $k_1\ne k_2$;</li>'
         r'<li><b>párhuzamos</b> (nincs közös pont), ha $k_1=k_2$ és $n_1\ne n_2$;</li>'
         r'<li><b>egybeesik</b> (minden pontjuk közös), ha $k_1=k_2$ és $n_1=n_2$.</li></ul>'
         r'<p>A közös pontot a két egyenletből álló rendszer megoldása adja — ugyanaz a három '
         r'eset, amelyet a <a href="' + V03 + r'tananyag-ket-ismeretlen.html#tetel-geometriai-jelentes">'
         r'lineáris egyenletrendszereknél</a> láttál.</p>'
         r'<p>Két függőleges egyenes párhuzamos vagy egybeesik; egy függőleges és egy nem függőleges '
         r'egyenes mindig metszi egymást.</p>',
         hid="tetel-kolcsonos-helyzet"),
   r'<p><b>Példa.</b> Az $y=2x-3$ és az $x+y-6=0$ egyenes iránytényezője $2$, illetve $-1$, '
   r'tehát metszik egymást. A metszéspont: $x+(2x-3)=6$, ahonnan $x=3$ és $y=3$, azaz $M(3;3)$.</p>',
   kviz(r'Milyen helyzetű az $y=2x+3$ és a $4x-2y+6=0$ egyenes?',
        ['egybeesnek', 'párhuzamosak', 'metszik egymást', 'merőlegesek'], 0,
        jo="✔ A második y-ra rendezve y = 2x + 3 — ugyanaz az egyenes.",
        nem="✘ A második egyenletet rendezd y-ra: 2y = 4x + 6, y = 2x + 3. Az iránytényező "
            "ÉS a tengelymetszet is egyezik, tehát a két egyenes egybeesik, nem csak párhuzamos."),
 ]),

 ("Párhuzamosság és merőlegesség", [
   doboz("tetel", "A párhuzamosság és a merőlegesség feltétele",
         r'<p>Az $y=k_1x+n_1$ és az $y=k_2x+n_2$ egyenes</p>'
         r'<ul><li><b>párhuzamos</b> (vagy egybeesik), ha $k_1=k_2$;</li>'
         r'<li><b>merőleges</b>, ha $k_1\cdot k_2=-1$, azaz $k_2=-\dfrac1{k_1}$.</li></ul>'
         r'<p>A vízszintes ($k=0$) és a függőleges egyenes (nincs $k$) szintén merőleges egymásra — '
         r'ezt az esetet a képlet nem fedi le, külön kell észrevenni.</p>',
         hid="tetel-parhuzamos-meroleges"),
   r'<p><i>Miért $-1$?</i> Az egyenesek irányvektora $(1;k_1)$, illetve $(1;k_2)$. Két vektor '
   r'pontosan akkor <a href="' + V04 + r'tananyag-skalaris-szorzat.html#tetel-merolegesseg">'
   r'merőleges</a>, ha skaláris szorzatuk $0$: $1\cdot1+k_1k_2=0$.</p>',
   abra(SVG_MEROLEGES, 'Az $y=2x$ és az $y=-\\frac12x+5$ egyenes merőleges: $2\\cdot\\left(-\\frac12\\right)=-1$.'),
   doboz("csapda", "Maxi trükkje",
         r'<p>Maxi merőleges pályát akart húzni az $y=4x-1$ pályára. Először $k=-4$-et írt („az '
         r'ellentettje”), aztán $k=\frac14$-et („a reciproka”). Mindkét pálya ferdén metszette a '
         r'célt.</p>'
         r'<p>A merőleges iránytényező <b>egyszerre</b> ellentett és reciprok — a <b>negatív '
         r'reciprok</b>: $-\frac14$. Ellenőrzés: $4\cdot\left(-\frac14\right)=-1$ ✔.</p>'),
   kviz(r'Mennyi az $y=4x-1$ egyenesre merőleges egyenes iránytényezője?',
        [r'$-\frac14$', '$-4$', r'$\frac14$', '$4$'], 0,
        jo="✔ k₁·k₂ = −1, tehát k₂ = −1/4.",
        nem="✘ A merőleges iránytényező a negatív reciprok: −1/4. A −4 csak ellentett, az 1/4 "
            "csak reciprok — a szorzatuk nem −1."),
 ]),

 ("Párhuzamos és merőleges egyenes adott ponton át", [
   r'<p>A recept két lépés: <b>1)</b> az adott egyenes iránytényezőjéből kiszámoljuk a keresett '
   r'iránytényezőt (párhuzamosnál ugyanaz, merőlegesnél a negatív reciprok); <b>2)</b> felírjuk '
   r'az $y-y_1=k(x-x_1)$ egyenletet. Ha az adott egyenes vízszintes, a rá merőleges '
   r'egyenes függőleges: $x=x_1$.</p>'
   r'<p><b>Példa.</b> $P(-2;3)$ és $e\colon 3x-4y+1=0$, ahol $k_e=\frac34$.</p>'
   r'<ul><li>Párhuzamos: $y-3=\frac34(x+2)$, szorozva $4$-gyel: $4y-12=3x+6$, azaz '
   r'$3x-4y+18=0$.</li>'
   r'<li>Merőleges: $k=-\frac43$, $y-3=-\frac43(x+2)$, szorozva $3$-mal: $3y-9=-4x-8$, azaz '
   r'$4x+3y-1=0$.</li></ul>',
   doboz("pelda", "Kristály-kamra szimuláció — a felezőmerőleges",
         r'<p>Két bázisunk van: $A(-2;1)$ és $B(4;5)$. Tér-eb olyan vonalon akar járőrözni, '
         r'amelynek minden pontja <b>egyenlő távolságra</b> van a két bázistól. Ez az $AB$ szakasz '
         r'<b>felezőmerőlegese</b>. Írd fel az egyenletét!</p>',
         hid="pelda-felezomeroleges",
         lenyilo=("Megoldás",
                  r'<p>A felezőmerőleges átmegy az $AB$ felezőpontján, és merőleges az $AB$-re.</p>'
                  r'<p>$F\left(\frac{-2+4}{2};\ \frac{1+5}{2}\right)=F(1;3)$, '
                  r'$k_{AB}=\frac{5-1}{4-(-2)}=\frac23$, tehát a merőleges iránytényező '
                  r'$k=-\frac32$.</p>'
                  r'<p>$y-3=-\frac32(x-1)$, szorozva $2$-vel: $2y-6=-3x+3$, azaz $3x+2y-9=0$.</p>'
                  r'<p class="vegeredmeny">$3x+2y-9=0$</p>')),
 ]),

 ("Két egyenes szöge", [
   doboz("tetel", "Két egyenes szöge",
         r'<p>Két metsző egyenes szöge a keletkező szögek közül a <b>nem tompa</b> szög: '
         r'$0^\circ\lt\varphi\le90^\circ$. Ha az egyenesek iránytényezője $k_1$ és $k_2$, és '
         r'$1+k_1k_2\ne0$, akkor</p>'
         r'$$\operatorname{tg}\varphi=\left|\frac{k_2-k_1}{1+k_1k_2}\right| .$$'
         r'<p>Ha $1+k_1k_2=0$, az egyenesek merőlegesek: $\varphi=90^\circ$. Ha az egyik egyenes '
         r'függőleges, a másik hajlásszögéből számolunk: $\varphi=|90^\circ-\alpha|$.</p>',
         hid="tetel-szog"),
   abra(SVG_SZOG, 'Az $y=2x+1$ és az $y=-3x+4$ egyenes szöge.'),
   doboz("pelda", "Két egyenes szöge",
         r'<p>Számítsd ki a következő egyenespárok szögét! Ha nem kerek érték jön ki, egy tizedesre kerekíts!</p>'
         r'<p><b>a)</b> $y=2x+1$ és $y=-3x+4$: $\operatorname{tg}\varphi=\left|\frac{-3-2}{1+2\cdot(-3)}\right|'
         r'=\left|\frac{-5}{-5}\right|=1$, tehát $\varphi=45^\circ$.</p>'
         r'<p><b>b)</b> $y=3x$ és $y=-\frac12x+1$: $\operatorname{tg}\varphi=\left|\frac{-\frac12-3}'
         r'{1+3\cdot\left(-\frac12\right)}\right|=\left|\frac{-3{,}5}{-0{,}5}\right|=7$, '
         r'számológéppel $\varphi=\operatorname{arctg}7\approx81{,}9^\circ$ (egy tizedesre kerekítve).</p>'
         r'<p><b>c)</b> $x=1$ és $y=2x+1$: a második hajlásszöge $\alpha=\operatorname{arctg}2'
         r'\approx63{,}4^\circ$, tehát $\varphi\approx90^\circ-63{,}4^\circ=26{,}6^\circ$.</p>',
         hid="pelda-szog"),
   doboz("erdekesseg", "Vektorokkal is megy",
         r'<p>A két egyenes szöge megegyezik a normálvektoraik szögével (ha az tompa, a '
         r'kiegészítőjével). A $2x-y+1=0$ és a $3x+y-4=0$ egyenesnél (ez az a) feladat egyenespárja) '
         r'$\vec N_1=(2;-1)$, $\vec N_2=(3;1)$:</p>'
         r'$$\cos\varphi=\frac{|\vec N_1\cdot\vec N_2|}{|\vec N_1|\,|\vec N_2|}=\frac{|6-1|}'
         r'{\sqrt5\cdot\sqrt{10}}=\frac{1}{\sqrt2},\qquad\varphi=45^\circ .$$'
         r'<p>Ez a módszer a függőleges egyenesnél is működik — a '
         r'<a href="' + V04 + r'tananyag-skalaris-szorzat.html#pelda-szog">vektorok szögénél</a> '
         r'már így számoltál.</p>'),
   r'<p><b>Két gyakori hiba.</b> Ha elhagyod az abszolút értéket, negatív tangenst kaphatsz, és a '
   r'számológép negatív szöget ad. Ha pedig a gép <b>radián</b> üzemmódban van, az '
   r'$\operatorname{arctg}1$ eredménye $0{,}785$ lesz $45$ helyett — mindig nézd meg a kijelzőn a '
   r'<b>D</b> vagy <b>DEG</b> jelet.</p>',
   GY(FGY + "#alap-11", "A 11–18", FGY + "#kozep-7", "K 7–12"),
   brief('<b>Kanrak:</b> Metszéspont és szög: megvan. Most egy másik kérdés '
         'jön: a mi bázisunk egy <b>pont</b>, Maxi pályája egy <b>egyenes</b>. Milyen közel repül '
         'el mellettünk? Mert a riasztó csak egy bizonyos távolságon belül szól.', outro=True),
 ]),
]

# ---------------------------------------------------------------- B3
B3 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Kanrak:</b> A bázis riasztója akkor szól, ha Maxi drónja <b>3 egységnél közelebb</b> '
         'repül el mellette. Hogy közel jár-e, azt nem a pálya bármelyik pontja dönti el, hanem a '
         'legközelebbi: a bázisból a pályára bocsátott merőleges talppontja.'),
 ]),

 ("Pont és egyenes távolsága", [
   doboz("definicio", "Pont és egyenes távolsága",
         r'<p>A $P$ pont és az $e$ egyenes <b>távolsága</b> a $P$-ből az $e$-re bocsátott merőleges '
         r'szakasz hossza — ez a $P$ és az egyenes pontjai közötti legrövidebb távolság. Ha a $P$ '
         r'az egyenesen van, a távolság $0$.</p>',
         hid="def-pont-egyenes-tavolsag"),
   doboz("tetel", "A távolság képlete",
         r'<p>A $P(x_0;y_0)$ pont távolsága az $ax+by+c=0$ egyenestől</p>'
         r'$$d=\frac{|a\,x_0+b\,y_0+c|}{\sqrt{a^2+b^2}} .$$'
         r'<p>A képlet az egyenes <b>általános alakjára</b> vonatkozik: ha az egyenlet $y=kx+n$ '
         r'alakban adott, előbb $0$-ra rendezzük.</p>',
         hid="tetel-tavolsagkeplet"),
   doboz("pelda", "Szól-e a riasztó?",
         r'<p>A bázis a $K(2;3)$ pontban van, Maxi drónja a $4x+3y-27=0$ egyenes mentén repül. '
         r'Megszólal-e a riasztó, amely $3$ egységnél közelebbi elhaladásra van beállítva?</p>'
         + abra(SVG_TAVOLSAG, 'A bázis és a pálya távolsága a merőleges szakasz, $d$.'),
         hid="pelda-riasztas",
         lenyilo=("Megoldás",
                  r'<p>$d=\frac{|4\cdot2+3\cdot3-27|}{\sqrt{4^2+3^2}}=\frac{|8+9-27|}{5}=\frac{10}{5}=2$.</p>'
                  r'<p>Mivel $2\lt3$, a drón a riasztási körzeten belül halad el.</p>'
                  r'<p class="vegeredmeny">$d=2$, a riasztó megszólal</p>')),
   doboz("csapda", "Maxi trükkje",
         r'<p>Maxi a $P(1;4)$ pont és az $y=\frac34x+2$ egyenes távolságát kereste. Az egyenletből '
         r'kiolvasta, hogy „$a=\frac34$, $b=1$, $c=2$”, és ezt kapta:</p>'
         r'$$d=\frac{\left|\frac34\cdot1+1\cdot4+2\right|}{\sqrt{\frac9{16}+1}}=\frac{6{,}75}{1{,}25}=5{,}4 .$$'
         r'<p>A képlet az $ax+by+c=0$ alakot várja. $0$-ra rendezve $\frac34x-y+2=0$, tehát $b=-1$, '
         r'nem $1$. (Érdemes $4$-gyel szorozni: $3x-4y+8=0$.) Így '
         r'$d=\frac{|3\cdot1-4\cdot4+8|}{\sqrt{9+16}}=\frac{|-5|}{5}=1$.</p>'),
   kviz(r'Mekkora a $P(1;1)$ pont távolsága az $y=2x+1$ egyenestől?',
        [r'$\frac{2}{\sqrt5}$', r'$\frac{4}{\sqrt5}$', r'$\frac25$', '$2$'], 0,
        jo="✔ Rendezve 2x − y + 1 = 0, így d = |2 − 1 + 1| / √5 = 2/√5 ≈ 0,89.",
        nem="✘ Előbb rendezd 0-ra: 2x − y + 1 = 0, tehát b = −1. Ekkor d = |2·1 − 1·1 + 1| / "
            "√(4 + 1) = 2/√5. (A 4/√5 a b = +1-ből, a 2/5 a gyökvonás elhagyásából jön.)"),
 ]),

 ("Két párhuzamos egyenes távolsága", [
   r'<p>Két párhuzamos egyenes minden pontja ugyanakkora távolságra van a másik egyenestől. '
   r'Ezért elég az egyik egyenesen <b>egy tetszőleges pontot</b> választani, és annak a '
   r'távolságát kiszámolni a másiktól — külön képletre nincs szükség.</p>',
   doboz("pelda", "Két párhuzamos egyenes távolsága",
         r'<p>Milyen messze van egymástól a $3x+4y-7=0$ és a $3x+4y+8=0$ egyenes?</p>',
         hid="pelda-parhuzamos",
         lenyilo=("Megoldás",
                  r'<p>A két egyenes párhuzamos (az $x$ és az $y$ együtthatói egyenlők, a konstans tagok nem). Az első '
                  r'egyenesen van például a $P(1;1)$, hiszen $3+4-7=0$.</p>'
                  r'<p>$d=\frac{|3\cdot1+4\cdot1+8|}{\sqrt{9+16}}=\frac{15}{5}=3$.</p>'
                  r'<p class="vegeredmeny">$d=3$</p>')),
   doboz("erdekesseg", "Hol találkozol vele?",
         r'<p>Egy autópálya-sáv két szélét leíró egyenesek párhuzamosak; a sáv szélessége a két '
         r'egyenes távolsága. Nálunk egy forgalmi sáv jellemzően $3{,}5$–$3{,}75$ méter széles.</p>'),
 ]),

 ("Háromszög koordinátákkal", [
   r'<p>Az eddigi eszközökkel egy háromszög szinte minden adatát ki tudjuk számolni a csúcsaiból. '
   r'Két nevezetes vonalat érdemes élesen megkülönböztetni:</p>'
   r'<ul><li>a $C$-hez tartozó <b>magasságvonal</b> átmegy a $C$-n, és <b>merőleges</b> az $AB$ '
   r'oldal egyenesére;</li>'
   r'<li>a $C$-hez tartozó <b>súlyvonal</b> átmegy a $C$-n és az $AB$ oldal <b>felezőpontján</b>.</li></ul>'
   r'<p>A magasság hossza a $C$ csúcs távolsága az $AB$ egyenestől. Ha csak az oldalegyenesek '
   r'adottak, a csúcsokat két-két oldalegyenes <b>metszéspontja</b> adja.</p>',
   doboz("pelda", "Kristály-kamra szimuláció — a háromszög minden adata",
         r'<p>Maxi három jeladója egy háromszöget alkot: $A(-2;-1)$, $B(6;3)$, $C(1;5)$.</p>'
         r'<ol type="a"><li>Írd fel az $AB$ oldal egyenesének egyenletét!</li>'
         r'<li>Írd fel a $C$-hez tartozó magasságvonal egyenletét!</li>'
         r'<li>Milyen hosszú a $C$-hez tartozó magasság? (Pontos alakban és két tizedesre kerekítve.)</li>'
         r'<li>Számítsd ki a háromszög területét kétféleképpen!</li>'
         r'<li>Írd fel a $C$-hez tartozó súlyvonal egyenletét!</li></ol>',
         hid="pelda-haromszog",
         lenyilo=("Megoldás",
                  r'<p><b>a)</b> $k_{AB}=\frac{3-(-1)}{6-(-2)}=\frac12$; $y+1=\frac12(x+2)$, '
                  r'szorozva $2$-vel: $2y+2=x+2$, azaz $x-2y=0$.</p>'
                  r'<p><b>b)</b> A merőleges iránytényező $-2$; $y-5=-2(x-1)$, azaz $2x+y-7=0$.</p>'
                  r'<p><b>c)</b> $m_c=\frac{|1-2\cdot5|}{\sqrt{1+4}}=\frac9{\sqrt5}\approx4{,}02$.</p>'
                  r'<p><b>d)</b> $|AB|=\sqrt{8^2+4^2}=\sqrt{80}=4\sqrt5$, így '
                  r'$T=\frac{|AB|\cdot m_c}{2}=\frac{4\sqrt5\cdot\frac9{\sqrt5}}{2}=18$. '
                  r'Determinánssal: $D=-2\cdot(3-5)+6\cdot(5-(-1))+1\cdot(-1-3)=4+36-4=36$, '
                  r'$T=\frac12\cdot36=18$ ✔.</p>'
                  r'<p><b>e)</b> Az $AB$ felezőpontja $F(2;1)$; a $C(1;5)$ és az $F$ ponton átmenő '
                  r'egyenes: $k=\frac{1-5}{2-1}=-4$, $y-5=-4(x-1)$, azaz $4x+y-9=0$.</p>'
                  + abra(SVG_HAROMSZOG, 'A magasság (piros) az $M\\left(\\frac{14}5;\\frac75\\right)$ '
                         'talppontba fut, a súlyvonal (zöld) az $F(2;1)$ felezőpontba.') +
                  r'<p class="vegeredmeny">a) $x-2y=0$ · b) $2x+y-7=0$ · c) $\frac9{\sqrt5}\approx4{,}02$ · '
                  r'd) $T=18$ · e) $4x+y-9=0$</p>')),
   kviz(r'Az $ABC$ háromszögben melyik az a nevezetes vonal, amely átmegy a $C$ csúcson, és '
        r'merőleges az $AB$ oldal egyenesére?',
        ['a magasságvonal', 'a súlyvonal', 'az $AB$ felezőmerőlegese', 'a szögfelező'], 0,
        jo="✔ A magasságvonal a csúcson át merőleges a szemközti oldalra.",
        nem="✘ A súlyvonal a felezőponton megy át, és általában nem merőleges. A felezőmerőleges "
            "merőleges, de a felezőponton megy át, és a csúcson általában nem (csak ha CA = CB). A C-n átmenő merőleges a "
            "magasságvonal."),
 ]),

 ("🧾 Gyorsismétlő", [
   r'<p>Az I. rész minden képlete egy helyen — a 3. dolgozat előtt.</p>'
   r'<div class="tblwrap"><table class="tt-table">'
   r'<tr><th>Mit keresünk?</th><th>Képlet</th><th>Hol tanultuk?</th></tr>'
   r'<tr><td>két pont távolsága</td><td>$|AB|=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$</td>'
   r'<td><a href="tananyag-pontok-a-sikban.html#tetel-tavolsag">Pontok a síkban</a></td></tr>'
   r'<tr><td>osztópont, felezőpont</td><td>$C\left(\frac{nx_1+mx_2}{m+n};\frac{ny_1+my_2}{m+n}\right)$, '
   r'$F\left(\frac{x_1+x_2}2;\frac{y_1+y_2}2\right)$</td>'
   r'<td><a href="tananyag-pontok-a-sikban.html#tetel-osztopont">Pontok a síkban</a></td></tr>'
   r'<tr><td>súlypont</td><td>$S\left(\frac{x_1+x_2+x_3}3;\frac{y_1+y_2+y_3}3\right)$</td>'
   r'<td><a href="tananyag-pontok-a-sikban.html#tetel-sulypont">Pontok a síkban</a></td></tr>'
   r'<tr><td>háromszög területe</td><td>$T=\frac12|D|$, $D=x_1(y_2-y_3)+x_2(y_3-y_1)+x_3(y_1-y_2)$</td>'
   r'<td><a href="tananyag-haromszog-terulete.html#tetel-terulet">A háromszög területe</a></td></tr>'
   r'<tr><td>kollinearitás</td><td>$D=0$</td>'
   r'<td><a href="tananyag-haromszog-terulete.html#tetel-kollinearitas">A háromszög területe</a></td></tr>'
   r'<tr><td>iránytényező</td><td>$k=\operatorname{tg}\alpha=\frac{y_2-y_1}{x_2-x_1}$ ($x_1\ne x_2$)</td>'
   r'<td><a href="tananyag-egyenes-egyenlete.html#def-iranytenyezo">Az egyenes egyenlete</a></td></tr>'
   r'<tr><td>az egyenes alakjai</td><td>$y=kx+n$ · $ax+by+c=0$ · $\frac xm+\frac yn=1$</td>'
   r'<td><a href="tananyag-egyenes-egyenlete.html#tetel-altalanos">Az egyenes egyenlete</a></td></tr>'
   r'<tr><td>egyenes adott pontból</td><td>$y-y_1=k(x-x_1)$</td>'
   r'<td><a href="tananyag-egyenes-egyenlete.html#tetel-ket-pont">Az egyenes egyenlete</a></td></tr>'
   r'<tr><td>párhuzamos · merőleges</td><td>$k_1=k_2$ · $k_1k_2=-1$</td>'
   r'<td><a href="tananyag-ket-egyenes.html#tetel-parhuzamos-meroleges">Két egyenes</a></td></tr>'
   r'<tr><td>két egyenes szöge</td><td>$\operatorname{tg}\varphi=\left|\frac{k_2-k_1}{1+k_1k_2}\right|$</td>'
   r'<td><a href="tananyag-ket-egyenes.html#tetel-szog">Két egyenes</a></td></tr>'
   r'<tr><td>pont és egyenes távolsága</td><td>$d=\frac{|ax_0+by_0+c|}{\sqrt{a^2+b^2}}$</td>'
   r'<td><a href="#tetel-tavolsagkeplet">fent</a></td></tr>'
   r'</table></div>',
   GY(FGY + "#alap-19", "A 19–24", FGY + "#kozep-13", "K 13–18"),
   brief('<b>Kanrak:</b> Az egyenes pályákat lezártuk: Maxi drónjai nem jutnak át a hálózaton. '
         'Csakhogy Maxi nem adta fel — <b>teleport-kapukat</b> nyitott a Kamrában, és ezeknek a '
         'peremét nem egyenesek, hanem <b>körívek</b> alkotják. Új egyenletekre lesz szükség.',
         outro=True),
 ]),
]

# ---------------------------------------------------------------- lapok
KI = [
 lap(**T, fajl="tananyag-egyenes-egyenlete.html",
     cim="Az egyenes egyenlete",
     alcim="Az iránytényező, az egyenes iránytényezős, általános és tengelymetszetes alakja, "
           "valamint az adott ponton és a két adott ponton átmenő egyenes.",
     chip=KUL + " · 3/13", szakaszok=B1,
     elozo=("feladatok-pontok.html", "Pontok — feladatok"),
     kovetkezo=("tananyag-ket-egyenes.html", "Két egyenes")),
 lap(**T, fajl="tananyag-ket-egyenes.html",
     cim="Két egyenes — metszéspont, szög, párhuzamosság, merőlegesség",
     cim_tiszta="Két egyenes",
     alcim="Két egyenes kölcsönös helyzete, a párhuzamosság és a merőlegesség feltétele, "
           "egyenes adott ponton át és két egyenes szöge.",
     chip=KUL + " · 4/13", szakaszok=B2,
     elozo=("tananyag-egyenes-egyenlete.html", "Az egyenes egyenlete"),
     kovetkezo=("tananyag-pont-es-egyenes-tavolsaga.html", "Pont és egyenes távolsága")),
 lap(**T, fajl="tananyag-pont-es-egyenes-tavolsaga.html",
     cim="Pont és egyenes távolsága — háromszögek koordinátákkal",
     cim_tiszta="Pont és egyenes távolsága",
     alcim="A pont és az egyenes távolsága, két párhuzamos egyenes távolsága, a háromszög "
           "nevezetes vonalai koordinátákkal, és az I. rész gyorsismétlője.",
     chip=KUL + " · 5/13", szakaszok=B3,
     elozo=("tananyag-ket-egyenes.html", "Két egyenes"),
     kovetkezo=(FGY, "Egyenesek — feladatok")),
]
for u in KI:
    print("✓", os.path.basename(u))
