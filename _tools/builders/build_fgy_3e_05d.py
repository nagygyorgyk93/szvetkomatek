# -*- coding: utf-8 -*-
"""3e/05 — 4. feladatgyujtemeny: ellipszis es hiperbola (D1-D4).
Horgony-terv: narrativa_05-analitikus-geometria.md · feladat-terkep: terkep_fgy_05-analitikus-geometria.md.
Forras-szamok: 6. Feladatok - Analitikus geometria - II. resz.pdf (17-45).
Felmero-utkozes miatt uj szamok: 18a-b, 20, 23 helyett 24, 30b, 32a, 19a helyett 19c, joker."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fgy_common import cards, joker_card, oldal

# ============================== ÖNELLENŐRZÉS ==============================
from sympy import sqrt, Rational as Q, symbols, solve, simplify, N, expand, Poly, Abs
E = []


def _egyenlo(g, w):
    if isinstance(g, (list, tuple)):
        return len(g) == len(w) and all(_egyenlo(a, b) for a, b in zip(g, w))
    return simplify(g - w) == 0


def chk(nev, g, w, tur=None):
    ok = abs(float(N(g)) - float(w)) <= tur if tur is not None else _egyenlo(g, w)
    if not ok:
        E.append((nev, g, w))


x, y, n, p, m = symbols("x y n p m", real=True)


def metsz(g, l):
    s = solve([g, l], [x, y], dict=True)
    return sorted([(r[x], r[y]) for r in s if r[x].is_real and r[y].is_real],
                  key=lambda u: (float(N(u[0])), float(N(u[1]))))


def hur(pp):
    return sqrt((pp[0][0] - pp[1][0])**2 + (pp[0][1] - pp[1][1])**2)


def rajta(g, pt):
    return simplify(g.subs({x: pt[0], y: pt[1]})) == 0


def aranyos(p1, p2):
    """ket polinom (x-ben) skalarszorosa-e egymasnak"""
    a, b = Poly(expand(p1), x).all_coeffs(), Poly(expand(p2), x).all_coeffs()
    return len(a) == len(b) and all(simplify(a[i] * b[j] - a[j] * b[i]) == 0 for i in range(len(a)) for j in range(len(a)))


def felt(g, k, par):
    """y = kx + par behelyettesitve: (masodfoku polinom, D=0 megoldasai)"""
    e = expand(g.subs(y, k * x + par))
    A2, B2, C2 = Poly(e, x).all_coeffs()
    return e, sorted(solve(B2**2 - 4 * A2 * C2, par), key=lambda u: float(N(u)))


# --- alap: D1
def ell(a2, b2):
    return (sqrt(a2), sqrt(b2), sqrt(a2 - b2))


def hip(a2, b2):
    return (sqrt(a2), sqrt(b2), sqrt(a2 + b2))


chk("a1", [ell(4, 1), ell(5, 3), ell(16, 1), ell(16, 9)],
    [(2, 1, sqrt(3)), (sqrt(5), sqrt(3), sqrt(2)), (4, 1, sqrt(15)), (4, 3, sqrt(7))])
chk("a2", [(36, 4), (8 + 1, 8), (20, 20 - 16)], [(36, 4), (9, 8), (20, 4)])
assert expand(36 * (x**2/36 + y**2/4 - 1)) == x**2 + 9*y**2 - 36
assert expand(72 * (x**2/9 + y**2/8 - 1)) == 8*x**2 + 9*y**2 - 72
assert expand(20 * (x**2/20 + y**2/4 - 1)) == x**2 + 5*y**2 - 20
chk("a3", sqrt(289 - 225), 8)
chk("a4", [4*a**2 + 9*b**2 for a, b in [(3, 2), (4, 1), (-3, -2), (0, 2)]], [72, 73, 72, 36])
chk("a6", sqrt(5**2 - 3**2), 4)
# D2
E7 = x**2 + 2*y**2 - 18
chk("a7", [metsz(E7, x - y - 3), metsz(E7, x + y - 8), metsz(E7, 2*x - y + 9)], [[(0, -3), (4, 1)], [], [(-4, 1)]])
E29 = x**2 + 16*y**2 - 80
assert rajta(E29, (-8, 1)) and metsz(E29, x - 2*y + 10) == [(-8, 1)]
E30 = x**2 + 4*y**2 - 25
assert rajta(E30, (-3, 2)) and metsz(E30, -3*x + 8*y - 25) == [(-3, 2)]
E10 = x**2/36 + y**2/16 - 1
chk("a10", [metsz(E10, y - 4), metsz(E10, y - 5), metsz(E10, x - 6), len(metsz(E10, y - 2))], [[(0, 4)], [], [(6, 0)], 2])
# D3
chk("a11", [hip(100, 25), hip(25, 16), hip(4, 4), hip(4, Q(16, 9))],
    [(10, 5, 5*sqrt(5)), (5, 4, sqrt(41)), (2, 2, 2*sqrt(2)), (2, Q(4, 3), 2*sqrt(13)/3)])
chk("a12", [13 - 4, 9 - 4, 16 - 10], [9, 5, 6])
assert expand(36 * (x**2/4 - y**2/9 - 1)) == 9*x**2 - 4*y**2 - 36
assert expand(20 * (x**2/5 - y**2/4 - 1)) == 4*x**2 - 5*y**2 - 20
assert expand(30 * (x**2/10 - y**2/6 - 1)) == 3*x**2 - 5*y**2 - 30
chk("a13", [sqrt(4)/sqrt(25), sqrt(4)/sqrt(4), sqrt(4)/sqrt(9)], [Q(2, 5), 1, Q(2, 3)])
chk("a14", [a**2 - 4*b**2 for a, b in [(4, 1), (5, 2), (-4, 1), (2*sqrt(3), 0)]], [12, 9, 12, 12])
chk("a16", [sqrt(36 + 64), Q(8, 6)], [10, Q(4, 3)])
# D4
H34 = 4*x**2 - 5*y**2 - 20
chk("a17", [metsz(H34, 2*x + 5*y - 10), metsz(H34, 3*x + y - 3), metsz(H34, 2*x + y + 4)],
    [[(-5, 4), (Q(5, 2), 1)], [], [(Q(-5, 2), 1)]])
H43 = 3*x**2 - 4*y**2 - 12
assert rajta(H43, (-4, 3)) and metsz(H43, x + y + 1) == [(-4, 3)]
H44 = 2*x**2 - 5*y**2 - 30
assert rajta(H44, (-5, -2)) and metsz(H44, x - y + 3) == [(-5, -2)]
chk("a20", metsz(x**2 - 4*y**2 - 4, y - x/2 - 2), [(Q(-5, 2), Q(3, 4))])
# --- közép
assert rajta(2*x**2 + 3*y**2 - 56, (2, -4)) and rajta(2*x**2 + 3*y**2 - 56, (-1, 3*sqrt(2)))
assert rajta(x**2 + 4*y**2 - 100, (6, 4)) and rajta(x**2 + 4*y**2 - 100, (-8, 3))
chk("k3", [36 + 64, 49 - 25], [100, 24])
M5 = metsz(x**2 + 3*y**2 - 12, x + y - 2); chk("k5", [M5, hur(M5)], [[(0, 2), (3, -1)], 3*sqrt(2)])
M6 = metsz(x**2 + 4*y**2 - 40, x - 2*y + 4); chk("k6", [M6, hur(M6)], [[(-6, -1), (2, 3)], 4*sqrt(5)])
chk("k56", [3*sqrt(2), 4*sqrt(5)], [sqrt(18), sqrt(80)])
chk("k5k", 3*sqrt(2), 4.24, .005); chk("k6k", 4*sqrt(5), 8.94, .005)
E7k = x**2/18 + y**2/8 - 1
assert rajta(E7k, (3, -2)) and metsz(E7k, 2*x - 3*y - 12) == [(3, -2)]
M8 = metsz(x**2/4 + y**2 - 1, y - x/2); chk("k8", hur(M8), sqrt(10)); chk("k8k", sqrt(10), 3.16, .005)
assert all(rajta(x**2 - 4*y**2 - 40, pt) for pt in [(7, Q(-3, 2)), (11, Q(9, 2))])
assert all(rajta(7*x**2 - 4*y**2 - 12, pt) for pt in [(2, 2), (4, 5)])
chk("k12", [solve(a2 + 4*a2 - 45, a2) for a2 in [symbols("a2")]], [[9]])
M13 = metsz(9*x**2 - y**2 - 144, x - y + 4); chk("k13", [M13, hur(M13)], [[(-4, 0), (5, 9)], 9*sqrt(2)])
M14 = metsz(3*x**2 - 4*y**2 - 8, x + 2*y - 4); chk("k14", [M14, hur(M14)], [[(-6, 5), (2, 1)], 4*sqrt(5)])
chk("k13k", 9*sqrt(2), 12.73, .005)
H15 = x**2/5 - y**2/4 - 1
assert rajta(H15, (Q(5, 2), -1)) and metsz(H15, 2*x + y - 4) == [(Q(5, 2), -1)]
H45 = 3*x**2 - 4*y**2 - 8
M16 = metsz(H45, y - x + 1)
chk("k16", M16, [(2, 1), (6, 5)])
assert metsz(H45, 3*x - 2*y - 4) == [(2, 1)] and metsz(H45, 9*x - 10*y - 4) == [(6, 5)]
# --- nehéz (érintési feltétel, bontva)
e1, s1 = felt(2*x**2 + 9*y**2 - 54, Q(5, 3), n)
chk("n1", s1, [-9, 9]); assert aranyos(e1, 9*x**2 + 10*n*x + 3*n**2 - 18)
chk("n1f", 27*Q(25, 9) + 6, 81); assert metsz(2*x**2 + 9*y**2 - 54, 5*x - 3*y + 27) == [(-5, Q(2, 3))]
e2, s2 = felt(x**2 + 4*y**2 - 40, Q(-3, 2), n)
chk("n2", s2, [-10, 10]); assert aranyos(e2, 5*x**2 - 6*n*x + 2*n**2 - 20)
e3, s3 = felt(x**2 + 2*y**2 - 12, Q(-1, 2), p / 2)
s3 = sorted(solve(Poly(e3, x).all_coeffs()[1]**2 - 4*Poly(e3, x).all_coeffs()[0]*Poly(e3, x).all_coeffs()[2], p))
chk("n3", s3, [-6, 6]); assert aranyos(e3, 3*x**2 - 2*p*x + p**2 - 24)
e4, s4 = felt(x**2 - 12*y**2 - 36, Q(1, 3), n)
chk("n4", s4, [-1, 1]); assert aranyos(e4, x**2 + 24*n*x + 36*n**2 + 108)
e5, s5 = felt(x**2 - 2*y**2 - 14, 2, -m)
s5 = sorted(solve(Poly(e5, x).all_coeffs()[1]**2 - 4*Poly(e5, x).all_coeffs()[0]*Poly(e5, x).all_coeffs()[2], m))
chk("n5", s5, [-7, 7]); assert aranyos(e5, 7*x**2 - 8*m*x + 2*m**2 + 14)
chk("n6", metsz(x**2 - 9*y**2 - 9, x - 3*y + 6), [(Q(-15, 4), Q(3, 4))])
assert expand((3*y - 6)**2 - 9*y**2 - 9) == -36*y + 27
# joker
J = metsz(x**2/20 + y**2/4 - 1, x**2/4 - y**2/12 - 1)
chk("jok", [len(J), J[-1], 20 - 4, 4 + 12, 4*sqrt(5)*sqrt(3)], [4, (sqrt(5), sqrt(3)), 16, 16, 4*sqrt(15)])
chk("jokk", 4*sqrt(15), 15.49, .005)
assert not E, E
print("sympy önteszt: OK")

# ============================== ALAPSZINT ==============================
ALAP = [
 # --- D1: az ellipszis (alap 1–6)
 (r"Határozd meg az ellipszis féltengelyeit és lineáris excentricitását!",
  [r"$\dfrac{x^2}{4}+y^2=1$", r"$\dfrac{x^2}{5}+\dfrac{y^2}{3}=1$", r"$x^2+16y^2=16$", r"$9x^2+16y^2=144$"],
  [r"$a=2$, $b=1$, $e=\sqrt3$", r"$a=\sqrt5$, $b=\sqrt3$, $e=\sqrt2$", r"$a=4$, $b=1$, $e=\sqrt{15}$",
   r"$a=4$, $b=3$, $e=\sqrt7$"], True),

 (r"Írd fel az ellipszis kanonikus egyenletét a megadott adatokból!",
  [r"$a=6$, $b=2$", r"$b=2\sqrt2$, $e=1$", r"$a=2\sqrt5$, $e=4$"],
  [r"$\dfrac{x^2}{36}+\dfrac{y^2}{4}=1$", r"$\dfrac{x^2}{9}+\dfrac{y^2}{8}=1$", r"$\dfrac{x^2}{20}+\dfrac{y^2}{4}=1$"], True),

 (r"Adott az $\dfrac{x^2}{289}+\dfrac{y^2}{225}=1$ ellipszis. Határozd meg a lineáris excentricitását és a "
  r"fókuszpontjait!", None, r"$e=8$, $F_1(8;0)$ és $F_2(-8;0)$"),

 (r"Rajta van-e a pont a $4x^2+9y^2=72$ ellipszisen? Ha nincs, belül vagy kívül van?",
  [r"$A(3;2)$", r"$B(4;1)$", r"$C(-3;-2)$", r"$D(0;2)$"],
  [r"rajta", r"nincs, kívül ($73\gt72$)", r"rajta", r"nincs, belül ($36\lt72$)"], True),

 (r"Egy origó középpontú, $x$-tengelyen fekvő fókuszú ellipszis nagytengelye $10$, kistengelye $4$ egység. "
  r"Írd fel az egyenletét!", None, r"$\dfrac{x^2}{25}+\dfrac{y^2}{4}=1$"),

 (r"Egy kertész így jelöl ki ellipszis alakú virágágyást: két cöveket $6$ méterre ver le egymástól, egy "
  r"$10$ méteres zsinór két végét a cövekekhez köti, és a kifeszített zsinór mentén körbe rajzol.",
  [r"Az ellipszis mely adatainak felel meg a zsinór hossza és a cövekek távolsága?",
   r"Írd fel az ellipszis egyenletét, ha a cövekek az $x$-tengelyen, az origóra szimmetrikusan állnak!",
   r"Milyen hosszú és milyen széles lesz a virágágyás?"],
  [r"a zsinór $2a=10$, a cövekek távolsága $2e=6$", r"$\dfrac{x^2}{25}+\dfrac{y^2}{16}=1$",
   r"$10$ m hosszú és $8$ m széles"]),

 # --- D2: az ellipszis és az egyenes (alap 7–10)
 (r"Határozd meg az $x^2+2y^2=18$ ellipszis és az $l$ egyenes kölcsönös helyzetét! Ha van közös pontjuk, "
  r"add meg.",
  [r"$l\colon x-y-3=0$", r"$l\colon x+y-8=0$", r"$l\colon 2x-y+9=0$"],
  [r"szelő: $(4;1)$ és $(0;-3)$", r"nincs közös pontjuk", r"érintő: $(-4;1)$"]),

 (r"Írd fel az $x^2+16y^2=80$ ellipszis érintőjének egyenletét az $A(-8;1)$ pontjában!", None, r"$x-2y+10=0$"),

 (r"Az $x^2+4y^2=25$ ellipszis $M$ pontjának első koordinátája $-3$, a második pozitív. Határozd meg $M$-et, és "
  r"írd fel az ellipszis érintőjét $M$-ben!", None, r"$M(-3;2)$, az érintő $-3x+8y=25$, azaz $3x-8y+25=0$"),

 (r"Hány közös pontja van az $\dfrac{x^2}{36}+\dfrac{y^2}{16}=1$ ellipszisnek és az egyenesnek? Ha egy "
  r"van, add meg!",
  [r"$y=4$", r"$y=5$", r"$x=6$", r"$y=2$"],
  [r"egy: $(0;4)$, érintő", r"nincs", r"egy: $(6;0)$, érintő", r"kettő, szelő"], True),

 # --- D3: a hiperbola (alap 11–16)
 (r"Határozd meg a hiperbola valós és képzetes féltengelyét, valamint lineáris excentricitását!",
  [r"$x^2-4y^2=100$", r"$16x^2-25y^2=400$", r"$x^2-y^2=4$", r"$4x^2-9y^2=16$"],
  [r"$a=10$, $b=5$, $e=5\sqrt5$", r"$a=5$, $b=4$, $e=\sqrt{41}$", r"$a=2$, $b=2$, $e=2\sqrt2$",
   r"$a=2$, $b=\tfrac43$, $e=\tfrac{2\sqrt{13}}{3}$"]),

 (r"Írd fel a hiperbola kanonikus egyenletét a megadott adatokból!",
  [r"$a=2$, $e=\sqrt{13}$", r"$b=2$, $e=3$", r"$a=\sqrt{10}$, $e=4$"],
  [r"$\dfrac{x^2}{4}-\dfrac{y^2}{9}=1$", r"$\dfrac{x^2}{5}-\dfrac{y^2}{4}=1$", r"$\dfrac{x^2}{10}-\dfrac{y^2}{6}=1$"], True),

 (r"Írd fel a hiperbola aszimptotáinak egyenletét!",
  [r"$\dfrac{x^2}{25}-\dfrac{y^2}{4}=1$", r"$x^2-y^2=4$", r"$\dfrac{x^2}{9}-\dfrac{y^2}{4}=1$"],
  [r"$y=\pm\tfrac25x$", r"$y=\pm x$", r"$y=\pm\tfrac23x$"], True),

 (r"Rajta van-e a pont az $x^2-4y^2=12$ hiperbolán?",
  [r"$A(4;1)$", r"$B(5;2)$", r"$C(-4;1)$", r"$D\left(2\sqrt3;0\right)$"],
  [r"igen", r"nem ($9\ne12$)", r"igen", r"igen"], True),

 (r"Milyen görbe egyenlete?",
  [r"$\dfrac{x^2}{9}+\dfrac{y^2}{4}=1$", r"$\dfrac{x^2}{9}-\dfrac{y^2}{4}=1$", r"$x^2+y^2=9$", r"$y^2=9x$",
   r"$4x^2-y^2=4$"],
  [r"ellipszis", r"hiperbola", r"kör", r"parabola", r"hiperbola"], True),

 (r"Adott az $\dfrac{x^2}{36}-\dfrac{y^2}{64}=1$ hiperbola. Határozd meg a lineáris excentricitását, a "
  r"fókuszpontjait és az aszimptotáit!", None, r"$e=10$; $F_1(10;0)$, $F_2(-10;0)$; $y=\pm\tfrac43x$"),

 # --- D4: a hiperbola és az egyenes (alap 17–20)
 (r"Határozd meg a $4x^2-5y^2=20$ hiperbola és az $l$ egyenes kölcsönös helyzetét! Ha van közös pontjuk, add meg.",
  [r"$l\colon 2x+5y-10=0$", r"$l\colon 3x+y-3=0$", r"$l\colon 2x+y+4=0$"],
  [r"szelő: $(-5;4)$ és $\left(\tfrac52;1\right)$", r"nincs közös pontjuk", r"érintő: $\left(-\tfrac52;1\right)$"]),

 (r"Írd fel a $3x^2-4y^2=12$ hiperbola érintőjének egyenletét az $A(-4;3)$ pontjában!", None, r"$x+y+1=0$"),

 (r"A $2x^2-5y^2=30$ hiperbola $M$ pontjának első koordinátája $-5$, a második negatív. Határozd meg $M$-et, "
  r"és írd fel a hiperbola érintőjét $M$-ben!", None, r"$M(-5;-2)$, az érintő $x-y+3=0$"),

 (r"Hány közös pontja van az $x^2-4y^2=4$ hiperbolának és az $y=\tfrac12x+2$ egyenesnek? Érintő-e az egyenes?",
  None, r"egy közös pont: $\left(-\tfrac52;\tfrac34\right)$; nem érintő, mert párhuzamos az $y=\tfrac12x$ "
  r"aszimptotával, és átmetszi a görbét"),
]

# ============================== KÖZÉPSZINT ==============================
KOZEP = [
 # --- D1 (közép 1–4)
 (r"Írd fel annak az ellipszisnek az egyenletét, amely átmegy a $P(2;-4)$ és a $Q\left(-1;3\sqrt2\right)$ ponton!",
  None, r"$2x^2+3y^2=56$, azaz $\dfrac{x^2}{28}+\dfrac{y^2}{\frac{56}{3}}=1$"),

 (r"Írd fel annak az ellipszisnek az egyenletét, amely átmegy az $M(6;4)$ és az $N(-8;3)$ ponton!", None,
  r"$\dfrac{x^2}{100}+\dfrac{y^2}{25}=1$"),

 (r"Egy ellipszis fókuszai $F_1(8;0)$ és $F_2(-8;0)$, egyik csúcspontja $(0;6)$. Írd fel az egyenletét!", None,
  r"$\dfrac{x^2}{100}+\dfrac{y^2}{36}=1$"),

 (r"Egy ellipszis fókuszai $F_1(5;0)$ és $F_2(-5;0)$. Az ellipszis egyik pontja az egyik fókusztól $3$, a másiktól "
  r"$11$ egységre van. Írd fel az ellipszis egyenletét!", None,
  r"$2a=14$, $a=7$, $b^2=24$: $\dfrac{x^2}{49}+\dfrac{y^2}{24}=1$"),

 # --- D2 (közép 5–8)
 (r"Milyen hosszú húrt metsz ki az $x^2+3y^2=12$ ellipszis az $x+y-2=0$ egyenesből?", None,
  r"a metszéspontok $(0;2)$ és $(3;-1)$, a húr $3\sqrt2\approx4{,}24$"),

 (r"Milyen hosszú húrt metsz ki az $x^2+4y^2=40$ ellipszis az $x-2y+4=0$ egyenesből?", None,
  r"a metszéspontok $(-6;-1)$ és $(2;3)$, a húr $4\sqrt5\approx8{,}94$"),

 (r"Az $\dfrac{x^2}{18}+\dfrac{y^2}{8}=1$ ellipszis $M$ pontjának első koordinátája $3$, a második negatív. "
  r"Írd fel az ellipszis érintőjét $M$-ben!", None, r"$M(3;-2)$, az érintő $2x-3y-12=0$"),

 (r"Egy $4$ m hosszú és $2$ m széles, ellipszis alakú tárgyalóasztalra díszcsíkot ragasztanak. A csík átmegy "
  r"az asztal középpontján, az asztal hosszanti tengelyével $\varphi$ szöget zár be "
  r"($\operatorname{tg}\varphi=\tfrac12$), és az asztal egyik szélétől a másikig tart. Milyen hosszú a csík? <i>(Az asztal széle az $\frac{x^2}{4}+y^2=1$ ellipszis, "
  r"a csík az $y=\frac12x$ egyenesen van.)</i>", None, r"$\sqrt{10}\approx3{,}16$ m"),

 # --- D3 (közép 9–12)
 (r"Írd fel annak a hiperbolának az egyenletét, amely átmegy a $P\left(7;-\tfrac32\right)$ és a "
  r"$Q\left(11;\tfrac92\right)$ ponton!", None, r"$x^2-4y^2=40$, azaz $\dfrac{x^2}{40}-\dfrac{y^2}{10}=1$"),

 (r"Írd fel annak a hiperbolának az egyenletét, amely átmegy a $K(2;2)$ és az $L(4;5)$ ponton!", None,
  r"$7x^2-4y^2=12$, azaz $\dfrac{x^2}{\frac{12}{7}}-\dfrac{y^2}{3}=1$"),

 (r"Egy hiperbola valós tengelyének hossza $2$, aszimptotái az $y=\pm\sqrt2\,x$ egyenesek. Írd fel az egyenletét!",
  None, r"$x^2-\dfrac{y^2}{2}=1$"),

 (r"Egy hiperbola fókuszai $F_{1,2}\left(\pm3\sqrt5;0\right)$, aszimptotái az $y=\pm2x$ egyenesek. Írd fel az "
  r"egyenletét!", None, r"$\dfrac{x^2}{9}-\dfrac{y^2}{36}=1$"),

 # --- D4 (közép 13–16)
 (r"Milyen hosszú húrt metsz ki a $9x^2-y^2=144$ hiperbola az $x-y+4=0$ egyenesből?", None,
  r"a metszéspontok $(-4;0)$ és $(5;9)$, a húr $9\sqrt2\approx12{,}73$"),

 (r"Milyen hosszú húrt metsz ki a $3x^2-4y^2=8$ hiperbola az $x+2y-4=0$ egyenesből?", None,
  r"a metszéspontok $(-6;5)$ és $(2;1)$, a húr $4\sqrt5\approx8{,}94$"),

 (r"Az $\dfrac{x^2}{5}-\dfrac{y^2}{4}=1$ hiperbola $M$ pontjának második koordinátája $-1$, az első pozitív. "
  r"Írd fel a hiperbola érintőjét $M$-ben!", None, r"$M\left(\tfrac52;-1\right)$, az érintő $2x+y-4=0$"),

 (r"Határozd meg a $3x^2-4y^2=8$ hiperbola és az $y=x-1$ egyenes metszéspontjait, majd írd fel a hiperbola "
  r"érintőit ezekben a pontokban!", None,
  r"$(2;1)$ és $(6;5)$; az érintők $3x-2y-4=0$ és $9x-10y-4=0$"),
]

# ============================== NEHÉZ ==============================
NEHEZ = [
 (r"Írd fel a $2x^2+9y^2=54$ ellipszis azon érintőit, amelyek merőlegesek a $3x+5y-1=0$ egyenesre!",
  [r"Mekkora az érintők $k$ iránytényezője? Helyettesítsd az $y=kx+n$ egyenest az ellipszis egyenletébe!",
   r"Milyen $n$ esetén van pontosan egy közös pont?", r"Írd fel az érintők egyenletét!"],
  [r"$k=\tfrac53$; $9x^2+10nx+3n^2-18=0$", r"$D=0$: $n^2=81$, $n=\pm9$",
   r"$y=\tfrac53x+9$ és $y=\tfrac53x-9$, azaz $5x-3y\pm27=0$"]),

 (r"Írd fel az $x^2+4y^2=40$ ellipszis azon érintőit, amelyek merőlegesek a $2x-3y+8=0$ egyenesre!",
  [r"Mekkora az érintők $k$ iránytényezője? Helyettesítsd az $y=kx+n$ egyenest az ellipszis egyenletébe!",
   r"Határozd meg $n$-et!",
   r"Írd fel az érintőket!"],
  [r"$k=-\tfrac32$; $5x^2-6nx+2n^2-20=0$", r"$n=\pm10$", r"$y=-\tfrac32x+10$ és $y=-\tfrac32x-10$"]),

 (r"Határozd meg a $p$ paramétert úgy, hogy az $x+2y-p=0$ egyenes érintse az $x^2+2y^2=12$ ellipszist!",
  [r"Fejezd ki $y$-t, és helyettesítsd be!", r"Határozd meg $p$-t!"],
  [r"$3x^2-2px+p^2-24=0$", r"$D=0$: $p^2=36$, $p=6$ vagy $p=-6$"]),

 (r"Írd fel az $x^2-12y^2=36$ hiperbola azon érintőit, amelyek párhuzamosak az $x-3y+6=0$ egyenessel!",
  [r"Helyettesítsd az $y=\tfrac13x+n$ egyenest a hiperbola egyenletébe!", r"Határozd meg $n$-et!",
   r"Írd fel az érintőket!"],
  [r"$x^2+24nx+36n^2+108=0$", r"$n=\pm1$", r"$y=\tfrac13x+1$ és $y=\tfrac13x-1$"]),

 (r"Határozd meg az $m$ paramétert úgy, hogy a $2x-y-m=0$ egyenes érintse az $x^2-2y^2=14$ hiperbolát!",
  [r"Helyettesítsd be az egyenest!", r"Határozd meg $m$-et, és írd fel az érintőket!"],
  [r"$7x^2-8mx+2m^2+14=0$", r"$m=\pm7$: $y=2x-7$ és $y=2x+7$"]),

 (r"Adott az $x^2-9y^2=9$ hiperbola és az $x-3y+6=0$ egyenes.",
  [r"Helyettesítsd az $x=3y-6$ kifejezést a hiperbola egyenletébe! Milyen egyenletet kapsz?",
   r"Hány közös pontjuk van? Add meg!",
   r"Maxi szerint az egyenes érintő, „mert egy közös pont van”. Igaza van? Indokold!"],
  [r"elsőfokú egyenletet: $-36y+27=0$", r"egy: $\left(-\tfrac{15}{4};\tfrac34\right)$",
   r"nincs igaza: az egyenes párhuzamos az $y=\tfrac13x$ aszimptotával, és átmetszi a görbét; érintőnél a "
   r"másodfokú egyenletnek kettős gyöke van"]),
]

JOKER = (r"Az $\dfrac{x^2}{20}+\dfrac{y^2}{4}=1$ ellipszisnek és az $\dfrac{x^2}{4}-\dfrac{y^2}{12}=1$ "
         r"hiperbolának közösek a fókuszai.",
         [r"mindkettőnél $e=4$, a fókuszok $(\pm4;0)$", r"$(\sqrt5;\sqrt3)$, $(\sqrt5;-\sqrt3)$, $(-\sqrt5;\sqrt3)$, "
          r"$(-\sqrt5;-\sqrt3)$", r"a téglalap oldalai $2\sqrt5$ és $2\sqrt3$, a területe $4\sqrt{15}\approx15{,}49$"],
         [r"Ellenőrizd, hogy valóban közösek a fókuszok!", r"Határozd meg a két görbe metszéspontjait!",
          r"A négy metszéspont téglalapot alkot. Mekkora a területe?"])

# ============================== OLDAL ==============================
body = [
 '    <h2 id="alap">🟢 Alapszint — Különleges fokozat</h2>\n' + cards(ALAP, "alap", "alap"),
 '    <h2 id="kozep">🟡 Középszint — Királyi Gárda</h2>\n' + cards(KOZEP, "kozep", "kozep"),
 '    <h2 id="nehez">🔴 Nehéz szint — Kristály-protokoll</h2>\n' + cards(NEHEZ, "nehez", "nehez"),
 '    <h2 id="joker">🃏 Joker</h2>\n' + joker_card(JOKER[0], JOKER[1], JOKER[2]),
]
assert (len(ALAP), len(KOZEP), len(NEHEZ)) == (20, 16, 6), (len(ALAP), len(KOZEP), len(NEHEZ))

ut = oldal(tagozat="3e", mappa="05-analitikus-geometria", fajl="feladatok-ellipszis-hiperbola.html",
           cim="Ellipszis és hiperbola", temakor="Síkbeli analitikus geometria",
           alcim="Az ellipszis és a hiperbola egyenlete és adatai, közös pontjuk egyenessel, húr és érintő. "
                 "Számológép használható: a szögeket egy, minden más közelítő értéket két tizedesre kerekíts. "
                 "A végeredmény minden feladatnál lenyitható — előbb számolj, csak utána nézd meg!",
           sections_html="\n".join(body),
           prev="tananyag-hiperbola-es-egyenes.html", prevc="A hiperbola és az egyenes",
           nxt="tananyag-parabola.html", nxtc="A parabola")
print("✓", os.path.basename(ut), "| Alap", len(ALAP), "Közép", len(KOZEP),
      "Nehéz", len(NEHEZ), "+ Joker")
