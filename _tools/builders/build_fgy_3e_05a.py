# -*- coding: utf-8 -*-
"""3e/05 — 1. feladatgyujtemeny: pontok a sikban (A1-A2).
Horgony-terv: narrativa_05-analitikus-geometria.md · feladat-terkep: terkep_fgy_05-analitikus-geometria.md.
Forras-szamok: 5_Analitikus geometria a sikban/Pont, egyenes/5. Feladatok - Analitikus geometria - I. resz.pdf."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, joker_card, oldal

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import Matrix, sqrt, Rational as Q, symbols, solve, simplify, N, Abs
E = []


def _egyenlo(g, w):
    if isinstance(g, (list, tuple)):
        return len(g) == len(w) and all(_egyenlo(x, y) for x, y in zip(g, w))
    if hasattr(g, "shape"):
        return g.shape == w.shape and all(simplify(x - y) == 0 for x, y in zip(g, w))
    return simplify(g - w) == 0


def chk(n, g, w, tur=None):
    ok = abs(float(N(g)) - float(w)) <= tur if tur is not None else _egyenlo(g, w)
    if not ok:
        E.append((n, g, w))


P = lambda x, y: Matrix([x, y])
tav = lambda a, b: sqrt((a - b).dot(a - b))
fel = lambda a, b: (a + b) / 2
D = lambda a, b, c: (b - a)[0] * (c - a)[1] - (b - a)[1] * (c - a)[0]
T = lambda a, b, c: Abs(D(a, b, c)) / 2


def cipo(pp):
    return Abs(sum(pp[i][0] * pp[(i + 1) % len(pp)][1] - pp[(i + 1) % len(pp)][0] * pp[i][1]
                   for i in range(len(pp)))) / 2


x, y, t, k = symbols("x y t k", real=True)
# alap
chk("a3", [tav(P(7, 10), P(-5, 5)), tav(P(6, -5), P(-2, 1)), tav(P(6, 1), P(2, -1)),
           tav(P(3, -2), P(4, Q(5, 3))), tav(P(1, -4), P(-6, 3))],
    [13, 10, 2*sqrt(5), sqrt(130)/3, 7*sqrt(2)])
chk("a3k1", 2*sqrt(5), 4.47, .005); chk("a3k2", sqrt(130)/3, 3.80, .005); chk("a3k3", 7*sqrt(2), 9.90, .005)
chk("a4", [tav(P(6, -8), P(0, 0)), tav(P(-5, 12), P(0, 0)), tav(P(3, -3), P(0, 0))], [10, 13, 3*sqrt(2)])
chk("a4k", 3*sqrt(2), 4.24, .005)
chk("a5", [fel(P(-6, 4), P(4, -10)), fel(P(8, 9), P(-6, -3)), fel(P(-5, 7), P(3, -2)), fel(P(4, 8), P(-10, 14))],
    [P(-1, -3), P(1, 3), P(-1, Q(5, 2)), P(-3, 11)])
chk("a6", [(P(4, 2) + P(-7, -2) + P(6, -9)) / 3, (P(3, 4) + P(-5, 2) + P(-1, -6)) / 3], [P(1, -3), P(-1, 0)])
A, B = P(-4, 1), P(8, 7)
chk("a7", [A + (B - A) / 3, A + 2*(B - A) / 3, A + 3*(B - A) / 4], [P(0, 3), P(4, 5), P(5, Q(11, 2))])
chk("a8", P(-3, -1) + P(5, -1) - P(3, -4), P(-1, 2))
A, B, C = P(-1, 1), P(5, 1), P(2, 5)
chk("a9", [tav(A, B), tav(B, C), tav(A, C)], [6, 5, 5])
chk("a10", [T(P(-2, 1), P(6, -1), P(5, 4)), T(P(-3, -2), P(5, -1), P(-2, 6)), T(P(-4, 9), P(7, 3), P(-2, 1))],
    [19, Q(63, 2), 38])
chk("a11", [cipo([(3, -1), (6, 5), (-3, 6), (-2, -3)]), cipo([(4, 7), (-1, 4), (-2, -2), (3, 0)])], [52, 30])
chk("a12", [D(P(-7, 1), P(2, -2), P(5, -3)), D(P(0, 1), P(2, 4), P(5, 8))], [0, -1])
chk("a13", cipo([(-3, -2), (3, -2), (4, 1), (0, 4), (-3, 2)]), Q(63, 2))
chk("a14", T(P(0, 0), P(6, 1), P(2, 5)), 14)
A, B, C = P(1, 1), P(5, 1), P(5, 4)
chk("a15", [T(A, B, C), tav(A, C)], [6, 5])
chk("a16", [D(P(0, 0), P(2, 6), P(6, 6)), T(P(0, 0), P(2, 6), P(6, 6))], [-24, 12])
# közép
chk("k1", solve((x - 7)**2 + 16 - (x - 1)**2 - 4, x), [5])
chk("k2", sorted(solve((x + 4)**2 + 25 - 169, x)), [-16, 8])
chk("k3", [2*P(1, 1) - P(-3, 5), 2*P(1, 1) - P(1, 7)], [P(5, -3), P(1, -5)])
A, B, C = P(-7, -3), P(1, -5), P(9, 5)
chk("k4", [tav(A, fel(B, C)), tav(B, fel(A, C)), tav(C, fel(A, B))], [3*sqrt(17), 6, 15])
chk("k4k", 3*sqrt(17), 12.37, .005)
K_, A, B = P(2, 6), P(1, -1), P(-5, 7)
chk("k5", [tav(K_, A)**2, tav(K_, B)**2, fel(A, B)], [50, 50, P(-2, 3)])
chk("k6", sorted(solve(Abs(D(P(-4, -2), P(2, 4), P(-3, y))) - 42, y)), [-8, 6])
chk("k7", sorted(solve(Abs(D(P(-4, 1), P(2, 5), P(0, y))) - 28, y)), [-1, Q(25, 3)])
chk("k8", [s for s in solve(Abs(D(P(-4, 1), P(5, -2), P(-1, y))) - 27, y) if s < 0], [-3])
chk("k9", [s for s in solve(Abs(D(P(1, -3), P(-6, 4), P(x, -1))) - 21, x) if s > 0], [2])
chk("k10", solve(D(P(1, 2), P(3, 6), P(k, 10)), k), [5])
# nehéz
s = solve([tav(P(x, y), P(-1, -3))**2 - tav(P(x, y), P(-4, 6))**2,
           tav(P(x, y), P(-1, -3))**2 - tav(P(x, y), P(3, -1))**2], [x, y], dict=True)
chk("n1", [s[0][x], s[0][y], tav(P(-1, 2), P(3, -1))], [-1, 2, 5])
A, B, C = P(-1, -2), P(-2, 6), P(5, 2)
F_ = fel(A, C)
chk("n2", [tav(A, B)**2, tav(C, B)**2, tav(A, C)**2, F_, tav(F_, B), tav(A, C)*tav(F_, B)/2, T(A, B, C), (A+B+C)/3],
    [65, 65, 52, P(2, 0), 2*sqrt(13), 26, 26, P(Q(2, 3), 2)])
chk("n2k1", sqrt(65), 8.06, .005); chk("n2k2", 2*sqrt(13), 7.21, .005)
A, B, C, D_ = P(-3, -1), P(2, -2), P(4, 3), P(-1, 4)
chk("n3", [fel(A, C), fel(B, D_), cipo([tuple(A), tuple(B), tuple(C), tuple(D_)])], [P(Q(1, 2), 1), P(Q(1, 2), 1), 27])
chk("n4", sorted(solve(Abs(D(P(0, 0), P(6, 0), P(t, t))) - 30, t)), [-5, 5])
chk("n4b", [solve(tav(P(t, t), P(0, 0))**2 - tav(P(t, t), P(6, 0))**2, t), T(P(0, 0), P(6, 0), P(3, 3))], [[3], 9])
# joker: rácspontok a (0;0),(7;0),(0;7) háromszög belsejében
belso = sum(1 for i in range(1, 7) for j in range(1, 7) if i + j < 7)
chk("jok", [belso, cipo([(0, 0), (7, 0), (0, 7)]) - Q(21, 2) + 1], [15, 15])
assert not E, E
print("sympy önteszt: OK")

# ============================== ALAPSZINT ==============================
ALAP = [
 # --- A1: pontok a síkban (alap 1–9)
 (r"Melyik síknegyedben van a pont? Ha koordinátatengelyen van, add meg, melyiken!",
  [r"$A(3;-5)$", r"$B(-2;7)$", r"$C(0;-4)$", r"$D(-6;-1)$", r"$E(5;0)$", r"$F(1;8)$"],
  [r"IV. síknegyed", r"II. síknegyed", r"az $y$-tengelyen", r"III. síknegyed", r"az $x$-tengelyen",
   r"I. síknegyed"], True),

 (r"Add meg a pont tükörképét az $x$-tengelyre, az $y$-tengelyre és az origóra!",
  [r"$P(4;-3)$", r"$Q(-2;5)$"],
  [r"$(4;3)$, $(-4;-3)$, $(-4;3)$", r"$(-2;-5)$, $(2;5)$, $(2;-5)$"], True),

 (r"Számítsd ki a két pont távolságát! A közelítő értéket két tizedesre kerekítsd.",
  [r"$A(7;10)$, $B(-5;5)$", r"$M(6;-5)$, $N(-2;1)$", r"$P(6;1)$, $Q(2;-1)$",
   r"$R(3;-2)$, $S\left(4;\tfrac53\right)$", r"$E(1;-4)$, $F(-6;3)$"],
  [r"$13$", r"$10$", r"$2\sqrt5\approx4{,}47$", r"$\frac{\sqrt{130}}{3}\approx3{,}80$",
   r"$7\sqrt2\approx9{,}90$"]),

 (r"Milyen messze van a pont az origótól?",
  [r"$A(6;-8)$", r"$B(-5;12)$", r"$C(3;-3)$"],
  [r"$10$", r"$13$", r"$3\sqrt2\approx4{,}24$"], True),

 (r"Határozd meg az $AB$ szakasz felezőpontját!",
  [r"$A(-6;4)$, $B(4;-10)$", r"$A(8;9)$, $B(-6;-3)$", r"$A(-5;7)$, $B(3;-2)$", r"$A(4;8)$, $B(-10;14)$"],
  [r"$F(-1;-3)$", r"$F(1;3)$", r"$F\left(-1;\tfrac52\right)$", r"$F(-3;11)$"], True),

 (r"Határozd meg az $ABC$ háromszög $S$ súlypontját!",
  [r"$A(4;2)$, $B(-7;-2)$, $C(6;-9)$", r"$A(3;4)$, $B(-5;2)$, $C(-1;-6)$"],
  [r"$S(1;-3)$", r"$S(-1;0)$"], True),

 (r"Adott az $A(-4;1)$ és a $B(8;7)$ pont. Határozd meg az $AB$ szakasz azon $P$ pontját, amelyre "
  r"$AP:PB$ egyenlő",
  [r"$1:2$;", r"$2:1$;", r"$3:1$!"],
  [r"$P(0;3)$", r"$P(4;5)$", r"$P(5;\,5{,}5)$"], True),

 (r"Az $ABCD$ paralelogramma három egymást követő csúcsa $A(-3;-1)$, $B(3;-4)$ és $C(5;-1)$. "
  r"Határozd meg a $D$ csúcsot!", None, r"$D(-1;2)$"),

 (r"Adott az $A(-1;1)$, $B(5;1)$, $C(2;5)$ csúcsú háromszög.",
  [r"Számítsd ki a háromszög kerületét!", r"Milyen a háromszög az oldalai szerint?"],
  [r"$AB=6$, $BC=5$, $AC=5$, a kerület $K=16$", r"egyenlő szárú ($BC=AC=5$)"]),

 # --- A2: a háromszög területe (alap 10–16)
 (r"Számítsd ki az $ABC$ háromszög területét!",
  [r"$A(-2;1)$, $B(6;-1)$, $C(5;4)$", r"$A(-3;-2)$, $B(5;-1)$, $C(-2;6)$", r"$A(-4;9)$, $B(7;3)$, $C(-2;1)$"],
  [r"$T=19$", r"$T=31{,}5$", r"$T=38$"]),

 (r"Számítsd ki az $ABCD$ négyszög területét! A csúcsok a körüljárás sorrendjében vannak megadva; "
  r"bontsd a négyszöget két háromszögre egy átlóval.",
  [r"$A(3;-1)$, $B(6;5)$, $C(-3;6)$, $D(-2;-3)$", r"$A(4;7)$, $B(-1;4)$, $C(-2;-2)$, $D(3;0)$"],
  [r"$T=52$", r"$T=30$"], True),

 (r"Egy egyenesen vannak-e a pontok? Válaszodat a háromszög-területképlet determinánsával indokold!",
  [r"$M(-7;1)$, $N(2;-2)$, $P(5;-3)$", r"$A(0;1)$, $B(2;4)$, $C(5;8)$"],
  [r"igen, $D=0$", r"nem, $D=-1\ne0$"]),

 (r"Egy telek alaprajzát koordináta-rendszerben rajzolták meg (egy egység $10$ méter). A telek "
  r"ötszög, csúcsai sorban: $(-3;-2)$, $(3;-2)$, $(4;1)$, $(0;4)$, $(-3;2)$. Hány területegység a telek, "
  r"és hány négyzetméter? <i>(Bontsd az ötszöget háromszögekre az egyik csúcsból húzott átlókkal.)</i>", None, r"$31{,}5$ területegység, azaz $3150\ \text{m}^2$"),

 (r"Számítsd ki annak a háromszögnek a területét, amelynek csúcsai az origó, az $A(6;1)$ és a "
  r"$B(2;5)$ pont!", None, r"$T=14$"),

 (r"Adott az $A(1;1)$, $B(5;1)$, $C(5;4)$ pont.",
  [r"Milyen háromszöget alkotnak? Indokold!", r"Számítsd ki a területét kétféleképpen: a befogókból "
   r"és determinánssal!", r"Milyen hosszú az átfogó?"],
  [r"derékszögű: $AB$ vízszintes, $BC$ függőleges, a derékszög $B$-nél van", r"$T=\frac{4\cdot3}{2}=6$, "
   r"és $\frac12|D|=6$", r"$AC=5$"]),

 (r"Maxi kiszámolta az $A(0;0)$, $B(2;6)$, $C(6;6)$ csúcsú háromszög területét: "
  r"$D=2\cdot6-6\cdot6=-24$, „tehát a terület $-12$”. Mit rontott el? Mennyi a helyes terület?", None,
  r"A determináns lehet negatív (a csúcsok körüljárási irányától függ), a terület viszont nem: "
  r"$T=\frac12|D|=12$."),
]

# ============================== KÖZÉPSZINT ==============================
KOZEP = [
 # --- A1 (közép 1–5)
 (r"Határozd meg az $x$-tengelynek azt a pontját, amely egyenlő távolságra van az $M(7;-4)$ és az "
  r"$N(1;-2)$ ponttól!", None, r"$(5;0)$"),

 (r"Határozd meg az $A(x;3)$ pont első koordinátáját úgy, hogy a $B(-4;8)$ ponttól való távolsága "
  r"$13$ legyen!", None, r"$x=8$ vagy $x=-16$"),

 (r"Az $ABCD$ paralelogramma két szomszédos csúcsa $A(-3;5)$ és $B(1;7)$, az átlók metszéspontja "
  r"$M(1;1)$. Határozd meg a másik két csúcsot!", None, r"$C(5;-3)$, $D(1;-5)$"),

 (r"Az $ABC$ háromszög csúcsai $A(-7;-3)$, $B(1;-5)$ és $C(9;5)$. Számítsd ki a súlyvonalak hosszát!",
  None, r"$t_a=3\sqrt{17}\approx12{,}37$, $t_b=6$, $t_c=15$"),

 (r"Maxi szerint a $K(2;6)$ pont az $A(1;-1)$ és a $B(-5;7)$ pont által meghatározott szakasz "
  r"felezőpontja, „hiszen mindkét ponttól ugyanolyan messze van”. Ellenőrizd a távolságokat! Igaza van?",
  None, r"$KA=KB=\sqrt{50}$, de Maxinak nincs igaza: a felezőpont $F(-2;3)$. Az egyenlő távolság nem "
  r"elég, a pontnak a szakaszon is rajta kell lennie."),

 # --- A2 (közép 6–10)
 (r"Az $ABC$ háromszög két csúcsa $A(-4;-2)$ és $B(2;4)$, a harmadik $C(-3;y)$. Határozd meg a $C$ "
  r"csúcsot, ha a háromszög területe $21$!", None, r"$C(-3;6)$ vagy $C(-3;-8)$"),

 (r"A $PQR$ háromszög két csúcsa $P(-4;1)$ és $Q(2;5)$. A harmadik csúcs az $y$-tengelyen van, és a "
  r"háromszög területe $14$. Határozd meg az $R$ csúcsot!", None,
  r"$R(0;-1)$ vagy $R\left(0;\tfrac{25}{3}\right)$"),

 (r"Az $ABC$ háromszög csúcsai $A(-4;1)$, $B(5;-2)$ és $C(-1;y)$, ahol $y\lt0$. Határozd meg a $C$ "
  r"csúcsot, ha a háromszög területe $13{,}5$!", None, r"$C(-1;-3)$"),

 (r"Az $ABC$ háromszög csúcsai $A(1;-3)$, $B(-6;4)$ és $C(x;-1)$, ahol $x\gt0$. Határozd meg a $C$ "
  r"csúcsot, ha a háromszög területe $10{,}5$!", None, r"$C(2;-1)$"),

 (r"Az $A(1;2)$, $B(3;6)$ és $C(k;10)$ pont egy egyenesen van. Határozd meg $k$ értékét!", None,
  r"$k=5$"),
]

# ============================== NEHÉZ ==============================
NEHEZ = [
 (r"Határozd meg azt az $M$ pontot, amely egyenlő távolságra van az $A(-1;-3)$, a $B(-4;6)$ és a "
  r"$C(3;-1)$ ponttól! Mekkora ez a távolság? <i>(Két egyenletet kapsz: $MA=MB$ és $MA=MC$.)</i>", None,
  r"$M(-1;2)$, a távolság $5$ (ez a háromszög köré írt körének középpontja)"),

 (r"Adott az $A(-1;-2)$, $B(-2;6)$, $C(5;2)$ csúcsú háromszög.",
  [r"Mutasd meg, hogy a háromszög egyenlő szárú! Melyik az alapja?",
   r"Határozd meg az alap $F$ felezőpontját és az alaphoz tartozó magasság hosszát!",
   r"Számítsd ki a területet kétféleképpen: az alapból és a magasságból, illetve determinánssal!",
   r"Határozd meg a súlypontot!"],
  [r"$AB=CB=\sqrt{65}\approx8{,}06$, az alap $AC=2\sqrt{13}$", r"$F(2;0)$, $m_b=FB=2\sqrt{13}\approx7{,}21$",
   r"$T=\frac{2\sqrt{13}\cdot2\sqrt{13}}{2}=26$, és $\frac12|D|=26$", r"$S\left(\tfrac23;2\right)$"]),

 (r"Adott az $A(-3;-1)$, $B(2;-2)$, $C(4;3)$ és $D(-1;4)$ pont.",
  [r"Mutasd meg, hogy az $ABCD$ négyszög paralelogramma! <i>(Felezik-e egymást az átlók?)</i>",
   r"Számítsd ki a paralelogramma területét!"],
  [r"az $AC$ és a $BD$ felezőpontja egyaránt $\left(\tfrac12;1\right)$, tehát paralelogramma",
   r"$T=27$ (két egybevágó háromszög: $2\cdot13{,}5$)"]),

 (r"Az $ABC$ háromszög csúcsai $A(0;0)$, $B(6;0)$ és $C(t;t)$, ahol $t\ne0$.",
  [r"Határozd meg $t$ értékét úgy, hogy a háromszög területe $15$ legyen!",
   r"Határozd meg $t$ értékét úgy, hogy a háromszög egyenlő szárú legyen, $AC=BC$ szárakkal!",
   r"Mekkora ekkor a háromszög területe?"],
  [r"$t=5$ vagy $t=-5$: $C(5;5)$ vagy $C(-5;-5)$", r"$2t^2=(t-6)^2+t^2$, tehát $t=3$: $C(3;3)$", r"$T=9$"]),
]

JOKER = (r"Rácspontnak nevezzük azokat a pontokat, amelyeknek mindkét koordinátája egész szám. "
         r"Pick tétele szerint egy rácspont-csúcsú sokszög területe $T=b+\frac h2-1$, ahol $b$ a sokszög "
         r"belsejében, $h$ a határán lévő rácspontok száma.",
         [r"$T=24{,}5$", r"$h=21$ (mindhárom oldalon $7$ új rácspont)",
          r"$24{,}5=b+10{,}5-1$, tehát $b=15$ — és valóban, összeszámolva is $5+4+3+2+1=15$"],
         [r"Mekkora a $(0;0)$, $(7;0)$, $(0;7)$ csúcsú háromszög területe?",
          r"Hány rácspont van a határán?", r"Hány rácspont van a belsejében?"])

# ============================== OLDAL ==============================
body = [
 '    <h2 id="alap">🟢 Alapszint — Különleges fokozat</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — Királyi Gárda</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint — Kristály-protokoll</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1], JOKER[2]),
]
assert (len(ALAP), len(KOZEP), len(NEHEZ)) == (16, 10, 4), (len(ALAP), len(KOZEP), len(NEHEZ))

ut = oldal(tagozat="3e", mappa="05-analitikus-geometria", fajl="feladatok-pontok.html",
           cim="Pontok", temakor="Síkbeli analitikus geometria",
           alcim="Pontok a koordináta-síkon: távolság, felezőpont, súlypont, osztópont és a háromszög "
                 "területe. Számológép használható: a szögeket egy, minden más közelítő értéket két "
                 "tizedesre kerekíts. A végeredmény minden feladatnál lenyitható — előbb számolj, csak "
                 "utána nézd meg!",
           sections_html="\n".join(body),
           prev="tananyag-haromszog-terulete.html", prevc="A háromszög területe",
           nxt="tananyag-egyenes-egyenlete.html", nxtc="Az egyenes egyenlete")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP),
      "Nehéz", len(NEHEZ), "+ Joker")
