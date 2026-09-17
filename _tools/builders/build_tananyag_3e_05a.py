# -*- coding: utf-8 -*-
"""3e/05 — A blokk: pontok a sikban (A1), a haromszog terulete (A2).
Mentor: Kanrak (Ter-eb). Kuldetes: A Terkep Halozata."""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tananyag_common import lap, doboz, brief, kviz, gyakorolj, abra
from abra_common import svg_koordsik, KEK, BOROSTYAN, ZOLD, PIROS, SZURKE, LILA

T = dict(tagozat="3e", mappa="05-analitikus-geometria", temakor="Síkbeli analitikus geometria")
FGY = "feladatok-pontok.html"
KUL = "A Térkép Hálózata"
V04 = "../04-vektorok/"
V03 = "../03-linearis-rendszerek/"


def GY(k_h, k_c, n_h, n_c):
    return gyakorolj(k_h, k_c, n_h, n_c, tagozat="3e")


# ---------------------------------------------------------------- önteszt
from sympy import Matrix, sqrt, Rational, simplify, Abs, symbols, solve, expand
E = []
def chk(n, g, w):
    if isinstance(g, (tuple, list)):
        ok = len(g) == len(w) and all(simplify(Rational(0) + u - v) == 0 for u, v in zip(g, w))
    else:
        ok = simplify(g - w) == 0
    if not ok:
        E.append((n, g, w))

def tav(P, Q):
    return sqrt((Q[0] - P[0])**2 + (Q[1] - P[1])**2)

def oszto(P, Q, m, n):
    return (Rational(n*P[0] + m*Q[0], m + n), Rational(n*P[1] + m*Q[1], m + n))

def Dm(P, Q, R):
    return Matrix([[P[0], P[1], 1], [Q[0], Q[1], 1], [R[0], R[1], 1]]).det()

def cipofuzo(P):
    k = len(P)
    return Rational(1, 2)*Abs(sum(P[i][0]*P[(i+1) % k][1] - P[(i+1) % k][0]*P[i][1] for i in range(k)))

# A1
chk("tukor-x", (3, 2), (3, -(-2))); chk("tukor-y", (-3, -2), (-3, -2))
chk("tav-AB", tav((-2, 5), (6, -1)), 10)
chk("tav-maxi", tav((0, 5), (4, -1)), sqrt(52))
chk("tav-origo", tav((0, 0), (-5, 12)), 13)
chk("kviz-tav", tav((1, 1), (4, 5)), 5)
chk("oszto", oszto((-2, 1), (7, 4), 1, 2), (1, 2))
chk("felezo", oszto((-2, 1), (7, 4), 1, 1), (Rational(5, 2), Rational(5, 2)))
chk("kviz-oszto", oszto((0, 0), (8, 0), 1, 3), (2, 0))
chk("kviz-oszto-rossz", oszto((0, 0), (8, 0), 3, 1), (6, 0))
Ap, Bp, Cp = (-1, -2), (4, 0), (6, 4)
Fk = oszto(Ap, Cp, 1, 1)
chk("par-F", Fk, (Rational(5, 2), 1))
Dp = (2*Fk[0] - Bp[0], 2*Fk[1] - Bp[1])
chk("par-D", Dp, (1, 2)); chk("par-BD-felezo", oszto(Bp, Dp, 1, 1), Fk)
A, B, C = (-1, -2), (7, -2), (3, 4)
chk("dron-AB", tav(A, B), 8); chk("dron-AC", tav(A, C), 2*sqrt(13))
chk("dron-AC-kozel", round(float(2*sqrt(13)), 2), Rational(721, 100))
F = oszto(A, B, 1, 1); chk("dron-F", F, (3, -2))
S = (Rational(A[0] + B[0] + C[0], 3), Rational(A[1] + B[1] + C[1], 3)); chk("dron-S", S, (3, 0))
chk("dron-sc", tav(C, F), 6); chk("dron-CS", tav(C, S), 4); chk("dron-SF", tav(S, F), 2)
# A2
PENT = [(-3, -1), (2, -1), (4, 2), (1, 4), (-3, 3)]
chk("darab", cipofuzo(PENT), 27); chk("darab-lepes", 35 - 3 - 3 - 2, 27)
A2, B2, C2 = (-2, -1), (4, 1), (1, 5)
chk("ter-D", Dm(A2, B2, C2), 30); chk("ter-T", Rational(1, 2)*Abs(Dm(A2, B2, C2)), 15)
chk("ter-kifejt", A2[0]*(B2[1] - C2[1]) + B2[0]*(C2[1] - A2[1]) + C2[0]*(A2[1] - B2[1]), 30)
chk("ter-darab", 36 - 6 - 6 - 9, 15)
chk("ter-vekt", (B2[0]-A2[0])*(C2[1]-A2[1]) - (B2[1]-A2[1])*(C2[0]-A2[0]), 30)
chk("kolin", Dm((-1, -3), (1, 1), (4, 7)), 0)
x = symbols("x", real=True)
Dx = expand(Dm((-1, 1), (3, -1), (x, 3)))
chk("ismeretlen-D", Dx, 2*x + 10)
chk("ismeretlen-1", solve(Dx - 18, x), [4]); chk("ismeretlen-2", solve(Dx + 18, x), [-14])
chk("ism-ell-1", Rational(1, 2)*Abs(Dm((-1, 1), (3, -1), (4, 3))), 9)
chk("ism-ell-2", Rational(1, 2)*Abs(Dm((-1, 1), (3, -1), (-14, 3))), 9)
Q = [(-2, -2), (4, -1), (3, 3), (-1, 4)]
chk("negy-ABC", Dm(Q[0], Q[1], Q[2]), 25); chk("negy-ACD", Dm(Q[0], Q[2], Q[3]), 25)
chk("negy-T", cipofuzo(Q), 25); chk("negy-rossz", cipofuzo([Q[0], Q[1], Q[3], Q[2]]), 5)
chk("negy-rossz-PS", Rational(1, 2)*Abs(Dm(Q[0], Q[1], Q[3])) + Rational(1, 2)*Abs(Dm(Q[0], Q[3], Q[2])), 30)
chk("negy-rossz-QR", Rational(1, 2)*Abs(Dm(Q[1], Q[3], Q[2])) + Rational(1, 2)*Abs(Dm(Q[1], Q[2], Q[0])), 20)
chk("kviz-ter", Rational(1, 2)*Abs(-14), 7)
assert not E, E
print("sympy önteszt: OK")

# ---------------------------------------------------------------- ábrák
H = {"dolt": True}
SVG_SIK = svg_koordsik(
    xr=(-5, 5), yr=(-4, 5),
    pontok=[((3, 2), "A"), ((-2, 4), "B"), ((-3, -1), "C", {"dx": -10}), ((4, -2), "D"),
            ((0, -3), "E", {"dx": 11, "dy": 5})],
    szakaszok=[((3, 2), (3, 0), SZURKE, {"szaggat": "4 3", "sz": 1.4}),
               ((3, 2), (0, 2), SZURKE, {"szaggat": "4 3", "sz": 1.4})],
    feliratok=[((4.3, 4.3), "I.", {"szin": SZURKE, "meret": 15}),
               ((-4.3, 4.3), "II.", {"szin": SZURKE, "meret": 15}),
               ((-4.3, -3.4), "III.", {"szin": SZURKE, "meret": 15}),
               ((4.3, -3.4), "IV.", {"szin": SZURKE, "meret": 15})],
    leiras="Koordináta-rendszer a négy síknegyeddel és öt ponttal: A(3;2), B(−2;4), C(−3;−1), "
           "D(4;−2) és az y-tengelyen E(0;−3); az A pontból a tengelyekre húzott merőlegesek")
SVG_TAV = svg_koordsik(
    xr=(-3, 7), yr=(-2, 6),
    pontok=[((-2, 5), "A", {"dx": -4, "dy": -9}), ((6, -1), "B", {"dx": 12, "dy": 4}),
            ((6, 5), "C", {"ures": True, "dx": 11, "dy": -6})],
    szakaszok=[((-2, 5), (6, -1), KEK, {"sz": 2.6, "felirat": "d", "dx": -10, "dy": -4}),
               ((-2, 5), (6, 5), SZURKE, {"szaggat": "5 3", "felirat": "|x₂ − x₁| = 8", "dy": -8,
                                          "dolt": False, "meret": 12}),
               ((6, 5), (6, -1), SZURKE, {"szaggat": "5 3", "felirat": "|y₂ − y₁| = 6", "dx": -46,
                                          "dy": 30, "dolt": False, "meret": 12})],
    leiras="Az A(−2;5) és B(6;−1) pont távolsága egy derékszögű háromszög átfogója; a befogók "
           "8 és 6 egység")
SVG_OSZTO = svg_koordsik(
    xr=(-3, 8), yr=(-1, 5),
    pontok=[((-2, 1), "A", {"dx": -4, "dy": -10}), ((7, 4), "B", {"dx": 4, "dy": -10}),
            ((1, 2), "C", {"szin": PIROS, "dx": -2, "dy": -11}),
            ((2.5, 2.5), "F", {"szin": ZOLD, "dx": 4, "dy": -11})],
    szakaszok=[((-2, 1), (7, 4), KEK, {"sz": 2.4})],
    leiras="Az AB szakasz A(−2;1) és B(7;4) végpontokkal; a C(1;2) pont harmadolja (AC:CB = 1:2), "
           "az F(2,5;2,5) a felezőpontja")
SVG_PAR = svg_koordsik(
    xr=(-2, 7), yr=(-3, 5),
    sokszogek=[([(-1, -2), (4, 0), (6, 4), (1, 2)], KEK)],
    szakaszok=[((-1, -2), (6, 4), SZURKE, {"szaggat": "5 3", "sz": 1.4}),
               ((4, 0), (1, 2), SZURKE, {"szaggat": "5 3", "sz": 1.4})],
    pontok=[((-1, -2), "A", {"dx": -10, "dy": 4}), ((4, 0), "B", {"dx": 10, "dy": 14}),
            ((6, 4), "C", {"dx": 10}), ((1, 2), "D", {"dx": -10, "dy": -6}),
            ((2.5, 1), "M", {"szin": ZOLD, "dx": 2, "dy": -10})],
    leiras="Az ABCD paralelogramma; az AC és a BD átló közös felezőpontja M(2,5;1)")
SVG_DRON = svg_koordsik(
    xr=(-2, 8), yr=(-3, 5),
    sokszogek=[([(-1, -2), (7, -2), (3, 4)], KEK, {"kitolt": 0.10})],
    szakaszok=[((3, 4), (3, -2), ZOLD, {"sz": 2.2, "felirat": "s", "dx": -9, "dy": -18})],
    pontok=[((-1, -2), "A", {"dx": -10, "dy": 4}), ((7, -2), "B", {"dx": 10, "dy": 4}),
            ((3, 4), "C", {"dx": 10, "dy": -4}), ((3, -2), "F", {"szin": ZOLD, "dx": 10, "dy": 14}),
            ((3, 0), "S", {"szin": PIROS, "dx": 11, "dy": -6})],
    leiras="A drónraj háromszöge A(−1;−2), B(7;−2), C(3;4) csúcsokkal; a C-ből induló súlyvonal "
           "az AB felezőpontjába, F(3;−2)-be fut, és az S(3;0) súlypont harmadolja")
PENT = [(-3, -1), (2, -1), (4, 2), (1, 4), (-3, 3)]
SVG_DARAB = svg_koordsik(
    xr=(-4, 5), yr=(-2, 5),
    sokszogek=[(PENT, KEK, {"kitolt": 0.16}),
               ([(2, -1), (4, -1), (4, 2)], BOROSTYAN, {"kitolt": 0.30, "sz": 1.2}),
               ([(4, 2), (4, 4), (1, 4)], BOROSTYAN, {"kitolt": 0.30, "sz": 1.2}),
               ([(1, 4), (-3, 4), (-3, 3)], BOROSTYAN, {"kitolt": 0.30, "sz": 1.2})],
    szakaszok=[((-3, -1), (4, -1), SZURKE, {"szaggat": "5 3", "sz": 1.2}),
               ((4, -1), (4, 4), SZURKE, {"szaggat": "5 3", "sz": 1.2}),
               ((4, 4), (-3, 4), SZURKE, {"szaggat": "5 3", "sz": 1.2})],
    pontok=[((-3, -1), "A", {"dx": -10, "dy": 14}), ((2, -1), "B", {"dx": 0, "dy": 16}),
            ((4, 2), "C", {"dx": 11, "dy": 4}), ((1, 4), "D", {"dx": 0, "dy": -9}),
            ((-3, 3), "E", {"dx": -11, "dy": 4})],
    leiras="Az ABCDE ötszög a 7-szer 5-ös körülírt téglalapban; a téglalapból három derékszögű "
           "háromszöget vágunk le")
SVG_TER = svg_koordsik(
    xr=(-3, 5), yr=(-2, 6),
    sokszogek=[([(-2, -1), (4, 1), (1, 5)], KEK, {"kitolt": 0.16})],
    szakaszok=[((-2, -1), (4, -1), SZURKE, {"szaggat": "5 3", "sz": 1.2}),
               ((4, -1), (4, 5), SZURKE, {"szaggat": "5 3", "sz": 1.2}),
               ((4, 5), (-2, 5), SZURKE, {"szaggat": "5 3", "sz": 1.2}),
               ((-2, 5), (-2, -1), SZURKE, {"szaggat": "5 3", "sz": 1.2})],
    pontok=[((-2, -1), "A", {"dx": -10, "dy": 14}), ((4, 1), "B", {"dx": 11, "dy": 4}),
            ((1, 5), "C", {"dx": 0, "dy": -9})],
    leiras="Az A(−2;−1), B(4;1), C(1;5) csúcsú háromszög a 6-szor 6-os körülírt négyzetben")
SVG_KOLIN = svg_koordsik(
    xr=(-2, 5), yr=(-4, 8), egyseg=26,
    egyenesek=[((2, -1, -1), SZURKE, "", {"szaggat": "6 4", "sz": 1.4})],
    pontok=[((-1, -3), "A", {"dx": -11, "dy": 2}), ((1, 1), "B", {"dx": 12, "dy": 6}),
            ((4, 7), "C", {"dx": -12, "dy": 0})],
    leiras="Az A(−1;−3), B(1;1) és C(4;7) pont egy egyenesen van")
Q = [(-2, -2), (4, -1), (3, 3), (-1, 4)]
_QP = [((-2, -2), "P", {"dx": -10, "dy": 14}), ((4, -1), "Q", {"dx": 11, "dy": 12}),
       ((3, 3), "R", {"dx": 11, "dy": -4}), ((-1, 4), "S", {"dx": -11, "dy": -4})]
SVG_NEGY = svg_koordsik(
    xr=(-3, 5), yr=(-3, 5),
    sokszogek=[(Q, KEK, {"kitolt": 0.14})],
    szakaszok=[((-2, -2), (3, 3), ZOLD, {"sz": 1.8, "szaggat": "6 4"})],
    pontok=_QP,
    leiras="A PQRS négyszög, a PR átlóval két háromszögre bontva")
SVG_NEGY_ROSSZ = svg_koordsik(
    xr=(-3, 5), yr=(-3, 5),
    sokszogek=[([Q[0], Q[1], Q[3], Q[2]], PIROS, {"kitolt": 0.14})],
    pontok=_QP,
    leiras="Hibás sorrend, P–Q–S–R: a „négyszög” oldalai keresztezik egymást")

# ---------------------------------------------------------------- A1
A1 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Kanrak:</b> Feltörtük Maxi navigációs hálózatát — de ne várjatok térképet. A '
         'rendszer <b>számpárokat</b> mutat: minden drón helye két szám. Tér-eb bármelyik '
         'drón mellé oda tud ugrani, ha pontos koordinátát kap tőlünk. Egyetlen elszámolt '
         'előjel, és a sík rossz negyedében landol. Kezdjük a legelején: hogyan lesz helyből szám?'),
   r'<p>Az <b>analitikus geometria</b> a geometriai alakzatokat számokkal és egyenletekkel írja '
   r'le: a pontból számpár, az egyenesből és a körből egyenlet lesz. A vektoroknál már '
   r'<a href="' + V04 + r'tananyag-koordinatak-terben.html#def-koordinatak">koordinátákkal '
   r'dolgoztál</a> — most visszatérünk a síkba, és pontokkal számolunk.</p>',
 ]),

 ("Pont és számpár", [
   doboz("definicio", "A derékszögű koordináta-rendszer",
         r'<p>Vegyünk fel a síkban két, egymásra <b>merőleges számegyenest</b> közös kezdőponttal és azonos egységgel. '
         r'A közös pont az $O$ <b>origó</b>, a vízszintes számegyenes az $x$-tengely '
         r'(abszcisszatengely), a függőleges az $y$-tengely (ordinátatengely).</p>'
         r'<p>A sík egy $P$ pontjából merőlegest bocsátunk mindkét tengelyre. A talppontokhoz '
         r'tartozó két szám a pont <b>koordinátái</b>: $P(x;y)$, ahol $x$ az <b>első</b> '
         r'koordináta (abszcissza), $y$ a <b>második</b> (ordináta).</p>'
         r'<p>A sík minden pontjához <b>pontosan egy</b> rendezett számpár tartozik, és minden '
         r'rendezett számpárhoz <b>pontosan egy</b> pont. Ezért mondhatjuk röviden, hogy „a '
         r'$(3;2)$ pont”.</p>'
         r'<p>A tengelyek négy <b>síknegyedre</b> osztják a síkot: I. ($x>0$, $y>0$), '
         r'II. ($x<0$, $y>0$), III. ($x<0$, $y<0$), IV. ($x>0$, $y<0$). Az $x$-tengely pontjai '
         r'$(x;0)$, az $y$-tengely pontjai $(0;y)$ alakúak; ezek egyik síknegyedhez sem '
         r'tartoznak.</p>',
         hid="def-koordinatasik"),
   abra(SVG_SIK, 'Az $A(3;2)$ az I., a $B(-2;4)$ a II., a $C(-3;-1)$ a III., a $D(4;-2)$ a IV. '
        'síknegyedben van; az $E(0;-3)$ az $y$-tengelyen. A szaggatott vonalak az $A$ '
        'koordinátáit mutatják.'),
   r'<p><b>Tükörképek.</b> A $P(x;y)$ pont tükörképe az $x$-tengelyre $(x;-y)$, az '
   r'$y$-tengelyre $(-x;y)$, az origóra $(-x;-y)$. Például a $P(3;-2)$ tükörképe az '
   r'$x$-tengelyre $(3;2)$, az $y$-tengelyre $(-3;-2)$, az origóra $(-3;2)$.</p>',
   doboz("erdekesseg", "Hol találkozol vele?",
         r'<p>A sakktábla „e4” mezője, a mozijegy „7. sor 12. szék” adata és a telefonod '
         r'helymeghatározása (földrajzi szélesség és hosszúság) mind ugyanazt teszi: <b>két '
         r'adattal</b> egyértelműen megad egy helyet. A koordináta-rendszer ennek a matematikai '
         r'változata.</p>'),
 ]),

 ("Két pont távolsága", [
   r'<p>Legyen $A(x_1;y_1)$ és $B(x_2;y_2)$ két pont. Vegyük fel a $C(x_2;y_1)$ segédpontot: '
   r'az $AC$ szakasz vízszintes, hossza $|x_2-x_1|$, a $CB$ szakasz függőleges, hossza '
   r'$|y_2-y_1|$. Az $ACB$ háromszög derékszögű, az $AB$ az átfogója — a Pitagorasz-tételből '
   r'megkapjuk a távolságot.</p>',
   abra(SVG_TAV, 'Az $A(-2;5)$ és a $B(6;-1)$ távolsága egy $8$ és $6$ befogójú derékszögű '
        'háromszög átfogója: $d=\\sqrt{8^2+6^2}=10$.'),
   doboz("tetel", "Két pont távolsága",
         r'<p>Az $A(x_1;y_1)$ és a $B(x_2;y_2)$ pont távolsága:</p>'
         r'$$|AB|=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}.$$'
         r'<p>A kivonás sorrendje mindegy, mert a különbségeket négyzetre emeljük. A $P(x;y)$ '
         r'pont távolsága az origótól $\sqrt{x^2+y^2}$.</p>'
         r'<p>Vektorokkal nézve ez az $\overrightarrow{AB}=(x_2-x_1;\,y_2-y_1)$ vektor '
         r'<a href="' + V04 + r'tananyag-koordinatak-terben.html#tetel-hossz">intenzitása</a> (hossza).</p>',
         hid="tetel-tavolsag"),
   r'<p><b>Számolás.</b> Az ábra két pontjára: $|AB|=\sqrt{(6-(-2))^2+(-1-5)^2}='
   r'\sqrt{8^2+(-6)^2}=\sqrt{64+36}=10$. A $P(-5;12)$ pont távolsága az origótól '
   r'$\sqrt{25+144}=13$.</p>',
   doboz("csapda", "Maxi trükkje",
         r'<p>Maxi is kiszámolta az $A(-2;5)$ és a $B(6;-1)$ távolságát, csak kicsit „rövidebbre” '
         r'jött ki:</p>'
         r'$$|AB|=\sqrt{(6-2)^2+(-1-5)^2}=\sqrt{16+36}=\sqrt{52}\approx7{,}21.$$'
         r'<p>A hiba az első zárójelben van: $6-(-2)$ nem $4$, hanem $6+2=8$. <b>Negatív '
         r'koordináta kivonásakor</b> a zárójel és az előjel a legfontosabb — írd ki mindig, '
         r'mielőtt fejben számolsz.</p>'
         r'<p>A másik gyakori hiba, hogy a végén elmarad a gyökvonás. A $100$ nem a távolság, '
         r'hanem a <b>négyzete</b>; a távolság $\sqrt{100}=10$.</p>'),
   kviz(r'Tér-eb az $A(1;1)$ pontból a $B(4;5)$ pontba ugrik. Milyen hosszú az ugrás?',
        ['$5$', '$7$', '$25$', r'$\sqrt7$'], 0,
        jo="✔ √((4 − 1)² + (5 − 1)²) = √(9 + 16) = 5 — légvonalban.",
        nem="✘ A 7 a „lépcsős” út: 3 jobbra, aztán 4 fel. Tér-eb légvonalban ugrik, ez "
            "egy derékszögű háromszög átfogója: √(3² + 4²) = 5."),
 ]),

 ("Felezőpont és osztópont", [
   doboz("tetel", "Szakasz osztópontja és felezőpontja",
         r'<p>Ha a $C$ pont az $AB$ szakaszt $AC:CB=m:n$ arányban osztja ($m,n\gt0$), akkor</p>'
         r'$$C\left(\frac{n\,x_1+m\,x_2}{m+n};\ \frac{n\,y_1+m\,y_2}{m+n}\right).$$'
         r'<p>A súlyozás <b>keresztben</b> történik: az $A$ koordinátái az $n$-nel, a $B$ '
         r'koordinátái az $m$-mel szorzódnak. Ha $m\lt n$, a $C$ az $A$-hoz van közelebb; ha '
         r'$m\gt n$, a $B$-hez.</p>'
         r'<p>A <b>felezőpont</b> az $m=n$ eset — a koordináták átlaga:</p>'
         r'$$F\left(\frac{x_1+x_2}{2};\ \frac{y_1+y_2}{2}\right).$$',
         hid="tetel-osztopont"),
   r'<p><i>Honnan jön?</i> Vektorokkal: $\overrightarrow{AC}=\frac{m}{m+n}\,\overrightarrow{AB}$, '
   r'vagyis a $C$ az $A$-ból az $AB$ vektor $\frac{m}{m+n}$-ed részével tolt pont — ha a '
   r'koordinátákat kiírod, pontosan a fenti képlet jön ki.</p>'
   r'<p><b>Példa.</b> $A(-2;1)$, $B(7;4)$, és $AC:CB=1:2$. Ekkor '
   r'$C\left(\frac{2\cdot(-2)+1\cdot7}{3};\ \frac{2\cdot1+1\cdot4}{3}\right)=C(1;2)$. '
   r'Az $AB$ felezőpontja $F\left(\frac{-2+7}{2};\ \frac{1+4}{2}\right)=F(2{,}5;2{,}5)$.</p>',
   abra(SVG_OSZTO, 'A $C(1;2)$ az $A$-hoz van közelebb: az $AC$ a szakasz harmada. Az '
        '$F(2{,}5;2{,}5)$ a felezőpont.'),
   doboz("pelda", "A paralelogramma negyedik csúcsa",
         r'<p>Az $ABCD$ paralelogramma három egymást követő csúcsa $A(-1;-2)$, $B(4;0)$ és '
         r'$C(6;4)$. Határozd meg a $D$ csúcs koordinátáit!</p>'
         r'<p><b>Ötlet.</b> A paralelogramma átlói <b>felezik egymást</b>, tehát az $AC$ és a '
         r'$BD$ felezőpontja ugyanaz az $M$ pont.</p>',
         hid="pelda-paralelogramma",
         lenyilo=("Megoldás",
                  r'<p>Az $AC$ felezőpontja $M\left(\frac{-1+6}{2};\ \frac{-2+4}{2}\right)='
                  r'M(2{,}5;1)$. Ez a $BD$ felezőpontja is: $\frac{4+x_D}{2}=2{,}5$ és '
                  r'$\frac{0+y_D}{2}=1$, ahonnan $x_D=1$ és $y_D=2$.</p>'
                  r'<p><i>Ellenőrzés: a $BD$ felezőpontja $\left(\frac{4+1}{2};\frac{0+2}{2}\right)'
                  r'=(2{,}5;1)$ ✔.</i></p>'
                  + abra(SVG_PAR, 'Az $ABCD$ paralelogramma és az átlók közös felezőpontja, $M$.') +
                  r'<p class="vegeredmeny">$D(1;2)$</p>')),
   kviz(r'Az $A(0;0)$ és $B(8;0)$ végpontú szakaszon a $C$ pontra $AC:CB=1:3$. Hol van a $C$?',
        [r'$C(2;0)$', r'$C(6;0)$', r'$C(4;0)$', r'$C\left(\tfrac83;0\right)$'], 0,
        jo="✔ Az AC a szakasz negyede: 8 : 4 = 2, tehát C(2; 0) — az A-hoz van közelebb.",
        nem="✘ Az 1 : 3 arányban az AC a rövidebb rész: a szakasz negyede, 2 egység. "
            "A C(6; 0) a felcserélt súlyokból jön — az 3 : 1 arány lenne."),
 ]),

 ("A háromszög súlypontja", [
   r'<p>A háromszög <b>súlyvonala</b> egy csúcsot a szemközti oldal felezőpontjával köti össze. '
   r'A három súlyvonal egy pontban, az $S$ <b>súlypontban</b> metszi egymást, és ez a pont '
   r'mindegyik súlyvonalat $2:1$ arányban osztja — a csúcs felől a hosszabb rész.</p>',
   doboz("tetel", "A súlypont koordinátái",
         r'<p>Az $A(x_1;y_1)$, $B(x_2;y_2)$, $C(x_3;y_3)$ csúcsú háromszög súlypontja</p>'
         r'$$S\left(\frac{x_1+x_2+x_3}{3};\ \frac{y_1+y_2+y_3}{3}\right).$$'
         r'<p>A súlypont tehát a három csúcs koordinátáinak <b>átlaga</b>.</p>',
         hid="tetel-sulypont"),
   doboz("pelda", "Kristály-kamra szimuláció — a drónraj középpontja",
         r'<p>Maxi három drónja egy háromszöget tart: $A(-1;-2)$, $B(7;-2)$ és $C(3;4)$. '
         r'Tér-eb a raj <b>súlypontjába</b> akar ugrani, mert onnan mindhárom drón jelét '
         r'egyszerre zavarhatja.</p>'
         r'<ol type="a"><li>Számítsd ki az $AB$ és az $AC$ oldal hosszát (pontos alakban és két tizedesre kerekítve)!</li>'
         r'<li>Határozd meg az $AB$ oldal $F$ felezőpontját!</li>'
         r'<li>Határozd meg az $S$ súlypontot!</li>'
         r'<li>Milyen hosszú a $C$ csúcsból induló súlyvonal?</li>'
         r'<li>Ellenőrizd, hogy az $S$ a $CF$ súlyvonalat $2:1$ arányban osztja!</li></ol>',
         hid="pelda-dronraj",
         lenyilo=("Megoldás",
                  r'<p><b>a)</b> $|AB|=\sqrt{(7-(-1))^2+(-2-(-2))^2}=\sqrt{64}=8$; '
                  r'$|AC|=\sqrt{(3-(-1))^2+(4-(-2))^2}=\sqrt{16+36}=\sqrt{52}=2\sqrt{13}'
                  r'\approx7{,}21$.</p>'
                  r'<p><b>b)</b> $F\left(\frac{-1+7}{2};\ \frac{-2+(-2)}{2}\right)=F(3;-2)$.</p>'
                  r'<p><b>c)</b> $S\left(\frac{-1+7+3}{3};\ \frac{-2+(-2)+4}{3}\right)=S(3;0)$.</p>'
                  r'<p><b>d)</b> $|CF|=\sqrt{(3-3)^2+(-2-4)^2}=6$.</p>'
                  r'<p><b>e)</b> $|CS|=\sqrt{0^2+(0-4)^2}=4$ és $|SF|=\sqrt{0^2+(-2-0)^2}=2$, '
                  r'tehát $|CS|:|SF|=4:2=2:1$ ✔.</p>'
                  + abra(SVG_DRON, 'A drónraj háromszöge, a $C$-ből induló súlyvonal és a súlypont.') +
                  r'<p class="vegeredmeny">a) $|AB|=8$, $|AC|=2\sqrt{13}\approx7{,}21$ · '
                  r'b) $F(3;-2)$ · c) $S(3;0)$ · d) $6$ · e) $4:2=2:1$</p>')),
   GY(FGY + "#alap-1", "A 1–9", FGY + "#kozep-1", "K 1–5"),
   brief('<b>Kanrak:</b> A drónok helyét már pontosan tudjuk, sőt a raj középpontját is. '
         'De a három drón nem csak áll: <b>zónát zár körül</b>, és ezen a területen belül '
         'minden jelünk elhal. Mekkora ez a zóna — és mi történik, ha a drónok egy vonalba '
         'állnak?', outro=True),
 ]),
]

# ---------------------------------------------------------------- A2
A2 = [
 ("📡 Küldetés-eligazítás", [
   brief('<b>Kanrak:</b> Három drón egy háromszög alakú <b>zárt zónát</b> tart: a területén '
         'belül Tér-eb nem tud teleportálni. Minél nagyobb a zóna, annál több energiát fogyaszt '
         'Maxi rendszere. És itt a töréspont: ha a három drón <b>egy egyenesbe</b> kerül, a '
         'zóna összeomlik. Számoljuk ki a területet — csak a csúcsok koordinátáiból.'),
 ]),

 ("Terület darabolással", [
   r'<p>Ha a csúcsok rácspontokon vannak, képlet nélkül is célba érünk: a sokszöget egy '
   r'tengelyekkel párhuzamos oldalú <b>téglalapba foglaljuk</b>, és a téglalap területéből '
   r'levonjuk a „fölösleges” derékszögű háromszögeket.</p>',
   doboz("pelda", "Ötszög területe a rácson",
         r'<p>Számítsd ki az $A(-3;-1)$, $B(2;-1)$, $C(4;2)$, $D(1;4)$, $E(-3;3)$ csúcsú '
         r'ötszög területét!</p>'
         + abra(SVG_DARAB, 'A körülírt téglalap $7\\times5$-ös; a borostyánszínű háromszögek '
                'nem tartoznak az ötszöghöz.'),
         hid="pelda-darabolas",
         lenyilo=("Megoldás",
                  r'<p>A körülírt téglalap: $-3\le x\le4$ és $-1\le y\le4$, területe '
                  r'$7\cdot5=35$.</p>'
                  r'<p>Levágunk három derékszögű háromszöget: a $B$–$C$ sarokban $\frac{2\cdot3}{2}=3$, '
                  r'a $C$–$D$ sarokban $\frac{2\cdot3}{2}=3$, a $D$–$E$ sarokban '
                  r'$\frac{4\cdot1}{2}=2$. Az $AE$ oldal a téglalap bal oldalán fekszik, ott nem '
                  r'vágunk.</p>'
                  r'<p class="vegeredmeny">$T=35-3-3-2=27$</p>')),
 ]),

 ("A háromszög területe képlettel", [
   r'<p>Ha a csúcsok nem rácspontok, vagy túl nagyok a számok, a darabolás körülményes. '
   r'Ilyenkor egy képlet dolgozik helyettünk — és ismerős eszközt használ: a '
   r'<a href="' + V03 + r'tananyag-determinans.html#tetel-sarrus">harmadrendű determinánst</a>.</p>',
   doboz("tetel", "A háromszög területe a csúcsok koordinátáiból",
         r'<p>Az $A(x_1;y_1)$, $B(x_2;y_2)$, $C(x_3;y_3)$ csúcsú háromszög területe</p>'
         r'$$T=\frac12\,|D|,\qquad D=\begin{vmatrix}x_1&y_1&1\\x_2&y_2&1\\x_3&y_3&1\end{vmatrix}.$$'
         r'<p>A determinánst kifejtve:</p>'
         r'$$D=x_1(y_2-y_3)+x_2(y_3-y_1)+x_3(y_1-y_2).$$'
         r'<p>A $D$ előjele csak a csúcsok körüljárási irányától függ, ezért a területhez '
         r'az <b>abszolút értékét</b> vesszük.</p>',
         hid="tetel-terulet"),
   doboz("pelda", "Ugyanaz a terület kétféleképpen",
         r'<p>Számítsd ki az $A(-2;-1)$, $B(4;1)$, $C(1;5)$ csúcsú háromszög területét '
         r'képlettel, majd ellenőrizd darabolással!</p>'
         + abra(SVG_TER, 'A háromszög a $6\\times6$-os körülírt négyzetben.'),
         hid="pelda-terulet",
         lenyilo=("Megoldás",
                  r'<p><b>Képlettel:</b> $D=-2\cdot(1-5)+4\cdot(5-(-1))+1\cdot(-1-1)='
                  r'8+24-2=30$, tehát $T=\frac12\cdot|30|=15$.</p>'
                  r'<p><b>Darabolással:</b> a körülírt négyzet $6\times6=36$; a három levágott '
                  r'háromszög $\frac{6\cdot2}{2}=6$, $\frac{3\cdot4}{2}=6$ és $\frac{3\cdot6}{2}=9$. '
                  r'$36-6-6-9=15$ ✔.</p>'
                  r'<p class="vegeredmeny">$T=15$</p>')),
   r'<p><i>Vektorokkal nézve</i> ugyanez a $\frac12\left|\overrightarrow{AB}\times\overrightarrow{AC}\right|$ '
   r'képlet, amelyet a <a href="' + V04 + r'tananyag-vektorialis-szorzat.html#tetel-terulet">'
   r'vektoriális szorzatnál</a> láttál (a síkvektorokat $0$ harmadik koordinátával térvektornak '
   r'tekintve): itt $\overrightarrow{AB}=(6;2)$, '
   r'$\overrightarrow{AC}=(3;6)$, és $6\cdot6-2\cdot3=30$.</p>',
   kviz(r'Egy háromszög csúcsaiból $D=-14$ jött ki. Mekkora a háromszög területe?',
        ['$7$', '$-7$', '$14$', 'nincs ilyen háromszög'], 0,
        jo="✔ T = ½·|−14| = 7. A negatív előjel csak azt jelzi, hogy a csúcsokat az "
           "óramutató járásával egyező irányban vettük.",
        nem="✘ A terület sosem negatív, és a D előjele csak a körüljárási irányt mutatja. "
            "T = ½·|D| = ½·14 = 7."),
 ]),

 ("Három pont egy egyenesen", [
   doboz("tetel", "Három pont kollinearitása",
         r'<p>Az $A$, $B$, $C$ pont <b>pontosan akkor</b> van egy egyenesen (kollineáris), ha '
         r'$D=0$ — vagyis ha az általuk meghatározott „háromszög” területe $0$.</p>',
         hid="tetel-kollinearitas"),
   r'<p><b>Példa.</b> $A(-1;-3)$, $B(1;1)$, $C(4;7)$: '
   r'$D=-1\cdot(1-7)+1\cdot(7-(-3))+4\cdot(-3-1)=6+10-16=0$, tehát a három pont egy '
   r'egyenesen van.</p>',
   abra(SVG_KOLIN, 'A három pont egy egyenesre illeszkedik — a „háromszög” összeomlik.'),
   doboz("pelda", "Kristály-kamra szimuláció — hol a harmadik drón?",
         r'<p>Két drón az $A(-1;1)$ és a $B(3;-1)$ pontban áll, a harmadik az $x$-tengellyel párhuzamos, '
         r'$y=3$ egyenes mentén mozog (minden pontjának második koordinátája $3$), vagyis $C(x;3)$. Hol lehet a harmadik drón, ha a zóna területe pontosan $9$?</p>',
         hid="pelda-ismeretlen-csucs",
         lenyilo=("Megoldás",
                  r'<p>$D=-1\cdot(-1-3)+3\cdot(3-1)+x\cdot(1-(-1))=4+6+2x=2x+10$.</p>'
                  r'<p>A terület $9$, tehát $\frac12|2x+10|=9$, azaz $|2x+10|=18$. Két eset van:</p>'
                  r'<ul><li>$2x+10=18$, ahonnan $x=4$;</li>'
                  r'<li>$2x+10=-18$, ahonnan $x=-14$.</li></ul>'
                  r'<p><i>Ellenőrzés: $C(4;3)$ esetén $D=18$, $C(-14;3)$ esetén $D=-18$; mindkettőnél '
                  r'$T=9$ ✔.</i></p>'
                  r'<p class="vegeredmeny">$C(4;3)$ vagy $C(-14;3)$</p>')),
   doboz("csapda", "Maxi trükkje",
         r'<p>Maxi a fenti feladatban a $2x+10=18$ egyenletet oldotta meg, $x=4$-et kapott, és '
         r'büszkén jelentette, hogy megtalálta a drónt. A második lehetséges helyet elnézte: a drón a '
         r'$C(-14;3)$ pontban is lehetett.</p>'
         r'<p>A képletben <b>abszolút érték</b> van, és az $|u|=18$ egyenletnek két megoldása '
         r'van: $u=18$ és $u=-18$. Aki az abszolút értéket elhagyja, vagy negatív területet '
         r'kap, vagy a megoldások felét elveszíti.</p>'),
   kviz(r'Mit jelent, ha három pontra $D=0$?',
        ['a három pont egy egyenesen van', 'a háromszög derékszögű',
         'a csúcsokat rossz sorrendben vettük', 'a háromszög egyik csúcsa az origó'], 0,
        jo="✔ A D = 0 azt jelenti, hogy a „háromszög” területe 0: a pontok egy egyenesen vannak.",
        nem="✘ A D a terület kétszerese (előjellel). Ha 0, akkor nincs valódi háromszög: a "
            "három pont egy egyenesre esik."),
 ]),

 ("A négyszög területe", [
   r'<p>Egy négyszöget egy <b>átlóval</b> két háromszögre bontunk, és a két terület összegét '
   r'vesszük. Ehhez a csúcsokat <b>körüljárási sorrendben</b> kell megadni: $ABCD$ esetén '
   r'a $PR$ és a $QS$ az átló. <i>(Konvex négyszögnél bármelyik átló jó; konkávnál a '
   r'négyszög belsejében futó átlót válaszd.)</i></p>'
   r'<p><b>Példa.</b> $P(-2;-2)$, $Q(4;-1)$, $R(3;3)$, $S(-1;4)$. A $PR$ átló mentén: '
   r'$T_{PQR}=\frac12\cdot|25|=12{,}5$ és $T_{PRS}=\frac12\cdot|25|=12{,}5$, tehát '
   r'$T_{PQRS}=25$.</p>',
   abra(SVG_NEGY, 'A $PQRS$ négyszög a $PR$ átlóval két háromszögre bontva.'),
   r'<p><b>Figyelj a sorrendre!</b> Ha valaki a $P$, $Q$, $S$, $R$ sorrendben köti össze '
   r'ugyanezt a négy pontot, az „oldalak” keresztezik egymást, és az „átló” mentén bontva hibás '
   r'terület jön ki: a $PS$ mentén $30$, a $QR$ mentén $20$, pedig a valódi terület $25$. '
   r'Mielőtt számolsz, rajzold fel a pontokat, és ellenőrizd, hogy a sorrend körbejár-e.</p>',
   abra(SVG_NEGY_ROSSZ, 'Hibás sorrend, P–Q–S–R: a vonal önmagát metszi — ez nem a $PQRS$ négyszög.'),
   doboz("erdekesseg", "Hol találkozol vele?",
         r'<p>A földmérők egy telek területét a sarokpontok koordinátáiból számolják. Bármely '
         r'$n$ csúcsú, nem önmetsző sokszögre működik az úgynevezett <b>Gauss-féle területképlet</b> (angol nevén '
         r'<i>shoelace formula</i>, azaz „cipőfűző-képlet”): körbejárva a csúcsokat</p>'
         r'$$T=\frac12\left|x_1y_2-x_2y_1+x_2y_3-x_3y_2+\dots+x_ny_1-x_1y_n\right|.$$'
         r'<p>Háromszögre ez pontosan a fenti $\frac12|D|$.</p>'),
   GY(FGY + "#alap-10", "A 10–16", FGY + "#kozep-6", "K 6–10"),
   brief('<b>Kanrak:</b> A zónákat lemértük. Maxi drónjai azonban nem ugrálnak ide-oda: '
         '<b>egyenes pályán</b> repülnek. Ha egy pályát egyenlettel le tudunk írni, Tér-eb '
         'bármelyik pontjára odaugorhat, és elvághatja. Irány az egyenesek!', outro=True),
 ]),
]

# ---------------------------------------------------------------- lapok
KI = [
 lap(**T, fajl="tananyag-pontok-a-sikban.html",
     cim="Pontok a síkban — távolság, felezőpont, súlypont",
     cim_tiszta="Pontok a síkban",
     alcim="A derékszögű koordináta-rendszer, két pont távolsága, a szakasz osztópontja és "
           "felezőpontja, a háromszög súlypontja.",
     chip=KUL + " · 1/13", szakaszok=A1,
     elozo=("index.html", "Síkbeli analitikus geometria — témakör"),
     kovetkezo=("tananyag-haromszog-terulete.html", "A háromszög területe")),
 lap(**T, fajl="tananyag-haromszog-terulete.html",
     cim="A háromszög területe koordinátákból",
     cim_tiszta="A háromszög területe",
     alcim="Sokszög területe darabolással, a háromszög területe determinánssal, három pont "
           "kollinearitása és a négyszög területe.",
     chip=KUL + " · 2/13", szakaszok=A2,
     elozo=("tananyag-pontok-a-sikban.html", "Pontok a síkban"),
     kovetkezo=(FGY, "Pontok — feladatok")),
]
for u in KI:
    print("✓", os.path.basename(u))
